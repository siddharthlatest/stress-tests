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
    def patchProperties(self):
        self.client.post( "/", 
                           '{"operation":"UPDATE PROPERTIES", "root_id":"foo1", "traverse":["foo2", "foo3"], "data":{"foo3":"bar4"}}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)
                         )

class WebsiteUser(HttpLocust):
    # base URL
    host = "http://ec2-54-164-114-172.compute-1.amazonaws.com:8080/test/v3/query/"
    task_set = tasks

    # Waiting before consecutive requests
    min_wait = 500
    max_wait = 5000
