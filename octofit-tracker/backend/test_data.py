# Test data for OctoFit Tracker

test_users = [
    {"username": "student1", "email": "student1@example.com", "password": "password123"},
    {"username": "student2", "email": "student2@example.com", "password": "password123"},
    {"username": "student3", "email": "student3@example.com", "password": "password123"}
]

test_teams = [
    {"name": "Team Alpha", "members": ["student1", "student2"]},
    {"name": "Team Beta", "members": ["student3"]}
]

test_activities = [
    {"user": "student1", "activity": "running", "duration": 30},
    {"user": "student2", "activity": "walking", "duration": 45},
    {"user": "student3", "activity": "cycling", "duration": 60}
]

test_leaderboard = [
    {"team": "Team Alpha", "points": 100},
    {"team": "Team Beta", "points": 80}
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day."},
    {"name": "Evening Yoga", "description": "Relaxing yoga session to wind down."}
]
