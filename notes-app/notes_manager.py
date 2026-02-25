from datetime import datetime
from notes_db import DB
from model import Note


class NotesManager(DB):
    def __init__(self):
        super().__init__()

    def get_notes(self,title:str):
        with self._get_connection() as conn:
            cursor=conn.cursor()
            notes=cursor.execute("""
            Select title,content From notes Where title =?
            """,(title,)).fetchall()
            return notes
        
    def save_notes(self,note:Note):
        try:
         date_time=datetime.now()
         with self._get_connection() as conn:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO notes(title,content,created_at) VALUES(?,?,?)",(note.title,note.content,date_time.isoformat()))
            conn.commit()
            return True,None
        except  Exception as e:
           return False,str(e)
        
    def update_notes(self,id:int,note:Note):
       try:
          date_of_modification=datetime.now()
          with self._get_connection() as conn:
             cursor=conn.cursor()
             cursor.execute("""
             UPDATE notes
             SET title=?,
             content=?,
             date_of_modification=?
             WHERE id=? """,(note.title,note.content,date_of_modification.isoformat(),id))
             row_delted=cursor.rowcount
             conn.commit()
             if row_delted==0:
                  return False,"No notes have been updated"
             return True,None
          
       except Exception as e:
          return False,str(e)
          

        
    def delete_notes(self,id:int):
       try:
        with self._get_connection() as conn:
          cursor=conn.cursor()
          cursor.execute("DELETE FROM  notes WHERE id=?",(id,))
          row_delted=cursor.rowcount
          conn.commit()
          if row_delted==0:
                return False,"No notes have been deleted"

          return True,None
       except Exception as e:
          return False,str(e)
    
            