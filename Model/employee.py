

class Employee:
    def __init__(self, nid="1611042050", name="Óttar Atli", role="Kóngurinn", rank = "hæsta", licence = "dómarapróf", address = "Kleifakór 12", phone_nr = "spurðu snap", pref_nr = "snap", slot_param = "juju"):
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

    