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
};
lessonInfo inputLesson();
void outputLesson(lessonInfo lesson);
void inputLessons(const string& fileName);
void displayTimetable(const string& fileName);
void askToDelete(const string& fileName);
void insertSorted(lessonInfo lesson, vector<lessonInfo>& lessonList);
vector <lessonInfo> getVector(string fileName);
void CheckIntervals(vector<lessonInfo> lessonList);

