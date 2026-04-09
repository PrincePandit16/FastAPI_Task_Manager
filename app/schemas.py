from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal, Optional



#user create
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role:str

    class Config:
        from_attributes = True


#token schema
class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: Optional[str] = None



#task base
class TaskBase(BaseModel):
    title:str
    description:Optional[str] = None
    completed:bool = False
    priority: Literal["low","medium","high"] = "medium"


#task create
class TaskCreate(TaskBase):
    pass
    # title:str
    # description:Optional[str] = None
    # completed:bool = False
    # priority: Literal["low","medium","high"] = "medium"

#task update use for put
class TaskUpdate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    completed:Optional[bool] = None
    priority:Optional[Literal["low","medium","high"]] = None


class TaskOut(TaskBase):
    id:int
    created_at:datetime
    updated_at:datetime
    owner_id:int

    class Config:
        from_attributes = True

