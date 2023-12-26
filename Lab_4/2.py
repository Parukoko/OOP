class Student:
	def __init__(self, id, name):
		self.id = id
		self.name = name
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
		self.teachers_list.append(teachers[idx])
class Teacher:
	def __init__(self, id, name):
		self.id = id
		self.name = name

#instance
students = [
	Student("001", "Alice"),
	Student("002", "Bob"),
	Student("003", "Peter"),
	Student("004", "Kevin"),
	Student("005", "Luke")
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
