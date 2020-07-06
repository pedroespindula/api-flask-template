import json

from flask import Response

def make_response(body, status_code):
    return Response(
        json.dumps(body),
        status=status_code,
        mimetype="application/json"
    )

def make_error_reponse(message, status_code):
    return Response(
        json.dumps({"error": message}),
        status=status_code,
        mimetype="application/json"
    )

METHOD_NOT_DEFINED = make_error_reponse("Metodo não definido. Favor definir o método.", 500)
DEFAULT_SERVER_ERROR_RESPONSE = make_error_reponse("Algo de errado aconteceu.", 500)
