from re import match, search, sub

class LexicalAnalyzer: 

    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.linebyline = self.sourceCode.split('\n')
        self.symbolTable = []

    def getSourceCode(self):
        return self.sourceCode

    def getlinebyline(self):
        return self.linebyline

    def createSTable(self):
        sourceCode1 = sub(r'\n\s+|^\s+\n', '\n', self.sourceCode)
        sourceCode1 = sub(r'^\s+', '', sourceCode1)
        while True:
            if match(r'int\s*|str\s*', sourceCode1) != None: 
                sourceCode1 = self.reservedWord(match(r'int\s*|str\s*', sourceCode1), sourceCode1)
            elif match(r'[a-zA-Z]\w{0,14}', sourceCode1) != None:
                sourceCode1 = self.identifierWord(match(r'[a-zA-Z]\w{0,14}', sourceCode1), sourceCode1)
            elif match(r'=|>|\+|-|/|\"', sourceCode1) != None:
                sourceCode1 = self.identifierWord(match(r'=|>|\+|-|/', sourceCode1), sourceCode1)
            elif match(r'\"[^\"]*\"|\d', sourceCode1) != None: 
                sourceCode1 = self.values(match(r'\"[^\"]*\"|\d', sourceCode1), sourceCode1)
                print(sourceCode1)
                break
    
    def reservedWord(self, lexeme, sourceCode):
        self.symbolTable.append((lexeme.group(), 100))
        return sourceCode[lexeme.end():]
        
    def identifierWord(self, lexeme, sourceCode):
        self.symbolTable.append((lexeme.group(), 200))
        return sourceCode[lexeme.end():]
    
    def operators(self, lexeme, sourceCode):
        self.symbolTable.append((lexeme.group(), 300))
        return sourceCode[lexeme.end():]

    def values(self, lexeme, sourceCode):
        self.symbolTable.append((lexeme.group, 400))
        return sourceCode[lexeme.end():]