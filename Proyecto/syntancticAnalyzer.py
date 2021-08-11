from re import search
#^(\w)+=(\"[^\"]*\"|\d+)
class SyntacticAnalyzer:
    
    def __init__(self, symbolTable): 
        self.symbolTable = symbolTable
        self.finalInstruction = []
        self.lexeme = []
        self.code = []
        self.extractInfo()
        self.doIt()

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
        for i in range(0, len(self.symbolTable)):
            if self.symbolTable[i][1] == 100:
                if(search(r"^(\w)+=('[^']*'|\d+)", "".join(self.lexeme[i+1:self.finalInstruction[0]]))) != None:
                    # print(self.code[i+1:self.finalInstruction[0]])
                    if(self.symbolTable[i][0]) == "str":        
                        if(search(r"'[^']*'",self.lexeme[i + 1: self.finalInstruction[0]][self.code[i + 1 : self.finalInstruction[0]].index(400)]) != None):
                            print("Aqui se va hacer todo el almacenamiento de las variables")
                        else: 
                            print("Aqui ha ocurrido un error :c")
                    del(self.finalInstruction[0])
                    