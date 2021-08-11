#^(\w)+=(\"[^\"]*\"|\d+)
# print(self.code[i+1:self.finalInstruction[0]])
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
                line, i = self.reserveMemory(i, line)
        self.output += "Codigo finalizado"
    
    def reserveMemory(self, i, line):
        if(search(r"^(\w)+=('[^']*'|\d+)", "".join(self.lexeme[i+1:self.finalInstruction[0]]))) != None:
            if(self.symbolTable[i][0]) == "str":        
                if(search(r"'[^']*'", self.obtainLexeme(i, 400)) != None):
                    self.memoryStr[self.obtainLexeme(i, 200)] = self.obtainLexeme(i, 400)
                    line = line + 1
                else: 
                    i = len(self.symbolTable)
                    self.output += "Error:1\nError de tipado\nLine:" + str(line) + "\n"
            # ¿En esta parte se tiene que aclarar el tipo de la variable?
            else: 
                if(search(r"\d+", self.obtainLexeme(i, 400)) != None):
                    self.memoryInt[self.obtainLexeme(i, 200)] = int(self.obtainLexeme(i, 400))
                    line = line + 1
                else: 
                    i = len(self.symbolTable)
                    self.output += "Error:1\nError de tipado\nLine:" + str(line) + "\n"
        else:
            self.output += "Error:2\nSintaxis erronea\nLine:" + str(line) + "\n"
        del(self.finalInstruction[0])
        return line, i

    def obtainLexeme(self, i, code):
        return self.lexeme[i + 1: self.finalInstruction[0]][self.code[i + 1 : self.finalInstruction[0]].index(code)]
