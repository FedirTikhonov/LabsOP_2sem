#include "library.h"
using namespace std;

lessonInfo inputLesson() {
    lessonInfo lesson;
    setlocale(LC_ALL, "");
    cout << "Введіть назву предмета" << endl;
    cin >> lesson.subject;
    cout << "Введіть початок пари в форматі ГГ:ХХ" << endl;
    scanf("%d:%d", &lesson.start.hours, &lesson.start.minutes);
    cout << "Введіть час у хвилинах після пари:" << endl;
    cin >> lesson.rest;
    lesson.finish.hours = (lesson.start.hours*60 + lesson.start.minutes + 105) / 60;
    lesson.finish.minutes = (lesson.start.hours*60 + lesson.start.minutes + 105) % 60;
    return lesson;
}
void outputLesson(lessonInfo lesson){
    cout << "Дисципліна - " << lesson.subject << endl;
    printf("Час проведення: %d:%02d - %d:%02d\n", lesson.start.hours, lesson.start.minutes, lesson.finish.hours, lesson.finish.minutes);
    cout << "Перерва - " << lesson.rest << "хв\n";
}
vector <lessonInfo> OverlaidLessons(vector <lessonInfo>& lessons, lessonInfo lesson){
    vector <lessonInfo> overlaid_lessons = {};
    if(lessons.empty()){
        lessons.push_back(lesson);
        return overlaid_lessons;
    }
    if(!lessons.empty()){
        for(int i = 0; i < lessons.size(); i++){
            if(lesson.start.hours >= lessons[i].start.hours) {
                if (lesson.start.hours * 60 + lesson.start.minutes - lessons[i].finish.hours * 60 -
                    lessons[i].finish.minutes - lessons[i].rest < 0) {
                    overlaid_lessons.push_back(lessons[i]);
                }
            }
            else if(lesson.start.hours <= lessons[i].start.hours){
                if(lessons[i].start.hours*60 + lessons[i].start.minutes - lesson.finish.hours*60 -
                lesson.finish.minutes - lesson.rest < 0){
                    overlaid_lessons.push_back(lessons[i]);
                }
            }
        }
    }
    lessons.push_back(lesson);
    return overlaid_lessons;
}
void displayOverlaid(vector <lessonInfo> overlaid){
    setlocale(LC_ALL, "");
    int len = overlaid.size();
    if(!overlaid.empty()){
        cout << "Деякі пари накладаються на введену пару:"  << endl;
        for(int i = 0; i< len; i++){
            outputLesson(overlaid[i]);
        }
    }
}
void inputLessons(string fileName){
    setlocale(LC_ALL, "");
    vector <lessonInfo> lessons = {};
    vector <lessonInfo> overlaid_lessons = {};
    ofstream file;
    file.open(fileName, ios::app | ios::binary);
    string move_on = "т";
    while(move_on == "т"){
        lessonInfo lesson_buffer = inputLesson();
        overlaid_lessons = OverlaidLessons(lessons, lesson_buffer);
        displayOverlaid(overlaid_lessons);
        file.write((char*)&lesson_buffer, sizeof(lesson_buffer));
        cout << "Чи бажаєте ви доповнити розклад?\nНапишіть 'т', якщо хочете продовжити. Напишіть 'н', якщо розклад заповнений.\n";
        cin.ignore();
        cin >> move_on;
    }
    file.close();
}

void displayTimetable(string fileName){
    ifstream file;
    file.open(fileName, ios::in | ios::binary);
    lessonInfo lesson;
    cout << "Читаємо розклад з бінарного файлу " << fileName << endl;
    while(file.read((char*)&lesson, sizeof(lesson))){
        cout << endl;
        outputLesson(lesson);

    }
    file.close();
}

void askToDelete(string fileName){
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