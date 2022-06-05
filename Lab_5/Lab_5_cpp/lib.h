#pragma once

#include <string>
#include <iostream>
#include <vector>
#include <cmath>
class Person{
public:
    virtual double countRating() = 0;
    virtual void inputFullInfo();
    virtual void printInfo();
protected:
    double _rating;
    int _age;
    std::string _name;
    std::string _middleName;
    std::string _lastName;
};
class Subject{
public:
    void inputSubject();
    void outputSubject() const;
    Subject();
    Subject(std::string subName, int mark);
    std::string subjectName;
    int Mark;
};
class Student : public Person{
public:
    Student();
    double countRating() override;
    void inputFullInfo() override;
    void Check();
    void printInfo() override;
    void inputSubjects();
private:
    std::vector<Subject> _subjectsToStudy;
};

class Teacher : public Person{
public:
    Teacher();
    void printInfo() override;
    double countRating() override;
    void inputFullInfo() override;
    void inputSubjects();
private:
    std::vector<Subject> _subjectsToTeach;

};
std::string splitName(std::string fullName, std::string& Surname, std::string& SecondName);

void mainTask();