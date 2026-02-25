from ejercicios.ejercicio1 import ejercicio_1
from ejercicios.ejercicio2 import ejercicio_2
from ejercicios.ejercicio3 import ejercicio_3
from ejercicios.ejercicio4 import ejercicio_4
#Preferenciar la clase
from poo.Clases.ejer1poo import Ejercicio1
#carpeta carpeta carpeta          calse

def menuprincipal():
    while True:
        print("\n :: Menú :: ")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Salir")
        
        op = int(input("ingresar la opcion deseada:"))
        match(op):
            case 1:
                #llamada a la funcion 
                #ejercicio_1()
                
                #crear eñl objeto de la clase 
                e1= Ejercicio1
                #Llamada a los metodos 
                e1.leerDatos()
                e1.calcularAprox()
                e1.mostrarResultado()
                
                ejercicio_1()
            case 2:
                ejercicio_2 ()
            case 3:
                ejercicio_3 ()
            case 4:
                ejercicio_4 ()
            case 5:
                print ("hasta pronto")
                break
            case _:
                print("Ingrese un dato valido ")
                