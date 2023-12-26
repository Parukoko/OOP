class Student:
    def __init__(self, student_id, student_name, student_year):
        self.student_id = student_id
        self.student_name = student_name
        self.student_year = student_year
        self.mentor_id = None

    def set_mentor(self, mentor_id):
        self.mentor_id = mentor_id

    def find_mentors(self):
        mentors = []
        current_student = self.find_student_by_id(self.mentor_id)
        while current_student:
            mentors.append((current_student.student_id, current_student.student_name))
            current_student = self.find_student_by_id(current_student.mentor_id)
        return mentors

    def find_student_by_id(self, student_id):
        for student in students:
            if student.student_id == student_id:
                return student
        return None

    def are_students_in_same_line(self, student_x, student_y):
        mentors_x = set(self.find_student_by_id(student_x).find_mentors())
        mentors_y = set(self.find_student_by_id(student_y).find_mentors())
        return bool(mentors_x.intersection(mentors_y)) and abs(self.find_student_by_id(student_x).student_year - self.find_student_by_id(student_y).student_year) == 1

# Instances
students = [
    Student("63010978", "Ann", 4),
    Student("64010456", "Alex", 3),
    Student("65010947", "Alean", 2),
    Student("66010345", "Alix", 1),
]

students[1].set_mentor("63010978")
students[2].set_mentor("64010456")
students[3].set_mentor("65010947")

# Function #3
def find_mentors_for_student(student_id):
    student = None
    for s in students:
        if s.student_id == student_id:
            student = s
            break
    if student:
        mentors = student.find_mentors()
        if mentors:
            print(f"Mentors for {student_id}: {mentors}")
        else:
            print(f"{student_id} has no mentors.")
    else:
        print(f"Student with ID {student_id} not found.")

# Function #4
def are_students_in_same_line(student_x, student_y):
    student_obj = Student(None, None, None)
    result = student_obj.are_students_in_same_line(student_x, student_y)
    print(f"{student_x} and {student_y} are in the same line : {result}")


find_mentors_for_student("64010456")
find_mentors_for_student("66010345")

are_students_in_same_line("64010456", "66010345")
are_students_in_same_line("63010978", "65010947")
are_students_in_same_line("64010456", "65010947")
