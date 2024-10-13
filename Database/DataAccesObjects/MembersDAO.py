from CryptUtils.argon import ph
from CryptUtils.CryptoManager import encrypt


class MembersDAO:
    def __init__(self, connection):
        self.conn = connection
    
    def InsertMembers(self, members: iter) -> bool:
        cursor = self.conn.cursor()
        for member in members:
            insertMemberQ = """INSERT OR IGNORE INTO members (MembershipID, FirstName, LastName, Age, Gender, Weight, Street, HouseNumber, ZipCode, City, Email, PhoneNumber, RegistrationDate)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            insertMemberValues = [encrypt(member.MembershipID),
                                  encrypt(member.FirstName),
                                  encrypt(member.LastName),
                                  encrypt(str(member.Age)),
                                  encrypt(member.Gender),
                                  encrypt(str(member.Weight)),
                                  encrypt(member.Street),
                                  encrypt(member.HouseNumber),
                                  encrypt(member.ZipCode),
                                  encrypt(member.City),
                                  encrypt(member.Email),
                                  encrypt(member.PhoneNumber),
                                  encrypt(str(member.RegistrationDate))]
            cursor.execute(insertMemberQ, insertMemberValues)
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def DeleteMember(self, membershipID, firstName, lastName) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM members WHERE MembershipID=? AND FirstName=? AND LastName=?", [encrypt(membershipID), encrypt(firstName), encrypt(lastName)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberMembershipID(self, oldMembershipId, newMembershipID) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET MembershipID=? WHERE MembershipID=?", [encrypt(newMembershipID), encrypt(oldMembershipId)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    
    def UpdateMemberFirstName(self, membershipID, oldFirstName, newFirstName) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET FirstName=? WHERE FirstName=? AND MembershipID=?", [encrypt(newFirstName), encrypt(oldFirstName), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberLastName(self, membershipID, oldLastName, newLastName) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET LastName=? WHERE LastName=? AND MembershipID=?", [encrypt(newLastName), encrypt(oldLastName), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberAge(self, membershipID, oldAge, newAge) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Age=? WHERE Age=? AND MembershipID=?", [encrypt(str(newAge)), encrypt(oldAge), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberGender(self, membershipID, oldGender, newGender) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Gender=? WHERE Gender=? AND MembershipID=?", [encrypt(newGender), encrypt(oldGender), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberWeight(self, membershipID, oldWeight, newWeight) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Weight=? WHERE Weight=? AND MembershipID=?", [encrypt(str(newWeight)), encrypt(oldWeight), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberStreet(self, membershipID, oldStreet, newStreet) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Street=? WHERE Street=? AND MembershipID=?", [encrypt(newStreet), encrypt(oldStreet), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberHouseNumber(self, membershipID, olHouseNumber, newHouseNumber) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET HouseNumber=? WHERE HouseNumber=? AND MembershipID=?", [encrypt(newHouseNumber), encrypt(olHouseNumber), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberZipCode(self, membershipID, oldZipCode, newZipCode) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET ZipCode=? WHERE ZipCode=? AND MembershipID=?", [encrypt(newZipCode), encrypt(oldZipCode), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberCity(self, membershipID, oldCity, newCity) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET City=? WHERE City=? AND MembershipID=?", [encrypt(newCity), encrypt(oldCity), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberEmail(self, membershipID, oldEmail, newEmail) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET Email=? WHERE Email=? AND MembershipID=?", [encrypt(newEmail), encrypt(oldEmail), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def UpdateMemberPhoneNumber(self, membershipID, oldPhoneNumber, newPhoneNumber) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE members SET PhoneNumber=? WHERE PhoneNumber=? AND MembershipID=?", [encrypt(newPhoneNumber), encrypt(oldPhoneNumber), encrypt(membershipID)])
        self.conn.commit()
        if cursor.rowcount > 0:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def SelectMember(self, firstName, lastName) -> any:
        cursor = self.conn.cursor()
        fetchedMember = cursor.execute("SELECT * FROM members WHERE FirstName=? AND LastName=?", [encrypt(firstName), encrypt(lastName)]).fetchone()
        cursor.close()
        return fetchedMember
    
    # NOTE: partial match was not possible with encryption as it wasnt able to match
    #       correctly. it only matched to the whole value. 
    #       Micheal will match, but icheal will not
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
        fetchedMembers = cursor.execute(fetchedMemberQuery, ('%' + encrypt(searchTerm) + '%',) * 9).fetchall()
        return fetchedMembers

    
    
    
# Other CRUD operations...
