# Las 2 siguientes lineas no comentadas se usan para importar lo que este dentro de los archivos lexicalAnalyzer y syntacticAnalyzer 
# estas lineas se podrian leer de la siguiente manera. 
# from lexicalAnalyzer import * == De el archivo llamada lexicalAnalyzer utiliza todo
# aspectos a considerar es que el interprete de python ya entiende que lexicalAnalyzer y syntacticAnalyzer son archivos con extension .py 
# por ende no es necesario agregarlo
# Otro aspecto a considerar es que yo podria importar solo algunos segmentos de codigo es decir si dentro de ese archivo yo tengo otras clases 
# u otras funciones y no quiero importarlas todas entonces reemplazaria el asterisco "*" por el nombre de la clase o funcion a importar.
# el asterisco "*" importara todo lo que este dentro del archivo
from lexicalAnalyzer import *
from syntancticAnalyzer import *

# Esta es la manera en la que se declara una funcion y tiene como parametro fileTxt
def fileReader(fileTxt):
    fileR = open(fileTxt, "r")
    lines = fileR.read().split('\n')    


fileReader("file.txt") 