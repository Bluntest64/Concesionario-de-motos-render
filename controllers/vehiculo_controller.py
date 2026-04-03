from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.vehiculo import Vehiculo

vehiculo_bp = Blueprint('vehiculo', __name__)

@vehiculo_bp.route('/')
def listar():
    marca    = request.args.get('marca', '')
    modelo   = request.args.get('modelo', '')
    precio   = request.args.get('precio_max', '')
    estado   = request.args.get('estado', '')
    vehiculos = Vehiculo.obtener_todos(marca, modelo, precio or None, estado or None)
    return render_template("vehiculos/lista.html", vehiculos=vehiculos)

@vehiculo_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        datos = {k: request.form.get(k, '') for k in
                 ['marca', 'modelo', 'precio', 'cilindraje', 'color', 'anio', 'estado']}
        Vehiculo.crear(datos)
        flash('Motocicleta registrada exitosamente.', 'success')
        return redirect(url_for('vehiculo.listar'))
    return render_template('vehiculos/formulario.html', vehiculo=None, accion='Registrar')

@vehiculo_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    vehiculo = Vehiculo.obtener_por_id(id)
    if not vehiculo:
        flash('Vehículo no encontrado.', 'danger')
        return redirect(url_for('vehiculo.listar'))
    if request.method == 'POST':
        datos = {k: request.form.get(k, '') for k in
                 ['marca', 'modelo', 'precio', 'cilindraje', 'color', 'anio', 'estado']}
        Vehiculo.actualizar(id, datos)
        flash('Motocicleta actualizada.', 'success')
        return redirect(url_for('vehiculo.listar'))
    return render_template('vehiculos/formulario.html', vehiculo=vehiculo, accion='Editar')

@vehiculo_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    Vehiculo.eliminar(id)
    flash('Motocicleta eliminada.', 'warning')
    return redirect(url_for('vehiculo.listar'))
