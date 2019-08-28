print ("Hola mundo")
#variables
#int, str, bool, float
x = 2
print (type(x))

y = 0.5
print (type(y))

z = "hola"
print (type(z))

#funciones
#def persona(nombre, apellido, edad):
#  print("Hola", nombre, "su apellido es:", apellido, "ud tiene:", edad)

#persona("Tania","Delgado,","22 años.")

#nombre = input("Digite su nombre: ")
#apellido = input("Digite su apellido: ")
#edad = input("Digite su edad: ")
#persona(nombre,apellido,edad)

def suma(a,b):
    sumar=a+b
    print("El suma es: ",sumar)

a = int(input("Digite a: "))
b = int(input("Digite b: "))
suma(a,b)

def resta(a,b):
    restar=a-b
    print("La resta es: ", restar)

resta(a,b)

def multi(a,b):
    multipli=a*b
    print("La resta es: ", multipli)

multi(a,b)

def division(a,b):
    dividir=a/b
    print("La resta es: ", dividir)

division(a,b)