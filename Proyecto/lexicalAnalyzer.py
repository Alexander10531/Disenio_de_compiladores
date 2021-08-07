class LexicalAnalyzer: 

    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.linebyline = self.sourceCode.split('\n')

    def getSourceCode(self):
        return self.sourceCode

    def getlinebyline(self):
        return self.linebyline

    def createSTable(self):
        # for i in self.linebyline: 
        for j in self.linebyline[0]: 
            print(j)