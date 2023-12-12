# from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.mainmenu_ui import MainMenu_ui
# from UI_layer.Destinations_menu_UI import Destiantions_menu_ui
# from UI_layer.Airplane_menu_UI import Airplane_menu_ui
# from UI_layer.Voyage_menu_UI import Voyage_menu_ui

main_menu = MainMenu_ui()
# employee_menu = Employee_menu_ui()
# destinations_menu = Destiantions_menu_ui()
# airplane_menu = Airplane_menu_ui()
# Voyage_menu = Voyage_menu_ui()

QUIT = "q"
BACK = "b"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"

def input_prompt():
    return input("Enter your selection: ").lower()

def main(): # I will change the name 
    while True:
        print(main_menu.ascii_nanair)
        print(main_menu.main_menu)
        print(main_menu.main_menu_options)
        user_selection = input_prompt()

        if user_selection == QUIT:
            quit()
        
        elif user_selection == SELECTION_ONE: # Manager
            print(main_menu.ascii_nanair)
            print(main_menu.manager_and_shift_supervisor_menu)
            print(main_menu.options)
            user_selection = input_prompt()

            if user_selection == SELECTION_ONE: # Airplanes
                print(main_menu.ascii_nanair)
                print(airplane_menu.manager_menu)
                print(main_menu.options)
                user_selection = input_prompt()

                if user_selection == SELECTION_ONE: # Register airplane
                    pass

                elif user_selection == SELECTION_TWO: # Edit airplane
                    pass

                elif user_selection == SELECTION_THREE: # List airplanes
                    print(main_menu.ascii_nanair)
                    print(airplane_menu.list_menu)
                    print(main_menu.options)
                    user_selection = input_prompt()

                elif user_selection == QUIT:
                    quit()
                
                else: # Go back
                    pass
            
            elif user_selection == SELECTION_TWO: # Destinations
                pass

            elif user_selection == SELECTION_THREE: # Employees
                pass

            elif user_selection == SELECTION_FIVE: # Voyages
                pass

            elif user_selection == QUIT:
                quit()
            
            else: # Go back
                pass

        elif user_selection == SELECTION_TWO: # Shift supervisor
            print(main_menu.ascii_nanair)
            print(main_menu.manager_and_shift_supervisor_menu)
            print(main_menu.options)
            user_selection = input_prompt()

            if user_selection == SELECTION_ONE: # Airplanes
                print(airplane_menu.ascii_nanair)
                print(airplane_menu.list_menu)
                print(main_menu.options)
                user_selection = input_prompt
            
            elif user_selection == SELECTION_TWO: # Destinations
                pass

            elif user_selection == SELECTION_THREE: # Employees
                pass

            elif user_selection == SELECTION_FOUR: # Flights
                pass

            elif user_selection == SELECTION_FIVE: # Voyages
                pass

            elif user_selection == QUIT:
                quit()
            
            else: # Go back
                pass

        elif user_selection == SELECTION_THREE: # Employee
            print(main_menu.ascii_nanair)
            print(main_menu.employee_name())
            print(main_menu.employee_menu)
            print(main_menu.options)
            user_selection = input_prompt()

            if user_selection == SELECTION_ONE: # Display Shifts
                pass

            elif user_selection == SELECTION_TWO: # Display Hours
                pass

            elif user_selection == QUIT:
                quit()
            
            else: # Go back
                pass

if __name__ == "__main__":
    #main()
    main_menu.main()