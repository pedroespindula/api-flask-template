from .ping import ping

def define_routes(app):
    # Test route
    app.register_blueprint(ping, url_prefix='/ping')
