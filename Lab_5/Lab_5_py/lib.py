class Person:
    def __init__(self):
        self._Name = ""
        self._MiddleName = ""
        self._LastName = ""
        self._Rating = 0

    def countRating(self):
        self._Rating = 0

    def inputFullInfo(self):
        FullName = input("Введіть ПІБ:\n")
        self._Name, self._MiddleName, self._LastName = FullName.split(" ")
        self._Age = int(input("Введіть вік:\n"))
        self._Rating = 0

    def printInfo(self):
        print(f'ПІБ - {self._Name} {self._MiddleName} {self._LastName}')
        print(f'Вік - {self._Age}')
        print(f'Рейтинг - {self._Rating}')


class Subject:
    def __init__(self):
        Name = ""
        Mark = 0

    def inputSubject(self):
        self.Name = input("Введіть назву предмета:\n")
        self.Mark = int(input("Введіть рейтинг дисципліни:\n"))

    def __str__(self):
        return f"Назва - {self.Name}\nОцінка - {self.Mark}"


class Student(Person):
    def __init__(self):
        super().__init__()
        self.__LessonsLst = []

    def countRating(self):
        sum = 0
        for lesson in self.__LessonsLst:
            sum += lesson.Mark
        self._Rating = float(sum/len(self.__LessonsLst))

    def inputFullInfo(self):
        super().inputFullInfo()
        response = ""
        while response != "СТОП":
            subj = Subject()
            subj.inputSubject()
            self.__LessonsLst.append(subj)
            response = input("Продовжити? Напишіть \"СТОП\" щоб зупинитись.")
        self.countRating()


    def printInfo(self):
        super().printInfo()
        for subj in self.__LessonsLst:
            print(subj)

    def Check(self):
        if self._Age < 18 and self._Rating < 60:
            print(f"\nНеповнолітній студент {self._Name} { self._MiddleName} {self._LastName}"
                  f" має недостатню кількість балів ({self._Rating})")
        else:
            pass


class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.LessonLst = []

    def countRating(self):
        sum = 0
        for lesson in self.LessonLst:
            sum += lesson.Mark
        self._Rating = float(sum / len(self.LessonLst))

    def printInfo(self):
        super().printInfo()
        for lesson in self.LessonLst:
            print(lesson)

    def inputFullInfo(self):
        super().inputFullInfo()
        response = ""
        while response != "СТОП":
            subj = Subject()
            subj.inputSubject()
            self.LessonLst.append(subj)
            response = input("Продовжити? Напишіть \"СТОП\" щоб зупинитись.")
        self.countRating()


