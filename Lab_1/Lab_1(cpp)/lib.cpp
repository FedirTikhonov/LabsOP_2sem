#include "lib.h"
using namespace std;

void pushLinesInFile(const string& fileName) {
    ofstream file;
    file.open(fileName, ios::app);
    string line;
    cout << "Enter lines." << endl;
    while (getline(cin, line)) {
        if (!line.empty()) {
            file << line << endl;
        }
    }
    file.close();
}
void outputContents(const string& oldFileName, const string& newFileName){
    string line;
    ifstream oldFile;
    ifstream newFile;
    oldFile.open(oldFileName, ios::in);
    newFile.open(newFileName, ios::in);
    cout << endl << "Outputting contents for oldFile:" << endl;
    while(getline(oldFile, line)){
        cout << line << endl;
    }
    cout << endl << "Outputting contents for newFile:" << endl;
    while(getline(newFile, line)){
        cout << line << endl;
    }
    oldFile.close();
    newFile.close();
}
void DeleteFile(const string& oldFileName, const string& newFileName, const string& permission){
    if(permission == "no"){
        ofstream oldFile(oldFileName, ios::out);
        ofstream newFile(newFileName, ios::out);
        oldFile.close();
        newFile.close();

    }
}
void sortStrings(vector<string>& lines){
    string buffer;
    for(int i = 0; i<lines.size(); i++){
        for(int j = 0; j< lines.size() - i - 1; j++){
            if(countChars(lines[j]) < countChars(lines[j+1])){
                buffer = lines[j];
                lines[j] = lines[j+1];
                lines[j+1] = buffer;
            }
        }
    }
}
int countChars(const string& line){
    int count = 0;
    for(char i : line){
        if(i != ' '){
            count++;
        }
    }
    return count;
}
vector<string> getLines(const string& fileName){
    string line;
    ifstream file(fileName, ios::in);
    vector<string> lines;
    while(!file.eof()){
        getline(file, line);
        lines.push_back(line);
    }
    file.close();
    return lines;
}
void copyLinesToAnotherFile(const string& fileName1, string fileName2){
    ifstream file1(fileName1, ios::in);
    ofstream file2(fileName2, ios::out);
    vector <string> lines = getLines(fileName1);
    sortStrings(lines);
    for( const string& line : lines){
        if(!line.empty()) {
            file2 << "Length of this line is " << countChars(line) << "----" << line << endl;
        }
    }
    file1.close();
    file2.close();
}
string askForPermission(){
    string answer;
    cout << "Do you want to save your work? Type 'no' to delete it afterwards." << endl;
    getline(cin, answer);
    return answer;
}