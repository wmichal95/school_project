from tests.base import BaseTestCase


class TestPrime(BaseTestCase):
    def test_should_return_200(self):
        pass

    def _get_healthcheck(self):
        return self.client.get('/healthcheck')
