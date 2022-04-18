#include "lib.h"

int main() {
    std::vector<TextClass> texts = createTexts();
    outputTexts(texts);
    askToFindLongestString(texts);
    askToAppendLines(texts);
    return 0;
}
