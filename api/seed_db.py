from pymongo_get_database import get_database

user_col = get_database()["users"]

#Example entries for sanity check, passwords not hashed
user_col.insert_many([
    {
        "email": "email@gmail.com",
        "password": "password123",
        "name": "John Doe",
    }
    ,
    {
        "email": "jane.doe@gmail.com",
        "password": "password456",
        "name": "Jane Doe",
    }
    ,
    {
        "email": "bob.smith@gmail.com",
        "password": "password789",
        "name": "Bob Smith",
    }
])