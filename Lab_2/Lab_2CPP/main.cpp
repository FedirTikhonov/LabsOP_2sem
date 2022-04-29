#include "library.h"
using namespace std;
int main() {
    setlocale(LC_ALL, "");

    string fileName = "lessons_data.dat";

    inputLessons(fileName);

    displayTimetable(fileName);

    askToDelete(fileName);

    return 0;
}