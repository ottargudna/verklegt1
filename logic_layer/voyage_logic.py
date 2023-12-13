from Model.voyage import Voyage
from logic_layer.flights_logic import Flights

class Voyage_Logic:
    
    def __init__(self) -> None:

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        self.data_wrapper.create_voyage(voyage)

    def get_all_voyages(self):
        self.data_wrapper.get_all_voyages()

    def is_employee_available(self, employee ,start_date, end_date):
        every_voyage = self.data_wrapper.get_all_voyages()
        

        if (self.voyages[4] <= end_date) and (self.voyages[3] >= start_date):
            return True
        else:
            return False

    
    ''' def schedule_employee(employee, start_date, end_date, other_details):
        
        if is_employee_available(employee, start_date, end_date):
        # Update the DataFrame with new assignment
        # Add your logic here to update the DataFrame
            pass
        else:
            return False '''

       
        #check if captain is workin else where
               
       
        ''' for voyage[5] in every_voyage:
            if self.date in (voyage[3],voyage[4]):
                return False
            else:
                return True '''
                

        #check if copilot


        #check if fsm

        #check fa1

        #check fa2

    def list_worktrips(self):

    

    