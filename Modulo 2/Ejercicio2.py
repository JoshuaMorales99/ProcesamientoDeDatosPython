# Escribir un programa que pida al usuario dos numeros y devuelva su division. Si el usuario no introduce
# numeros o introduce una division por 0, se debe devolver un aviso de error.

# Se declaran las variables con los valores numericos ingresados.
Dividendo = int(input("Ingrese el numero dividendo: "))
Divisor = int(input("Ingrese el numero divisor: "))

if Divisor == 0 :
    # Si el divisor es igual a 0, se imprime un error.
    print("Error, no se puede dividir por 0")
else :
    # En cualquir otro caso, se muestra el resultado de la division.
    print(Dividendo / Divisor)