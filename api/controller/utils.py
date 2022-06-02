from flask import jsonify

unexpected_error = jsonify(code=500, message="Unexpected error").json, 500


def error_arg_not_found(arg_name: str):
    return jsonify(code=400, message=f"request must contain {arg_name} arg").json, 400


def error_arg_invalid(arg_name: str, message: str):
    return jsonify(code=400, message=f"{arg_name} arg is invalid, {message}").json, 400
