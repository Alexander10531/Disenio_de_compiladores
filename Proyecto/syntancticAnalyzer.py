class SyntacticAnalyzer:
    
    def __init__(self, symbolTable): 
        self.symbolTable = symbolTable
        self.finalInstruction = []
        self.lexeme = []
        self.code = []
        self.extractInfo()

    def extractInfo(self):
        for i in range(0, len(self.symbolTable)):
            if self.symbolTable[i][0] == "$":
                self.finalInstruction.append(i)
            else: 
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
    
    # def doIt(self):
    #     for i in range(0, len(self.symbolTable)):
    #         if self.symbolTable[i][1] == 400: 
    #             pass