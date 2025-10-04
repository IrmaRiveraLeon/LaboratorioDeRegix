# Práctica 3 para validar contraseñas
# Irma Patricia Rivera León


import re

#Para poder Validar las contraseñas a utilizar, optaremos por las más utilizadas que llevan lo siguiente:
#Mínimo 8 caractéres, al menos 1 mayúscula, 1 minúscula, 1 número y 1 caracter especial


def ValidarContraseña (contrasena):
    patron = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#.]).{8,}$'

    if re.match(patron, contrasena):
        return "Válida"
    else:
        return "Inválida"

# Casos de prueba
contrasenas = [
    "contraseña",
    "SOLOMASYUS",
    "123456789",
    "MiK0ntr45eñ4!",
    "Enorm1zar123.",
    "PorElPoderDeLaAudiencia1.",
]

print("Contraseñas a validar de ejemplo:\n")
for c in contrasenas:
    print(f"{c} → {ValidarContraseña(c)}")

# Interacción con el usuario
print("\nAhora puedes ingresar tu propia contraseña para validarla.\n")
contrasena_usuario = input("Ingresa una contraseña: ")
print(f"{contrasena_usuario} → {ValidarContraseña(contrasena_usuario)}")


