BORDER = 109 * "="
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
SEVEN = "7"

MAIN_MENU_CHOICES = f"""
                                What kind of staff member are you?
                                
                                [{ONE}] Manager
                                [{TWO}] Shift Supervisor
                                [{THREE}] Employee
{BORDER}
        """
MAIN_MENU_FOOTER = f"""
                                [{QUIT}]uit
        """
FOOTER = f"""
                                [{BACK}]ack to main menu     [{QUIT}]uit
{BORDER}
        """
LOGO = f"""
{BORDER}
                              _    _          _    _       __     _____  _____
                __|__        |  \ | |   __ _ |  \ | |     /  \   |_   _||  _  \         __|__ 
            ---o-(_)-o---    |   \| | / __' ||   \| |    / /\ \    | |  | |_|  |    ---o-(_)-o---
                             | |\   || |__| || |\   |   /  __  \  _| |_ |  _ _/      
                             |_| \__| \___,_||_| \__|  /__/  \__\|_____||_| \_\ 
{BORDER}
        """
MANAGER_CHOICES = f"""
                                Manager menu

                                [{ONE}] Airplanes
                                [{TWO}] Destinations
                                [{THREE}] Employees
                                [{FOUR}] Voyages

{BORDER}
        """
SHIFT_SUPERVISOR_MENU = f"""
                                Shift supervisor menu

                                [{ONE}] Destinations
                                [{TWO}] Employees
                                [{THREE}] Voyages

{BORDER}
        """
EMPLOYEE_MENU = f"""
                                Employee menu

                                [{ONE}] Display Shifts

{BORDER}
        """
AIRPLANE_MENU = f"""
                                Airplane

                                [{ONE}] Register airplane
                                [{TWO}] List all airplanes

{BORDER}
        """
DESTINATIONS_MENU = f"""
                                Destinations

                                [{ONE}] Register a new destination
                                [{TWO}] Edit destinations
                                [{THREE}] List all destinations

{BORDER}
        """
EMPLOYEES_MENU_MANAGER = f"""
                                Employees

                                [{ONE}] List employees
                                [{TWO}] List information of an employee
                                [{THREE}] List all employees not working on a given day
                                [{FOUR}] List all employees working on a given day
                                [{FIVE}] Printable work summary for an employee in a giving week
                                [{SIX}] Register new employee
                                [{SEVEN}] Edit employee

{BORDER}
        """
LIST_EMPLOYEES_MENU = f"""
                                List employees
                                
                                [{ONE}] List all employees
                                [{TWO}] List all pilots
                                [{THREE}] List all crew members

{BORDER}
        """
EMPLOYEES_MENU_SHIFT_MANAGER = f"""
                                Employees

                                [{ONE}] List all employees
                                [{TWO}] List information of an employee
                                [{THREE}] List all employees not working on a given day
                                [{FOUR}] List all employees working on a given day
                                [{FIVE}] Printable work summary for an employee in a giving week

{BORDER}
        """
VOYAGE_MANAGER_MENU = f"""
                                Voyages

                                [{ONE}] Register a new voyage
                                [{TWO}] List all voyages
                                [{THREE}] List all voyages for a given day
                                [{FOUR}] List all voyages for a given week
                                [{FIVE}] List all voyages of a staff member for a given week

{BORDER}
        """
VOYAGE_SHIFT_SUPER_MENU = f"""
                                Voyages

                                [{ONE}] List all voyages
                                [{TWO}] List all voyages for a given day
                                [{THREE}] List all voyages for a given week
                                [{FOUR}] List all voyages of a staff member for a given week

{BORDER}
        """

def main_menu():
    return LOGO + MAIN_MENU_CHOICES + MAIN_MENU_FOOTER

def manager_menu():
    return LOGO + MANAGER_CHOICES + FOOTER

def shift_supervisor_menu():
    return LOGO + SHIFT_SUPERVISOR_MENU + FOOTER

def employee_menu():
    return LOGO + EMPLOYEE_MENU + FOOTER

def airplane_menu():
    return LOGO + AIRPLANE_MENU + FOOTER

def destinations_menu():
    return LOGO + DESTINATIONS_MENU + FOOTER

def employees_menu_manager():
    return LOGO + EMPLOYEES_MENU_MANAGER + FOOTER

def list_employees_menu():
    return LOGO + LIST_EMPLOYEES_MENU + FOOTER

def employees_menu_shift_manager():
    return LOGO + EMPLOYEES_MENU_SHIFT_MANAGER + FOOTER

def voyage_menu_manager():
    return LOGO + VOYAGE_MANAGER_MENU + FOOTER

def voyage_menu_shift_superviser():
    return LOGO + VOYAGE_SHIFT_SUPER_MENU + FOOTER

def input_selection():
    return input("Enter your selection: ")
