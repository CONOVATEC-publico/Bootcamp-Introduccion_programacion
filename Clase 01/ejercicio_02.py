"""
Escribir un programa que pregunte el nombre del usuario en la consola y después devuelva un saludo personalizado.
"""
your_name = input("What's your name?: ")

print(f"Un saludo para ti {your_name}!. Tu nombre tiene {len(your_name)} letras!.")

print("Script finalizado.")

"""
Las f-string `f"Texto {algun_codigo}"` son una manera de formatear cadenas en python
que nos permite incluir expresiones de código. Puede ser una simple variable,
una suma o cualquier operación, e incluso llamar a una función que nos devuelva algo y
lo coloque dentro.

En este caso estamo usando la función len() para devolver el número de carácteres que tiene
la variable tipo string 'your_name' (correspondiente a lo que ingresó el usuario).

En versiones más antiguas de Python también podrías encontrar el uso de str.format().
El mismo código en este formato sería:

print("Un saludo para ti {}!. Tu nombre tiene {} letras!.".format(your_name, len(your_name)))

Siendo un solución mucho más verbosa y menos intuitiva.
"""
