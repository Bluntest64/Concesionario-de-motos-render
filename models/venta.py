from database import get_connection

class Venta:

    @staticmethod
    def obtener_todas():
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT v.*, c.nombre AS nombre_cliente, c.documento,
                   ve.marca, ve.modelo, ve.cilindraje
            FROM ventas v
            JOIN clientes c  ON v.id_cliente  = c.id
            JOIN vehiculos ve ON v.id_vehiculo = ve.id
            ORDER BY v.fecha_venta DESC
        """)
        ventas = cursor.fetchall()
        cursor.close()
        return ventas

    @staticmethod
    def obtener_por_id(id):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT v.*, c.nombre AS nombre_cliente,
                   ve.marca, ve.modelo
            FROM ventas v
            JOIN clientes c   ON v.id_cliente  = c.id
            JOIN vehiculos ve ON v.id_vehiculo = ve.id
            WHERE v.id = %s
        """, (id,))
        venta = cursor.fetchone()
        cursor.close()
        conexion.close()
        return venta

    @staticmethod
    def crear(datos):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO ventas (id_cliente, id_vehiculo, fecha_venta, valor, observacion)
            VALUES (%s, %s, %s, %s, %s)
        """, (datos['id_cliente'], datos['id_vehiculo'], datos['fecha_venta'],
              datos['valor'], datos['observacion']))
        cursor.execute("UPDATE vehiculos SET estado='vendido' WHERE id=%s", (datos['id_vehiculo'],))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def total_ingresos():
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT SUM(valor) AS total FROM ventas")
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado['total'] or 0

    @staticmethod
    def historial():
        return Venta.obtener_todas()
