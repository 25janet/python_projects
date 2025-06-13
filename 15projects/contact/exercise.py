students = {}
def calculate_grade(avg):
    if avg >= 80 :
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    elif avg >= 40:
        return 'E'
    else:
        return 'F'

def add_students():
    name = input("Enter the name of the student: ")
    subjects = ["Maths", "English" , "Kiswahili" , "Chem"]
    total = 0
    mark = []
    for subject in subjects:
        marks = int(input("Enter the marks of the subjects: "))
        total += marks
        mark.append(marks)

    average = total/len(subjects)
    grade = calculate_grade(average)
    students[name] = {
        "Name": name,
        "Subjects": subjects,
        "Average": average,
        "Grade": grade
    }
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

    
def top_students():
    if not students:
        print("It is empty.")
    highest = max(students,key=lambda name: students[name]['Average'])
    top_info = students[highest]
    print("\n🏆 Student with the highest average:")
    print(f"Name: {highest}")
    print(f"Average: {top_info['Average']}")
    print(f"Grade: {top_info['Grade']}")

while True:
    add_students()
    more = input("keep adding more students(y/n): ")
    if more != 'y':
        break
top_students()

