from flask_testing import TestCase
from app import build_app
from lib.api.auth import encode_token


class BaseTestCase(TestCase):
    def create_app(self):
        return build_app()

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()


class AuthorizedTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.auth_bearer = 'Bearer ' + encode_token('test_user')

    def tearDown(self) -> None:
        super().tearDown()
