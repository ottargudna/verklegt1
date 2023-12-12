import csv
from Model.employee import Employee

class Employee_Data:
    def __init__(self) -> None:
        self.file_name = "Files/crew.csv"


    def get_all_employees(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Employee(row["nid"], row ["name"], row ["role"], row ["rank"], row ["licence"], row ["address"], row ["phone_nr"], row ["email"], row ["homephone_nr"]))
        return list
    
    def create_employee(self, employee):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["nid","name","role", "rank","licence", "address", "phone_nr"]
            writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name, "role": employee.role, "rank": employee.rank, "licence":employee.licence, "address": employee.address, "phone_nr": employee.phone_nr, "email": employee.email, "homephone_nr":employee.homephone.nr})


    def update_employee(self, updated_employee):
        employees = self.get_all_employees() 

        for employee in employees: 
            if employee.nid == updated_employee.nid:
                #update the employee information
                employee.role = updated_employee.role
                employee.rank = updated_employee.rank
                employee.address = updated_employee.address
                employee.phone_nr = updated_employee.phone_nr

                with open(self.file_name, "w", newline = "", encoding = "utf-8") as csvfile:
                    fieldnames = ["nid", "name", "role", "rank", "address", "phone_nr"]
                    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                    writer.writeheader()
                    
                    for employee in employees:
                        writer.writerow({"role": employee.role, "rank": employee.rank, "address": employee.address, "phone_nr": employee.phone_nr})


                
