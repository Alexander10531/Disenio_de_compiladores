from re import search, match, findall, sub
from operator import add

#Creacion de la clase syntacticAnalyzer
class SyntacticAnalyzer:

    # Creacion del constructor asociado a syntactint analizer
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
    # Creacion de la funcion que retorna la variable output
    # recordando que esta funcion funciona para almacenar todos los prints de pantalla
    def getOutput(self):
        return self.output

    # Funcion que sirve para retornar los valores que se almacenan en memoria, todos aquellos
    # que sean de tipo string
    def getStrMemory(self):
        return self.memoryStr

    # Funcion que sirve para retornar los valores que se almacenan en memoria, todos aquellos
    # que sean de tipo string
    def getIntMemory(self):
        return self.memoryInt

    # Funcion que sirve para extraer todos los lexemas y tokens que se encuentran dentro de la
    # variable symbolTable
    def extractInfo(self):
        for i in range(0, len(self.symbolTable)):
            if self.symbolTable[i][0] == "$":
                self.finalInstruction.append(i)
            self.lexeme.append(self.symbolTable[i][0])
            self.code.append(self.symbolTable[i][1])
    
    # Funcion que retorna los lexemas que se encuntran dentro de la variable lexeme 
    def getLexemes(self):
        return self.lexeme

    # Funcion que sirve para enviar los datos almacenados en code, que almacenan 
    # todos los tokens asociados a los lexemas encontrados
    def getCode(self):
        return self.code

    # Funcion que retornara la lista que obtiene la funcion finalInstrucition 
    # donde estan almacenados donde terminan cada una de las instrucciones
    def getFinalInstruction(self):
        return self.finalInstruction

    # Funcion que retorna la variable symbolTable donde se almacenaro todos los 
    # tokens y lexemas en el analizador lexicografico
    def getSymbolTable(self):
        return self.symbolTable

    # Funcion que sirve como parte toral dentro del analizador lexicografico
    # y analizador sintactico 
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

    # Funcion que sirve para almacenar en memoria las asignaciones como puede llegar a ser 
    # str var_1 = 'Esta es una cadena'
    # str var_2 = "Esta otra cadena"
    # int cadena1 = 2
    # int cadena2 = 3
    # int cadena3 = cadena1 
    # Todas estas son asignaciones que se almacenaran dentro de un diccionario.
    # Dentro de esta funcion tambien se evitara que se almacenen cadenas en variables que 
    # fueron declaradas como str o enteros en variables que fueron declaradas como int
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

    # Obtain Lexeme es una funcion que sirve para retornar un lexema en especifico a partir del indice i
    def obtainLexeme(self, i, code):
        return self.lexeme[i + 1: self.finalInstruction[0]][self.code[i + 1 : self.finalInstruction[0]].index(code)]

    # saveValue es una subFuncion que se utiliza en reserveMemory en la cual se realiza 
    # sobre la cual se verifica si la variable ya fue declara y si fue declara y se quiere 
    # cambiar el tipado de la variable entonces la elimiara dentro del diccionario correspondiente y 
    # y lo agregara en el otro diccionario
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

    # Change Value es la funcion que sirve para poder cambiar las apareciones de una variable por su valor correspondiente 
    # por ejemplo cuando se esta realizando las siguientes instrucciones. 
    # int var = 1
    # show(var_1)
    # Por lo que luego de pasar por esta funcion lo que hara sera
    # int var = 1 
    # show(1)
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
    
    # FindFunction lo que hara sera encontrar las palarabas reservadas a las funciones es 
    # decir cuando el analizador lexicografico encuentra la palabra reservada repeat
    # se redigira a la funcion llamada functionRepeat y la functionRepeat hara las operaciones
    # correspondientes y se hara lo mismo con las funciones concat y show.   
    def findFunction(self, i):
        lista = self.code[i : self.finalInstruction[0]]
        lista1 = self.lexeme[i : self.finalInstruction[0]]
        lista.reverse()
        while True:
            if 500 in self.code[i : self.finalInstruction[0]]:
                start = (len(lista) - 1) - lista.index(500)
                final = lista1.index(")")
                self.functions[self.lexeme[i + start]](i, start, final)
                lista = self.code[i : self.finalInstruction[0]]
                lista1 = self.lexeme[i : self.finalInstruction[0]]
                lista.reverse()
            else: 
                break
    
    # Funcion changeOperation lo que hara sera encontrar cada una de las operaciones matematicas correspondientes 
    # y cambiarlas por su resultando. Se mostraria en la tabla de simbolos de la siguiente manera: 
    # show(1 + 1)
    # luedo de pasar por esta funcion la tabla de simbolos lo vera de la siguiente manera. 
    # show(2)
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

    # SetSymbol sirve en caso de que se necesite cambiar los valores que estan dentro de la tabla de simbolos,
    # esta funcion mantendra los valores dentro de las variables lexeme y la variable code.
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
    
    # FunctionShow encargado de realizar todas las operaciones logicas pertinentes para imprimir en pantalla, 
    # realiza una validacion en caso de que la instruccion este bien construida a partir de una expresion regular
    def functionShow(self, i, start, final):
        if(match(r"show\(('[^']*'|\d+)\)", "".join(self.lexeme[start + i : final + (1 + i)])) != None):
            value = search(r"('[^']*'|\d+)", "".join(self.lexeme[start + i : final + (1 + i)])).group()
            value = sub(r"'","",value)
            self.code[i + start] = 400
            self.lexeme[i + start] = value
            self.symbolTable[i + start] = [value, 400]
            self.output += value + "\n"
            del(self.code[start + i + 1 : final + i + 1])
            del(self.lexeme[start + i + 1 : final + i + 1])
            del(self.symbolTable[start + i + 1 : final + i + 1])
            self.fixPosition(self.finalInstruction, -((i + final) - (start + i)))
        else:
            self.error = False
            self.output += "Error:4\nError de sintaxis"

    # FunctionRepeat es un simil la instruccion 2*'Alexander' que retornara "AlexanderAlexander"
    # con la diferencia que en nuestra gramatica se hara de la siguiente manera
    # repeat('Alexander', 2)
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
            self.fixPosition(self.finalInstruction, -((i + final) - (start + i)))
        else: 
            self.error = False
            self.output += "Error:4\nError de sintaxis\n"
    
    # FunctionConcat establece una funcion para concatenar, de nuevo es una analogia a lo que se hace en javascript y python 
    # de la siguiente manera "Alexander" + "Alexander" que retornara el siguiente valor AlexanderAlexander
    # con la distincion que cuando se usa concat se hara de la siguiente manera
    # concat('Alexander','Ismael','Tejeda','Barahona') en la cual retornara el siguiente valor 
    # AlexanderIsmaelTejedaBarahona
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
            self.fixPosition(self.finalInstruction, -((i + final) - (start + i)))
        else:
            self.error = False
            self.output += "Error:4\nError de sintaxis\n"

    # La funcion fixPosition es una funcion transitoria que se utiliza sobre una lista para hacer una suma de   
    # tipo broadcasting.
    def fixPosition(self, lista, position):
        for i in range(0, len(lista)): 
            lista[i] = lista[i] + position
        return lista

    # Reemplaza un caracter e una lista
    def replaceCharInList(self, charR, wordList):
        for i in range(0, len(wordList)):
            wordList[i] = wordList[i].replace(charR, "")
        return wordList
    
    # Encuntra un caracter dentro de una lista.
    def findChar(self, i, char):
        for j in range(i, len(self.lexeme)):
            if self.lexeme[j] == char:
                return j 
