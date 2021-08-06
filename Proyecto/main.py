from lexicalAnalyzer import *
from syntancticAnalyzer import *

def fileReader(fileTxt):
    fileR = open(fileTxt, "r")
    lines = fileR.read().split('\n')    


fileReader("file.txt") 