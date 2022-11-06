from tests.base import BaseTestCase


class TestGetPrime(BaseTestCase):
    def test_should_return_200_and_prime_false(self):
        response = self._get_prime(10)

        self.assert200(response)
        self.assertDictEqual(response.json, {'is_prime_number': False})

    def test_should_return_200_and_prime_true(self):
        response = self._get_prime(11)

        self.assert200(response)
        self.assertDictEqual(response.json, {'is_prime_number': True})

    def test_should_return_404_when_param_is_not_number(self):
        response = self._get_prime('string')

        self.assert404(response)

    def _get_prime(self, number):
        return self.client.get(f'/prime/{number}')
