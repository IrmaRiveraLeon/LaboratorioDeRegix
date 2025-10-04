# Práctica 5 para validar contraseñas
# Irma Patricia Rivera León

import re
from datetime import datetime

# Texto de ejemplo
texto = "El pasado viernes 10/09/2025 tuvimos una reunión con el equipo de trabajo, acordamos realizar una base de datos para entregarla aproximadamente el 2025-11-15 sin embargo, creo que terimnaremos entregándola el 20-nov-2025."


# Diccionario para meses en español y abreviaturas en inglés
meses = {
    'Enero':1, 'Febrero':2, 'Marzo':3, 'Abril':4, 'Mayo':5, 'Junio':6,
    'Julio':7, 'Agosto':8, 'Septiembre':9, 'Octubre':10, 'Noviembre':11, 'Diciembre':12,
    'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
    'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12
}

# Patrones regex para los distintos formatos
patrones = {
    'DD/MM/YYYY': r'(\b\d{2}/\d{2}/\d{4}\b)',
    'YYYY-MM-DD': r'(\b\d{4}-\d{2}-\d{2}\b)',
    'DD-MMM-YYYY': r'(\b\d{2}-[A-Za-z]{3}-\d{4}\b)',
    'Mes DD, YYYY': r'(\b(?:Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre) \d{1,2}, \d{4}\b)'
}

fechas_encontradas = []

# Buscar y convertir fechas
for formato, patron in patrones.items():
    for match in re.findall(patron, texto):
        try:
            if formato == 'DD/MM/YYYY':
                fecha_estandar = datetime.strptime(match, '%d/%m/%Y').strftime('%Y-%m-%d')
            elif formato == 'YYYY-MM-DD':
                fecha_estandar = datetime.strptime(match, '%Y-%m-%d').strftime('%Y-%m-%d')
            elif formato == 'DD-MMM-YYYY':
                # Convertir mes abreviado a número
                dia, mes_abre, anio = match.split('-')
                mes = meses[mes_abre]
                fecha_estandar = f"{anio}-{mes:02d}-{dia}"
            elif formato == 'Mes DD, YYYY':
                # Separar mes, día y año
                mes_texto, dia_coma, anio = match.split()
                dia = dia_coma.rstrip(',')
                mes = meses[mes_texto]
                fecha_estandar = f"{anio}-{mes:02d}-{int(dia):02d}"
            fechas_encontradas.append((match, fecha_estandar))
        except Exception as e:
            # Si hay un error en conversión, se ignora
            pass

# Mostrar resultados
print("Fechas encontradas y convertidas:")
for original, estandar in fechas_encontradas:
    print(f"- Formato original: {original} → Estándar: {estandar}")
