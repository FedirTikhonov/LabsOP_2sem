#include "lib.h"

int main() {
    std::vector<TextClass> texts = createTexts();
    outputTexts(texts);
    askToFindLongestString(texts);
    askToAppendLines(texts);
    outputShortestOfLongest(texts);
    outputTexts(texts);

    return 0;
}
