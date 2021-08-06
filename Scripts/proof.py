import re

def findPattern(fileName): 
    fileR = open(fileName, 'r+')
    coincidence = fileR.read()
    finalRes = re.findall(r'(\w*a\w*a\w*a[A-z]*|\w*e\w*e\w*e[A-z]*|\w*i\w*i\w*i[A-z]*|\w*o\w*o\w*o[A-z]*|\w*u\w*u\w*u[A-z]*)', coincidence) + re.findall(r'\d+\w*', coincidence)
    coincidence = re.split(r"\n|\s", coincidence)
    specialChar = []
    for i in coincidence:
        for j in i: 
            if re.match('[\W_]', j) != None: 
                specialChar.append(i)
    finalRes = list(set(specialChar)) + finalRes
    fileR.close()
    del(coincidence)
    del(specialChar)
    del(j)
    del(i)
    printResults(finalRes)

def printResults(finalRes):
    fileW = open("finalResults.txt", 'w')
    if len(finalRes) > 0: 
        fileW.write(str(finalRes))
        print("Se imprimieron los resultados correctamente")
    else: 
        print("No hay ninguna coincidencia")

findPattern("textPattern.txt")