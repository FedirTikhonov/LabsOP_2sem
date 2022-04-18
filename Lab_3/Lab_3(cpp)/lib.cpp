#include "lib.h"


TextClass::TextClass() {
    text_ = {};
}

void TextClass::appendToText(std::string line) {
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
            text.appendToText(line);
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
    std::string answer;
    int i;
    int counter = 0;
    std::string line;
    std::cout << "Do you want to append lines to a text?" << std::endl << "Type 'yes' if you do." << std::endl;
    std::cin.ignore();
    std::getline(std::cin, answer);
    if(answer == "yes"){
        std::cout << "Enter a number of text: ";
        std::cin >> i;
        i--;
        while(answer == "yes"){
            std::cout << "Enter a line" << std::endl;
            if(counter<1){
                std::cin.ignore();
            }
            std::getline(std::cin, line);
            texts[i].appendToText(line);
            std::cout << "Type 'yes' to keep pushing lines." << std::endl;
            std::getline(std::cin, answer);
            counter++;
        }
        texts[i].outputText();
        std::cout << std::endl << "The longest string in the updated text is: " << std::endl;
        std::cout << texts[i].findLongest() << std::endl;
    }


}
