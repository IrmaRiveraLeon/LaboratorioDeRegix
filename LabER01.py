# Práctica de clase para validar correos desde un archivo
# Irma Patricia Rivera León


import re
import matplotlib.pyplot as plt

# Patrón del regix
patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Variables para contabilizar
validos = 0
invalidos = 0

# Abrir archivo de
with open("correos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Abrir archivo de salida
with open("resultado.txt", "w", encoding="utf-8") as salida:
    for linea in lineas:
        # Eliminar espacios y numeración al inicio
        correo = re.sub(r'^\d+\.\s*', '', linea.strip())

        # Validar correo
        if re.match(patron, correo):
            print(f"Válido: {correo}")
            salida.write(f"Válido: {correo}\n")
            validos += 1
        else:
            print(f"Inválido: {correo}")
            salida.write(f"Inválido: {correo}\n")
            invalidos += 1

# Mostrar todo listo en la consola
print("\n RESUMEN DE VALIDACIÓN:")
print(f"Total procesados: {validos + invalidos}")
print(f"Total de correos válidos: {validos}")
print(f"Total de correos inválidos: {invalidos}")
print("Se ha generado el archivo 'resultado.txt' con la información.")


#Abrir la gráfica de pastel para mostrar el resumen
labels = ['Válidos', 'Inválidos']
valores = [validos, invalidos]
colores = ["#FCBE2E", "#36AEF4"]

#Gráfica circular
plt.figure(figsize=(6,6))
plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=colores)
plt.title('Resultados de Validación de Correos')
plt.axis('equal') 
plt.show()

# Gráfica de barras
plt.subplot(1, 2, 2)
plt.bar(labels, valores, color=colores)
plt.title('Comparativa de validación')
plt.ylabel('Cantidad de correos')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar ambas gráficas
plt.tight_layout()
plt.show()
