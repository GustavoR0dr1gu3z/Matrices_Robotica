import numpy as np
import os

# ASIGNAR MEMORIA PARA LAS MATRICES Y VECTORES
P = np.array([0.0,0.0,0.0])
R = np.array([0.0,0.0,0.0,1.0])
mat = np.array([[1.0,0.0,0.0,0.0],
                [0.0,1.0,0.0,0.0],
                [0.0,0.0,1.0,0.0],
                [0.0,0.0,0.0,1.0]])

res = np.array([[0.0,0.0,0.0,0.0],
                [0.0,0.0,0.0,0.0],
                [0.0,0.0,0.0,0.0],
                [0.0,0.0,0.0,0.0]])

######################################################################
def tx():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[1][1] = round(np.cos(grados))
    mat[1][2] = round(-np.sin(grados))
    mat[2][1] = round(np.sin(grados))
    mat[2][2] = round(np.cos(grados))
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")
        
    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])        
        
    
######################################################################    
def ty():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[0][0] = round(np.cos(grados))
    mat[0][2] = round(np.sin(grados))
    mat[2][0] = round(-np.sin(grados))
    mat[2][2] = round(np.cos(grados))
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)
    
    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    
    
    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])
        
        
######################################################################    
def tz():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[0][0] = round(np.cos(grados))
    mat[0][1] = round(-np.sin(grados))
    mat[1][0] = round(np.sin(grados))
    mat[1][1] = round(np.cos(grados))
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")        
        
    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])
        
        
######################################################################
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
        
######################################################################  
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
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
    print("\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

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

######################################################################
def rtx():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
        
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[1][1] = round(np.cos(grados))
    mat[1][2] = round(-np.sin(grados))
    mat[2][1] = round(np.sin(grados))
    mat[2][2] = round(np.cos(grados))
    mat[0][3] = P[0]
    mat[1][3] = P[1]
    mat[2][3] = P[2]
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])        
        
######################################################################                
def rty():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
        
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[0][0] = round(np.cos(grados))
    mat[0][2] = round(np.sin(grados))
    mat[2][0] = round(-np.sin(grados))
    mat[2][2] = round(np.cos(grados))
    mat[0][3] = P[0]
    mat[1][3] = P[1]
    mat[2][3] = P[2]
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])        
        
######################################################################        
def rtz():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
        
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[0][0] = round(np.cos(grados))
    mat[0][1] = round(-np.sin(grados))
    mat[1][0] = round(np.sin(grados))
    mat[1][1] = round(np.cos(grados))
    mat[0][3] = P[0]
    mat[1][3] = P[1]
    mat[2][3] = P[2]
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])            
        
######################################################################
def trx():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
        
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[1][1] = round(np.cos(grados))
    mat[1][2] = round(-np.sin(grados))
    mat[2][1] = round(np.sin(grados))
    mat[2][2] = round(np.cos(grados))
    mat[0][3] = P[0]
    mat[1][3] = (P[1]*round(np.cos(grados)))-(P[2]*round(np.sin(grados)))
    mat[2][3] = (P[1]*round(np.sin(grados)))+(P[2]*round(np.cos(grados)))
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])        
        
######################################################################                
def tryy():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
        
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[0][0] = round(np.cos(grados))
    mat[0][2] = round(np.sin(grados))
    mat[2][0] = round(-np.sin(grados))
    mat[2][2] = round(np.cos(grados))
    mat[0][3] = P[0]
    mat[1][3] = (P[1]*round(np.cos(grados)))-(P[2]*round(np.sin(grados)))
    mat[2][3] = (P[1]*round(np.sin(grados)))+(P[2]*round(np.cos(grados)))
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])        
        
######################################################################        
def trz():
    print("\n\n------GRADOS DEL GIRO------")
    grados = int(input("Que grados tendrá el giro: "))
    
    print("\n\n------LLENADO DE VECTOR P------")
    for i in range(len(P)):
        P[i] = float(input("Digite el valor {} del punto P: ".format(i)))
        
    print("\n\n------LLENADO DE VECTOR R------")
    for i in range(len(R)-1):
        R[i] = float(input("Digite el valor {} del punto R: ".format(i)))

    mat[0][0] = round(np.cos(grados))
    mat[0][1] = round(-np.sin(grados))
    mat[1][0] = round(np.sin(grados))
    mat[1][1] = round(np.cos(grados))
    mat[0][3] = P[0]
    mat[1][3] = (P[1]*round(np.cos(grados)))-(P[2]*round(np.sin(grados)))
    mat[2][3] = (P[1]*round(np.sin(grados)))+(P[2]*round(np.cos(grados)))
    
    print("\n\n------MOSTRANDO MATRIZ------")
    for i in mat:
        print(i)

    print("\n\n-----MOSTRANDO VECTOR-------")
    for i in R:
        print("["+str(i)+"]")    

    print("\n\n-----MOSTRANDO RESULTADO-------")
    a = mat.dot(R)
    for i in range(len(a)):
        print(a[i])            

######################################################################
def tras_rot():
    # MOSTRAR MATRIZ
    for i in range(len(mat)): # Filas
        for j in range(len(mat)): # Columnas
            res[i][j] = mat[i][j]

    sentido = input("Eje en que rotará (X, Y, Z): ")
    if(sentido == 'X' or sentido == 'x'):
        trx()
    elif(sentido == 'Y' or sentido == 'y'):
        tryy()
    elif(sentido == 'Z' or sentido == 'z'):
        trz()
    else:
        print("DIGITO INCORRECTO")  

######################################################################  
def rot_tras():
    # MOSTRAR MATRIZ
    for i in range(len(mat)): # Filas
        for j in range(len(mat)): # Columnas
            res[i][j] = mat[i][j]

    sentido = input("Eje en que rotará (X, Y, Z): ")
    if(sentido == 'X' or sentido == 'x'):
        rtx()
    elif(sentido == 'Y' or sentido == 'y'):
        rty()
    elif(sentido == 'Z' or sentido == 'z'):
        rtz()
    else:
        print("DIGITO INCORRECTO")         
######################################################################        
# SI ES ROTACIÓN O TRASLACIÓN
os.system("clear")
f = input("Resolver para rotación, traslacion, Rot_Tras, Tras_Ror? (R/T/RT/TR): ")

if(f == 'r' or f == 'R'):
    rotacion()
elif (f == 'T' or f == 't'):
    traslacion()
elif (f == 'RT' or f == 'rt' or f == 'rT' or f == 'Rt'):
    rot_tras()
elif (f == 'TR' or f == 'tr' or f == 'Tr' or f == 'tR'):
    tras_rot()
else:
    print("DIGITO INCORRECTO")


