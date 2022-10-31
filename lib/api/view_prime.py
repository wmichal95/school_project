from http import HTTPStatus
from lib.config import CONFIG
from prime_test import prime  # todo to jest niedeterministyczne XD


def get(number):
    if number > CONFIG.PRIME_MAX_NUMBER:
        return {}, HTTPStatus.BAD_REQUEST

    if prime.test(number):
        return {
                   'is_prime_number': True
               }, HTTPStatus.OK
    else:
        return {
                   'is_prime_number': False
               }, HTTPStatus.OK
