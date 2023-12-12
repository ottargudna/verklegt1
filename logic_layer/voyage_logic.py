from Model.voyage import Voyage
from logic_layer.flights_logic import Flights

class Voyage_Logic:
    
    def __init__(self) -> None:
        pass

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        self.data_wrapper.create_voyage(voyage)


    def schedule_voyage(self):
        pass

    def get_all_voyages(self):
        self.data_wrapper.get_all_voyages()






    def check_working_status(self, date):
        voyages = self.get_all_voyages()
        voyages_in_date = []
        every_employee = self.get_all_employee()

        for voyage in voyages:
            if voyages[3] >= date <= voyages[4]:
                voyages_in_date.append(voyage)

        working = []
        not_working = []    
        for voyage in voyages_in_date:
            working.append(voyage[5])
            working.append(voyage[6])
            working.append(voyage[7])
            working.append(voyage[8])
            working.append(voyage[9])

        for employee in every_employee:
            if employee[0] not in working:
                not_working.append(employee[0])

        return working, not_working


    