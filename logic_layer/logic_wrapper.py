

from data_layer.data_wrapper import Data_Wrapper
from logic_layer.airplane_logic import Airplane_Logic
from logic_layer.destinations_logic import Destinations_Logic
from logic_layer.employee_logic import Employee_Logic
from logic_layer.voyage_logic import Voyage_Logic


class Logic_Wrapper:
    def __init__(self) -> None:
        self.data_wrapper = Data_Wrapper()
        self.employee_logic = Employee_Logic(self.data_wrapper)
        self.airplane_logic = Airplane_Logic(self.data_wrapper)
        self.destination_logic = Destinations_Logic(self.data_wrapper)
        self.voyage = Voyage_Logic(self.data_wrapper)


    """Here comes all functions sem that are used in the logic layer and returns them"""

    #Employees
    def create_employee(self, employee):
        self.employee_logic.create_employee(employee)

    def get_all_employees(self):
        self.employee_logic.get_all_employees()

    def edit_employee(self, employee):
        self.employee_logic.edit_employee(employee)

    def get_one_employee(self, nid):
        '''searches for one employee'''
        self.employee_logic.get_one_employee(nid)
    
    def get_week_work(self, nid, date):
        '''Gets a list of voyages that the nid is working on'''
        self.employee_logic.get_week_work(nid, date)
    
    def check_if_voyages_are_fully_staffed(self):
        '''Cheks if user has a voyage where there is not an a employee in it'''
        self.employee_logic.check_if_voyages_are_fully_staffed()
      


    #Airplane
    def create_airplane(self, airplane):
        return self.airplane_logic.create_airplane(airplane)

    def get_all_airplanes(self):
        return self.airplane_logic.get_all_airplanes()

    #Destinations

    def create_destination(self, destination):
        """Takes in destination object and forwards it to the data layer"""
        self.destination_logic.create_destination(destination)

    def get_all_destinations(self):
        """Gets all destinations"""
        return self.destination_logic.get_all_destinations()

    def edit_destanations(self, destination):
        '''Takes in name of an destination and forwards it to data layer'''
        self.destination_logic.update_destination(destination)
        
    #Voyage
    def get_all_voyages(self):
        self.voyage_logic.get_all_voyages()

    def create_voyage(self, voyage):
        """Takes in voyage object and forwards it to the data layer"""
        self.voyage_logic.create_voyage(voyage)

    def check_day(self, date):
        '''checks if people are working, not working on perticuler 
        day and also gets every voyages on that day'''
        self.voyage_logic.check_day(date)

    def check_week(self, date): #enter the first day in that week
        '''checks if people are working, not working on perticuler 
        week and also gets every voyages on that week'''
        self.voyage_logic.check_week(date)

    def generte_voyage_nr(self):
        '''Create voyage number, counts all voyages and then gives it a number'''
        self.voyage.generte_voyage_nr()




