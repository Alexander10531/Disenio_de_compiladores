from lexicalAnalyzer import *
from syntancticAnalyzer import *

def fileReader(fileTxt):
    fileR = open(fileTxt, "r")
    return fileR.read()

def showMeWhatUGot(data):
    symbolTFile = open('resources/symbolTable.html', "w")
    firstContent = """
<!DOCTYPE html>
<html lang="en">
<head>
\t<meta charset="UTF-8">
\t<meta http-equiv="X-UA-Compatible" content="IE=edge">
\t<meta name="viewport" content="width=device-width, initial-scale=1.0">
\t<link rel="stylesheet" href="styles.css">
\t<link rel="preconnect" href="https://fonts.googleapis.com">
\t<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
\t<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
\t<script src="https://kit.fontawesome.com/26a131d264.js" crossorigin="anonymous"></script>
\t<title>Document</title>
</head>
<body>
\t<header>
\t\t<nav>
\t\t\t<div class="navbar-container">
\t\t\t\t<div class="logo-container">
\t\t\t\t\t<i class="fas fa-atom logo-atom"></i>
\t\t\t\t</div>
\t\t\t\t<div class="container-mode">
\t\t\t\t\t<div class="button-container">
\t\t\t\t\t\t<div class="button"></div>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</nav>
\t</header>
\t<main id="main">
\t\t<svg class="wave" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#000000" fill-opacity="0.12" d="M0,160L120,170.7C240,181,480,203,720,202.7C960,203,1200,181,1320,170.7L1440,160L1440,320L1320,320C1200,320,960,320,720,320C480,320,240,320,120,320L0,320Z"></path></svg>
\t\t<div class="containerTable">
\t\t\t<table class="symbolTable">
\t\t\t\t<tr>
\t\t\t\t\t<th>No&#176;</th>
\t\t\t\t\t<th>Tipo</th>
\t\t\t\t\t<th>Lexema encontrado</th>
\t\t\t\t</tr>
    """
    secondContent = """
\t\t\t\t</table>
\t\t</div>
\t</main>
</body>
<script src="script.js"></script>
</html>
    """
    value = """"""
    for i in range(0, len(data)):
        value += """\t\t\t\t<tr>
\t\t\t\t\t<td>""" + str(i) +"""</td>
\t\t\t\t\t<td>""" + str(data[i][0]) +"""</td>
\t\t\t\t\t<td>""" + str(data[i][1])+ """</td>
\t\t\t\t</tr>
"""
    symbolTFile.write(firstContent + value + secondContent)

lexicalAnalyzer = LexicalAnalyzer(fileReader("file.txt"))
lexicalAnalyzer.createSTable()
showMeWhatUGot(lexicalAnalyzer.getSymbolTable())
syntacticAnalyzer = SyntacticAnalyzer(lexicalAnalyzer.getSymbolTable())