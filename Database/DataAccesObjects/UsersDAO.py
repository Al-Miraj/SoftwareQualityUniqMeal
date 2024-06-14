class UsersDAO:
    def __init__(self, connection):
        self.conn = connection
    
    def InsertUsers(self, users: iter) -> None:
        for user in users:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO users (Username, Password, FirstName, LastName, RegistrationDate, Role)
                              VALUES (?, ?, ?, ?, ?, ?)""", [*user.__dict__.values()])
        self.conn.commit()
        cursor.close()

    def DeleteUser(self, username, password) -> None:
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE Username=? AND Password=?", [username, password])
        self.conn.commit()
        cursor.close()
    
    def UpdateUserUserName(self, oldUsername, newUsername) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET Username=? WHERE Username=?", [newUsername, oldUsername])
        self.conn.commit()
        cursor.close()

    def UpdateUserPassword(self, username, oldPassword, newPassword) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET Password=? WHERE Password=? AND Username=?", [newPassword, oldPassword, username])
        self.conn.commit()
        cursor.close()

    def UpdateUserFirstName(self, username, oldFirstName, newFirstName) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET FirstName=? WHERE FirstName=? AND Username=?", [newFirstName, oldFirstName, username])
        self.conn.commit()
        cursor.close()

    def UpdateUserLastName(self, username, oldLastName, newLastName) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET LastName=? WHERE LastName=? AND Username=?", [newLastName, oldLastName, username])
        self.conn.commit()
        cursor.close()

    def UpdateUserRole(self, username, oldRole, newRole) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET Role=? WHERE Role=? AND Username=?", [newRole, oldRole, username])
        self.conn.commit()
        cursor.close()
    
    def SelectUser(self, username):
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        fetchedUser = cursor.execute("SELECT * FROM users WHERE Username=?", [username]).fetchone()
        cursor.close()
        return fetchedUser

    def SelectAllUsers(self):
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        fetchedUsers = cursor.execute("SELECT * FROM users").fetchall()
        cursor.close()
        return fetchedUsers
    
    
    
# Other CRUD operations...
