#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void pushLinesInFile(const string& fileName);                         //push lines into file

void outputContents(const string& oldFileName, const string& newFileName);  //output contents of the file

vector<string> getLines(const string& fileName);//copy lines from file to vector

void copyLinesToAnotherFile(const string& fileName1, string fileName2); //copy lines from file1 to file2

int countChars(const string& line);//count characters in a string

void sortStrings(vector<string>& lines);            //sort strings in vector

void DeleteFile(const string& oldFileName, const string& newFileName, const string& permission); //BASED on th decision made by the user,
                                                                            // delete contents of files or not.
string askForPermission();
