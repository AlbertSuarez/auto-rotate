from flask import request, jsonify

from src.helper.response_maker import make_response


def post():
    """
    Main function for /rotate endpoint.
    :return: JSON response.
    """
    try:
        body = request.json

        return jsonify(make_response(False, image_base64=None)), 200

    except Exception as e:
        return jsonify(make_response(True, message=f'Unexpected error: {e}')), 400
