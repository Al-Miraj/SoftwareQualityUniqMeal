from .User import User
from .Member import Member

class Consultant(User):
    def UpdatePassword(self, password):
        self.Password = password
    
    def AddNewMember(self, firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber):
        newMember = Member(firstName, lastName, age, gender, weight, street, houseNumber, zipCode, city, email, phoneNumber)
        #todo save this member to database
    
    def UpdateMemberInfo(self, member):
        #todo figure out what can and cannot be updated or modified
        pass

    def SearchMemberInfo(self, searchTerm):
        #todo set up database and use this query to fetch any rows containing searchTerm
        '''
        sql_query = f"""
        SELECT * FROM your_table
        WHERE 
            firstName LIKE ? OR
            lastName LIKE ? OR
            street LIKE ? OR
            houseNumber LIKE ? OR
            zipCode LIKE ? OR
            city LIKE ? OR
            email LIKE ? OR
            phoneNumber LIKE ?
        """

        # Execute the query with the search term
        cursor.execute(sql_query, ('%' + searchTerm + '%',) * 8)
        '''
        pass


