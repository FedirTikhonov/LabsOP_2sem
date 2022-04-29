#pragma once
#include <iostream>
#include <string>
#include <vector>

class TextClass{
public:
    TextClass();
    std::string findLongest();
    void appendLine(std::string line);
    void outputText();
    std::vector<std::string> getText();
    void setText(std::vector<std::string> text);
    ~TextClass();
private:
    std::vector<std::string> text_;
};

std::vector<TextClass> createTexts();
void outputTexts(std::vector<TextClass> texts);
void askToFindLongestString(std::vector<TextClass> texts);
void askToAppendLines(std::vector<TextClass>& texts);
void outputShortestOfLongest(std::vector<TextClass>(texts));