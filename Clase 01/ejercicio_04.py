"""
Escribe un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
user_try = int(input("Dame un numero:"))
is_even_number = (user_try % 2) == 0


if is_even_number:
    print("Es par.")
else:
    print("Es impar.")

print("Script finalizado.")

"""
En este caso, en vez de hacer la comprobación directamente en la condicional (if/else),
guardamos el resultado del operador de igualdad (==) en una variable, y luego, 
utilizamos su resultado.

Recuerda que el resultado de una operación relacional siempre será un booleano (True o False),
y que el if evalúa una condición con resultado booleano (Si x número es igual a y número, si a es mayor que b).
"""
