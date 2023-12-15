

class Validate:

    def __init__(self, input = None) -> None:
        self.input = input

    def validate_name(self, name):
        if name.isdigit():
            return False
        else: 
            return True

    def aircraft_id(self, aircraft_id):
        if len(aircraft_id) == 6:
            if "-" in aircraft_id:
                splited = aircraft_id.split("-")
                if len(splited[0]) == 2 and len(splited[1]) == 3:
                    if splited[0].isalpha and splited[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


    def validate_email(self, email):
        if "@" and "." in email:
            return True
        else:
            return False

    def validate_phone_number(self, p_number):
        if len(p_number) == 7 and p_number.isdigit():
            return True
        else: 
            return False

    def validate_nid(self, nid):
        if len(nid) == 10 and nid.isdigit():
            return True
        else: 
            return False

    def validate_destination(self, destination):
        if destination.isalpha():
            return True
        else:
            return False

    def validate_addres(self, address):
        ad_num = address.split(" ")
        if address[0].isalpha() and address[1].isdigit():
            return True
        else:
            return False

    def validate_role(self, role):
        roles = ["pilot", "cabincrew"]
        role = role.lower()
        if role in roles:
            return True
        else:
            return False

    def validate_rank(self, role, rank):
        rank_pilot = ["captain", "copilot"]
        rank_cabain_crew = ["flight attendant", "flight service manager"]
        if role == "pilot":
            if rank in rank_pilot:
                return True
            else:
                return False
        else:
            if rank in rank_cabain_crew:
                return True
            else:
                return False
            
    def airplane_type(self, airplane_type):
        if airplane_type.isdigit():
            return False
        elif airplane_type.isalpha():
            return False
        elif 6 > len(airplane_type) > 20:
            return False
        for char in airplane_type:
            if not (char.isalpha() or char.isdigit()):
                return False
        return True
            
    def validate_cap(self, cap):
        try:
            if cap.isdigit() and 0 < int(cap) < 1000:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def dest_intials(self, intials):
        if len(intials) == 3 and intials.isalpha():
            return True
        else:
            return False
        
    def flight_time_and_distance(self, time):
        try:
            if time.isdigit():
                int(time)
                if time > 0:
                    return True
            else: 
                return False
        except ValueError:
            return False
        


        
