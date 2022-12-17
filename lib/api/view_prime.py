from http import HTTPStatus
from lib.config import CONFIG
import math


def get(number):
    if number > CONFIG.PRIME_MAX_NUMBER:
        return {}, HTTPStatus.BAD_REQUEST

    if is_prime(number):
        return {
                   'is_prime_number': True
               }, HTTPStatus.OK
    else:
        return {
                   'is_prime_number': False
               }, HTTPStatus.OK


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True
