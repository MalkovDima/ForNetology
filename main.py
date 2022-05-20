class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        n = 0
        summa = 0
        for k, v in self.grades.items():
            for d in v:
                summa += d
                n += 1
        reting = round(summa / n, 2)

        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {reting}' \
               f'\nКурсы в процессе изучения: ' \
               f'{" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        n = 0
        summa = 0
        for k, v in self.grades.items():
            for d in v:
                summa += d
                n += 1
        reting = round(summa / n, 2)

        n1 = 0
        summa1 = 0
        for k1, v1 in other.grades.items():
            for d1 in v1:
                summa1 += d1
                n1 += 1
        reting_other = round(summa1 / n1, 2)
        return reting < reting_other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        n = 0
        summa = 0
        for k, v in self.grades.items():
            for d in v:
                summa += d
                n += 1
        reting = round(summa/n, 2)

        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {reting}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        n = 0
        summa = 0
        for k, v in self.grades.items():
            for d in v:
                summa += d
                n += 1
        reting = round(summa / n, 2)

        n1 = 0
        summa1 = 0
        for k1, v1 in other.grades.items():
            for d1 in v1:
                summa1 += d1
                n1 += 1
        reting_other = round(summa1 / n1, 2)

        return reting < reting_other


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}'
        return text


def reiting_students_courses(students):
    all_points = []
    one_courses = input('Введите курс по которому посчитать средний бал всех студентов: ')
    for i in students:
        if one_courses in i.grades:
            all_points += i.grades[one_courses]
    if all_points:
        res = round(sum(all_points) / len(all_points), 2)
    else:
        res = 'Такой курс ни кто не сдавал!'
    return res


def reiting_lectors_courses(lectors):
    all_points = []
    one_courses = input('Введите курс по которому посчитать средний бал всех лекторов: ')
    for i in lectors:
        if one_courses in i.courses_attached:
            all_points += i.grades[one_courses]
    if all_points:
        res = round(sum(all_points) / len(all_points), 2)
    else:
        res = 'Такой курс ни кто не читает!'
    return res


best_student = Student('Ваня', 'Петров', 'мужской')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C']

bad_student = Student('Петя', 'Иванов', 'мужской')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['C']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Alex', 'Smith')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C']
cool_reviewer.rate_hw(best_student, 'C', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'C', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 3)
cool_reviewer.rate_hw(bad_student, 'C', 6)
cool_reviewer.rate_hw(bad_student, 'Python', 2)

cool_lector = Lecturer('Djon', 'Bon')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['C']

bad_lector = Lecturer('Djoni', 'Boni')
bad_lector.courses_attached += ['Python']
bad_lector.courses_attached += ['C']

best_student.rate_hw(cool_lector, 'Python', 10)
best_student.rate_hw(cool_lector, 'Python', 10)
best_student.rate_hw(cool_lector, 'C', 10)

best_student.rate_hw(bad_lector, 'Python', 10)
best_student.rate_hw(bad_lector, 'Python', 3)
best_student.rate_hw(bad_lector, 'C', 10)
print(cool_reviewer)
print()
print(cool_lector)
print()
print(bad_lector)
print()
print(bad_lector < cool_lector)
print(bad_student > best_student)

all_student = [best_student, bad_student]
all_lector = [cool_lector, bad_lector]


print(reiting_students_courses(all_student))
print()
print(reiting_lectors_courses(all_lector))

#git remote add https://github.com/MalkovDima/ForNetology