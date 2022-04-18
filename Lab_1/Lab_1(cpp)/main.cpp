#include "lib.h"
using namespace std;
int main(){

    string oldFileName = "oldFile.txt";  //naming our files
    string newFileName = "new.txt";


    string perm = askForPermission(); //asking the user whether to save their text.


    pushLinesInFile(oldFileName); //push lines into a source file.


    copyLinesToAnotherFile(oldFileName, newFileName);   //copy lines from file1 to file2,
                                                                           //sort lines.

    outputContents(oldFileName, newFileName);                               //output everything in our files to console.


    DeleteFile(oldFileName, newFileName, perm);                 //BASED on th decision made by the user,
                                                                          // delete contents of files or not.

    return 0;
}