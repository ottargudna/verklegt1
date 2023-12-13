from UI_layer.mainmenu_ui import MainMenu_ui
main_menu = MainMenu_ui()


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
    main_menu.main()

if __name__ == "__main__":
    main_menu.main()