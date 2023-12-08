

class Employee:
    def __init__(self, nid, name, role, rank, licence, address, phone_nr, pref_nr, slot_param):
        self.nid = nid
        self.name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phone_nr = phone_nr
        self.pref_nr = pref_nr
        self.slot_param = slot_param

    def __str__(self):
        return f"ID number: {self.nid}, Name: {self.name}, Role: {self.role}, Rank: {self.rank}, Licence: {self.licence}, Addres: {self.address}, Phone number: {self.phone_nr}, Preferd phone number: {self.pref_nr}"

    