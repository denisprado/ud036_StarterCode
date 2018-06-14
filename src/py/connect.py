import json
import httplib

# function to retrive The Movie Database API (https://www.themoviedb.org/documentation/api) in JSON format
class Connect:
    def __init__(self, http_type, request):
        self.conn = httplib.HTTPSConnection("api.themoviedb.org")
        self.payload = "{}"
        self.key="253bdb880d421ceb9caefa2113e61ca3"
        self.http_type = http_type
        self.request = request
        self.conn.request(self.http_type, self.request+self.key, self.payload)
        self.res = self.conn.getresponse()        
        self.data = self.res.read()
        self.conn.close()