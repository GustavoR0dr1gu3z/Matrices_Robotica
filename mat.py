import numpy as np
import os

# ASIGNAR MEMORIA PARA LAS MATRICES Y VECTORES
P = np.array([0,0,0])
R = np.array([0,0,0,1])
mat = np.array([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])

res = np.array([[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]])


def tx():
    print("TX")
def ty():
    print("TY")
def tz():
    print("TZ")


def rotacion():
    sentido = input("Eje en que rotará (X, Y, Z): ")
    if(sentido == 'X' or sentido == 'x'):
        tx()
    elif(sentido == 'Y' or sentido == 'y'):
        ty()
    elif(sentido == 'Z' or sentido == 'z'):
        tz()
    else:
        print("DIGITO INCORRECTO")  
        
        
def traslacion():    
        # MOSTRAR MATRIZ
    for i in range(len(mat)): # Filas
        for j in range(len(mat)): # Columnas
            res[i][j] = mat[i][j]
    '''
    for i in res:
        print(i)
    '''
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = int(input("Digite el valor {} del punto P: ".format(i)))
    print("\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = int(input("Digite el valor {} del punto R: ".format(i)))

    res[0][3] = P[0]
    res[1][3] = P[1]
    res[2][3] = P[2]
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in res:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = res.dot(R)
    for i in range(len(a)):
        print(a[i])

            
# SI ES ROTACIÓN O TRASLACIÓN
os.system("clear")
f = input("Resolver para rotación o traslacion? (R/T): ")

if(f == 'r' or f == 'R'):
    rotacion()
elif (f == 'T' or f == 't'):
    traslacion()
else:
    print("DIGITO INCORRECTO")


