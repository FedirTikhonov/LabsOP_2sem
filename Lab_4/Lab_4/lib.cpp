
#include "lib.h"

#include <utility>

using std::cout;
using std::string;
using std::vector;
using std::endl;

Roman_numerals Roman_numerals::operator+(Roman_numerals rNum) {
    int ArabNum1 = this->convertToInt();
    int ArabNum2 = rNum.convertToInt();
    int result = ArabNum1 + ArabNum2;
    this->setRoman(intToRoman(result));
    return *this;
}

void Roman_numerals::operator++() {
    int ArabNum1 = this->convertToInt();
    ++ArabNum1;
    this->setRoman(intToRoman(ArabNum1));
}

Roman_numerals& Roman_numerals::operator+=(Roman_numerals rNum) {
    int num1 = this->convertToInt();
    int num2 = rNum.convertToInt();
    num1+=num2;
    setRoman(intToRoman(num1));
    return *this;
}

int Roman_numerals::convertToInt() {
    int answer = 0;
    string copyNumeral = numeral;
    int i = copyNumeral.length() - 1;
    std::reverse(copyNumeral.begin(), copyNumeral.end());
    while(copyNumeral[i] == 'M'){
        answer += 1000;
        copyNumeral.pop_back();
        i--;
    }
    if (copyNumeral[i] == 'C' && copyNumeral[i - 1] == 'M') {
        answer += 900;
        copyNumeral.pop_back();
        copyNumeral.pop_back();
        i -= 2;
    }
    if (copyNumeral[i] == 'D') {
        answer += 500;
        copyNumeral.pop_back();
        i--;
        while(copyNumeral[i] == 'C'){
            answer += 100;
            copyNumeral.pop_back();
            i--;
        }
    }
    if (copyNumeral[i] == 'C' && copyNumeral[i - 1] == 'D') {
        answer += 400;
        copyNumeral.pop_back();
        copyNumeral.pop_back();
        i -= 2;
    }
    while(copyNumeral[i] == 'C'){
        answer += 100;
        copyNumeral.pop_back();
        i--;
    }
    if(copyNumeral[i] == 'X' && copyNumeral[i-1] == 'C'){
        answer += 90;
        copyNumeral.pop_back();
        copyNumeral.pop_back();
        i-=2;
    }
    if(copyNumeral[i] == 'L'){
        answer += 50;
        copyNumeral.pop_back();
        i--;
        while(copyNumeral[i] == 'X'){
            answer += 10;
            copyNumeral.pop_back();
            i--;
        }
    }
    if (copyNumeral[i] == 'X' && copyNumeral[i - 1] == 'L') {
        answer += 40;
        copyNumeral.pop_back();
        copyNumeral.pop_back();
        i -= 2;
    }
    while(copyNumeral[i] == 'X'){
        answer += 10;
        copyNumeral.pop_back();
        i--;
    }
    if(copyNumeral[i] == 'I' && copyNumeral[i-1] == 'X'){
        answer += 9;
        copyNumeral.pop_back();
        copyNumeral.pop_back();
        i-=2;
    }
    if(copyNumeral[i] == 'V'){
        answer += 5;
        copyNumeral.pop_back();
        i--;
        while(copyNumeral[i] == 'I'){
            answer += 1;
            copyNumeral.pop_back();
            i--;
        }
    }
    if (copyNumeral[i] == 'I' && copyNumeral[i - 1] == 'V') {
        answer += 4;
        copyNumeral.pop_back();
        copyNumeral.pop_back();
        i -= 2;
    }
    while(copyNumeral[i] == 'I'){
        answer += 1;
        copyNumeral.pop_back();
        i--;
    }
    return answer;
}
    Roman_numerals::Roman_numerals(string num) {
        numeral = num;
    }

    void Roman_numerals::setRoman(string num) {
        numeral = num;
    }

void Roman_numerals::outputRoman() {
    cout << numeral << endl;
}

void Roman_numerals::operator++(int) {
    int ArabNum1 = this->convertToInt();
    ArabNum1++;
    this->setRoman(intToRoman(ArabNum1));
}

string Roman_numerals::getRoman() {
    return numeral;
}

Roman_numerals::Roman_numerals() {
    numeral = "I";
}

Roman_numerals::Roman_numerals(const Roman_numerals &toBeCopied) {
    this->numeral = toBeCopied.numeral;
}

vector<int> intToVector(int num) {
        string line;
        int k;
        vector<int> numerals = {};
        string strNum = std::to_string(num);
        for (char i: strNum) {
            line = "";
            line.push_back(i);
            k = std::stoi(line);
            numerals.push_back(k);
        }
        return numerals;
    }
    string intToRoman(int num) {
        vector<int> numbers = intToVector(num);
        int len = numbers.size();
        string RomanNumeral;
        int i = 0;
        int tempNum = numbers[i];
        if (len > 3) {
            for (int k = 0; k < tempNum; k++) {
                RomanNumeral += 'M';
            }
            len--;
            i++;
        }
        tempNum = numbers[i];
        if (len > 2 && tempNum < 4) {
            for (int k = 0; k < tempNum; k++) {
                RomanNumeral.push_back('C');
            }
            len--;
            i++;
        } else if (len > 2 && tempNum == 4) {
            RomanNumeral += "CD";
            len--;
            i++;
        } else if (len > 2 && tempNum == 5) {
            RomanNumeral.push_back('D');
            len--;
            i++;
        } else if (len > 2 && tempNum > 5 && tempNum < 9) {
            RomanNumeral.push_back('D');
            for (int k = 0; k < tempNum - 5; k++) {
                RomanNumeral.push_back('C');
            }
            len--;
            i++;
        } else if (len > 2 && tempNum == 9) {
            RomanNumeral += "CM";
            len--;
            i++;
        }
        tempNum = numbers[i];
        if (len > 1 && tempNum < 4) {
            for (int k = 0; k < tempNum; k++) {
                RomanNumeral.push_back('X');
            }
            len--;
            i++;
        }
        else if (len > 1 && tempNum == 4) {
            RomanNumeral += "XL";
            len--;
            i++;
        } else if (len > 1 && tempNum == 5) {
            RomanNumeral += "L";
            len--;
            i++;
        } else if (len > 1 && tempNum > 5 && tempNum < 9) {
            RomanNumeral.push_back('L');
            for (int k = 0; k < tempNum - 5; k++) {
                RomanNumeral.push_back('X');
            }
            len--;
            i++;
        } else if (len > 1 && tempNum == 9) {
            RomanNumeral += "XC";
            len--;
            i++;
        }
        tempNum = numbers[i];
        if (len > 0 && tempNum < 4) {
            for (int k = 0; k < tempNum; k++) {
                RomanNumeral.push_back('I');
            }
        } else if (len > 0 && tempNum == 4) {
            RomanNumeral += "IV";
            len--;
            i++;
        } else if (len > 0 && tempNum == 5) {
            RomanNumeral.push_back('V');
            len--;
            i++;
        } else if (len > 0 && tempNum > 5 && tempNum < 9) {
            RomanNumeral.push_back('V');
            for (int k = 0; k < tempNum - 5; k++) {
                RomanNumeral.push_back('I');
            }
            len--;
            i++;
        } else if (len > 0 && tempNum == 9) {
            RomanNumeral += "IX";
            len--;
            i++;
        }
        return RomanNumeral;
    }
