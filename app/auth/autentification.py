from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer

token_url = "my_token_URL"
o_auth_scheme = OAuth2PasswordBearer(tokenUrl=token_url)