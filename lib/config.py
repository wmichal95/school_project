import os
from datetime import timedelta
from typing import NamedTuple


class AppConfig(NamedTuple):
    ENVIRONMENT: str
    SECRET_KEY: str
    DEBUG: bool = False
    TESTING: bool = False
    JWT_TOKEN_LIFETIME_SECONDS: int = timedelta(days=10).total_seconds()
    JWT_ALGORITHM: str = 'HS256'
    JWT_ISSUER: str = 'TEST_ISSUER'
    PRIME_MAX_NUMBER: int = 9223372036854775807


def get_config(environment) -> AppConfig:
    if environment == 'testing':
        return AppConfig(
            ENVIRONMENT='testing',
            SECRET_KEY='TEST_SECRET',
            TESTING=True,
            DEBUG=True
        )
    if environment == 'development':
        return AppConfig(
            ENVIRONMENT='development',
            SECRET_KEY=os.getenv('SECRET_KEY', 'DEV_SECRET'),
            DEBUG=False
        )
    if environment == 'production':
        return AppConfig(
            ENVIRONMENT='production',
            SECRET_KEY=os.environ['SECRET_KEY'],
            DEBUG=False,
            TESTING=False,
            JWT_ISSUER='APPLICATION_ISSUER'
        )

    raise EnvironmentError(f'Unknown enviroment type {environment} in APP_SETTINGS env var')


CONFIG = get_config(os.getenv(
    'APP_SETTINGS',
    'development'
))
