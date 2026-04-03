from database import get_connection

class Cliente:

    @staticmethod
    def obtener_todos(nombre=None, documento=None, telefono=None):
        conexion = get_connection()
        cursor = conexion.cursor()
        query = "SELECT * FROM clientes WHERE 1=1"
        params = []
        if nombre:
            query += " AND nombre LIKE %s"
            params.append(f"%{nombre}%")
        if documento:
            query += " AND documento LIKE %s"
            params.append(f"%{documento}%")
        if telefono:
            query += " AND telefono LIKE %s"
            params.append(f"%{telefono}%")
        query += " ORDER BY nombre ASC"
        cursor.execute(query, params)
        clientes = cursor.fetchall()
        cursor.close()
        conexion.close()
        return clientes

    @staticmethod
    def obtener_por_id(id):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
        cursor.close()
        conexion.close()
        return cliente

    @staticmethod
    def crear(datos):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO clientes (nombre, documento, telefono, email, direccion)
            VALUES (%s, %s, %s, %s, %s)
        """, (datos['nombre'], datos['documento'], datos['telefono'],
              datos['email'], datos['direccion']))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar(id, datos):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE clientes SET nombre=%s, documento=%s, telefono=%s,
            email=%s, direccion=%s WHERE id=%s
        """, (datos['nombre'], datos['documento'], datos['telefono'],
              datos['email'], datos['direccion'], id))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
