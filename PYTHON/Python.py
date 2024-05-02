saludo="hola mundo"
print(saludo)
#A continuación viene una prueba de cadena
s_edad = 35
numero = s_edad+1
print(numero)

nombre="John"
print(nombre + " tiene " + str(s_edad) + " años");

#Definimos una función y le decimos los parámetros que tiene
def suma(a, b):
    return a+b #Esto es lo que tiene que hacer la función. Delante se puede poner "return"
    
print ("el resultado es ", suma(2, 3)) #Aquí le damos valores a los parámetros.

#Ahora otro ejemplo pero con palabras
def muestra_en_pantalla(frase1, frase2): #A los parámetro no hace falta ponerles ""
    print(frase1, frase2)
muestra_en_pantalla("Dj Tosom", "es el mejor DJ")

x=suma(5, 8) #Si la función "suma" la guardamos en una variable "x" podemos llamar a la función desde "x"
print(x)

def f1(a): #Función dentro de otra función
    print(a)
    b = 100
    def f2(x): #Es importante poner ":" al final de declarar la función
        print(x)
    f2(b)
f1("Python")

#Recursividad

def factorial(x):
    if x>1:
        return x*factorial(x-1) #Aquí si es necesario poner "return"
    else:
        return 1 #Aquí si es necesario poner "return"

print(factorial(x))

def maxmin(lista):
    return max(lista), min(lista)
num=[1, 5, 6, 9, 12]
maximo, minimo = maxmin(num)
print(maximo , minimo, sep="  ")

#Calcular númer primo

def es_primo(numero):
    if numero<=1:
        return False
    for i in range(2, int(numero **0.5)+1):
        if numero % i ==0:
            return False
    return True
numero=11
if es_primo(numero):
    print(f"{numero} este número es primo")
else: print(f"{numero} este número no es primo")