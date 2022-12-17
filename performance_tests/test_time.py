from locust import HttpUser, task


class LocustTestPrime(HttpUser):
    def on_start(self):
        response = self.client.post("/token", json={"username": "PROD_USER", "password": "PASSWORD"})
        self.auth_token = response.json()

    @task
    def test_prime(self):
        self.client.get(f'/time', headers={"authorization": "Bearer " + self.auth_token},)

