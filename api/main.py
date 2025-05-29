from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.post("/register/")
def register_user(email: str, password: str, username: str):
    # Here you would typically handle the registration logic, such as saving the user to a database
    # For demonstration purposes, we'll just log the email, password, and username
    print("Email:", email)
    print("Password:", password)
    print("Username:", username)

    # Return a response or redirect as needed
    return {"success": True, "message": "Registration successful!"}