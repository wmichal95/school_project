from lib.api.auth import encode_token
from http import HTTPStatus


def get(username):
    return encode_token(username), HTTPStatus.OK
