from locust import HttpLocust, TaskSet, task

class ObjectTests(TaskSet):
    # @task(weight), weight defines the weight of the task.
    @task(1)
    def create(self):
        self.client.get("/.json")

    @task(1)
    def get(self):
        self.client.put("/child1/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')

    @task(1)
    def update(self):
        self.client.patch("/child1/.json", '{"property1": "new_value1", "property2":"new_value2"}')

    @task(1)
    def delete(self):
        self.client.post("/child2/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')


class RelationTests(TaskSet):
    # @task(weight), weight defines the weight of the task.
    @task(1)
    def create(self):
        self.client.get("/.json")

    @task(1)
    def update(self):
        self.client.put("/child1/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}')

    @task(1)
    def delete(self):
        self.client.patch("/child1/.json", '{"property1": "new_value1", "property2":"new_value2"}')

    @task(1)
    def get(self):
        self.client.post("/child2/.json", '{"property1": "value1", "property2":"value2", "property3": "value3"}') 


class WebsiteUser(HttpLocust):
    # base host
    host = "https://fire-suck.firebaseio.com"
    task_set = UserBehavior

    # Waiting before consecutive requests
    min_wait = 2000
    max_wait = 4000