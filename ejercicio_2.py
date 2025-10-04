# Práctica 2 para validar números de teléfono
# Irma Patricia Rivera León

import re

# Texto de ejemplo
texto = "En este texto se muestra una historia en donde todos los nuevos integrantes del grupo 5SS le daban sus números de teléfono al jefe de grupo para no perderse nada de las sesiones de clases o avisos generales. Como era tarde, cada quien le dio una hoja al jefe de grupo con su número, Irma le dio su número 646-103-4252, Luis le dio el suyo  6461305005, Juan les dio el suyo 646-103-4224 y Anette les dio uno también 5551234598. El jefe de grupo creó un progama que escaneaba la hoja de texto y rescataba únicamente los números de teléfono, ésto lo había hecho al utilizar las expresiones regulares para permitir 10 dígitos pegados O 10 dígitos con algún caractér separándolos, por lo cual la expresión regular que utilizó fue la de un or, en donde se escaneaba todo o simplemente incluía los guiones o espacios,m incluso paréntesis, para poder identificarlos y guardarlos en su base de datos de alumnos"

#El siguiente pratrón es el descrito anteriormente
patron = r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-\s]?\d{3}[-\s]?\d{4})'

#Guarda los datos de teléfonos que encontró
telefonos = re.findall(patron, texto)

#Al final entrega las coicidencias de la búsqueda
print("Teléfonos encontrados:", telefonos)
