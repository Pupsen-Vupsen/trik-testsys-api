import logging

from api.controller.utils import (
    error_arg_invalid,
    error_arg_not_found,
    unexpected_error,
)
from api.loader import app
from api.repository.UserRepository import UserRepository
from flask import jsonify, request


@app.route("/user", methods=["GET", "POST"])
async def user_handler():
    if request.method == "GET":
        return await handle_get()
    if request.method == "POST":
        return await handle_post()


async def handle_get() -> (any, int):
    user_id = request.args.get("user_id")

    if user_id is None:
        return error_arg_not_found("user_id")

    try:
        user = await UserRepository.get_user(user_id)

        if user is None:
            return jsonify(exist=False), 200
        else:
            return jsonify(exist=True), 200

    except Exception as e:
        logging.log(level=logging.ERROR, msg=e)
        return unexpected_error


async def handle_post() -> (any, int):
    user_id = request.args.get("user_id")
    if user_id is None:
        return error_arg_not_found("user_id")

    role = request.args.get("role")
    if role is None:
        return error_arg_not_found("role")
    if role not in ["teacher", "student"]:
        return error_arg_invalid("role", "role must be teacher or student")

    user = await UserRepository.get_user(user_id)
    if user is not None:
        return "", 409

    try:
        await UserRepository.create_user(user_id=user_id, role=role)
        return "", 201
    except Exception as e:
        logging.log(level=logging.ERROR, msg=e)
        return unexpected_error
