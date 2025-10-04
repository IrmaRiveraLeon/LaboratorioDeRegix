# Práctica 4 para validar contraseñas
# Irma Patricia Rivera León

#Esta práctica no me salió, por más que intenté que me mostrara los dominios, me marcaba como inválidos los comandos, no sé si fueron los Urls o alguna parte de la condición del if


import re

# Solicitar el texto al usuario
texto = input("Visita mis redes en https://www.youtube.com/channel/UCe6wR8BHtEYEZbgNmt8usfQ?view_as=subscriber o https://www.facebook.com/profile.php?id=100040158717182 a seguirme en LinkedIn https://www.linkedin.com/in/irma-rivera-leon/ y también puedes ir a mi repositorio de proyectos en https://github.com/Pattynk\n")

# Regex para detectar URLs reales: http(s):// o www. al inicio
patron = r'["\']?((?:http[s]?://|www\.)[\w.-]+\.[\w.-]+(?:/[^\s"\']*)?)["\']?'


# Buscar todas las URLs en el texto
urls = re.findall(patron, texto)

# Verificar si se encontraron URLs
if not urls:
    print("\nNo se encontraron URLs válidas.")
else:
    for i, completa in enumerate(urls, 1):
        # Limpiar posible punto o coma al final
        completa = completa.rstrip('.,')

        # Detectar protocolo
        if completa.startswith("http://"):
            protocolo = "http"
            resto = completa[len("http://"):]
        elif completa.startswith("https://"):
            protocolo = "https"
            resto = completa[len("https://"):]
        else:
            protocolo = "No especificado"
            resto = completa

        # Separar dominio y ruta
        partes = resto.split('/', 1)
        dominio = partes[0]
        ruta = '/' + partes[1] if len(partes) > 1 else ''

        # Mostrar resultado en consola de
