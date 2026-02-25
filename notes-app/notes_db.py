import sqlite3
import os
from contextlib import contextmanager
   
class DB:

    def __init__(self,db_path="storage/notes.db"):
        self.db_path=db_path
        os.makedirs(os.path.dirname(db_path),exist_ok=True)
        self._setup_database()

    def _setup_database(self):
       with self._get_connection() as conn:
          cursor=conn.cursor()
          cursor.execute("""
             CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL, 
                content TEXT NOT NULL,
                created_at TEXT,
                date_of_modification TEXT)
              """)
         
          conn.commit()
       

    @contextmanager
    def _get_connection(self):
      connection=sqlite3.connect(self.db_path)
      try:
         yield connection
      finally:
         connection.close()

