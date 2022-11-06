from lib.api.auth import encode_token
from http import HTTPStatus
from lib.config import CONFIG


def get(body):
    if body['username'] == CONFIG.USERNAME and body['password'] == CONFIG.STRONG_PASSWORD:
        return encode_token(body['username']), HTTPStatus.OK
    else:
        return {}, HTTPStatus.FORBIDDEN
