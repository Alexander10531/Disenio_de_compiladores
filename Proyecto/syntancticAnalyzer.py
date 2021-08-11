from os import truncate
from re import search
class SyntacticAnalyzer:
    
    def __init__(self, symbolTable): 
        self.symbolTable = symbolTable
        self.finalInstruction = []
        self.memoryInt = {}
        self.memoryStr = {}
        self.lexeme = []
        self.code = []
        self.output = ""
        self.extractInfo()
        self.doIt()

    def getOutput(self):
        return self.output
    
    def getStrMemory(self):
        return self.memoryStr
    
    def getIntMemory(self):
        return self.memoryInt

    def extractInfo(self):
        for i in range(0, len(self.symbolTable)):
            if self.symbolTable[i][0] == "$":
                self.finalInstruction.append(i)
            self.lexeme.append(self.symbolTable[i][0])
            self.code.append(self.symbolTable[i][1])

    def getLexemes(self):
        return self.lexeme

    def getCode(self):
        return self.code

    def getFinalInstruction(self):
        return self.finalInstruction

    def getSymbolTable(self):
        return self.symbolTable
    
    def doIt(self):
        line = 0
        for i in range(0, len(self.symbolTable)):
            if self.symbolTable[i][1] == 100:
                # self.changeValue(i, True)
                line, i = self.reserveMemory(i, line)                
        self.output += "Codigo finalizado"
    
    def reserveMemory(self, i, line):
        if(search(r"^(\w)+=('[^']*'|\d+|(\w)+)", "".join(self.lexeme[i+1:self.finalInstruction[0]]))) != None:
            if(self.changeValue(i, True)):
                if(self.symbolTable[i][0]) == "str":        
                    if(search(r"'[^']*'", self.obtainLexeme(i, 400)) != None):
                        self.saveValue(self.obtainLexeme(i, 200), self.obtainLexeme(i, 400), "str")
                        line = line + 1
                    else: 
                        i = len(self.symbolTable)
                        self.output += "Error:1\nError de tipado\nLine:"
                # ¿En esta parte se tiene que aclarar el tipo de la variable?
                else:
                    if(search(r"\d+", self.obtainLexeme(i, 400)) != None):
                        self.saveValue(self.obtainLexeme(i, 200), self.obtainLexeme(i, 400), "int")
                        line = line + 1
                    else: 
                        i = len(self.symbolTable)
                        self.output += "Error:1\nError de tipado\n:"
            else: 
                i = len(self.symbolTable)
                self.output += "Error:3\nReferencia a memoria no encontrada\n"    
        else:
            i = len(self.symbolTable)
            self.output += "Error:2\nSintaxis erronea\n"        
        
        del(self.finalInstruction[0])
        return line, i

    def obtainLexeme(self, i, code):
        return self.lexeme[i + 1: self.finalInstruction[0]][self.code[i + 1 : self.finalInstruction[0]].index(code)]

    def saveValue(self, identifier, value, typeMemory):
        if typeMemory == "str":
            if identifier in self.memoryInt: 
                del(self.memoryInt[identifier])
                self.memoryStr[identifier] = value
            else: 
                self.memoryStr[identifier] = value
        elif typeMemory == "int":
            if identifier in self.memoryStr: 
                del(self.memoryStr[identifier])
                self.memoryInt[identifier] = value
            else: 
                self.memoryInt[identifier] = value

    def changeValue(self, i, reserve):
        start = 0     
        if reserve: 
            start = self.code[i : self.finalInstruction[0]].index(300)
        for j in range(0, len(self.code[i : self.finalInstruction[0]])): 
            if self.code[i : self.finalInstruction[0]][j] == 200: 
                if j > start:
                    if (self.lexeme[i : self.finalInstruction[0]][j] in self.memoryStr) == True:
                        self.code[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = 400
                        self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][1] = 400
                        self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][0] = self.memoryStr[self.lexeme[i : self.finalInstruction[0]][j]]
                        self.lexeme[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = self.memoryStr[self.lexeme[i : self.finalInstruction[0]][j]] 
                    elif (self.lexeme[i : self.finalInstruction[0]][j] in self.memoryInt) == True:
                        self.code[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = 400
                        self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][1] = 400
                        self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][0] = self.memoryInt[self.lexeme[i : self.finalInstruction[0]][j]]
                        self.lexeme[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = self.memoryInt[self.lexeme[i : self.finalInstruction[0]][j]] 
                    else: 
                        return False
        return True