from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import Cliente

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/')
def listar():
    nombre    = request.args.get('nombre', '')
    documento = request.args.get('documento', '')
    telefono  = request.args.get('telefono', '')
    clientes  = Cliente.obtener_todos(nombre or None, documento or None, telefono or None)
    return render_template('clientes/lista.html', clientes=clientes,
                           filtros={'nombre': nombre, 'documento': documento, 'telefono': telefono})

@cliente_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        datos = {k: request.form.get(k, '') for k in
                 ['nombre', 'documento', 'telefono', 'email', 'direccion']}
        Cliente.crear(datos)
        flash('Cliente registrado exitosamente.', 'success')
        return redirect(url_for('cliente.listar'))
    return render_template('clientes/formulario.html', cliente=None, accion='Registrar')

@cliente_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cliente = Cliente.obtener_por_id(id)
    if not cliente:
        flash('Cliente no encontrado.', 'danger')
        return redirect(url_for('cliente.listar'))
    if request.method == 'POST':
        datos = {k: request.form.get(k, '') for k in
                 ['nombre', 'documento', 'telefono', 'email', 'direccion']}
        Cliente.actualizar(id, datos)
        flash('Cliente actualizado.', 'success')
        return redirect(url_for('cliente.listar'))
    return render_template('clientes/formulario.html', cliente=cliente, accion='Editar')

@cliente_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    Cliente.eliminar(id)
    flash('Cliente eliminado.', 'warning')
    return redirect(url_for('cliente.listar'))
