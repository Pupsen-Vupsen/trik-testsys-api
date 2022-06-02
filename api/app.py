from api.loader import app
import controller
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="api.txt")
    app.run(host='0.0.0.0', debug=True)

