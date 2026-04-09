from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas


#password hashing
pwd_context = CryptContext(schemes = ['argon2'],deprecated = "auto")

def hash_password(password:str) -> str:   #hash_password
    return pwd_context.hash(password)


def verify_password(plain_password:str, hash_password:str)->bool:    #verify_password
    return pwd_context.verify(plain_password,hash_password)





#token creation section
SECRET_KEY = "N6OCv2SPodGefIyqX1jXucBmtEnpPJ-E-oZ5zuNAc78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)



def decode_access_token(token:str):
    try:  
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        return payload
    except Exception:
        return None  
    


#verify tokens using oauth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    username = payload.get("sub")
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user




