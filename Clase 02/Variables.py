# Declaracion de variable de tipo dinamico que recibe una cadena de caracteres "String"
nombre = "Soy un panda feliz"
print(nombre)
# Se imprime la referencia de la memoria RAM donde esta almacenado
print(id(nombre))


nombre = input("Escribe tu nombre: ")
print(nombre)
print(id(nombre)) # se escribe el valor de referencia de la variable

'''
En python, las variables pueden recibir cualquier tipo de datos, por lo que se considera
como un lenguaje de tipado debil y es caracteristico de los lenguajes interpretados,
por lo que siempre se tiene que tener mas cuidado como se usa las variables en el proceso 
de codificacion y ejecucion del programa.

Siempre se tiene que usar una variable con la finalidad que no cambie el tipo de dato

NOTA: las variables se pueden nombrar bajo el modelo de camelCase o snake_case
es decir, si la variable tiene mas palabras, se puede hacer lo siguiente
    camelCase -> fechaNacimiento
    snake_case -> fecha_nacimiento
Los datos que son constantes, en python no existe pero hay una convencion que las constantes
se tiene que escribir en mayusculas, por lo que nunca cambian durante la ejecucion de un programa
    Valor de PI -> PI = 3.141516
    IVA  = 0.16
    etc.
'''

edad = int(input("Ingresa tu edad: "))
print(edad)
print(id(edad))
'''
este es un comentario
de multiples lineas 
en python
'''
"""
Ejemplo de declaracion de un lenguaje de fuerte tipado
String nombre = "";
int edad = 22;
nombre = 63;
"""