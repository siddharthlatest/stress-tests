from locust import HttpLocust, TaskSet, task

class tasks(TaskSet):
    #define at what level to perform the operations
    atLevel = 3
    
    #prepration: no need to touch
    URL = ''
    for x in xrange(1, atLevel + 1) :
      URL = URL + '/l' + str(x)
    
    # @task(weight), weight defines the weight of the task.
    @task(1)
    def patchProperties1(self):
        self.client.post( "/", 
                           '{"operation":"UPDATE PROPERTIES", "root_id":"foo1", "traverse":["foo2", "foo31"], "data":{"foo31":"bar1"}}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)+",1"
                         )

    @task(1)
    def patchProperties2(self):
        self.client.post( "/", 
                           '{"operation":"UPDATE PROPERTIES", "root_id":"foo1", "traverse":["foo2", "foo32"], "data":{"foo32":"bar2"}}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)+",2"
                         )

    @task(1)
    def patchProperties3(self):
        self.client.post( "/", 
                           '{"operation":"UPDATE PROPERTIES", "root_id":"foo1", "traverse":["foo2", "foo33"], "data":{"foo33":"bar3"}}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)+",3"
                         )

    @task(1)
    def patchProperties4(self):
        self.client.post( "/", 
                           '{"operation":"UPDATE PROPERTIES", "root_id":"foo1", "traverse":["foo2", "foo34"], "data":{"foo34":"bar4"}}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)+",4"
                         )

    @task(1)
    def patchProperties5(self):
        self.client.post( "/", 
                           '{"operation":"UPDATE PROPERTIES", "root_id":"foo1", "traverse":["foo2", "foo35"], "data":{"foo35":"bar5"}}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)+",5"
                         )

class WebsiteUser(HttpLocust):
    # base URL
    host = "http://ec2-54-164-114-172.compute-1.amazonaws.com:8080/test/v3/query/"
    task_set = tasks

    # Waiting before consecutive requests
    min_wait = 200
    max_wait = 2000
