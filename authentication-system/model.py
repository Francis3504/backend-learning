from pydantic import BaseModel,Field
import bcrypt

class User(BaseModel):
    username:str=Field(min_length=3)
    password:str=Field(min_length=8)


class UserCreated(BaseModel):
    username:str
    password_hashed:bytes
    
    def verify_password(self,password:str)->bool:
        return bcrypt.checkpw(password.encode("utf-8"),self.password_hashed)


