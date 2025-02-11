from flask import Flask
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from werkzeug.serving import run_simple

# SOAP service
class MathService(ServiceBase):
    @rpc(Float, Float, Unicode, _returns=Float)  # Change Integer to Float
    def calculate(ctx, num1, num2, operation):
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            return num1 / num2 if num2 != 0 else float('inf')  # Handle division by zero
        return 0.0  # Default return as float

# Create the Spyne SOAP Application
soap_app = Application(
    [MathService],
    'math.service.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Create Spyne WSGI application
spyne_wsgi_app = WsgiApplication(soap_app)

# Define a custom WSGI middleware to handle CORS preflight requests
class CORSMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # handling options request
        if environ.get("REQUEST_METHOD", "").upper() == "OPTIONS":
            status = "200 OK"
            response_headers = [
                ("Access-Control-Allow-Origin", "*"),
                ("Access-Control-Allow-Methods", "POST, OPTIONS"),
                ("Access-Control-Allow-Headers", "Content-Type"),
                ("Content-Length", "0")
            ]
            start_response(status, response_headers)
            return [b""]
        else:
            def custom_start_response(status, headers, exc_info=None):
                headers.append(("Access-Control-Allow-Origin", "*"))
                return start_response(status, headers, exc_info)
            return self.app(environ, custom_start_response)

# Wrap Spyne app with CORS middleware
wrapped_app = CORSMiddleware(spyne_wsgi_app)

# create Flask app and assign the wrapped WSGI app
soap_flask_app = Flask(__name__)
soap_flask_app.wsgi_app = wrapped_app

if __name__ == "__main__":
    # Run the server on port 5001
    run_simple("0.0.0.0", 5001, soap_flask_app)
