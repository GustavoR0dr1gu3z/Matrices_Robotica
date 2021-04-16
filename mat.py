import numpy as np
import os

# ASIGNAR MEMORIA PARA LAS MATRICES Y VECTORES
P = [0,0,0]
R = [0,0,0]
mat =  [[1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]]

res =  [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

def rotacion():
    # MOSTRAR MATRIZ
    for i in range(len(mat)): # Filas
        for j in range(len(mat)): # Columnas
            res[i][j] = mat[i][j]
    '''
    for i in res:
        print(i)
    '''
    print("\n\n------LLENADO DE VECTORES------")
    for i in range(len(P)):
        P[i] = int(input("Digite el valor {} del punto P: ".format(i)))

    

def traslacion():    
    print("Digite los valores del punto P")



# SI ES ROTACIÓN O TRASLACIÓN
os.system("clear")
f = input("Resolver para rotación o traslacion? (R/T): ")

if(f == 'r' or f == 'R'):
    rotacion()
elif (f == 'T' or f == 't'):
    traslacion()
else:
    print("DIGITO INCORRECTO")


