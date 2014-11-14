from locust import HttpLocust, TaskSet, task
import json
parseHeaders = {
                  'Content-Type': 'application/json',
                  "X-Parse-Application-Id" : "J8LxfvIdNfJtnEhzctPKik9BkPI96zjZ3JudUmPD",
                  "X-Parse-REST-API-Key" : "jvHEYfYK343qQ7E55ibUq2e6pEo1rdQPbzeCAz5K"
               }

class ObjectTests(TaskSet):
    # @task(weight), weight defines the weight of the task.
    objects = []
    @task(10)
    def create(self):
        response = self.client.post("/classes/stress_test_collection", 
                                    '{"number": 235234325, "string":"sgsdgsdgtthagadthzdfg", "array": ["value3", "asdfassdfS", "asfgadfgfszgf"]}',
                                    headers = parseHeaders,
                                    name = "Object: CREATE"
                                   )
        
        self.objects.append(json.loads(response.content)["objectId"])

    @task(10)
    def get(self):
        try:
          response = self.client.get("/classes/stress_test_collection/" + self.objects[-1],
                                      headers = parseHeaders,
                                      name = "Object: GET"
                                     )
        except AttributeError:
          pass

    @task(10)
    def update(self):
        try:
          response = self.client.put("/classes/stress_test_collection/" + self.objects[-1], 
                                    '{"string":"sgsdgsdgtthagadthzdfg", "array": ["sfsadsg", "sfSACSDF", "SEFSDSEFSDSF"]}',
                                      headers = parseHeaders,
                                      name = "Object: UPDATE"
                                     )
        except AttributeError:
          pass

    @task(9)
    def delete(self):
        try:
          response = self.client.delete("/classes/stress_test_collection/" + self.objects.pop(0), 
                                      headers = parseHeaders,
                                      name = "Object: DELETE"
                                     )
        except AttributeError:
          pass

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
    min_wait = 3000
    max_wait = 10000