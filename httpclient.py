import json
import http.client

""" PUT """


def put():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'd', 'contra': 'r'})
    conn.request("PUT", "/modificar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


""" PATCH """


def patch():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 'ss', 'contra': '123'})
    conn.request("PATCH", "/actualizar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


""" DELETE """


def delete():
    conn = http.client.HTTPConnection("localhost", 5000)
    headers = {'Content-type': 'application/json'}
    body = json.dumps({'usuario': 's', 'contra': '123'})
    conn.request("DELETE", "/eliminar", body, headers)
    response = conn.getresponse()
    return response.read().decode()


print("\n********** PUT ************\n")
print(put())


print("\n********* PATCH ***********\n")
print(patch())


print("\n******** DELETE **********\n")
print(delete())
