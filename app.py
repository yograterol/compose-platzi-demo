import falcon
import json
from wsgiref import simple_server


class IndexJSON():
    def on_get(self, req, res):
        hello = {'msg': 'Hello Platzi Docker Compose'}
        res.status = falcon.HTTP_200
        res.body = json.dumps(hello)

app = falcon.API()

index = IndexJSON()

app.add_route('/', index)

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 3000, app)
    httpd.serve_forever()

