from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    # @task(weight), weight defines the weight of the task.
    @task(1)
    def get(self):
        self.client.get("/.json")

    @task(1)
    def put(self):
        self.client.put("/child1/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')

    @task(1)
    def patch(self):
        self.client.patch("/child1/.json", '{"property1": "new_value1", "property2":"new_value2"}')

    @task(1)
    def post(self):
        self.client.post("/child2/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')

    @task(1)
    def delete(self):
        self.client.delete("/.json")

class WebsiteUser(HttpLocust):
    # base host
    host = "https://fire-suck.firebaseio.com"
    task_set = UserBehavior

    # Waiting before consecutive requests
    min_wait = 2000
    max_wait = 4000