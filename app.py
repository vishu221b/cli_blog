from database import Database
from prettytable import PrettyTable
from menu import Menu


Database.initialize()
print("-"*20 + "Welcome to the CLI Blog" + "-"*20, end="\n" + "-"*63 + "\n")
user = input(
        "Enter your author name (this name is CASE SENSITIVE): "
    )
while True:
    main_menu = PrettyTable(['S.No.', 'Action'])
    main_menu.add_row(["1", "Go to the main menu"])
    main_menu.add_row(["2", "Exit"])
    print(main_menu)
    user_selection = input("Enter your selection(1/2): ")
    if user_selection == "1":
        menu = Menu(user)
        flow = menu.run_menu()
    elif user_selection == "2":
        print("\nThank you for using CLI blog!! Hope you had a great experience.\n\nExiting...")
        break
    else:
        print("\nInvalid input detected, please make a valid selection...\n")
