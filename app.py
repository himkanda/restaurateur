import actions
import choices
from commonMethods import main_menu

try:
    # Main program loop
    while True:
        print("\n ~~~~~~~~~ RESTAURANT MANAGEMENT ~~~~~~~~~ ")
        # menu options
        print("1. View Menu")
        print("2. Add items in Menu")
        print("3. Edit Menu items")
        print("4. Delete Menu items")
        # order options
        print("5. Create Order")
        print("6. Add items to Order")
        print("7. Fetch Orders")
        print("9. Generate Bill")
        # exit
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            choices.choice1()
        elif choice == 2:
            choices.choice2()
        elif choice == 3:
            choices.choice3()
        elif choice == 4:
            choices.choice4()
        elif choice == 5:
            choices.choice5()
        elif choice == 6:
            choices.choice6()
        elif choice == 7:
            choices.choice7()
        elif choice == 9:
            choices.choice9()
        elif choice == 10:
            break
        else:
            print("***ERROR*** -> Incorrect input!")
            break
        main_menu()

finally:
    # Close the database connection
    print("INFO -> Closing the DB connection...")
    actions.db.close()
    print("INFO -> Closed the DB connection!")
