from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=timedelta(minutes=30))
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Workout A", description="Description of Workout A")
        self.assertEqual(workout.name, "Workout A")