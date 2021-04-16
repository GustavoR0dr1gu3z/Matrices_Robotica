import numpy as np

# SI ES ROTACIÓN O TRASLACIÓN
f = input("Resolver para rotación o traslacion? (R/T): ")

if(f == 'r' or f == 'R'):
    print("ROTACIÓN")
elif (f == 'T' or f == 't'):
    print("TRASLACIÓN")
else:
    print("DIGITE NUMERO VALIDO")