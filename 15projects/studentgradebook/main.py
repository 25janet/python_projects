#Concepts Used: Lists, Dictionaries
#Tasks:

#Add students with their names and marks in multiple subjects.

#Calculate average marks per student.

#Display top-scoring student(s).

#Allow updating or deleting a student.
def calculate_grade(avg):
    if avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60 :
        return 'C'
    elif avg >= 50:
        return 'D'
    elif avg >= 40:
        return 'E'
    else :
        return 'F'
def add_students():
    name = input("Enter the student name: ")
    subjects = ["Maths", "Chemistry","English", "Physics"]
    marks = {}
    for subject in subjects:
        score = int(input(f"Enter marks for {subject}: "))
        marks[subject] = score
    total = sum(marks.values())
    average = total/len(subjects)
    grade = calculate_grade(average)
    student = {
        'name':name,
        'marks': marks,
        'total':total,
        'average': average,
        'grade':grade
    }
    return student
students = []
students.append(add_students())
for s in students:
     print(f"\n🎓 Student: {s['name']}")
     print(f"📚 Marks: {s['marks']}")
     print(f"📊 Total: {s['total']}, Average: {s['average']:.2f}, Grade: {s['grade']}")

