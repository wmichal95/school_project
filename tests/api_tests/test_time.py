from tests.base import AuthorizedTestCase


class TestTime(AuthorizedTestCase):
    def test_should_return_time(self):
        response = self._get_time(self.auth_bearer)

        self.assert200(response)
        self.assertIsNotNone(response.json['time'])

    def test_should_return_unauthorized_when_not_token_specified(self):
        response = self._get_time(None)

        self.assert401(response)

    def _get_time(self, token):
        return self.client.get(
            '/time',
            headers={'Authorization': token}
        )
