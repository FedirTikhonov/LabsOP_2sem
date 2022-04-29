#pragma once
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <vector>
using namespace std;
struct timeFormat{
    int hours, minutes;
};
struct lessonInfo{
    char subject[100];
    timeFormat start, finish;
    int rest;
};
lessonInfo inputLesson();
void outputLesson(lessonInfo lesson);
vector <lessonInfo> OverlaidLessons(vector <lessonInfo>& lessons, lessonInfo lesson);
void inputLessons(string fileName);
void displayOverlaid(vector <lessonInfo> overlaid);
void displayTimetable(string fileName);
void askToDelete(string fileName);

