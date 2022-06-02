from flask import Flask

from api.repository.SubmitRepository import SubmitRepository
from api.repository.UserRepository import UserRepository

app = Flask(__name__)
UserRepository.init_repository()
SubmitRepository.init_repository()
