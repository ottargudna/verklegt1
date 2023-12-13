BORDER = 109 * "*"
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"

MAIN_MENU = f"""
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
                                [{TWO}] Display Hours
{BORDER}
        """
AIRPLANE_MENU = f"""
                                [{ONE}] Register airplane
                                [{TWO}] Edit airplane
{BORDER}
        """
DESTINATIONS_MENU = f"""
                                [{ONE}] Register a new destination
                                [{TWO}] Edit destinations
                                [{THREE}] List all destinations
{BORDER}
        """
STAFF_MENU = f"""
                                [{ONE}] Employees
                                [{TWO}] Pilot
                                [{THREE}] Crew
        {BORDER}
        """
PILOT_MANAGER_MENU = f"""
                                [{ONE}] Edit information of a pilot
                                [{TWO}] Search for a pilot
                                [{THREE}] List all pilots
{BORDER}
        """
CREW_MANAGER_MENU = f"""
                                [{ONE}] Edit information of a crew member
                                [{TWO}] Search for a crew member
                                [{THREE}] List all crew members
{BORDER}
        """
PILOT_SHIFT_SUP_MENU = f"""
                                [{ONE}] Search for a pilot
                                [{TWO}] List all pilots
{BORDER}
        """
CREW_SHIFT_SUP_MENU = f"""
                                [{ONE}] Search for a crew member
                                [{TWO}] List all crew members
{BORDER}
        """
EMPLOYEES_MENU = f"""
                                [{ONE}] List all employees
                                [{TWO}] List information of an employee
                                [{THREE}] List all employees not working on a given day
                                [{FOUR}] List all employees working on a given day
                                [{FIVE}] Printable work summary for an employee in a giving week
                                [{SIX}] Register new employee
{BORDER}
        """
VOYAGE_MANAGER_MENU = f"""
                                [{ONE}] Register a new voyage
                                [{TWO}] List all voyages
                                [{THREE}] List all voyages for a given day
                                [{FOUR}] List all voyages for a given week
                                [{FIVE}] List all voyages of a staff member for a given week
{BORDER}
        """
VOYAGE_SHIFT_SUPER_MENU = f"""
                                [{ONE}] List all voyages
                                [{TWO}] List all voyages for a given day
                                [{THREE}] List all voyages for a given week
                                [{FOUR}] List all voyages of a staff member for a given week
{BORDER}
        """
