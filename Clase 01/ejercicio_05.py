"""
Escribe un programa que pida al usuario su nombre y su edad, y muestre por
pantalla un mensaje que le diga si es mayor de edad o no.
"""
user_name = input("Cuál es tu nombre?: ")
user_age = int(input("Cuál es tu edad?: "))

if user_age > 18:
    print(f"Bienvenido {user_name}! Con {user_age} ya eres todo un adulto.")

elif user_age == 18:
    print(
        f"Uhmm... no lo sé {user_name}. Con {user_age} anhos recien cumplidos"
        + " no se si dejarte pasar."
    )

else:
    print(
        f"Lo siento {user_name}. Con solo {user_age} anhitos no puedo"
        + " dejarte pasar."
    )

print("Script finalizado.")

"""
Puedes observar como utilizo un operador + para concatenar dos strings
y poder continuarlo en la siguiente línea, evitando así una línea
muy larga en mi código. Es una buena práctica evitar construir lineas
muy alargadas a fin de mejorar la legibilidad, por lo general, el
limite se mantiene entre 80 - 120 caracteres por linea.
"""
