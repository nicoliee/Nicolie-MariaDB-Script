import re

def convertir_log_a_sql(log):
    # Expresión regular para encontrar las estadísticas de cada jugador
    patron = r"(\w+)={([^}]+)}"
    
    # Encontrar todas las coincidencias en el log
    matches = re.findall(patron, log)

    # Verificar de qué tabla se trata
    tabla = re.search(r"tables \[(\w+)\]", log).group(1)
    
    # Crear diccionario para almacenar las estadísticas de cada jugador
    estadisticas = {}

    # Procesar cada coincidencia encontrada
    for match in matches:
        username = match[0]
        stats_str = match[1]
        
        # Convertir las estadísticas a un diccionario
        stats = {}
        for stat in stats_str.split(", "):
            clave, valor = stat.split("=")
            stats[clave] = int(valor)

        # Agregar las estadísticas al diccionario global
        estadisticas[username] = stats

    # Generar comandos SQL
    sql_commands = []
    for username, stats in estadisticas.items():
        sql = f"UPDATE {tabla} SET "
        for clave, valor in stats.items():
            sql += f"{clave} = {clave} + {valor}, "
        sql = sql.rstrip(", ") + f" WHERE username = '{username}';"
        sql_commands.append(sql)

    return sql_commands

# Pedir al usuario que ingrese el nombre del archivo .txt
nombre_archivo = input("Ingrese el nombre del archivo .txt: ")

# Intentar abrir el archivo y leer su contenido
try:
    with open(nombre_archivo, 'r') as file:
        log_texto = file.read()
except FileNotFoundError:
    print("El archivo no existe.")
    exit()

# Convertir el log a comandos SQL
comandos_sql = convertir_log_a_sql(log_texto)

# Escribir los comandos SQL en un archivo de salida
nombre_salida = f"{nombre_archivo}_output.txt"
with open(nombre_salida, 'w') as output_file:
    for comando in comandos_sql:
        output_file.write(comando + '\n')

print(f"Los comandos SQL se han guardado en '{nombre_salida}'.")
