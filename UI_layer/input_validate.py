

class Validate:

    def __init__(self) -> None:
        pass

    def validate_name(self, name):
        if name.isditgit:
            return False
        else: 
            return True

    def validate_flight_number(self, number):
        pass

    def validate_email(self, email):
        if "@" and "." in email:
            return True
        else:
            return False

    def validate_phone_number(self, p_number):
        if len(p_number) == 7 and p_number.isditgit:
            return True
        else: 
            return False

    def validate_nid(self, nid):
        if len(nid) == 10 and nid.isditgit:
            return True
        else: 
            return False

    def validate_destination(self, destination):
        pass

    def validate_addres(self, address):
        pass

    def validate_role(self, role):
        pass

    def validate_rank(self, rank):
        pass