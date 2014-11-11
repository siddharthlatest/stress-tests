from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    @task(1)
    def get(self):
        self.client.get("/.json")

    @task(1)
    def put(self):
        self.client.put("/child1/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')

    @task(1)
    def put(self):
        self.client.patch("/child1/.json", '{"property1": "new_value1", "property2":"new_value2"}')

    @task(1)
    def post(self):
        self.client.post("/child2/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')

    @task(1)
    def delete(self):
        self.client.delete("/.json")


class WebsiteUser(HttpLocust):
    host = "https://fire-suck.firebaseio.com"
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000