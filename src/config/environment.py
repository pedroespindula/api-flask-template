# pylint: disable=R0903

from os import environ as environment

class Env():
    PORT = environment.get("PORT") or 80
    DEBUG = environment.get("DEBUG") or True
    HOST = environment.get("BASE_URL") or '0.0.0.0'
