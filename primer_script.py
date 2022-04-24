from ast import arg
import sys

if len (sys.argv)==3:
    texto =sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range (repeticiones):
        print (texto)
        print (sys.argv) #para ver el contexto entero
else:
    print("error, introduce los argumentos")
    print("ejemplo: escribir_lineas.py texto 5")


#C:\Users\27957541238\Desktop\python\primer_script.py