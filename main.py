from functions import *

students = {1}
menu = True
while menu:
    """
    Menu used to show all the possible options the user can choose, it's also used to call all the functions    
    """
    try:
        option = int (input(f"""
    --------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: """))
        if option == 1:
             students_registration()
        elif option == 2:
            show_students()
        elif option == 3:
            search_student (students)
        elif option == 4:
            update_student ()
        elif option == 5:
            delete_student()
        elif option == 6:
            menu = False
            print ("Exiting...")
        else:
            print ("invalid option")
    except ValueError:
        print ("invalid value")


