# Escribir un programa que pregunte al usuario su edad. Mostrar por pantalla si es mayor de edad o no.

# Mediante la funcion "input" pedimos al usuario que ingrese un determinado dato. Este siempre es un String.
# Mediante la funcion "int" podemos transformar un algo en un numero entero.

# Se declara la variable con el valor numerico ingresado.
Edad = int(input("Ingrese su edad: "))

if (Edad < 18) :
    # Si la edad es menor a 18, es menor de edad.
    print("Es menor de edad")
else :
    # En cualquier otro caso, es mayor de edad.
    print("Es mayor de edad")