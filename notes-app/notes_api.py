from fastapi import FastAPI,HTTPException,status
from model import Note
from notes_manager import NotesManager
app=FastAPI()
db=NotesManager()    


@app.get("/get_notes/{title}")
def search_notes(title:str):
    db_notes=db.get_notes(title)
    if not db_notes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Notes not found")
    return {"Notes":db_notes}

@app.post("/save_notes")
def save_notes(note:Note):
    saved,info=db.save_notes(note)
    if saved:
        return {"message":"Data successfully saved"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Failed to save notes,{info}")
        

@app.put("/edit_notes/{id}")
def update_notes(id:int,note:Note):
    edited,info=db.update_notes(id,note)
    if edited:
        return {"message":"Notes updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Failed to update notes,{info}")

@app.delete("/delete_notes/{id}")
def delete_notes(id:int):
    deleted,info=db.delete_notes(id)
    if deleted:
        return {"message":"Notes successfully deleted."}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Failed to delete notes,{info}")

