from lexicalAnalyzer import *
from syntancticAnalyzer import *

def fileReader(fileTxt):
    fileR = open(fileTxt, "r")
    return fileR.read()

lexicalAnalyzer = LexicalAnalyzer(fileReader("file.txt"))
lexicalAnalyzer.createSTable()
print(lexicalAnalyzer.symbolTable)