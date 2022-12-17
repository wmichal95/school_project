from locust import HttpUser, task


class LocustTestPrime(HttpUser):
    @task
    def test_prime(self):
        self.client.get(f'/prime/{123}')
