# Escribir un programa que pida al usuario un numero entero y muestre por pantalla si es par o impar.
# Mediante la funcion "str" podemos transformar un algo en una cadena de texto (String).

# Se declara la variable con el valor numerico ingresado.
UnNumero = int(input("Ingrese un numero entero: "))

if UnNumero % 2 == 0 :
    # Si el resto de la division entre el numero y 2 es cero, el numero es par.
    print("El numero " + str(UnNumero) + " es par")
else :
    # En cualquier otro caso, el numero es impar.
    print("Es un numero " + str(UnNumero) + " impar")