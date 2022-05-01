#include "library.h"
using namespace std;


lessonInfo inputLesson() {
    lessonInfo lesson{};
    setlocale(LC_ALL, "");
    cout << "Введіть назву предмета" << endl;
    cin >> lesson.subject;
    cout << "Введіть початок пари в форматі ГГ:ХХ" << endl;
    scanf("%d:%d", &lesson.start.hours, &lesson.start.minutes);
    lesson.finish.hours = (lesson.start.hours*60 + lesson.start.minutes + 105) / 60;
    lesson.finish.minutes = (lesson.start.hours*60 + lesson.start.minutes + 105) % 60;
    return lesson;
}


void outputLesson(lessonInfo lesson){
    cout << "Дисципліна - " << lesson.subject << endl;
    printf("Час проведення: %d:%02d - %d:%02d\n", lesson.start.hours, lesson.start.minutes, lesson.finish.hours, lesson.finish.minutes);
}


void inputLessons(const string& fileName){
    setlocale(LC_ALL, "");
    vector <lessonInfo> lessons = getVector(fileName);
    string move_on;
    while(move_on != "т"){
        lessonInfo lesson = inputLesson();
        insertSorted(lesson, lessons);
        CheckIntervals(lessons);
        cout << "Розклад заповнений? Введіть 'т', якщо розклад заповнений." << endl;
        cin >> move_on;
    }
    ofstream file;
    file.open(fileName, ios::out | ios::binary);
    for(lessonInfo lesson : lessons){
        file.write((char*)&lesson, sizeof(lesson));
    }
    file.close();
}


void displayTimetable(const string& fileName){
    ifstream file;
    file.open(fileName, ios::in | ios::binary);
    lessonInfo lesson{};
    cout << "Читаємо розклад з бінарного файлу " << fileName << endl;
    while(file.read((char*)&lesson, sizeof(lesson))){
        cout << endl;
        outputLesson(lesson);
    }
    file.close();
}


void askToDelete(const string& fileName){
    cout << "Хочете зберегти файл?" << endl;
    cout << "Напишіть 'т', якщо хочете." << endl;
    string answer;
    cin.ignore();
    getline(cin, answer);
    if(answer != "т"){
        ofstream file(fileName, ios::binary | ios::out);
        file.close();
    }
}


void insertSorted(lessonInfo lesson, vector<lessonInfo>& lessonList){
    bool inserted = false;
    for(int i = 0; i < lessonList.size() && !inserted; i++){
        if(lesson.start.hours * 60 + lesson.start.minutes -
        lessonList[i].finish.hours * 60 - lessonList[i].finish.minutes < 0){
            lessonList.insert(lessonList.begin() + i, lesson);
            inserted = true;
        }
    }
    if(!inserted){
        lessonList.push_back(lesson);
    }
}

vector <lessonInfo> getVector(string fileName){
    ifstream file;
    vector <lessonInfo> lessonVector = {};
    lessonInfo lesson{};
    file.open(fileName, ios::in | ios::binary);
    while (file.read((char*)&lesson, sizeof(lesson))){
        lessonVector.push_back(lesson);
    }
    file.close();
    return lessonVector;
}

void CheckIntervals(vector<lessonInfo> lessonList){
    for(int i = 0; i < lessonList.size() - 1; i++){
        int difference = lessonList[i+1].start.hours* 60 + lessonList[i+1].start.minutes -
                lessonList[i].finish.hours * 60 - lessonList[i].finish.minutes;
        if(difference > 45){
            cout << "Дуже велика перерва між парами:" << endl;
            outputLesson(lessonList[i]);
            outputLesson(lessonList[i+1]);
        }
        else if(difference > 0 && difference < 5){
            cout << "Дуже мала перерва між парами:" << endl;
            outputLesson(lessonList[i]);
            outputLesson(lessonList[i+1]);
        }
        else if(difference < 0) {
            cout << "Пари накладаються одна на іншу:" << endl;
            outputLesson(lessonList[i]);
            outputLesson(lessonList[i + 1]);
        }
    }
}