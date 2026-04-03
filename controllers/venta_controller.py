from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.venta import Venta
from models.vehiculo import Vehiculo
from models.cliente import Cliente

venta_bp = Blueprint('venta', __name__)

@venta_bp.route('/')
def listar():
    ventas = Venta.obtener_todas()
    return render_template('ventas/lista.html', ventas=ventas)

@venta_bp.route('/nueva', methods=['GET', 'POST'])
def nueva():
    if request.method == 'POST':
        datos = {k: request.form.get(k, '') for k in
                 ['id_cliente', 'id_vehiculo', 'fecha_venta', 'valor', 'observacion']}
        vehiculo = Vehiculo.obtener_por_id(datos['id_vehiculo'])
        if not vehiculo or vehiculo['estado'] != 'disponible':
            flash('El vehículo no está disponible para la venta.', 'danger')
            return redirect(url_for('venta.nueva'))
        Venta.crear(datos)
        flash('Venta registrada exitosamente.', 'success')
        return redirect(url_for('venta.listar'))
    clientes  = Cliente.obtener_todos()
    vehiculos = Vehiculo.obtener_disponibles()
    return render_template('ventas/formulario.html', clientes=clientes, vehiculos=vehiculos)

@venta_bp.route('/detalle/<int:id>')
def detalle(id):
    venta = Venta.obtener_por_id(id)
    if not venta:
        flash('Venta no encontrada.', 'danger')
        return redirect(url_for('venta.listar'))
    return render_template('ventas/detalle.html', venta=venta)
