from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from ...models import Matches, Deliveries

import csv

class Command(BaseCommand):

    def load_matches(self):
        csv_matches = 'matches.csv'
        with open(csv_matches, 'r') as matches_file:
            matches_data = csv.DictReader(matches_file)
            for match in matches_data:
            
                matches_obj = Matches(
                    season          = int(match['season']),
                    city            = match['city'],
                    date            = match['date'],
                    team1           = match['team1'],
                    team2           = match['team2'],
                    toss_winner     = match['toss_winner'],
                    toss_decision   = match['toss_decision'],
                    result          = match['result'],
                    dl_applied      = int(match['dl_applied']),
                    winner          = match['winner'],
                    win_by_runs     = int(match['win_by_runs']),
                    win_by_wickets  = int(match['win_by_wickets']),
                    player_of_match = match['player_of_match'],
                    venue           = match['venue'],
                    umpire1         = match['umpire1'],
                    umpire2         = match['umpire2'],
                    umpire3         = match['umpire3'],
                )
                matches_obj.save()


    def load_deliveries(self):
        csv_deliveries = 'deliveries.csv'
        with open(csv_deliveries, 'r') as deliveries_file:
            deliveries_data = csv.DictReader(deliveries_file)
            for delivery in deliveries_data:
                try:
                    # Create a Matches instance first if needed
                    # For example, assuming your CSV contains match data as well
                    match_id_value = int(delivery['match_id'])
                    match_instance = Matches.objects.get(id=match_id_value)

                    
                    delivery_obj    = Deliveries(
                        match_id         = match_instance,
                        inning           = int(delivery['inning']),
                        batting_team     = delivery['batting_team'],
                        bowling_team     = delivery['bowling_team'],
                        over             = int(delivery['over']),
                        ball             = int(delivery['ball']),
                        batsman          = delivery['batsman'],
                        non_striker      = delivery['non_striker'],
                        bowler           = delivery['bowler'],
                        is_super_over    = int(delivery['is_super_over']),
                        wide_runs        = int(delivery['wide_runs']),
                        bye_runs         = int(delivery['bye_runs']),
                        legbye_runs      = int(delivery['legbye_runs']),
                        noball_runs      = int(delivery['noball_runs']),
                        penalty_runs     = int(delivery['penalty_runs']),
                        batsman_runs     = int(delivery['batsman_runs']),
                        extra_runs       = int(delivery['extra_runs']),
                        total_runs       = int(delivery['total_runs']),
                        player_dismissed = delivery['player_dismissed'],
                        dismissal_kind   = delivery['dismissal_kind'],
                        fielder          = delivery['fielder'],
                    )
                    delivery_obj.save()
                except Matches.DoesNotExist:
                    
                    self.stderr.write(self.style.ERROR(f'Matches with ID {match_id_value} does not exist.'))


    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                self.load_matches()
                self.load_deliveries()
        except Exception as e:
            raise CommandError(f'An error occurred: {str(e)}')