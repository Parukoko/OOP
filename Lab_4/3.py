class Student:
	def __init__(self, id, name, year):
		self.id = id
		self.name = name
		self.student_mentor = None
		self.year = year
	def find_mentor(self):
		mentor = []
class Subject:
	def __init__(self, id, name, credit, section):
		self.id = id
		self.name = name
		self.credit = credit
		self.section = section
		self.students_list = []
		self.teacher = []
	def add_students(self, students, idx):
		self.students_list.append(students[idx])
	def add_teacher(self, teachers, idx):
		self.teacher.append(teachers[idx])
class Teacher:
	def __init__(self, id, name):
		self.id = id
		self.name = name

#instance
students = [
	Student("001", "Alice", 1),
	Student("002", "Bob", 2),
	Student("003", "Peter", 3),
	Student("004", "Kevin", 4),
	Student("005", "Luke", 1)
]

teachers = [
	Teacher("111", "John"),
	Teacher("112", "Frank")
]

oop_1 = Subject("101", "Object Oriented Programming", 3, "section 1")
oop_2 = Subject("102", "Object Oriented Programming", 3, "section 2")

oop_1.add_students(students[0])
oop_1.add_students(students[1])
oop_1.add_students(students[2])
oop_2.add_students(students[3])
oop_2.add_students(students[4])

oop_1.teacher = teachers[0]
oop_2.teacher = teachers[1]

subjects = [oop_1,oop_2]
def find_student_taught_by_teacher(teacher_id):
	taught_students = []
	for subject in subjects:
		if subject.teacher.id == teacher_id:
			taught_students.extend(subject.students_list)
	return taught_students
def find_subject_studied_by_student(student_id):
	studied_student = []
	for subject in subjects:
		for student in subject.students_list:
			if student.id == student_id:
				studied_student.append(subject)
	return studied_student
