from locust import HttpLocust, TaskSet, task
import json
parseHeaders = { 
                  'Content-Type': 'application/json',
                  "X-Parse-Application-Id" : "J8LxfvIdNfJtnEhzctPKik9BkPI96zjZ3JudUmPD",
                  "X-Parse-REST-API-Key" : "jvHEYfYK343qQ7E55ibUq2e6pEo1rdQPbzeCAz5K"
               }

class ObjectTests(TaskSet):
    # @task(weight), weight defines the weight of the task.
    @task(1)
    def create(self):
        response = self.client.post("/classes/stress_test_collection", 
                                    '{"number": 235234325, "string":"sgsdgsdgtthagadthzdfg", "array": ["value3", "asdfassdfS", "asfgadfgfszgf"]}',
                                    headers = parseHeaders,
                                    name = "Object: create"
                                   )
        self.objID = json.loads(response.content)["objectId"]
        print self.objID

    @task(1)
    def get(self):
        try:
          response = self.client.get("/classes/stress_test_collection/" + self.objID,
                                      headers = parseHeaders,
                                      name = "Object: get"
                                     )
          
          print response.content
        except NameError:
          pass

    @task(0)
    def update(self):
        self.client.patch("/child1/.json", '{"property1": "new_value1", "property2":"new_value2"}')

    @task(0)
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
    host = "https://api.parse.com/1"
    task_set = ObjectTests

    # Waiting before consecutive requests
    min_wait = 2000
    max_wait = 4000