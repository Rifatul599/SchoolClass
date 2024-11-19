class School:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students={}

    def add_teacher(self,teacher_name):
        if teacher_name not in self.teachers:
            self.teachers.append(teacher_name)
            print(f"Teacher {teacher_name} added to the class.")
        else:
            print(f"Teache {teacher_name} already in the school.")

    def add_student(self,student_name,grade_level):
        if grade_level not in self.students:
            self.students[grade_level]=[]

        if student_name not in self.students[grade_level]:
            self.students[grade_level].append(student_name)
            print(f"Student {student_name} added to grade {grade_level}.")
        else:
            print(f"Student {student_name} already in the grade {grade_level}.")

    def list_teachers(self):
        if self.teachers:
            print("Teachers in the school.")
            for teacher in self.teachers:
                print(f"- {teacher}")
        else:
            print("No teacher in the school.")


    def list_students_by_grade(self,grade_level):
        if grade_level in self.students and self.students[grade_level]:
            print(f"Students in grade {grade_level}.")
            for student in self.students[grade_level]:
                print(f"- {student}")
        else:
            print(f"No students found in grade {grade_level}.")


    def remove_teacher(self,teacher_name):
        if teacher_name in self.teachers:
            self.teachers.remove(teacher_name)
            print(f"Teacher {teacher_name} removed from the school.")
        else:
            print(f"Teacher {teacher_name} not found in school.")

    def remove_student(self,student_name):
        found=False
        for grade_level in self.students:
            if student_name in self.students[grade_level]:
                self.students[grade_level].remove(student_name)
                print(f"Student {student_name} removed from the grade {grade_level}.")
                found=True
                break

        if not found:
            print(f"Student {student_name} not found in the school.")

school=School("Greenwood High")

school.add_teacher("Mr. Smith")
school.add_teacher("Ms. Johnson")

school.add_student("Alice",10)
school.add_student("Bob",10)
school.add_student("Charlie",11)

school.list_teachers()
school.list_students_by_grade(10)
school.remove_teacher("Ms. Johnson")
school.remove_student("Alice")

school.list_teachers()
school.list_students_by_grade(10)




