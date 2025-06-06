from bcrypt import hashpw, gensalt, checkpw

def get_hashed_password(plain_password: str) -> str:
    """
    Hash a plain password using bcrypt.
    
    :param plain_password: The plain text password to hash.
    :return: The hashed password as a string.
    """
    return hashpw(plain_password.encode('utf-8'), gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    :param plain_password: The plain text password to verify.
    :param hashed_password: The hashed password to compare against.
    :return: True if the passwords match, False otherwise.
    """
    try:
        return checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except ValueError:
        return False