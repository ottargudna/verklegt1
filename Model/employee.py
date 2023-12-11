

class Employee:
    def __init__(self, nid, name, role, rank, licence, address, phone_nr, email, homephone_nr):
        self.nid = nid
        self.name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phone_nr = phone_nr
        self.email = email
        self.homephone_nr = homephone_nr

    def __str__(self):
        return f"ID number: {self.nid}, Name: {self.name}, Role: {self.role}, Rank: {self.rank}, Licence: {self.licence}, Addres: {self.address}, Phone number: {self.phone_nr}, email: {self.email}, homephone number:{self.homephone_nr}"

    