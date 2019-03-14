import json
import http.client


""" GET """


def get():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'admin', 'contra': '123'})
    conn.request("GET", "/buscar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


""" POST """


def post():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'admin', 'contra': '123'})
    conn.request("POST", "/insertar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


""" PUT """


def put():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'admin', 'contra': '123'})
    conn.request("PUT", "/modificar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


""" PATCH """


def patch():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'luis', 'contra': 'password'})
    conn.request("PATCH", "/actualizar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


""" DELETE """


def delete():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'root', 'contra': 'root'})
    conn.request("DELETE", "/eliminar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


print("\n********** GET ************\n")
print(get())

print("\n********** POST ************\n")
print(post())

print("\n********** PUT ************\n")
print(put())


print("\n********* PATCH ***********\n")
print(patch())


print("\n******** DELETE **********\n")
print(delete())
