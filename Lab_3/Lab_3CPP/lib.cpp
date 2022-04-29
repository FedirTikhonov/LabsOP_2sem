#include "lib.h"


TextClass::TextClass() {
    text_ = {};
}

void TextClass::appendLine(std::string line) {
    text_.push_back(line);
}

std::string TextClass::findLongest() {
    std::string longestLine;
    for(const std::string& line : text_){
        if(longestLine.length() < line.length()){
            longestLine = line;
        }
    }
    return longestLine;
}
void TextClass::outputText() {
    std::cout << std::endl << "Outputting the contents of the text:" << std::endl;
    for(const std::string& line : text_){
        std::cout << line << std::endl;
    }
    std::cout << std::endl;
}

TextClass::~TextClass() {
    text_.clear();
}

std::vector<std::string> TextClass::getText() {
    std::vector<std::string> text;
    for(const std::string& line : text_){
        text.push_back(line);
    }
    return text;
}

void TextClass::setText(std::vector<std::string> text) {
    text_.clear();
    for(const std::string& line : text){
        text_.push_back(line);
    }
}

std::vector<TextClass> createTexts(){
    std::vector<TextClass> texts;
    std::string stopPushingTexts = "n";
    std::string stopPushingLines = "n";
    std::string line;
    int textCounter = 1;
    while(stopPushingTexts != "y"){
        TextClass text;
        std::cout << "Pushing lines for text " << textCounter << std::endl;
        std::string stopPushingLines = "n";
        while(stopPushingLines != "y"){
            std::cout << "Enter a line" << std::endl;
            if(textCounter > 1){
                std::cin.ignore();
            }
            std::getline(std::cin, line);
            text.appendLine(line);
            std::cout << "If you want to stop pushing lines, type 'y'." << std::endl;
            std::getline(std::cin, stopPushingLines);
        }
        std::cout << "Stop pushing texts? y/n?" << std::endl;
        std::cin >> stopPushingTexts;
        texts.push_back(text);
        textCounter++;
    }
    return texts;
}
void outputTexts(std::vector<TextClass> texts){
    int textCounter = 0;
    for(TextClass text : texts){
        textCounter++;
        std::cout << "Text" << textCounter << std::endl;
        text.outputText();
    }
}
void askToFindLongestString(std::vector<TextClass> texts){
    std::string answer;
    std::cout << "Do you want to know the longest string in a certain text?\nType 'yes' if you do.\n";
    std::cin >> answer;
    if(answer == "yes"){
        int index;
        std::cout << "Enter a number of text: ";
        std::cin >> index;
        index--;
        std::cout<< texts[index].findLongest() << std::endl;
    }
}
void askToAppendLines(std::vector<TextClass>& texts){
    std::string permissionForTexts;
    int i;
    int counter = 0;
    std::string line;
    std::string permissionForLines;
    std::cout << "Do you want to append lines to a text?" << std::endl << "Type 'yes' if you do." << std::endl;
    std::cin.ignore();
    std::getline(std::cin, permissionForTexts);
    while(permissionForTexts == "yes"){
        std::cout << "Enter a number of text: ";
        std::cin >> i;
        i--;
        permissionForLines = "X";
        while(permissionForLines != "STOP"){
            std::cout << "Enter a line" << std::endl;
            std::cin.ignore();
            std::getline(std::cin, line);
            texts[i].appendLine(line);
            std::cout << "Type 'STOP' to stop pushing lines." << std::endl;
            std::getline(std::cin, permissionForLines);
            counter++;
        }
        texts[i].outputText();
        std::cout << std::endl << "The longest string in the updated text is: " << std::endl;
        std::cout << texts[i].findLongest() << std::endl;
        std::cout << "Do you want to keep pushing lines for texts? Type \"yes\" to keep pushing lines for texts." << std::endl;
        std::getline(std::cin, permissionForTexts);
    }
}

void outputShortestOfLongest(std::vector<TextClass>(texts)){
    std::string buffer = texts[0].findLongest();
    std::string comparable;
    int textNum = 1;
    int counter = 1;
    for(TextClass text : texts){
        comparable = text.findLongest();
        if(buffer.length() > comparable.length()){
            buffer = comparable;
            textNum = counter;
        }
        counter++;
    }
    std::cout << "The shortest line in text out of longest strings is in text № " << textNum << std::endl;
    std::cout << buffer << std::endl;
}
