from re import match, search, sub

class LexicalAnalyzer: 

    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.symbolTable = []

    def getSourceCode(self):
        return self.sourceCode

    def getSymbolTable(self):
        return self.symbolTable

    def createSTable(self):
        sourceCode1 = sub(r'\n+', ' ', self.sourceCode)
        while len(sourceCode1) != 0:
            if match(r'(int|str|repeat|show)\s*', sourceCode1) != None: 
                sourceCode1 = self.assignEntry2SymbolTable(match(r'(int|str|repeat|show)\s*', sourceCode1), sourceCode1, 100)
            elif match(r'[a-zA-Z]\w{0,14}\s*', sourceCode1) != None:
                sourceCode1 = self.assignEntry2SymbolTable(match(r'[a-zA-Z]\w{0,14}\s*', sourceCode1), sourceCode1, 200)
            elif match(r'(\(|\)|=|>|\+|-|/|,)\s*', sourceCode1) != None:
                sourceCode1 = self.assignEntry2SymbolTable(match(r'(\(|\)|=|>|\+|-|/|,)\s*', sourceCode1), sourceCode1, 300)
            elif match(r'(\"[^\"]*\"|\d)\s*', sourceCode1) != None: 
                sourceCode1 = self.assignEntry2SymbolTable(match(r'(\"[^\"]*\"|\d+)\s*', sourceCode1), sourceCode1, 400)

    def assignEntry2SymbolTable(self, lexeme, sourceCode, code):
        self.symbolTable.append((lexeme.group().strip(), code))
        return sourceCode[lexeme.end():]