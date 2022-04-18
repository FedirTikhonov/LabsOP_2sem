#pragma once
#include <iostream>
#include <string>
#include <vector>

class TextClass{
public:
    TextClass();
    std::string findLongest();
    void appendToText(std::string line);
    void outputText();
    ~TextClass();
private:
    std::vector<std::string> text_;
};

std::vector<TextClass> createTexts();
void outputTexts(std::vector<TextClass> texts);
void askToFindLongestString(std::vector<TextClass> texts);
void askToAppendLines(std::vector<TextClass>& texts);