import random

def getch():
    letra = input("Escribe una letra: ")
    return letra[0]  # Solo toma la primera letra

oportunidades = 6
palabras = ['Dado','Oso','Raton','Casa','Amistad']
palabra = random.choice(palabras)
n = len(palabra)
turnos = 0
aciertos = 0

cabeza = ' '
cuerpo = ' '
manoIzquierda = ' '
manoDerecha = ' '
pieIzquierdo = ' '
pieDerecho = ' '

casillas = ['_'] * n

while turnos < oportunidades and aciertos < n:
    print('\nOportunidades restantes:', oportunidades - turnos)
    print(' '.join(casillas))
    
    letra = getch()
    encontrado = False
    
    for i in range(n):
        if letra.upper() == palabra[i].upper():
            encontrado = True
            if casillas[i] == '_':
                casillas[i] = palabra[i]
                aciertos += 1
    
    if not encontrado:
        turnos += 1
        print('Letra no encontrada.')
        if turnos==1: cabeza = '☺'
        elif turnos==2: cuerpo = '┼'
        elif turnos==3: manoDerecha = '/'
        elif turnos==4: manoIzquierda = '\\'
        elif turnos==5: pieDerecho = '/'
        elif turnos==6: pieIzquierdo = '\\'
    
    print('     ' + cabeza)
    print('    ' + manoDerecha + cuerpo + manoIzquierda)
    print('    ' + pieDerecho + ' ' + pieIzquierdo)

if aciertos == n:
    print('Felicidades, has ganado.')
else:
    print('Has perdido.')
print('La palabra secreta era:', palabra)
