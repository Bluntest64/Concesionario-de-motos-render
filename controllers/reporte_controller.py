from flask import Blueprint, render_template
from models.vehiculo import Vehiculo
from models.venta import Venta

reporte_bp = Blueprint('reporte', __name__)

@reporte_bp.route('/')
def index():
    disponibles   = Vehiculo.obtener_todos(estado='disponible')
    vendidas      = Vehiculo.obtener_todos(estado='vendido')
    historial     = Venta.historial()
    total_ingresos = Venta.total_ingresos()
    return render_template('reportes/index.html',
                           disponibles=disponibles,
                           vendidas=vendidas,
                           historial=historial,
                           total_ingresos=total_ingresos)
