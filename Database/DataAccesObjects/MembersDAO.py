class MembersDAO:
    def __init__(self, connection):
        self.conn = connection
    
    def InsertMembers(self, members):
        for member in members:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO members (MembershipID, FirstName, LastName, Age, Gender, Weight, Street, HouseNumber, ZipCode, City, Email, PhoneNumber, RegistrationDate)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", [*member.__dict__.values()])
        self.conn.commit()
        cursor.close()

    def DeleteMember(self, member):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM members WHERE MembershipID=?", (member.MembershipID,))
        self.connection.commit()
        cursor.close()
    
    def UpdateMember(self, member):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET MembershipID=?, FirstName=?, LastName=?, Age=?, Gender=?, Weight=?, Street=?, HouseNumber=?, ZipCode=?, City=?, Email=?, PhoneNumber=?, RegistrationDate=?", [*member.__dict__.values()])
        self.connection.commit()
        cursor.close()
    
    def SelectMember(self, member):
        cursor = self.conn.cursor()
        fetchedMember = cursor.execute("SELECT * FROM members WHERE MembershipID=?", [member.MembershipID]).fetchone()
        cursor.close()
        return fetchedMember[0]
    
    
    
# Other CRUD operations...
