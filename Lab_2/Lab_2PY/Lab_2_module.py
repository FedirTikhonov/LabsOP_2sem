import _pickle


class timeFormat:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes


class lessonFormat:
    def __init__(self, startHours, startMinutes, finishHours, finishMinutes, lessonName):
        self.start = timeFormat(startHours, startMinutes)
        self.finish = timeFormat(finishHours, finishMinutes)
        self.lessonName = lessonName


def inputLesson():
    lessonName = input("Введіть назву предмета:\n")
    startHours, startMinutes = input("Введіть час початку пари у форматі ГГ:ХХ\n").split(":")
    startHours, startMinutes = int(startHours), int(startMinutes)
    finishHours = (startHours * 60 + startMinutes + 105) // 60
    finishMinutes = (startHours * 60 + startMinutes + 105) % 60
    newLesson = lessonFormat(startHours, startMinutes, finishHours, finishMinutes, lessonName)
    return newLesson


def printLesson(lesson):
    print(f"\nНазва дисципліни - {lesson.lessonName}.")
    print(
        f"Час проведення - {lesson.start.hours}:{str(lesson.start.minutes).zfill(2)} - "
        f"{lesson.finish.hours}:{str(lesson.finish.minutes).zfill(2)}")
    return None


def inputLessons(fileName):
    answer = ""
    lessonList = getList(fileName)
    while answer != "т":
        lesson = inputLesson()
        lessonList = insertSorted(lesson, lessonList)
        answer = input("Введіть 'т', якщо розклад заповнений.\n")
    CheckInterval(lessonList)
    with open(fileName, 'wb') as file:
        for lesson in lessonList:
            _pickle.dump(lesson, file)
    return None


def outputLessons(fileName):
    print("Виводимо розклад з файлу:")
    lesson = 0
    with open(fileName, 'rb') as file:
        try:
            lesson = _pickle.load(file)
            printLesson(lesson)
        except EOFError:
            print("Розклад пустий.")
        while lesson:
            try:
                lesson = _pickle.load(file)
                printLesson(lesson)
            except EOFError:
                break
    return None


def askToDelete(fileName):
    answer = input("Бажаєте стерти файл? Напишіть 'т' якщо ви хочете стерти файл.")
    if answer == 'т':
        f = open(fileName, 'wb')
        f.close()
    return None


def insertSorted(lesson, lessonList):
    if lessonList is None:
        lessonList = []
        lessonList.append(lesson)
    else:
        inserted = False
        for i in range(len(lessonList)):
            if lesson.start.hours * 60 + lesson.start.minutes < \
                    lessonList[i].start.hours * 60 + lessonList[i].start.minutes and not inserted:
                lessonList.insert(i, lesson)
                inserted = True
        if not inserted:
            lessonList.append(lesson)
    return lessonList


def CheckInterval(lessonList):
    if len(lessonList) > 1:
        for i in range(len(lessonList) - 1):
            difference = lessonList[i+1].start.hours * 60 + lessonList[i+1].start.minutes - lessonList[i].finish.hours*60 - lessonList[i].finish.minutes
            if difference > 45:
                print("Між даними дисциплінами дуже велика перерва:")
                printLesson(lessonList[i])
                printLesson(lessonList[i+1])
            if 5 > difference > 0:
                print("Між даними дисциплінами дуже мала перерва:")
                printLesson(lessonList[i])
                printLesson(lessonList[i + 1])
            if difference < 0:
                print("Одна дисципліна накладається на іншу:")
                printLesson(lessonList[i])
                printLesson(lessonList[i + 1])
        return None


def getList(fileName):
    lessonList = []
    with open(fileName, 'rb') as file:
        try:
            lesson = _pickle.load(file)
            lessonList.append(lesson)
        except EOFError:
            return lessonList
        while lesson:
            try:
                lesson = _pickle.load(file)
                lessonList.append(lesson)
            except EOFError:
                break
    return lessonList
