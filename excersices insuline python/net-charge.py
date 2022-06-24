# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  

lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

#Diccionario con pares de clave de valor
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

#identificar cuantos elementos de un tipo hay dentro de una lista

#determinar cuántos aminoácidos Y hay en la insulina
float(insulin.count("Y"))

#método para buscar todas las entidades de una lista
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

#bucle while que imprimirá la carga neta mientras que la variable de pH es igual o inferior a 14.
pH = 0
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    #imprimir la variable netCharge con el pH
    print('{0:.2f}'.format(pH), netCharge)
    #incremento de variable de pH
    pH += 1


