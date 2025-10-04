# Práctica 1 para validar correos electrónicos
# Irma Patricia Rivera León

import re

def ValidarCorreo(correo):
    # Patrón que valida correos terminados en .com, .mx, .org, .net, .edu, .gob


#El siguiente patrón permite validar cualquier caracter alfa numérico, incluido el punto y el guión medio
# de ahí es el arroba con espacio para cualquier cantidad de caracteres de igual modo alfa numérico
#seguido y finalizado por un punto literal y de ahí ya las frases del dominio según sea el correo
    patron = r'^[\w\.-]+@[\w\ob).-]+\.(com|mx|org|net|edu|g$'


    if re.match(patron, correo):
        return "Válido"
    else:
        return "Inválido"

# Ejemplos de correos que se muestran en consola
correos = [
    "mtra.irmarivera@gmail.com",
    "irma.rivera28@uabc.edu.mx",
    "al23760822@ite.edu.mx",
    "jajajameburlodemicuenta@cuentafalsa",
    "cuentaspam@dominio.conm",
    "alumno@dominante"
]

# Validación de los ejemplos
print("Validación de ejemplos:\n")
for c in correos:
    print(f"{c}: {ValidarCorreo(c)}")

# Interacción con el usuario
print("\nAhora ingresa tu propio correo para validarlo:\n")
correo_usuario = input("Ingresa un correo electrónico: ")

# Respuesta para el usuario
resultado = ValidarCorreo(correo_usuario)
print(f"{correo_usuario} → {resultado}")


