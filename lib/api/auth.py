import logging
import jwt
from datetime import datetime

from lib.config import CONFIG


def decode_token(token):
    try:
        return jwt.decode(
            token,
            CONFIG.SECRET_KEY,
            options={"require": ["exp", "iss", "sub", "iat"]},
            algorithms=[CONFIG.JWT_ALGORITHM])
    except jwt.DecodeError:
        logging.debug(f'Token decoding error')
        return None
    except jwt.ExpiredSignatureError:
        logging.debug(f'Token signature expired')
        return None
    except jwt.InvalidIssuerError:
        logging.debug(f'Invalid token issuer')
        return None
    except jwt.InvalidTokenError:
        logging.debug(f'Unknown error')
        return None


def encode_token(name):
    timestamp_now = int(datetime.utcnow().timestamp())
    token = jwt.encode({
        'iss': CONFIG.JWT_ISSUER,
        'iat': timestamp_now,
        "exp": timestamp_now + CONFIG.JWT_TOKEN_LIFETIME_SECONDS,
        "sub": name
    }, CONFIG.SECRET_KEY, algorithm=CONFIG.JWT_ALGORITHM)

    return token
