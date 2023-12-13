
from logic_layer.airplane_logic import Airplane_Logic
from data_layer.data_wrapper import Data_Wrapper

data_class = Data_Wrapper()
check_plane_ins = input('enter plane ins')

logic_class = Airplane_Logic(data_class)
result = logic_class.airplane_already_exist(check_plane_ins)

print(result)
    

    def create_employee(self, employee):
        """Takes in airplane object and forwards it to the data layer"""
        check_existing_employee = self.employee_already_exist(employee)
        if check_existing_employee == False:
            self.data_wrapper.create_employee(employee)
        else:
            return False
        #if false enter another name

    def get_all_employees(self):
        """Gets all airplane"""
        self.data_wrapper.get_all_employees()

    def employee_already_exist(self, employee):
        every_employer = self.datawrapper.get_all_airplanes()
        for employer in every_employer:
            if employee[0] == employer.nid:
                return True 
            
            # already exists