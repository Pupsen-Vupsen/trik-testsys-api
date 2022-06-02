import logging

from api.config import PATH_TO_LOG
from api.loader import app
import controller

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename=PATH_TO_LOG)
    app.run(host="0.0.0.0", debug=True)
