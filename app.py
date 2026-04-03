from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from controllers.vehiculo_controller import vehiculo_bp
    from controllers.cliente_controller import cliente_bp
    from controllers.venta_controller import venta_bp
    from controllers.reporte_controller import reporte_bp

    app.register_blueprint(vehiculo_bp, url_prefix='/vehiculos')
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(venta_bp, url_prefix='/ventas')
    app.register_blueprint(reporte_bp, url_prefix='/reportes')

    from flask import redirect, url_for
    @app.route('/')
    def index():
        return redirect(url_for('vehiculo.listar'))

    return app

app = create_app()
