from CryptUtils.argon import ph
from CryptUtils.CryptoManager import encrypt, decrypt
from argon2 import exceptions as ex



class UsersDAO:
    def __init__(self, connection):
        self.conn = connection
    
    def InsertUsers(self, users: iter) -> bool:
        cursor = self.conn.cursor()
        for user in users:
            insertUsersQ = """INSERT OR IGNORE INTO users (Username, Password, FirstName, LastName, RegistrationDate, Role)
                            VALUES (?, ?, ?, ?, ?, ?)"""
            insertUsersValues = [encrypt(userObj.Username), 
                                 encrypt(DBConfig.ph.hash(userObj.Username + userObj.Password)), 
                                 encrypt(userObj.FirstName), 
                                 encrypt(userObj.LastName), 
                                 encrypt(userObj.RegistrationDate), 
                                 encrypt(userObj.Role)]
            cursor.execute(insertUsersQ, insertUsersValues)
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def DeleteUser(self, username) -> bool:
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE Username=?", [encrypt(username)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    
    def UpdateUserUserName(self, oldUsername, newUsername) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET Username=? WHERE Username=?", [encrypt(newUsername), encrypt(oldUsername)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateUserPassword(self, username, oldPassword, newPassword) -> bool:
        cursor = self.conn.cursor()
        fetchedUser = self.SelectUser(username)
        if not fetchedUser:
            print("User not found.")
            return False

        password  = decrypt(fetchedUser[1])
        if password == oldPassword:
            cursor.execute("UPDATE users SET Password=? WHERE Username=?", [encrypt(ph.hash(username + newPassword)), encrypt(username)])
        else:
            print("Wrong username or password combination.")
            return False
        
        self.conn.commit()
        cursor.close()
        return True


    def UpdateUserFirstName(self, username, oldFirstName, newFirstName) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET FirstName=? WHERE FirstName=? AND Username=?", [encrypt(newFirstName), encrypt(oldFirstName), encrypt(username)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateUserLastName(self, username, oldLastName, newLastName) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET LastName=? WHERE LastName=? AND Username=?", [encrypt(newLastName), encrypt(oldLastName), encrypt(username)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateUserRole(self, username, oldRole, newRole) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET Role=? WHERE Role=? AND Username=?", [encrypt(newRole), encrypt(oldRole), encrypt(username)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    
    def SelectUser(self, username):
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        fetchedUser = cursor.execute("SELECT * FROM users WHERE Username=?", [encrypt(username)]).fetchone()
        cursor.close()
        return fetchedUser

    def SelectAllUsers(self):
        #todo we might have to change query later when username password are encrypted 
        cursor = self.conn.cursor()
        fetchedUsers = cursor.execute("SELECT * FROM users").fetchall()
        cursor.close()
        return fetchedUsers

    # def _createUserObj(self, fetchedUser):
    #     if fetchedUser == None:
    #         return None

    #     username  = decrypt(fetchedUser[0])
    #     password  = decrypt(fetchedUser[1])
    #     firtsname = decrypt(fetchedUser[2])
    #     lastname  = decrypt(fetchedUser[3])
    #     regDate   = decrypt(fetchedUser[4])
    #     role      = decrypt(fetchedUser[5])
    #     if role == "SuperAdmin":
    #         return SuperAdmin(username, password, firtsname, lastname, regDate)
    #     elif role == "SystemAdmin":
    #         return SystemAdmin(username, password, firtsname, lastname, regDate)
    #     elif role == "Consultant":
    #         return Consultant(username, password, firtsname, lastname, regDate)
    #     else:
    #         return None
    
    
    
# Other CRUD operations...
