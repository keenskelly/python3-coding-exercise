# ref: https://docs.python.org/3/tutorial/datastructures.html
from collections import deque
# ref: https://docs.python.org/3/library/http.client.html
import http.client
# ref: https://docs.python.org/3/library/re.html
import re
# ref: https://docs.python.org/3/library/logging.html
import logging

# ref: https://docs.python.org/3/library/collections.html#collections.deque
# ref: https://docs.python.org/3/tutorial/classes.html
class ApiClient:
    def __init__(self, apihost="localhost"):
        self.apihost = apihost

    # Send each user registration event in the collection over to the REST API
    def send_events(self, events):
        # Extract event properties from JSON matching {"event": "register", "user": { "id": <ID>, "email": "<EMAIL>" } }
        p = re.compile('.*(\d+), "email": "(.*?)".*')
        for event in events:
            # Format URI with event properties as /user/register/ID/EMAIL
            m = p.match(event)
            if m is not None:
                resource_uri = "/user/register/" + m.group(1) + "/" + m.group(2)

                # Make API HTTP call
                conn = http.client.HTTPConnection(self.apihost, 80, timeout=10)
                conn.request("GET", resource_uri)
                response = conn.getresponse()
                conn.close()

                # Log result/error
                print("User registration event for ID:" + m.group(1) + ", EMAIL:" + m.group(2) +" -> " + ("SUCCESS" if response.status == 200 else "FAILURE"))

# Initialize the ApiClient
api_client = ApiClient('localhost')

# Do a bunch of async work, collect up some user event registrations into a batch
events = deque()
events.append('{"event": "register", "user": { "id": 5901, "email": "john.doe@invalid" } }')
events.append('{"event": "register", "user": { "id": 5902, "email": "jane.doe@invalid" } }')
events.append('{"event": "register", "user": { "id": 5903, "email": "homer.doh@invalid" } }')

# Ding! Time to send over a batch of user event registrations!
api_client.send_events(events)

