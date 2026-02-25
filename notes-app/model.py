from pydantic import BaseModel,Field
class Note(BaseModel):
    title:str=Field(min_length=2)
    content:str=Field(min_length=1)
    
    

