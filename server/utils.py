import json
from io import StringIO

def extract_route(req):
    start_idx = req.find("/") + 1
    end_idx =  req.find("HTTP/") - 1
    return req[start_idx: end_idx]

def read_file(req):
    return open(req).read()

def load_data(req):
    path = 'data/'+ req
    content = read_file(path)
    io = StringIO(content)
    return json.load(io)

def load_template(req):
    file = open('templates/'+ req)
    content = file.read()
    file.close()
    return content