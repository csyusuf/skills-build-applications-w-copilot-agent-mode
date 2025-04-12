from pymongo import MongoClient

def verify_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]
        users = db["users"].find()
        print("Users collection:")
        for user in users:
            print(user)
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

if __name__ == "__main__":
    verify_connection()
