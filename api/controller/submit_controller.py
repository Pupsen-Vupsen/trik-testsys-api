import logging

from api.controller.utils import (
    error_arg_invalid,
    error_arg_not_found,
    unexpected_error,
)
from api.loader import app
from api.repository.SubmitRepository import SubmitRepository
from api.repository.UserRepository import UserRepository
from flask import jsonify, request


@app.route("/submit", methods=["GET"])
async def handler():
    user_id = request.args.get("user_id")
    if user_id is None:
        return error_arg_not_found("user_id")

    user = await UserRepository.get_user(user_id)
    if user is None:
        return error_arg_invalid("user_id", "user_id does not exist")

    try:
        results = await get_user_result(user_id)
        return results, 200
    except Exception as e:
        logging.log(level=logging.ERROR, msg=e)
        return unexpected_error


async def get_user_result(user_id: str):

    raw_submits = await SubmitRepository.get_student_submits(user_id)

    submits = [
        jsonify(
            task_name=submit.task_name,
            submit_id=submit.submit_id,
            status=result(str(submit.result)),
        ).json
        for submit in raw_submits
    ]

    return jsonify(user_id=user_id, submits=submits).json


def result(r: str) -> int:
    match r:
        case "+":
            return 1
        case "-":
            return 0
        case "?":
            return 2
        case _:
            raise Exception(f"Unexpected result={r}")
