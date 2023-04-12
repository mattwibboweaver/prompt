import duckdb

class Data:
    
    def __init__(self):
        self.db_conn = self.get_db_conn()
        self.db_cur = self.get_db_cursor()  
        
    def get_db_conn(self):
        if self.db_conn is None:
            self.db_conn = duckdb.connect('prompt.db')
            
        return self.db_conn
    
    def get_db_cursor(self):
        if self.db_cur is None:
            self.db_cur = self.db_conn.cursor()
            
        return self.db_cur   