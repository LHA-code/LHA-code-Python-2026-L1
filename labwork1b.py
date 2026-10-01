students = []
courses = []
marks = []

def input_students():
    n = int(input("Enter number of students:"))
    for i in range(n):
        print(f"\n Student {i+1}")
        s_id = input ("Enter ID:")
        name = input ("Enter name::")
        dob = input("Birthday (dd/mm/yyyy)")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    n = int(input("\Enter number of your courses:"))
    for i in range(n):
        print(f"\n Courses {i+1}")
        c_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        courses.append({"id": c_id, "name": name})

def input_marks():
    if not courses or not students:
        print("Please input students and courses first!")
        return
    
    list_courses()
    c_id = input("\nSelect a Course ID to enter marks: ")
    
    # Check if course exists
    if not any(c['id'] == c_id for c in courses):
        print("Course ID not found!")
        return

    if c_id not in marks:
        marks[c_id] = {}

    print(f"\n--- Entering marks for course {c_id} ---")
    for s in students:
        mark = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
        marks[c_id][s['id']] = mark

def list_courses():
    print("\n=== COURSE LIST ===")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n STUDENT LIST")
    for i in students:
        print(f"Number: {i['n']} | Name: {i['name']} | Birthday: {i['dob']}")

def show_marks():
    c_id = input("\nEnter Course ID to view marks: ")
    if c_id not in marks:
        print("No marks recorded for this course yet!")
        return

    print(f"\n=== MARKS FOR COURSE {c_id} ===")
    for s in students:
        s_id = s['id']
        mark = marks[c_id].get(s_id, "N/A")
        print(f"ID: {s_id} | Name: {s['name']} | Mark: {mark}")

def main():
    while True:
        print("\n" + "="*35)
        print("Studen Mark Management")
        print("="*35)
        print("1. input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")
        
        choice = input("Choose an option (0-6): ")
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_marks()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invaid option! Try again.")
    if __name__ == "__main__":
        main()