from flask import Blueprint

ping = Blueprint('ping', __name__)

@ping.route("/", methods=["GET"])
def main():
    return "ping"
