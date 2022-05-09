#include <iostream>
#include <vector>
#include <string>

using std::string;
using std::vector;

class Roman_numerals{
public:
    Roman_numerals(string num);
    Roman_numerals();
    Roman_numerals(const Roman_numerals& toBeCopied);

    Roman_numerals operator+(Roman_numerals rNum);
    Roman_numerals& operator+=(Roman_numerals rNum);
    void operator++();
    void operator++(int);

    void outputRoman();
    void setRoman(string num);
    string getRoman();
    int convertToInt();

private:
    string numeral;
};

vector<int> intToVector(int num);
string intToRoman(int num);
string getNumeral();
