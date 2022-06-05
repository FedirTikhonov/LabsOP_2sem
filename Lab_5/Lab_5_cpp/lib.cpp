
#include "lib.h"

#include <utility>


std::string splitName(std::string fullName, std::string& Surname, std::string& SecondName){
    std::string Name;
    int i = 0;
    while(i < fullName.length() && fullName[i] != ' '){
        Surname.push_back(fullName[i]);
        i++;
    }
    i++;
    while(i < fullName.length() && fullName[i] != ' '){
        Name.push_back(fullName[i]);
        i++;
    }
    i++;
    while(i < fullName.length() && fullName[i] != ' '){
        SecondName.push_back(fullName[i]);
        i++;
    }
    return Name;
}

void mainTask() {
    int m, n;
    std::cout << "Enter a number of students and teachers:" << std::endl;
    std::cin >> m >> n;
    for(int studentCounter = 0; studentCounter < m; studentCounter++){
        std::cout << "Введіть дані студента:" << std::endl;
        Student guy;
        guy.inputFullInfo();
        guy.printInfo();
        guy.Check();
    }
    std::cout << std::endl;
    for(int teacherCounter = 0; teacherCounter < n; teacherCounter++){
        std::cout << "Введіть дані викладача:" << std::endl;
        Teacher dude;
        dude.inputFullInfo();
        dude.printInfo();
    }
}

void Person::printInfo() {
    std::cout << "ПІБ - " << _middleName + ' ' << _name + ' ' << _lastName + ' ' << std::endl;
    std::cout << "Вік - " << _age << std::endl;
    std::cout << "Рейтинг - " << _rating << std::endl;
}

void Person::inputFullInfo() {
    std::string fullName;
    std::cout << "Введіть повне ім'я: " << std::endl;
    std::cin.ignore();
    std::getline(std::cin, fullName);
    _name = splitName(fullName, _middleName, _lastName);
    std::cout << "Введіть вік:" << std::endl;
    std::cin >> _age;
}


Subject::Subject(std::string subName, int mark) {
    Mark = mark;
    subjectName = std::move(subName);
}

void Subject::inputSubject() {
    std::cout << "Введіть назву дисципліни:" << std::endl;
    std::cin.ignore();
    std::getline(std::cin, subjectName);
    std::cout << "Введіть оцінку за дану дисципліну:" << std::endl;
    std::cin >> Mark;
    std::cin.ignore();
}

void Subject::outputSubject() const {
    std::cout << "Назва дисципліни - " << subjectName << std::endl;
    std::cout << "Рейтинг дисципліни - " << Mark << std::endl;
}

Subject::Subject() {
    subjectName = "";
    Mark = 0;
}

double Student::countRating() {
    double sum = 0;
    if(_subjectsToStudy.empty()) {
        return sum;
    }
    else{
        for(const Subject& lesson : _subjectsToStudy){
            sum += lesson.Mark;
        }
        double average = sum / (double)_subjectsToStudy.size();
        _rating = average;
        return average;
    }
}

Student::Student() {
    _rating = 0;
    _age = 0;
    _name = "", _middleName = "", _lastName = "";
    _subjectsToStudy = {};
}

void Student::inputSubjects() {
    Subject tmp;
    std::string line;
    while(line != "СТОП"){
        tmp.inputSubject();
        _subjectsToStudy.push_back(tmp);
        std::cout << "Додати ще одну дисципліну?\nНапишіть \"СТОП\" щоб перестати." << std::endl;
        std::getline(std::cin, line);
    }
    _rating = countRating();
}

void Student::printInfo() {
    Person::printInfo();
    for(const Subject& lesson : _subjectsToStudy){
        lesson.outputSubject();
    }
}



void Student::Check() {
    if(_rating < 60 && _age < 18){
        std::cout << "Неповнолітній студент за ім'ям " << _middleName << " " << _name << " " << _lastName << " має недостатню кількість балів (" << _rating << ")" << std::endl;
    }
}

void Student::inputFullInfo() {
    Person::inputFullInfo();
    inputSubjects();
}

Teacher::Teacher() {
    _rating = 0;
    _age = 0;
    _name = "", _lastName = "", _middleName = "";
    _subjectsToTeach = {};
}

void Teacher::printInfo() {
    Person::printInfo();
    for(const Subject& subj : _subjectsToTeach){
        subj.outputSubject();
    }
}

double Teacher::countRating() {
    int sum = 0;
    for(const Subject& subj : _subjectsToTeach){
        sum += subj.Mark;
    }
    return (double) sum / _subjectsToTeach.size();
}

void Teacher::inputFullInfo() {
    Person::inputFullInfo();
    inputSubjects();
}

void Teacher::inputSubjects() {
    Subject tmp;
    std::string line;
    while(line != "СТОП"){
        tmp.inputSubject();
        _subjectsToTeach.push_back(tmp);
        std::cout << "Додати ще одну дисципліну?\nНапишіть \"СТОП\" щоб перестати." << std::endl;
        std::getline(std::cin, line);
        _rating = countRating();
    }
}



