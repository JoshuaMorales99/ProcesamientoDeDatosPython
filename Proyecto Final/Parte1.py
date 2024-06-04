# PROYECTO FINAL INTEGRADOR - PARTE 1
###########################################################################################################
# 🔶 CONSIGNA
"""
Resolver el siguiente ejercicio de programacion en Python:

El empleado llamado Juan cobro 300 dolares por mes desde enero a junio, 500 dolares de julio a octubre, y
700 dolares por mes en noviembre y en diciembre. 

En base al escenario propuesto, se le solicita a los estudiantes que creen un pequenio programa que calcule
el sueldo promedio del empleado Juan. Ademas, se debe indicar si Juan se encuentra cobrando un sueldo bajo,
normal o mejor de lo normal, considerando las siguientes pautas:

a. Sueldo bajo: por debajo de 300 dolares.
b. Sueldo normal:  entre 300 a 900.
c. Sueldo mejor de lo normal: más de 900 dolares.

Tip: se debe utilizar estructuras condicionales.
"""

###########################################################################################################
# 🔶 PROPUESTA

# Definir al empleado.
Empleado = {
    'nombre': "Juan",
    'montos': {
        "enero": 300,
        "febrero": 300,
        "marzo": 300,
        "abril": 300,
        "mayo": 300,
        "junio": 300,
        "julio": 500,
        "agosto": 500,
        "septiembre": 500,
        "octubre": 500,
        "noviembre": 700,
        "diciembre": 700
    }
}

# Obtener el sueldo total del empleado.
SueldoTotal = sum(Empleado['montos'].values())

# Obtener el sueldo promedio del empleado.
SueldoPromedio = SueldoTotal / len(Empleado['montos'].values())

# Determinar la categoria de sueldo del empleado.
if SueldoPromedio < 300:
    CategoriaSueldo = "bajo"
elif SueldoPromedio > 900:
    CategoriaSueldo = "mejor de lo normal"
else:
    CategoriaSueldo = "normal"

# Imprimir por pantalla el resultado.
print(f"Sueldo promedio de {Empleado['nombre']}: {SueldoPromedio:.2f} dolares.\nPertenece a la categoria: Sueldo {CategoriaSueldo}.")