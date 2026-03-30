# Performance Test Python

Simple python program to allow the user to register, see, search, update and delete students, that they might new to keep track of

## > How can we run the program? 

To be able to run this program you need to:
- Have a enviroment to run code (It can be Visual Studio Code)
- Have Python 3.14.3 installed on your computer
- HAve Github and your Visual loggged in so you can copy this repository

##  > Wich functions does this program allows?

This program allows the user to:
- 1. Register as much students the user wants using: ID, names, ages, courses and status
- 2. Allows the user to see al the students that have been registered
- 3. Search the students by their ID so it's easier to access to their information
- 4. To update the students information and automatically update it, so if they want to see everything again the finromation will be updated
- 5. Allos the user to delete the students information from everywhere
 
## Flowchart
<img width="1011" height="1091" alt="Diagrama sin título drawio" src="https://github.com/user-attachments/assets/3cfa073e-2a27-49f9-8045-1d8bb2f1571f" />


## > How does it run like:

(This a copy-paste of the terminal from Visual Studio Code)


```bash
jhgjh
``
--------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: 1
============================================================

Please enter the student ID (numb):1234

Please enter the student name: valery

Please enter the student age:17

 Please enter the student course:lenguage

Please enter the student status (active/inactive):active

Student 'valery' registered successfully!
Do you want to add another student? (yes/no): yes
============================================================

Please enter the student ID (numb):4321

Please enter the student name: Alejo

Please enter the student age:23

 Please enter the student course:cience

Please enter the student status (active/inactive):inactive

Student 'Alejo' registered successfully!
Do you want to add another student? (yes/no): no

    --------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: 2

--- STUDENTS ---

------------------------------
ID       : 1234
Name     : valery
Age      : 17
Course   : lenguage
Status   : active
        


------------------------------
ID       : 4321
Name     : Alejo
Age      : 23
Course   : cience
Status   : inactive
        


    --------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: 3

 Please enter the student ID: 4321

ID       : 4321
Name     : Alejo
Age      : 23
Course   : cience
Status   : inactive

    --------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: 5 

Enter the name of the student to delete: 1234
 Are you sure you want to delete '1234'? (yes/no): yes
 Product '1234' deleted successfully!


    --------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: 2

--- STUDENTS ---

------------------------------
ID       : 4321
Name     : Alejo
Age      : 23
Course   : cience
Status   : inactive
        


    --------------------------MENU--------------------------
    1. Student registration
    2. Show students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit        
    Select an option: 6
Exiting...
