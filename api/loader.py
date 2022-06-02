from api.repository.SubmitRepository import SubmitRepository
from api.repository.UserRepository import UserRepository
from flask import Flask

app = Flask(__name__)
UserRepository.init_repository()
SubmitRepository.init_repository()
