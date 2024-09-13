import mysql.connector
from mysql.connector import Error #clase del connector que usaremos para hacer try except que interactuen con la BBDD (hay subclases pero con Error las cubrimos todas).
import xml.etree.ElementTree as ET

# Conexión a la base de datos con manejo de errores
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="fjeclot",  # pass de la BBDD que pusimos al instalar. VERIFICAR QUE ES LA QUE TENEMOS EN NUESTRO MYSQL
            database="BBDD_equip2"  # nombre de la BBDD 
        )
        if conn.is_connected():
            return conn
    except Error as e: #Aquí lo usamos para un error de conexión
        print(f"Error al conectar con la base de datos: {e}")
        return None


# Funciones para insertar datos con manejo de errores
def insertar_ong(cif, nombre_ong, pais_ong):
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ONG (CIF, nombre_ong, pais_ong) VALUES (%s, %s, %s)",
            (cif, nombre_ong, pais_ong)
        )
        conn.commit()
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        conn.close()

def insertar_animal(id_especie, estado, nombre_especie,nombre_animal,CIF_ong):
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ANIMALES (id_especie, estado, nombre_especie, nombre_animal,CIF_ong) VALUES (%s, %s, %s, %s, %s)",
            (id_especie, estado, nombre_especie,nombre_animal,CIF_ong)
        )
        conn.commit()
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        conn.close()

# Funciones para mostrar datos con manejo de errores
def mostrar_ong():
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ONG")
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al mostrar datos: {e}")
        return []
    finally:
        conn.close()

def mostrar_cif_nombre():
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT CIF,nombre_ong FROM ONG")
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al mostrar datos: {e}")
        return []
    finally:
        conn.close()


def mostrar_animales():
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ANIMALES")
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al mostrar datos: {e}")
        return []
    finally:
        conn.close()


# Funciones para buscar datos con manejo de errores
def buscar_ong_por_pais(pais_ong):
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ONG WHERE pais_ong = %s",
            (pais_ong,)
        )
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al buscar datos: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()


def buscar_ong_por_CIF(cif_ong):
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ONG WHERE CIF = %s",
            (cif_ong,)
        )
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al buscar datos: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()

# Función para buscar animales por nombre
def buscar_animales_por_nombre(nombre):
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ANIMALES WHERE nombre_animal = %s",
            (nombre)
        )
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al buscar datos: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()
#Función para buscar animales por ID
def buscar_animales_por_id(id_animal):
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ANIMALES WHERE id_especie = %s",
            (id_animal)
        )
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al buscar datos: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()

# Función para buscar animales por estado
def buscar_animales_por_estado(estado):
    conn = connect_to_database()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM ANIMALES WHERE estado = %s",
            (estado)
        )
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al buscar datos: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()

# Funciones para actualizar datos con manejo de errores
def actualizar_ong(cif, nuevo_nombre=None, nuevo_pais=None):
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        if nuevo_nombre:
            cursor.execute(
                "UPDATE ONG SET nombre_ong = %s WHERE CIF = %s",
                (nuevo_nombre, cif)
            )
        if nuevo_pais:
            cursor.execute(
                "UPDATE ONG SET pais_ong = %s WHERE CIF = %s",
                (nuevo_pais, cif)
            )
        conn.commit()
    except Error as e:
        print(f"Error al actualizar datos: {e}")
    finally:
        conn.close()

def actualizar_animal(id_especie, nuevo_estado, nuevo_nombre):
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        if nuevo_estado:
            cursor.execute(
                "UPDATE ANIMALES SET estado = %s WHERE id_especie = %s",
                (nuevo_estado, id_especie)
            )
        if nuevo_nombre:
            cursor.execute(
                "UPDATE ANIMALES SET nombre_animal = %s WHERE id_especie = %s",
                (nuevo_nombre, id_especie)
            )
        conn.commit()
    except Error as e:
        print(f"Error al actualizar datos: {e}")
    finally:
        conn.close()

# Funciones para eliminar datos con manejo de errores
def eliminar_ong(cif):
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM ONG WHERE CIF = %s",
            (cif)
        )
        conn.commit()
    except Error as e:
        print(f"Error al eliminar datos: {e}")
    finally:
        conn.close()

def eliminar_animal(id_especie):
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM ANIMALES WHERE id_especie = %s",
            (id_especie)
        )
        conn.commit()
    except Error as e:
        print(f"Error al eliminar datos: {e}")
    finally:
        conn.close()

def importarxml():
    conn = connect_to_database()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ONG")                        
        resultados = cursor.fetchall()

        root = ET.Element("datos")
        
        # Iterar sobre los resultados de la consulta y agregarlos al XML
        for resultado in resultados:
            item = ET.SubElement(root, "item")
            for i in range(len(cursor.column_names)):
                campo = ET.SubElement(item, cursor.column_names[i])
                campo.text = str(resultado[i])
        
        cursor.execute("SELECT * FROM ANIMALES")                        
        resultados2 = cursor.fetchall()
                
        for res in resultados2:
            item = ET.SubElement(root, "item")
            for i in range(len(cursor.column_names)):
                campo = ET.SubElement(item, cursor.column_names[i])
                campo.text = str(res[i])   
                    
        # Crear el árbol XML y escribirlo a un archivo
        tree = ET.ElementTree(root)
        tree.write("datos.xml")
    except Error as e:
        print(f"Error al importar datos como XML, error: {e}")
    finally:
        # Cerrar la conexión a la base de datos
        conn.close()

