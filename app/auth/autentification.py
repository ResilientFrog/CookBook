
from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated
from db.models import User
import os


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}
def fake_decode(token):
    return User(username=token + "fakedecoded", email="john@example.com", full_name="John Doe")

def fake_hash_password(password: str):
    return "fakehashed" + password

auth_router = APIRouter()

TOKEN=os.getenv("TOKEN_URL")
print(TOKEN)
o_auth_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN)


@auth_router.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token' : form_data.username + 'token'}

@auth_router.get('/')
async def index(token: str = Depends(o_auth_scheme)):
    return {'the_token': token}


async def get_current_user(token: Annotated[str, Depends(o_auth_scheme)]):
    user = fake_decode(token)
    return user


#injection with current user
@auth_router.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
