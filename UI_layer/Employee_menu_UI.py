from Model.employee import Employee
from UI_layer.input_validate import Validate
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper
from prettytable import PrettyTable
import os

class Employee_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
        self.input_validate = Validate()
    

    def get_employees_manager(self):
        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.employees_menu_manager())
            user_selection = self.const.input_selection()

            if user_selection == self.const.ONE: # List all employees
                self.get_list_employees()
                
            elif user_selection == self.const.TWO: # List information of an employee
                self.search_employee()

            elif user_selection == self.const.THREE: # List all employees not working on a given day
                self.not_working_given_day()

            elif user_selection == self.const.FOUR: # List all employees working on a given day
                self.get_working_given_day()

            elif user_selection == self.const.FIVE: # Printable work summary for an employee in a giving week
                self.employees_working_week()

            elif user_selection == self.const.SIX: #register new employee
                self.register_new_employee()
            
            elif user_selection == self.const.SEVEN:
                self.edit_employee()

            elif user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()
    
    def get_employees_menu_shift_manager(self):
        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.employees_menu_shift_manager())
            user_selection = self.const.input_selection()

            if user_selection == self.const.ONE: # List all employees
                self.get_list_employees()
                
            elif user_selection == self.const.TWO: # List information of an employee
                self.search_employee()

            elif user_selection == self.const.THREE: # List all employees not working on a given day
                self.not_working_given_day()

            elif user_selection == self.const.FOUR: # List all employees working on a given day
                self.get_working_given_day()

            elif user_selection == self.const.FIVE: # Printable work summary for an employee in a giving week
                self.employees_working_week()

            elif user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()
        
    def get_list_employees(self):
        employees = self.logic_wrapper.get_all_employees()
        for employee in employees:
            print(employee)
        input("Press ENTER to go back to the menu: ")
    

    def register_new_employee(self):
        """Gets all the information for a new employee and sends to the logic wrapper"""
        ssn = input("SSN: ")
        while self.input_validate.validate_nid(ssn) == False:
            print("Invalid SSN, please try again")
            ssn = input("SSN: ")
        
        name = input("Name: ").lower()
        while self.input_validate.validate_name(name) == False:
            print("Invalid name, please try again")
            name = input("Name: ")
        
        role = input("Role (pilot/crew): ")
        while self.input_validate.validate_role(role) == False:
            print("Invalid role, please try again")
            input("Role (pilot/crew): ")

        rank = input("Rank: ")
        while self.input_validate.validate_rank(role, rank) == False:
            print("Invalid rank, please try again")
            rank = input("Rank: ")

        if role == "pilot":
            license = input("Airplane licence: ")
        else:
            license = "N/A"

        address = input("Address: ").lower()
        while self.input_validate.validate_addres(address) == False:
            print("Invalid address, please try again")
            addres = input("Address: ").lower()

        phone = input("Phone: ")
        while self.input_validate.validate_phone_number(phone) == False:
            print("Invalid phone number, please try again")
            phone = input("Phone: ")

        email = input("Email: ").lower()
        while self.input_validate.validate_email(email) == False:
            print("Invalid email, please try again")
            email = input("Email: ").lower()

        homenumber = input("Home phone number: ")
        if homenumber == "":
            homenumber = "N/A"
        
        
        print("New employee has been registered")
        input("Press ENTER to go back to the menu: ")

        new_employee = self.logic_wrapper.create_employee(ssn, name, role, rank, license, address, phone, email, homenumber)
        return Employee(new_employee)

    def edit_employee(self):
        e = Employee
        nid  = input("What employee whould you like to edit, please enter SSD: ").lower()
        while self.input_validate.validate_nid(nid) == False:
            print("Invalid SSN, please try again")
            nid = input("SSN: ")
        e.nid = nid
        
        role = input("Enter new role (pilot/crew): ").lower()
        while self.input_validate.validate_role(role) == False:
            print("Invalid role, please try again")
            role = input("Enter new role (pilot/crew): ").lower()
        e.role = role

        rank = input("Enter new rank: ").lower()
        while self.input_validate.validate_rank(role, rank) == False:
            print("Invalid rank, please try again")
            rank = input("Enter new rank: ").lower()
        if role == "pilot":
            license = input("Enter new airplane license ").lower()
        else:
            license = "N/A"
        e.rank = rank
        e.licence = license
        
        address = input("Enter new address: ")
        while self.input_validate.validate_addres(address) == False:
            print("Invalid address, please try again")
            address = input("Enter new address: ").lower()
        e.address = address

        phone = input("Enter new phone number: ")
        while self.input_validate.validate_phone_number(phone) == False:
            print("Invalid phone number, please try again")
            phone = input("Enter new phone number: ")
        e.phone_nr = phone

        email = input("Enter new email: ")
        while self.input_validate.validate_email(email) == False:
            print("Invalid email, please try again")
            email = input("Enter new email: ").lower()
        e.email = email


        homephone_nr = input("Enter new homephone number: ")
        if homephone_nr == "":
            homephone_nr = "N/A"
        e.homephone_nr
        updated_employee = self.logic_wrapper.update_employee(e)
        return updated_employee

    def list_voyges_for_employee(self):
        pass

    def search_employee(self): # We need to change this
        nid = input("Enter NID to get Employee: ")
        while self.input_validate.validate_nid(nid) == False or one_employee == False:
            print('Invalid NID, please try again.')
            nid = input('Enter NID to get Employee: ')
            one_employee = self.logic_wrapper.get_one_employee(nid)
            if one_employee == False:
                print("Please enter a NID of an employee ")
        print(one_employee)
        
#        print("List of information of an Employee")
#        info_employee = PrettyTable(['NID','Name','Role','Rank', 'Licence', 'Address', 'Phone_nr', 'Email', 'Homephone_nr'])
#        for i in get_one_employee:
#            info_employee.add_row([i.nid, i.name, i.role, i.rank, i.licence, i.address, i.phone_nr, i.email, i.homephone_nr])
#        print(info_employee)
#        input("Press any key to go back to Employees Menu.")


    def not_working_given_day(self): # We need to change this
        date = input("Enter date (YYYY-MM-DD): ")
        not_working = self.logic_wrapper.check_day(date)
        while not_working == None:
            print("Invalid date")
            date = input("Enter date (YYYY-MM-DD): ")
            not_working = self.logic_wrapper.check_day(date)

        print("List of all employees not working on a given day:")
        not_working_day = not_working[1]
        for employee in not_working_day:
            print(f"Role: {employee.role:<25} SSN: {employee.nid:<17} Name: {employee.name:<13}")
        input("Press ENTER to go back to the menu: ")

    def get_working_given_day(self): # We need to change this
        date = input("Enter date: YYYY.MM.DD ")

        check_day = self.logic_wrapper.check_day(date)
        while check_day == False:
            print("Enter a valid date:")
            date = input("Enter date: YYYY.MM.DD ")
        print("List of employees working on a given day: ")
        working = check_day[0]
        table = PrettyTable(['Date', 'Name', 'NID', 'Destination'])
        for emp in working:
            emp_info = emp[0]
            dest = emp[1]
            table.add_row([date, emp_info.name, emp_info.nid, dest])
        print(table)


    def employees_working_week(self):
        week = input("Enter NID:")