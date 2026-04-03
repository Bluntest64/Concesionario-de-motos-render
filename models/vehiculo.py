from database import get_connection

class Vehiculo:

    @staticmethod
    def obtener_todos(marca=None, modelo=None, precio_max=None, estado=None):
        conexion = get_connection()
        cursor = conexion.cursor()
        query = "SELECT * FROM vehiculos WHERE 1=1"
        params = []
        if marca:
            query += " AND marca LIKE %s"
            params.append(f"%{marca}%")
        if modelo:
            query += " AND modelo LIKE %s"
            params.append(f"%{modelo}%")
        if precio_max:
            query += " AND precio <= %s"
            params.append(precio_max)
        if estado:
            query += " AND estado = %s"
            params.append(estado)
        query += " ORDER BY creado_en DESC"
        cursor.execute(query, params)
        vehiculos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return vehiculos

    @staticmethod
    def obtener_por_id(id):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos WHERE id = %s", (id,))
        vehiculo = cursor.fetchone()
        cursor.close()
        conexion.close()
        return vehiculo

    @staticmethod
    def crear(datos):
        conexion = get_connection()
        cursor = conexion.cursor()

        precio = float(datos['precio']) if datos['precio'] else None
        cilindraje = int(datos['cilindraje']) if datos['cilindraje'] else None
        anio = int(datos['anio']) if datos['anio'] else None

        cursor.execute("""
            INSERT INTO vehiculos (marca, modelo, precio, cilindraje, color, anio, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            datos['marca'],
            datos['modelo'],
            precio,
            cilindraje,
            datos['color'],
            anio,
            datos['estado']
        ))

        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod
    def actualizar(id, datos):
        conexion = get_connection()
        cursor = conexion.cursor()

        precio = float(datos['precio']) if datos['precio'] else None
        cilindraje = int(datos['cilindraje']) if datos['cilindraje'] else None
        anio = int(datos['anio']) if datos['anio'] else None

        cursor.execute("""
            UPDATE vehiculos SET marca=%s, modelo=%s, precio=%s,
            cilindraje=%s, color=%s, anio=%s, estado=%s
            WHERE id=%s
        """, (
            datos['marca'],
            datos['modelo'],
            precio,
            cilindraje,
            datos['color'],
            anio,
            datos['estado'],
            id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM vehiculos WHERE id = %s", (id,))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def obtener_disponibles():
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM vehiculos WHERE estado = 'disponible' ORDER BY marca")
        vehiculos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return vehiculos
