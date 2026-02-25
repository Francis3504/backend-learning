import bcrypt
from model import User,UserCreated
from fastapi import FastAPI,HTTPException,status
user_db:dict[str,UserCreated]={}
app=FastAPI()
    
@app.post("/register",status_code=status.HTTP_201_CREATED)
def register(user:User):
   if user.username in user_db:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Username already exists")
   password_hash=bcrypt.hashpw(user.password.encode("utf-8"),bcrypt.gensalt())
   user_create=UserCreated(user.username,password_hash)
   user_db[user.username]=user_create
   return {"message":"User sucessfully registered"}

@app.post("/login")
def login(user:User):
  user_info=user_db.get(user.username)

  if not user_info:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
  
  is_password_true=user_info.verify_password(user.password)
  if is_password_true:
     return {"message":"Login sucessful"}
  else:
     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
       