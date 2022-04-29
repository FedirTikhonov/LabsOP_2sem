import _pickle


class timeFormat:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


class lessonFormat:
    def __init__(self, startHours, startMinutes, finishHours, finishMinutes, lessonName, rest):
        self.start = timeFormat(startHours, startMinutes)
        self.finish = timeFormat(finishHours, finishMinutes)
        self.lessonName = lessonName
        self.rest = rest


def inputLesson():
    lessonName = input("Введіть назву предмета:\n")
    startHours, startMinutes = input("Введіть час початку пари у форматі ГГ:ХХ\n").split(":")
    startHours, startMinutes = int(startHours), int(startMinutes)
    rest = int(input("Введіть тривалість перерви:\n"))
    finishHours = (startHours * 60 + startMinutes + 105) // 60
    finishMinutes = (startHours * 60 + startMinutes + 105) % 60
    newLesson = lessonFormat(startHours, startMinutes, finishHours, finishMinutes, lessonName, rest)
    return newLesson


def printLesson(lesson):
    print(f"\nНазва дисципліни - {lesson.lessonName}.")
    print(
        f"Час проведення - {lesson.start.hours}:{str(lesson.start.minutes).zfill(2)} - {lesson.finish.hours}:{str(lesson.finish.minutes).zfill(2)}")
    print(f"Перерва - {lesson.rest}\n")
    return None


def OverlaidLessons(lesson, lessonList):
    overlaidList = []
    if len(lessonList) == 0:
        return None
    if len(lessonList) > 0:
        for lessonInList in lessonList:
            if lesson.start.hours >= lessonInList.start.hours:
                if lesson.start.hours * 60 + lesson.start.minutes - lessonInList.finish.hours * 60 - lessonInList.finish.minutes - lessonInList.rest < 0:
                    overlaidList.append(lessonInList)
            elif lesson.start.hours <= lessonInList.start.hours:
                if lessonInList.start.hours * 60 + lessonInList.start.minutes - lesson.finish.hours * 60 - lesson.finish.minutes - lesson.rest < 0:
                    overlaidList.append(lessonInList)
    return overlaidList


def inputLessons(fileName):
    with open(fileName, 'ab') as file:
        answer = ""
        lessonList = []
        while answer != "т":
            lesson = inputLesson()
            overlaid = OverlaidLessons(lesson, lessonList)
            displayOverlaid(overlaid)
            _pickle.dump(lesson, file)
            lessonList.append(lesson)
            answer = input("Введіть 'т', якщо розклад заповнений.\n")
    return None


def displayOverlaid(overlaidLessons):
    if overlaidLessons is not None:
        if len(overlaidLessons) > 0:
            print("Деякі пари накладаються на введену дисципліну:\n")
            for lesson in overlaidLessons:
                printLesson(lesson)
    return None


def outputLessons(fileName):
    lesson = 0
    with open(fileName, 'rb') as file:
        try:
            lesson = _pickle.load(file)
        except EOFError:
            print("Розклад пустий.")
        while lesson:
            printLesson(lesson)
            try:
                lesson = _pickle.load(file)
            except EOFError:
                break
    return None


def askToDelete(fileName):
    answer = input("Бажаєте стерти файл? Напишіть 'т' якщо ви хочете стерти файл.")
    if answer == 'т':
        f = open(fileName, 'wb')
        f.close()
    return None
