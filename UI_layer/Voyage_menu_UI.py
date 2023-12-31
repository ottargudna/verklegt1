from Model.voyage import Voyage
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper
from UI_layer.input_validate import Validate
import os

class Voyage_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
        self.input_validate = Validate()

    def get_manager_voyage(self):
        print(self.const.voyage_menu_manager())
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # Register a new voyage
            self.get_register_new_voyage()

        elif user_selection == self.const.TWO: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.const.THREE: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.const.FOUR: # List all voyages for a given week
            self.get_list_voyages_for_week()

        elif user_selection == self.const.FIVE: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    def get_shift_superviser_voyage(self):
        print(self.const.voyage_menu_shift_superviser())
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.const.TWO: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.const.THREE: # List all voyages for a given week
            self.get_list_voyages_for_week()

        elif user_selection == self.const.FOUR: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    
    def get_register_new_voyage(self):
        new_voyage = False

        v = Voyage

        while new_voyage == False:
            voyage_number = self.logic_wrapper.generte_voyage_nr()
            departing_from = input("Departing from: ").upper()
            arriving_at = input("Arriving at: ").upper()
            aircraft_id = input("Aircraft ID: ")
            date_out = input("Date out (YYYY.MM.DD): ")
            date_home = input("Date home (YYYY.MM.DD): ")
            captain = input("Captain (press ENTER to leave empty): ")
            if captain == "":
                captain = "N/A"

            copilot = input("Copilot (press ENTER to leave empty): ")
            if copilot == "":
                copilot = "N/A"

            flight_service_manager = input("Flight service manager (press enter to leave empty): ")
            if flight_service_manager == "":
                flight_service_manager = "N/A"

            flight_attendant1 = input("Flight attendant (press enter to leave empty): ")
            if flight_attendant1 == "":
                flight_attendant1 = "N/A"

            flight_attendant2 = input("Flight attendant (press enter to leave empty): ")
            if flight_attendant2 == "":
                flight_attendant2 = "N/A"


            v.voyage_number = voyage_number
            v.dep_from = departing_from 
            v.arr_at = arriving_at
            v.aircraft_id = aircraft_id
            v.date_out = date_out
            v.date_home = date_home
            v.captain = captain
            v.copilot = copilot
            v.flight_service_manager = flight_service_manager
            v.flight_attendant1 = flight_attendant1
            v.flight_attendant2 = flight_attendant2
            
            new_voyage = self.logic_wrapper.create_voyage(v)
            if new_voyage == False:
                print("Something is not right please renter information ")
                input("Press ENTER to retry: ")

        input("Press ENTER to go back to the menu: ")
        return new_voyage



    def get_list_all_voyages(self):
        voyages = self.logic_wrapper.get_all_voyages()
        for voyage in voyages:
            if self.logic_wrapper.check_if_voyages_are_fully_staffed() == False:
                print(f"Voyage number: {voyage.voyage_number:<7}", f"Dep. from: {voyage.dep_from:<5}", f"Ar. at: {voyage.arr_at:<5}\n", f"Plane ID: {voyage.aircraft_id:<13}", f"Date out: {voyage.date_out:<13}", f"Date home: {voyage.date_home:13}", f"{self.const.NOT_STAFFED:<13}")

            else:
                print(f"Voyage number: {voyage.voyage_number:<7}", f"Dep. from: {voyage.dep_from:<5}", f"Ar. at: {voyage.arr_at:<5}\n", f"Plane ID: {voyage.aircraft_id:<13}", f"Date out: {voyage.date_out:<13}", f"Date home: {voyage.date_home:<13}", f"{self.const.FULLY_STAFFED:13}")
        input("Press ENTER to go back to the menu: ")


    def get_list_voyages_for_day(self):
        day = input("Date (YYYY.MM.DD): ")
        voyages = self.logic_wrapper.check_day(day)
        voyages_day = voyages[2]

        for voyage in voyages_day:
            if self.logic_wrapper.check_if_voyages_are_fully_staffed() == False:
                print(f"Voyage number: {voyage.voyage_number:<7}", f"Dep. from: {voyage.dep_from:<5}", f"Ar. at: {voyage.arr_at:<5}\n", f"Plane ID: {voyage.aircraft_id:<13}", f"Date out: {voyage.date_out:<13}", f"Date home: {voyage.date_home:13}", f"{self.const.NOT_STAFFED:<13}")
            else:
                print(f"Voyage number: {voyage.voyage_number:<7}", f"Dep. from: {voyage.dep_from:<5}", f"Ar. at: {voyage.arr_at:<5}\n", f"Plane ID: {voyage.aircraft_id:<13}", f"Date out: {voyage.date_out:<13}", f"Date home: {voyage.date_home:<13}", f"{self.const.FULLY_STAFFED:13}")
        input("Press ENTER to go back to the menu: ")   


    def get_list_voyages_for_week(self):
        date = input("Date (YYYY.MM.DD): ")
        voyages = self.logic_wrapper.check_week(date)
        voyages_week = voyages[2]

        for voyage in voyages_week:
            if self.logic_wrapper.check_if_voyages_are_fully_staffed() == False:
                print(f"Voyage number: {voyage.voyage_number:<7}", f"Dep. from: {voyage.dep_from:<5}", f"Ar. at: {voyage.arr_at:<5}\n", f"Plane ID: {voyage.aircraft_id:<13}", f"Date out: {voyage.date_out:<13}", f"Date home: {voyage.date_home:13}", f"{self.const.NOT_STAFFED:<13}")
            else:
                print(f"Voyage number: {voyage.voyage_number:<7}", f"Dep. from: {voyage.dep_from:<5}", f"Ar. at: {voyage.arr_at:<5}\n", f"Plane ID: {voyage.aircraft_id:<13}", f"Date out: {voyage.date_out:<13}", f"Date home: {voyage.date_home:<13}", f"{self.const.FULLY_STAFFED:13}")
        input("Press ENTER to go back to the menu: ") 


    def get_list_voyages_of_employee(self):
        ssn = input("SSN: ")
        while self.input_validate.validate_nid(ssn) == False:
            print("Invalid SSN, please try again")
            ssn = input("SSN: ")
        
        date = input("Enter date (YYYY.MM.DD): ")
        
        shifts = self.logic_wrapper.get_week_work(ssn, date)
        while shifts == False:
            print("Enter a valid date:")
            date = input("Enter date (YYYY.MM.DD): ")
            shifts = self.logic_wrapper.get_week_work(ssn, date)
        
        if shifts == []:
            print("Employee is not working here, please try again")
            input("Press ENTER to go back to the menu: ")
        else:
            for shift in shifts:
                print(f"date out: {shift.date_out:<10}   date home: {shift.date_home:<10}   dep from: {shift.dep_from:<3}   arr at: {shift.arr_at:<3}")
            input("Press ENTER to go back to the menu: ")



