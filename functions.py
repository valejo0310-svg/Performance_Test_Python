register = []
def students_registration ():
    """
    This function will allow the user to register all the students data, including:
    - ID (Personal identification)
    - Name
    - Age
    - Course or program 
    - Status (active / inactive)
    For this function to work it'll be used dictionaries and lists (Called on main)
    """
      #Loop used to ask the user to enter the student information
    #It keeps track of any kind of error that may appear
    continuar = "yes"

    while continuar != "no":
        print("=" * 60)

        # Validate name — cannot be empty or contain numbers
        try:
            Id = int (input ("\nPlease enter the student ID (numb):"))
            if not Id:
                print ("This field cannot be empty")
                continue
        except ValueError:
            print ("Enter the right value.")
            continue
        name = input ("\nPlease enter the student name: ").strip()
        if not name:
                print ("\nThis field cannot be empty")
                continue
        try:
            age = int (input("\nPlease enter the student age:"))
            if not age:
                print ("\nThis field cannot be empty")
                continue
        except ValueError:
            print ("Please enter the roght values")
            continue
        course = input ("\n Please enter the student course:").strip()
        if not course:
                print ("\n This field cannot be empty")
                continue 
        status = input ("\nPlease enter the student status (active/inactive):").strip()
        if status not in ( "active" or "inactive"):
            print ("Please choose between the options")
            continue
        if not status:
            print ("This field cannot be empty")
            continue
            
        #Dictionary used to store all the information of the students to be used later on the code.        
        students={
            "ID" : Id,
            "Name" : name,
            "Age" : age,
            "Course" : course,
            "Status" : status
        }
        register.append(students)
        print(f"\nStudent '{name}' registered successfully!")
        
        #Question made to close de loop while if "no"
        question = input("Do you want to add another student? (yes/no): ").lower().strip()
        if question == "no":
            break

# ------------------------------------------------------------------------------------------------------------------------





def show_students ():
    """
    Function created to show the user all the students registered on the system.
    It works using a for loop that allows the system to search on the register list
    and show all the registratiton data.
    """
    #Used to show if there are no students registered
    if not register:
        print("No students registered.")
        return
    print("\n--- STUDENTS ---")
    for students in register: #For loop used to show all the students 
        print(f"""
------------------------------
ID       : {students ['ID']}
Name     : {students['Name']}
Age      : {students['Age']}
Course   : {students['Course']}
Status   : {students['Status']}
        """)
        print ()

# ---------------------------------------------------------------------------------------------------------------------------




def search_student (students):
    """
    Function made to allow the user to search for the students, it also uses a for loop
    that allows the system to see if the student search has been registered previously
    if not, it shows a message saying that there are no students registered under that ID 
    """
    student_id = int (input ("\n Please enter the student ID: "))
    if not student_id:
        print ("FIeld cannot be empty")
        return
    if not register:
        print ("\nNo student registered")
        return
    #Input to ask for the name tp be searched
    

    for students in  register: #For loop to show the student 
        if students ['ID'] == student_id:
            print (f"""
ID       : {students ['ID']}
Name     : {students['Name']}
Age      : {students['Age']}
Course   : {students['Course']}
Status   : {students['Status']}""")
            return students
        
    print(f"Student'{ student_id }' not found.") #Message shown if the students hasn't been registered
    return None

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




def update_student ():
    """
    Function created to update the students on the system, for it to work it's necessary to ask the user for the student ID they will change
    and after they put it in the system will look if it has been registered, if it is it will show the information previously registered and it'll create new variables
    to store the new data, after the clients add the new information the old one will be redefined as that.
    In case the ID has not been registered it will shoe the user a message saying the student has not been found.
    """
    id = int(input("Enter the student to update: ")) #ID input to search in the list "register"
    if not id:
        print("Name cannot be empty.")
        return
    
    for students in  register:
        if students["ID"] == id:  
   
            print(f"""
Current information:
ID       : {students ['ID']}
Name     : {students['Name']}
Age      : {students['Age']}
Course   : {students['Course']}
Status   : {students['Status']}
""")#Old info
            updated_name = input("New name (leave blank to keep current): ").strip()#new variables
            if updated_name:
                try:
                    new_name = (updated_name)
                    students["Name"] = new_name  
                    print("Name updated!")
                except ValueError:
                    print("Invalid name.")

            updated_age = int(input("New age (Have to update): ")).strip()#new variables
            if updated_age:
                try:
                    new_age = int(updated_age)
                    students["Age"] = new_age 
                    print("Age updated!")
                except ValueError:
                    print("Invalid age.")
            updated_course = input("New course(leave blank to keep current): ").strip()#new variables
            if updated_course:
                try:
                    new_course = (updated_course)
                    students["Course"] = new_course
                    print("Course updated!")
                except ValueError:
                    print("Invalid course.")
            updated_status = input("New status(leave blank to keep current): ").strip()#new variables
            if updated_status:
                try:
                    new_status = (updated_status)
                    students["Status"] = new_status
                    print("Status updated!")
                except ValueError:
                    print("Invalid status.")
            

            return

    print(f"Student '{id}' not found.")
    return None

#-----------------------------------------------------------------------------------------------------------------------------------------------



def delete_student():
    """
    Delete a product from the register by name after user confirmation.

    Searches for an exact name match (case-insensitive). Prompts for
    confirmation before removing. If the user cancels, inventory is unchanged.
    """
    id = int (input("\nEnter the name of the student to delete: "))

    # Validate delete target name
    if not id:
        print(" Field cannot be empty.")
        return

    for students in register:
        if students["ID"]== id:

            confirm = input(f" Are you sure you want to delete '{students['ID']}'? (yes/no): ").strip().lower()

            # Validate confirmation — only accept 'yes' or 'no'
            if confirm not in ("yes", "no"):
                print(" Please type 'yes' or 'no'. Deletion cancelled.")
                return

            if confirm == "yes":
                register.remove(students)
                print(f" Product '{students['ID']}' deleted successfully!\n")
            else:
                print(" Deletion cancelled.\n")
            return # Stop after finding the student, whether deleted or not

    print(f" student '{id}' not found.\n")
            

