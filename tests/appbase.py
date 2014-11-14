from locust import HttpLocust, TaskSet, task

class tasks(TaskSet):
    #define at what level to perform the operations
    atLevel = 10
    
    #prepration: no need to touch
    URL = ''
    for x in xrange(1, atLevel + 1) :
      URL = URL + '/l' + str(x)
    
    # @task(weight), weight defines the weight of the task.
    @task(1)
    def patchProperties(self):
        self.client.patch( self.URL + "/~properties", 
                           '{"data": {"property1": "value1", "property2":"value2", "property3": "value3"}, "secret": "aaf7c4cf139253df02cc23b5f67c076f"}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "patch properties at level:" + str(self.atLevel)
                         )
    @task(1)
    def setEdge(self):
        self.client.patch( self.URL + "/~edges", 
                           '{"data":  {"test_edge":{"path":"testing/l1", "order": null}}, "secret": "aaf7c4cf139253df02cc23b5f67c076f"}',
                           headers = { 'Content-Type': 'application/json'},
                           name = "set edge at level:" + str(self.atLevel)
                         )

class WebsiteUser(HttpLocust):
    # base URL
    host = "https://api.appbase.io/stress_test/v2/testing"
    task_set = tasks

    # Waiting before consecutive requests
    min_wait = 2000
    max_wait = 10000