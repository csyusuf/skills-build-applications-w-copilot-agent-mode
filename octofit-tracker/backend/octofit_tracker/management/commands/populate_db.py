from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import traceback

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Add detailed logging for debugging
        try:
            self.stdout.write('Populating users...')
            for user_data in test_users:
                self.stdout.write(f'Adding user: {user_data}')
                User.objects.get_or_create(**user_data)
        except Exception as e:
            self.stderr.write(f'Error populating users: {e}')
            self.stderr.write(traceback.format_exc())

        try:
            self.stdout.write('Populating teams...')
            for team_data in test_teams:
                self.stdout.write(f'Adding team: {team_data}')
                Team.objects.get_or_create(**team_data)
        except Exception as e:
            self.stderr.write(f'Error populating teams: {e}')
            self.stderr.write(traceback.format_exc())

        try:
            self.stdout.write('Populating activities...')
            for activity_data in test_activities:
                self.stdout.write(f'Adding activity: {activity_data}')
                Activity.objects.get_or_create(**activity_data)
        except Exception as e:
            self.stderr.write(f'Error populating activities: {e}')
            self.stderr.write(traceback.format_exc())

        try:
            self.stdout.write('Populating leaderboard...')
            for leaderboard_data in test_leaderboard:
                self.stdout.write(f'Adding leaderboard entry: {leaderboard_data}')
                Leaderboard.objects.get_or_create(**leaderboard_data)
        except Exception as e:
            self.stderr.write(f'Error populating leaderboard: {e}')
            self.stderr.write(traceback.format_exc())

        try:
            self.stdout.write('Populating workouts...')
            for workout_data in test_workouts:
                self.stdout.write(f'Adding workout: {workout_data}')
                Workout.objects.get_or_create(**workout_data)
        except Exception as e:
            self.stderr.write(f'Error populating workouts: {e}')
            self.stderr.write(traceback.format_exc())

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
