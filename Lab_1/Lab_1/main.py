import Lib_Lab1


sourceFileName = "sourceFile.txt"                   # Names of files.
newFileName = "newFile.txt"

Lib_Lab1.pushLinesToFile(sourceFileName)            # Push text to source file.

lineList = Lib_Lab1.fileToList(sourceFileName)      # Copy contents of the file to list.
lineList = Lib_Lab1.sortStrings(lineList)           # Sort list.

Lib_Lab1.listToFile(lineList, newFileName)          # Copy contents of the sorted list to a new file.

Lib_Lab1.askToDelete(sourceFileName, newFileName)   # Leave it up to user to decide whether to save the file or not.

