from re import search, match, findall
from operator import add, sub
class SyntacticAnalyzer:
    
    def __init__(self, symbolTable): 
        self.functions = {"repeat": self.functionRepeat, "show" : self.functionShow, "concat": self.functionConcat}
        self.symbolTable = symbolTable
        self.error = True
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
        i = 0
        while i < len(self.symbolTable) and self.error: 
            if self.symbolTable[i][1] == 100:
                i = self.reserveMemory(i)
            else: 
                if(self.changeValue(i, False)):
                    if(self.changeOperation(i)):
                        if(500 in self.code[i : self.finalInstruction[0]]):
                            self.findFunction(i)
                    else: 
                        self.output += "Error:4\nError de sintaxis"
                        break
                else: 
                    self.output += "Error:3\nReferencia a memoria no encontrada\n"    
                    break
                i = self.finalInstruction[0] + 1
                del(self.finalInstruction[0])
        self.output += "El Codigo finalizo"

    def reserveMemory(self, i):
        if(search(r"^(\w)+=('[^']*'|\d+|(\w)+)", "".join(self.lexeme[i+1:self.finalInstruction[0]]))) != None:
            if(self.changeValue(i, True)):
                if(self.symbolTable[i][0]) == "str":        
                    if(search(r"'[^']*'", self.obtainLexeme(i, 400)) != None):
                        self.saveValue(self.obtainLexeme(i, 200), self.obtainLexeme(i, 400), "str")
                    else: 
                        i = len(self.symbolTable)
                        self.output += "Error:1\nError de tipado:"
                # ¿En esta parte se tiene que aclarar el tipo de la variable?
                else:
                    if(search(r"\d+", self.obtainLexeme(i, 400)) != None):
                        self.saveValue(self.obtainLexeme(i, 200), self.obtainLexeme(i, 400), "int")
                    else: 
                        i = len(self.symbolTable)
                        self.output += "Error:1\nError de tipado\n:"
            else: 
                i = len(self.symbolTable)
                self.output += "Error:3\nReferencia a memoria no encontrada\n"    
        else:
            i = len(self.symbolTable)
            self.output += "Error:2\nSintaxis erronea\n"        
        newLine = self.finalInstruction[0] + 1
        del(self.finalInstruction[0])
        return newLine

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
                if j >= start:
                    if (self.lexeme[i : self.finalInstruction[0]][j] in self.memoryStr) == True:
                        self.setSymbolTable(i, j, 400)
                    elif (self.lexeme[i : self.finalInstruction[0]][j] in self.memoryInt) == True:
                        self.setSymbolTable(i, j, 400)
                    else: 
                        return False
        return True

    def findFunction(self, i):
        lista = self.code[i : self.finalInstruction[0]]
        lista1 = self.lexeme[i : self.finalInstruction[0]]
        lista.reverse()
        while True:
            if 500 in self.code[i : self.finalInstruction[0]]:
                print(lista)
                print(lista1)
                start = (len(lista) - 1) - lista.index(500)
                final = lista1.index(")")
                self.functions[self.lexeme[i + start]](i, start, final)
                lista = self.code[i : self.finalInstruction[0]]
                lista1 = self.lexeme[i : self.finalInstruction[0]]
                lista.reverse()
            else: 
                break

    def changeOperation(self, j):
        if '+' in self.lexeme[j : self.finalInstruction[0]] or '-' in self.lexeme[j : self.finalInstruction[0]]:
            if search(r'\d+(\+|-)\d+', "".join(self.lexeme[j : self.finalInstruction[0]])) != None:
                coincidence = search(r'\d+(\+|-)', "".join(self.lexeme[j : self.finalInstruction[0]])).group()
                coincidence1 = search(r'(\+|-)\d+', "".join(self.lexeme[j : self.finalInstruction[0]])).group()
                coincidence = coincidence[0:len(coincidence) - 1]
                operator = coincidence1[0]
                coincidence1 = coincidence1[1:]
                if operator == "+":
                    value = self.lexeme[j : self.finalInstruction[0]].index("+")
                    self.symbolTable[j + value - 1] = [str(add(int(coincidence), int(coincidence1))), 400]
                    self.lexeme[j + value - 1] = str(add(int(coincidence), int(coincidence1)))
                    self.code[j + value - 1] = 400
                    del(self.symbolTable[j + value])   
                    del(self.symbolTable[j + value])
                    del(self.code[j + value])   
                    del(self.code[j + value])   
                    del(self.lexeme[j + value])   
                    del(self.lexeme[j + value])
                    print("1. Se Eliminan unos cuantos - longitud" +  str(len(self.symbolTable)))
                else:
                    value = self.lexeme[j : self.finalInstruction[0]].index("-")
                    self.symbolTable[j + value - 1] = [str(add(int(coincidence), -int(coincidence1))), 400]
                    self.lexeme[j + value - 1] = str(add(int(coincidence), -int(coincidence1)))
                    self.code[j + value - 1] = 400
                    del(self.symbolTable[j + value])   
                    del(self.symbolTable[j + value])
                    del(self.code[j + value])   
                    del(self.code[j + value])   
                    del(self.lexeme[j + value])   
                    del(self.lexeme[j + value])            
            else: 
                return False
            self.finalInstruction = self.fixPosition(self.finalInstruction, -2)
        return True

    def setSymbolTable(self, i, j, code):
        try: 
            self.code[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = code
            self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][1] = code
            self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][0] = self.memoryStr[self.lexeme[i : self.finalInstruction[0]][j]]
            self.lexeme[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = self.memoryStr[self.lexeme[i : self.finalInstruction[0]][j]] 
        except: 
            self.code[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = code
            self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][1] = code
            self.symbolTable[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)][0] = self.memoryInt[self.lexeme[i : self.finalInstruction[0]][j]]
            self.lexeme[(self.finalInstruction[0] - len(self.code[i : self.finalInstruction[0]]) + j)] = self.memoryInt[self.lexeme[i : self.finalInstruction[0]][j]] 
    
    def functionShow(self):
        print("Aqui va la funcion show")

    def functionRepeat(self, i, start, final):
        if(match(r"repeat\('[^']*'\,\d+\)", "".join(self.lexeme[start + i : final + (1 + i)])) != None):
            stringRepeat = search(r"'[^']*'", "".join(self.lexeme[start + i : final + (1 + i)])).group()
            valueRepeat = search(r"\d+", "".join(self.lexeme[start + i : final + (1 + i)])).group()
            stringRepeat = stringRepeat[1 : len(stringRepeat) - 1] * int(valueRepeat)
            self.symbolTable[i + start] = ["'" + stringRepeat + "'", 400]
            self.lexeme[i + start] = "'" + stringRepeat + "'"
            self.code[start + i] = 400
            del(self.symbolTable[start + i + 1 : final + 1 + i])
            del(self.lexeme[start + 1 + i : final + 1 + i])
            del(self.code[start + i + 1 : final + 1 + i])
            self.fixPosition(self.finalInstruction, ((i + final) - (start + i)))
        else: 
            self.error = False
            self.output += "Error:4\nError de sintaxis\n"

    def functionConcat(self, i, start, final):
        if(match(r"concat\((('[^']*'\,)+'[^']*')", "".join(self.lexeme[start + i : final + (1 + i)])) != None):
            coincidences = self.replaceCharInList("'", findall(r"'[^']+'","".join(self.lexeme[start + i : final + (1 + i)])))
            concatStr = "'" + "".join(coincidences) + "'"
            self.symbolTable[i + start] = [concatStr, 400]
            self.lexeme[i + start] = concatStr
            self.code[start + i] = 400
            del(self.symbolTable[start + i + 1 : final + 1 + i])
            del(self.lexeme[start + 1 + i : final + 1 + i])
            del(self.code[start + i + 1 : final + 1 + i])
            self.fixPosition(self.finalInstruction, ((i + final) - (start + i)))
        else:
            self.error = False
            self.output += "Error:4\nError de sintaxis\n"

    def fixPosition(self, lista, position):
        for i in range(0, len(lista)): 
            lista[i] = lista[i] + position
        return lista

    def replaceCharInList(self, charR, wordList):
        for i in range(0, len(wordList)):
            wordList[i] = wordList[i].replace(charR, "")
        return wordList