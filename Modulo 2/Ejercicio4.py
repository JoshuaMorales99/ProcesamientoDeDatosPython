# Solicitar al usuario que ingrese dos numeros y mostrar cual es el menor. Considerar el caso en que ambos
# numeros son iguales.

# Se declaran las variables con los valores numericos ingresados.
UnNumero = int(input("Ingrese un numero: "))
OtroNumero = int(input("Ingrese otro numero: "))

if UnNumero < OtroNumero :
    # Si el primer numero es menor al segundo, se muestra el primer numero ingresado.
    print("El numero " + str(UnNumero) + " es menor")
elif OtroNumero < UnNumero :
    # Si el segundo numero es menor al segundo, se muestra el segundo numero ingresado.
    print("El numero " + str(OtroNumero) + " es menor")
else :
    # En cualquier otro caso, ambos numeros son iguales.
    print("Los numeros son iguales")