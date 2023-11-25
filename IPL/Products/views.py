from django.shortcuts import render
from .models import Matches, Deliveries
from django.db.models import Count, Sum, F
from django.http import JsonResponse, HttpResponse
import json




def matches_played(request):
    data = Matches.objects.values('season').annotate(matches_played=Count('id')).order_by('season')
    context = {'matches_played': list(data)}
    return JsonResponse(context,safe=False)



def matches_played_per_year_chart(request):
    response = matches_played('matches/')
    chart_data = json.loads(response.content)
    return render(request, 'matches.html', {'chart_data': json.dumps(chart_data)})



def matches_won_per_team_per_year(request):
    data = Matches.objects.values('season', 'winner').annotate(matches_won=Count('id')).order_by('season', 'winner')
    result = {}
    for entry in data:
        season = entry['season']
        team = entry['winner']
        matches_won = entry['matches_won']
        if season not in result:
            result[season] = {}
        result[season][team] = matches_won
    context = {'matches_won_per_team_per_year': result}
    return JsonResponse(context)


def matches_won_per_team_per_year_chart(request):
    response = matches_won_per_team_per_year('won_per_team/')
    chart_data = json.loads(response.content)
    return render(request, 'matches_won.html', {'chart_data': json.dumps(chart_data)})


def extra_runs_conceded_per_team_2016(request):
    matches_2016 = Matches.objects.filter(season=2016)
    deliveries_2016 = Deliveries.objects.filter(match_id__in=matches_2016)
    data = deliveries_2016.values('bowling_team').annotate(extra_runs=Sum('extra_runs')).order_by('bowling_team')
    result = {}
    for entry in data:
        team = entry['bowling_team']
        extra_runs = entry['extra_runs']
        result[team] = extra_runs
    context = {'extra_runs_conceded_per_team_2016': result}
    return JsonResponse(context)

def extra_runs_conceded_per_team_2016_chart(request):
    response = extra_runs_conceded_per_team_2016('extra_runs/')
    chart_data = json.loads(response.content)
    return render(request, 'extra_runs.html', {'chart_data': json.dumps(chart_data)})


def top_economical_bowlers_2015(request):
    deliveries_2015 = Deliveries.objects.filter(match_id__season=2015)
    overs_by_bowler = deliveries_2015.filter(ball=1).values('bowler').annotate(overs=Count('ball')).order_by('-overs')
    runs_given = deliveries_2015.values('bowler').annotate(total_runs=Sum('total_runs'))
    combined_data = overs_by_bowler.annotate(total_runs=F('total_runs')).values('bowler', 'overs', 'total_runs')
    for entry in combined_data:
        entry['economy'] = round(entry['total_runs'] / entry['overs'], 2)
    sorted_data = sorted(combined_data, key=lambda x: x['economy'])
    context = {'economy_of_each_bowler_2015': sorted_data}
    return JsonResponse(context)



