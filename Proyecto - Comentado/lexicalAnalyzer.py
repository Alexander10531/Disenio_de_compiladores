# De la misma manera que en el archivo principal pero con una libreria que es propia de python 
# importamos re, re es la libreria de python con la que se utilizan expresiones regulares. 
# y de aqui importamos las funciones match y sub, la razon por la que se utiliza match y sub y no search y subn 
# se describira a continuacion. 
# 1. Usaremos match porque para simular la funcionalidad de un analizador lexico debemos analizar cada uno de los 
# caracteres de manera simultanea con lo que si se consulta la documentacion veremos que search encontrara
# todas las coindicencias por el contrario de match que al utilizarse solo se concentra en los primeros 
# caracteres. 
# 2. Usaremos la funcion sub porque no hay razon de querer los valores que nos retorna subn.
from re import match, sub

# Creacion de la clase LexicalAnalyzer
class LexicalAnalyzer: 

    # Iniciailizacion del constructor
    def __init__(self, sourceCode):
        # Inicializacion de las variables sourceCode y symbolTable
        # Observe que se antepone "self." esto es mas sencillo de entender si se utilizo Java y se entenderia como
        # un analogo de "this". 
        # Si no se ha usado Java entiendase self como el indicador de que la variable sourceCode y symbolTable
        # son propias de la clase LexicalAnalyzer y su alcance se puede dar a traves de toda la instancia de la clase
        # o como veremos mas adelante acceder a estos valores mediante funciones get, no se describira el uso de las variables
        # porque sus nombres son autodescriptivos si se toma en cuenta que SourceCode = Codigo Fuente y SymbolTable = Tabla de simbolos 
        self.sourceCode = sourceCode
        self.symbolTable = []

    # <---------------------- Funciones get ---------------------->
    def getSourceCode(self):
        return self.sourceCode

    def getSymbolTable(self):
        return self.symbolTable
    # <---------------------- Fin funciones get ---------------------->

    # Funcion que sirve para la creacion de la tabla de simbolos en esta funcion se realizan algunas de lo que se describe
    # en el libro como microexpresiones regulares que se usan en el analizador lexico para indentificar con que se esta trabajando
    # en este punto solo veremos los siguientes elementos asociados a su codigo en la tabla de simbolos. 
    # Palabras reservadas - Codigo 100
    # Identificadores - Codigo 200
    # Operadores - Codigo 300
    # Valores - Codigo 400
    # Dado a la complejida de las expresiones regulares no se explicaran de manera documentada, para mas informacion se 
    # puede utilizar regex101.com para hacer prubeas de cada una de las expresiones regulares y aprender de manera dinamica como 
    # funcionan
    def createSTable(self):
        # En esta parte se eliminan todos los saltos de lineas, recordemos que una de las funciones del analizador lexicografico 
        # es la de eliminar los espacios y saltos de linea dentro del codigo fuente por ende para manera un estandar en el analis
        # se elemenina todos los saltos de linea y los espacios se limpiaran al agregarse a la tabla de simbolos que se asocia 
        # a cada uno de los lexemas encontrados. 
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

    # Se agregan cada uno de los lexemas encontrados con su respectivo codigo
    def assignEntry2SymbolTable(self, lexeme, sourceCode, code):
        # Aqui se hace uso de lo que se hablo anteriormente, en la funcion createStable eliminamos cada uno de los saltos de linea 
        # y con la funcion strip se eliminan los espacios dentro de los lexemas encontrados. 
        self.symbolTable.append((lexeme.group().strip(), code))
        return sourceCode[lexeme.end():]