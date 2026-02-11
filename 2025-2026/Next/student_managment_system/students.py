def add_student(students): 
    name = input("Enter student name: ").strip() 
    if not name: 
        print("Error: Name cannot be empty") 
        return

    roll_input = input("Enter student roll: ").strip() # strip() is only for strings 
    if not roll_input.isdigit():
        print("Error: Roll must be an integer")
        return

    roll = int(roll_input)


    # duplicate roll check 
    for s in students: 
        if s["roll"] == roll: 
            print("Error: Roll number already exists for another student.") 
            return

    email = input("Enter your email: ")
    if not email: 
        print("Error: Email cannot be empty")
        return

    department = input("Enter your department: ") 
    if not department: 
        print("Error: Department cannot be empty")
    return
    students.append({
        "name": name,
        "roll": roll,
        "email": email,
        "department": department
    })
    print("Student added successfully!")
    
def view_students(students): 
    if not students: 
        print("No students found.") 
        return
    print("\nStudent Records:") 
    for s in students: 
        print(f"Name: {s['name']}, Roll: {s['roll']}, Email: {s['email']}, Department: {s['department']}")
def search_students(students):
    roll_input = input("Enter student roll to search: ").strip()
    if not roll_input.isdigit():
        print("Error: Roll must be an integer")
        return

    roll = int(roll_input)
    for s in students: 
        if s["roll"] == roll: 
            print(f"Student found: Name: {s['name']}, Roll: {s['roll']}, Email: {s['email']}, Department: {s['department']}") 
            return
    print("Student not found.")
def remove_students(students):
    roll_input = input("Enter student roll to remove: ").strip()
    if not roll_input.isdigit():
        print("Error: Roll must be an integer")
        return

    roll = int(roll_input)
    for s in students: 
        if s["roll"] == roll: 
            students.remove(s)
            print("Student removed successfully!")
            return
    print("Student not found.")
 

        