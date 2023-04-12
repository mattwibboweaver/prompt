class User:
    
    def __init__(self, cursor, db):
        self.cursor = cursor
        self.conn = db

        def create_user_table(self):
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS user 
                                (username TEXT PRIMARY KEY,
                                password TEXT)""")
            self.conn.commit()  