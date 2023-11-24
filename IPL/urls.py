"""
URL configuration for IPL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path
from Products.views import matches_played,matches_won_per_team_per_year,extra_runs_conceded_per_team_2016,top_economical_bowlers_2015
from Products.views import matches_played_chart
urlpatterns = [
    path('matches_played/',matches_played,name="Matches_played"),
    path('won_per_team/', matches_won_per_team_per_year, name='matches_won_per_team_per_year'),
    path('extra_runs',extra_runs_conceded_per_team_2016,name = "extra_runs"),
    path('top10',top_economical_bowlers_2015,name = "top10"),
    path('graph1',matches_played_chart,name = "graph1"),
    path('admin/', admin.site.urls),
]
