from tests.base import BaseTestCase


class TestPicture(BaseTestCase):
    def test_should_return_200(self):
        pass

    def _get_healthcheck(self):
        return self.client.get('/healthcheck')
