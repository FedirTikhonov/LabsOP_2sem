#include "lib.h"

using std::cout;
using std::endl;

int main(){
    Roman_numerals R1;
    cout << "Initialising R1 with a default constructor: ";
    R1.outputRoman();

    Roman_numerals R2("MMM");
    cout << "Initialising R2 with a parameterized constructor: ";
    R2.outputRoman();

    Roman_numerals R3(R2);
    cout << "Initialising R3 with a copy constructor: ";
    R3.outputRoman();

    cout << "Incrementing a number R1(I):";
    ++R1;
    R1.outputRoman();

    int k = 121;
    cout << "Adding a value " << k << " to an already existing number R2 :";
    R2 += intToRoman(k);
    R2.outputRoman();

    cout << "Adding R2 and R1 and saving it in R3:" << endl;
    R3 = R1 + R2;
    R3.outputRoman();

    cout << "Converting R3 to N3:" << endl;
    int N3 = R3.convertToInt();
    cout << "R3: ";
    R3.outputRoman();
    cout << "N3: " << N3 << endl;

    return 0;
}
