from tests.base import BaseTestCase
import json


class TestToken(BaseTestCase):
    def test_should_return_token_for_correct_credentials(self):
        response = self._get_token(data=dict(username='TEST_USERNAME', password='STRONG_PASSWORD'))

        self.assert200(response)
        self.assertIsNotNone(response.json)

    def test_should_return_403_for_bad_credentials(self):
        response = self._get_token(data=dict(username='TEST_USER', password='BAD_PASSWORD'))

        self.assertStatus(response, 403)

    def _get_token(self, data):
        return self.client.post(
            '/token',
            content_type='application/json',
            data=json.dumps(data)
        )
