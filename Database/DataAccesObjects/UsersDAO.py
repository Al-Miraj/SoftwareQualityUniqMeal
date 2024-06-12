class UsersDAO:
    def __init__(self, connection):
        self.conn = connection
    
    def InsertUsers(self, users):
        for user in users:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO users (Username, Password, FirstName, LastName, RegistrationDate, Role)
                              VALUES (?, ?, ?, ?, ?, ?)""", [*user.__dict__.values()])
        self.conn.commit()
        cursor.close()

    def DeleteUser(self, user):
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE Username=? AND Password=?", [user.Username, user.Password])
        self.connection.commit()
        cursor.close()
    
    def UpdateUser(self, user):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET Username=?, Password=?, FirstName=?, LastName=?, RegistrationDate=?, Role=?", [*user.__dict__.values()])
        self.connection.commit()
        cursor.close()
    
    def SelectUser(self, user):
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        fetchedUser = cursor.execute("SELECT * FROM users WHERE Username=? AND Password=?", [user.Username, user.Password]).fetchone()
        cursor.close()
        return fetchedUser[0]
    
    
    
# Other CRUD operations...
