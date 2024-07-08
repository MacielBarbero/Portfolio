import mysql.connector
from mysql.connector import Error

# Configuración de la base de datos directamente en el script
DB_CONFIG = {
    "host": "localhost",
    "user": "adminps",
    "passwd": "adminps",
    "database": "petShop"
}

def crear_conexion():
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG) #  los dobles asteriscos (**) se usan para desempaquetar un diccionario en una llamada de función. El resultado sería mysql.connector.connect(host="localhost", user="adminps", passwd="adminps", database="petShop")
        print("Conexión a la base de datos exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    return connection

"""
 Usamos los dobles asteriscos (**) para desempaquetar el diccionario person_info en la llamada a print_person_info. Esto permite que cada clave del diccionario se convierta en un argumento de palabra clave para la función print_person_info. Si la función require 4 argumentos es válido pasarle un diccionario 
"""


def execute_query(query, params=None):
    connection = crear_conexion()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Consulta ejecutada con éxito")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()


def fetch_query(query, params=None):
    connection = crear_conexion()
    if connection is None:
        return None

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()
    return result


def ultimoid(query, params=None):
    connection = crear_conexion()
    if connection is None:
        return None

    cursor = connection.cursor()
    last_id = None
    try:
        cursor.execute(query, params)
        connection.commit()
        last_id = cursor.lastrowid
        print("Consulta ejecutada con éxito")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()
    return last_id

"""
Resumen:
execute_query: Para modificar la base de datos (INSERT, UPDATE, DELETE). No devuelve datos, solo confirma cambios.
fetch_query: Para recuperar datos de la base de datos (SELECT). Devuelve resultados como una lista de tuplas para su procesamiento.
Ambas funciones son esenciales dependiendo del tipo de operaciones que desees realizar con la base de datos. Es importante elegir la función correcta según si necesitas modificar datos en la base de datos (execute_query) o solo recuperar datos (fetch_query).

La función ultimoid es útil cuando necesitas recuperar el ID del último registro insertado después de una operación de inserción en una base de datos MySQL. No es necesaria esa función ya que:
La función LAST_INSERT_ID() en MySQL está diseñada específicamente para devolver el valor generado automáticamente por una columna AUTO_INCREMENT en una tabla después de una operación de inserción. Esta función no devuelve los valores de otras columnas que se insertaron junto con el ID generado automáticamente.
"""