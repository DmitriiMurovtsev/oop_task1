class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if grade > 10:
                grade = 10
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print('Ошибка')
            return

    def av_grade(self):
        grades_list = []
        sum_grades = 0
        for i in self.grades.values():
            grades_list += i
        for i in grades_list:
            sum_grades += i
        return '{:.1f}'.format(sum_grades / len(grades_list))

    def __str__(self):
        average_grades = Student.av_grade(self)
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {average_grades}\n'
               f'Курсы в процессе обучения: {self.courses_in_progress}\n'
               f'Завершенные курсы: {self.finished_courses}')
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.av_grade() < other.av_grade()
        else:
            print(f'{other} не Студент')
            return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grade(self):
        grades_list = []
        sum_grades = 0
        for i in self.grades.values():
            grades_list += i
        for i in grades_list:
            sum_grades += i
        return '{:.1f}'.format(sum_grades / len(grades_list))

    def __str__(self):
        average_grades = Lecturer.av_grade(self)
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {average_grades}')
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.av_grade() < other.av_grade()
        else:
            print(f'{other} не является Лектором')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')
            return

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}')
        return res


def calc_average_student(students_list, course):
    grades_list = []
    sum_grades = 0
    for student in students_list:
        grades_list += student.grades[course]
    for grade in grades_list:
        sum_grades += grade
    return (f'Средняя оценка студентов за домашние задания на курсе {course}: '
            f'{"{:.1f}".format(sum_grades / len(grades_list))}')


def calc_average_lecturer(lecturers_list, course):
    grades_list = []
    sum_grades = 0
    for lecturer in lecturers_list:
        grades_list += lecturer.grades[course]
    for grade in grades_list:
        sum_grades += grade
    return (f'Средняя оценка лекторов за лекции на курсе {course}: '
            f'{"{:.1f}".format(sum_grades / len(grades_list))}')


def calc_average(items_list, course):
    # функция, которая считает средние оценки на одном курсе
    # из общего списка студентов и лекторов
    students_list = []
    lecturers_list = []
    for item in items_list:
        if isinstance(item, Student):
            students_list.append(item)
        elif isinstance(item, Lecturer):
            lecturers_list.append(item)
    average_student = calc_average_student(students_list, course)
    average_lecturer = calc_average_lecturer(lecturers_list, course)
    return f'{average_student}\n{average_lecturer}'


Mark = Student('Mark', 'Zuckerberg', 'male')
Erica = Student('Erica', 'Albright', 'female')
Sean = Lecturer('Sean', 'Parker')
Dustin = Lecturer('Dustin', 'Moskovitz')
Eduardo = Reviewer('Eduardo', 'Saverin')
Divya = Reviewer('Divya', 'Narendra')

Sean.courses_attached.append('Python')
Dustin.courses_attached.append('Python')
Mark.courses_in_progress.append('Python')
Erica.courses_in_progress.append('Python')
Eduardo.courses_attached.append('Python')
Divya.courses_attached.append('Python')

Mark.rate_lector(Sean, 'Python', 5)
Mark.rate_lector(Dustin, 'Python', 8)
Erica.rate_lector(Sean, 'Python', 9)
Erica.rate_lector(Dustin, 'Python', 7)

Eduardo.rate_hw(Mark, 'Python', 2)
Eduardo.rate_hw(Erica, 'Python', 5)
Divya.rate_hw(Erica, 'Python', 3)
Divya.rate_hw(Mark, 'Python', 7)

print(Mark)
print(Sean)
print(Eduardo)

print(Erica > Mark)
print(Dustin > Sean)

print(calc_average_student([Mark, Erica], 'Python'))
print(calc_average_lecturer([Sean, Dustin], 'Python'))
print(calc_average([Mark, Erica, Sean, Dustin], 'Python'))
