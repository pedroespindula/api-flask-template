from app import create_app
from config import env

def main():
    app = create_app()

    app.run(env.HOST, port=env.PORT, debug=env.DEBUG)


if __name__ == "__main__":
    main()
