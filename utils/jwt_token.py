from datetime import datetime, timedelta
from models import User
from config import JWT
import jwt
def create_token(data:dict):
    to_encode = data.copy()
    if(JWT['expires_delta']):
        expire = datetime.now() + timedelta(seconds=JWT['expires_delta'])
    else:
        raise ValueError('No expire time provided for JWT token')

    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, JWT['secrets'], algorithm=JWT['algorithm'])
    return encoded_jwt


def verify_token(token:str):
    try:
        decoded_token = jwt.decode(token, JWT['secrets'], algorithms=[JWT['algorithm']])
        return decoded_token
    except:
        return None
    



