from pymongo import MongoClient

def initialize_database():
    # Connect to the MongoDB instance
    client = MongoClient("mongodb://localhost:27017/")

    # Initialize the octofit_db database
    db = client["octofit_db"]

    # Create collections
    collections = ["users", "teams", "activity", "leaderboard", "workouts"]
    for collection in collections:
        db.create_collection(collection, capped=False, size=None, max=None)

    # Set a unique index for the email field in the users collection
    db["users"].create_index("email", unique=True)

    # List all collections in the database
    print("Collections in octofit_db:", db.list_collection_names())

if __name__ == "__main__":
    initialize_database()
