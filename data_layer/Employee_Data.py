import csv
from Model.employee import Employee

class Employee_Data:
    def __init__(self) -> None:
        self.file_name = "files/employees.cvs"

    def get_all_employees(self):
        list = []
        with open(self.file_name, newline= " ", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Employee(row["name"], row ["social_security_number"], row ["home_address"], row ["phone_number"]))
        return list 
    
    def create_employee(self, employee):
        with open(self.file_name, "w", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["name"," social_security_number","home_address", "phone_number"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames)
