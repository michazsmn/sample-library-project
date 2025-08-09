from api.pymongo_get_database import get_database

def get_user_by_email(email: str, db=get_database()):
    """
    Retrieve a user from the database by their email address.

    Args:
        email (str): The email address of the user to retrieve.
        db: The database connection (default is the MongoDB database).

    Returns:
        dict: The user document if found, otherwise None.
    """
    user = db["users"].find_one({"email": email})
    return user