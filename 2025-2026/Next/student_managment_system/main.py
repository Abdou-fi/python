from students import add_student, view_students, search_students, remove_students
from file_handler import load_students, save_students
def menu(): 
    print ("\n==========MENU==========")   
    print("1. Add student") 
    print("2. View student") 
    print("3. Search student") 
    print("4. Remove student") 
    print("5. Exit")
    print ("==========================")   

def main(): 
    print("Welcome to the Student Record Management System!") 
    print("Loading student records from students.csv... ", end = "")
    
    students = load_students() 
    print("Done!")
    
    while True: 
        menu() 
        choice = input("Enter your choice: ")
        if choice == "1": 
            add_student(students) 
            save_students(students)
        elif choice == "2": 
            view_students(students)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            remove_students(students)
            save_students(students)
        elif choice == "5": 
            print("Goodbye!")
            break
        
if __name__ == "__main__":    
    main()

        