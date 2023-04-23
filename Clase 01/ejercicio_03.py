"""
Escribe un programa que pregunte al usuario una clave (solo string) y lo compare
con una variable guardada.
Si la clave es correcta, imprime `Bienvenido`, sino, imprime `Clave incorrecta`.
"""
PASSWORD = "thisIsMyBestPass"

user_try = input("Ingrese su contrasenha: ")

if user_try == PASSWORD:
    print("Bienvenido")
else:
    print("Clave incorrecta")


print("Script finalizado.")

"""
Es una buena práctica en Python, declarar las "constantes" en mayúsculas, para dar a entender
que sus valores no deben cambiar en la ejecución del programa.

Sin embargo, debe recordarse que en Python el concepto de constantes no existe como tal,
a diferencia de lenguajes como Javascript, no existe una sintaxis para definir una constante (como const),
y solo es una mera convención para que otros desarrolladores puedan entender las intenciones
del código y evitar errores (después de todo, si intentas cambiar el valor, e incluso el tipo
de dato de PASSWORD el interprete te lo permitirá sin problemas).
"""
