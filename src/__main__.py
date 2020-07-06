from app import create_app
from config import Env

def main():
    app = create_app()

    app.run(Env.HOST, port=Env.PORT, debug=Env.DEBUG)


if __name__ == "__main__":
    main()
