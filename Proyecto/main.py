from lexicalAnalyzer import *
from syntancticAnalyzer import *

def fileReader(fileTxt):
    fileR = open(fileTxt, "r")
    return fileR.read()

def showMeWhatUGot():
    SymbolTFile = open('resources/symbolTable.html', "w")

lexicalAnalyzer = LexicalAnalyzer(fileReader("file.txt"))
lexicalAnalyzer.createSTable()
showMeWhatUGot()