from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.Destinations_menu_UI import Destiantions_menu_ui
from UI_layer.Airplane_menu_UI import Airplane_menu_ui
from UI_layer.Voyage_menu_UI import Voyage_menu_ui


class MainMenu_ui:

    def __init__(self) -> None:
        self.employee_menu = Employee_menu_ui()
        self.destinations_menu = Destiantions_menu_ui()
        self.airplane_menu = Airplane_menu_ui()
        self.voyage_menu = Voyage_menu_ui()

    def main_screen(self):
        pass

    def main_menu(self):
        main_menu_apperance = '''

            ====================================================== 
            |        Which kind of staff member are you?         | 
            ======================================================
                        
            [1] Manager  

            [2] Shift Supervisor 

            [3] Employee       

            

            [Q] Quit
    
            ======================================================

'''

