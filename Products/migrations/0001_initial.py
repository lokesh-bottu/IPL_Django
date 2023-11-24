# Generated by Django 4.2.7 on 2023-11-24 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('season', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('toss_winner', models.CharField(max_length=100)),
                ('toss_decision', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('dl_applied', models.IntegerField()),
                ('winner', models.CharField(max_length=100, null=True)),
                ('win_by_runs', models.IntegerField()),
                ('win_by_wickets', models.IntegerField()),
                ('player_of_match', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('umpire1', models.CharField(max_length=100, null=True)),
                ('umpire2', models.CharField(max_length=100, null=True)),
                ('umpire3', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(max_length=100)),
                ('bowling_team', models.CharField(max_length=100)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(max_length=100)),
                ('non_striker', models.CharField(max_length=100)),
                ('bowler', models.CharField(max_length=100)),
                ('is_super_over', models.IntegerField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye_runs', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(max_length=100, null=True)),
                ('dismissal_kind', models.CharField(max_length=100, null=True)),
                ('fielder', models.CharField(max_length=100, null=True)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.matches')),
            ],
        ),
    ]