class MembersDAO:
    def __init__(self, connection):
        self.conn = connection
    
    def InsertMembers(self, members: iter) -> None:
        for member in members:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO members (MembershipID, FirstName, LastName, Age, Gender, Weight, Street, HouseNumber, ZipCode, City, Email, PhoneNumber, RegistrationDate)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", [*member.__dict__.values()])
        self.conn.commit()
        cursor.close()

    def DeleteMember(self, membershipID, firstName, lastName) -> None:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM members WHERE MembershipID=? AND FirstName=? AND LastName=?", [membershipID, firstName, lastName])
        self.conn.commit()
        cursor.close()

    def UpdateMemberMembershipID(self, oldMembershipId, newMembershipID) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET MembershipID=? WHERE MembershipID=?", [newMembershipID, oldMembershipId])
        self.conn.commit()
        cursor.close()
    
    def UpdateMemberFirstName(self, membershipID, oldFirstName, newFirstName) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET FirstName=? WHERE FirstName=? AND MembershipID=?", [newFirstName, oldFirstName, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberLastName(self, membershipID, oldLastName, newLastName) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET LastName=? WHERE LastName=? AND MembershipID=?", [newLastName, oldLastName, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberAge(self, membershipID, oldAge, newAge) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Age=? WHERE Age=? AND MembershipID=?", [newAge, oldAge, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberGender(self, membershipID, oldGender, newGender) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Gender=? WHERE Gender=? AND MembershipID=?", [newGender, oldGender, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberWeight(self, membershipID, oldWeight, newWeight) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Weight=? WHERE Weight=? AND MembershipID=?", [newWeight, oldWeight, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberStreet(self, membershipID, oldStreet, newStreet) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Street=? WHERE Street=? AND MembershipID=?", [newStreet, oldStreet, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberHouseNumber(self, membershipID, olHouseNumber, newHouseNumber) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET HouseNumber=? WHERE HouseNumber=? AND MembershipID=?", [newHouseNumber, olHouseNumber, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberZipCode(self, membershipID, oldZipCode, newZipCode) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET ZipCode=? WHERE ZipCode=? AND MembershipID=?", [newZipCode, oldZipCode, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberCity(self, membershipID, oldCity, newCity) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET City=? WHERE City=? AND MembershipID=?", [newCity, oldCity, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberEmail(self, membershipID, oldEmail, newEmail) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Email=? WHERE Email=? AND MembershipID=?", [newEmail, oldEmail, membershipID])
        self.conn.commit()
        cursor.close()

    def UpdateMemberPhoneNumber(self, membershipID, oldPhoneNumber, newPhoneNumber) -> None:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET PhoneNumber=? WHERE PhoneNumber=? AND MembershipID=?", [newPhoneNumber, oldPhoneNumber, membershipID])
        self.conn.commit()
        cursor.close()

    def SelectMember(self, firstName, lastName) -> any:
        cursor = self.conn.cursor()
        fetchedMember = cursor.execute("SELECT * FROM members WHERE FirstName=? AND LastName=?", [firstName, lastName]).fetchone()
        cursor.close()
        return fetchedMember
    
    def SelectMemberByMatch(self, searchTerm) -> any: #member ID, first name, last name, address, email address, and phone number
        cursor = self.conn.cursor()
        fetchedMemberQuery = """
                                SELECT * FROM members
                                WHERE
                                    MembershipID LIKE ? OR
                                    FirstName LIKE ? OR
                                    LastName LIKE ? OR
                                    Street LIKE ? OR
                                    HouseNumber LIKE ? OR
                                    ZipCode LIKE ? OR
                                    City LIKE ? OR
                                    Email LIKE ? OR
                                    PhoneNumber LIKE ?
                             """
        fetchedMembers = cursor.execute(fetchedMemberQuery, ('%' + searchTerm + '%',) * 9).fetchall()
        return fetchedMembers

    
    
    
# Other CRUD operations...
