# Lineas encargadas de importas las clases que se encuentran dentro de los archivos lexicalAnalyzer y dentro del 
# archivo syntactciAnalyzer tengase en cuenta que el simbolo asterisco (*) le dice al interprete que 
# importe absolutamente todo lo que esta dentro de esos archivos, si yo quisiera importar solo algunas funciones
# o solo algunas clases tendria que especificar el los identificadores de la clase o funciones respectivamente. 
# Otro aspecto a considerar es que no se le agrega la extesion .py al nombre de los archivos esto teniendo
# en cuenta que se sobreentiende que los archivos utilizados son .py
from lexicalAnalyzer import *
from syntancticAnalyzer import *

# Creacion de una funcion que sirve para realizar la lectura del archivo en cuestion
def fileReader(fileTxt):
    # Apertura del archivo. 
    # El objeto se almacena dentro de una variable llamada fileR
    # Y recibe una instancia de open que recibe como primer parametro fileTxt que es el parametro que se recibe de la funcion file Reader
    # Y el segundo parametro significa que vamos abrir este archivo en forma de lectura.
    fileR = open(fileTxt, "r")
    # Usamos el objeto que habiamos instanciado antes y usamos una funcion propia de la clase llamda read()
    # esta funcion sirve para leer el contendio del archivo (Esto teniendo en cuenta que estamos trabajando 
    # con una archivo que se abrio en forma de lectura)
    return fileR.read()
# Realizamos la instancia de las clases importadas en las primeras dos lineas del codigo. 
lexicalAnalyzer = LexicalAnalyzer(fileReader("file.txt"))
# Llamamos a la funcion llamada createSTable que veremos para que funciona en sus respectivos archivos.
lexicalAnalyzer.createSTable()