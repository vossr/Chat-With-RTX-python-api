from http.client import HTTPConnection

def send_message(message):
    connection = HTTPConnection('localhost', 8000)
    headers = {'Content-type': 'text/plain'}
    connection.request('POST', '/', message, headers)
    response = connection.getresponse()

    if response.status == 200:
        return response.read().decode()
    else:
        raise Exception("Error: Server responded with status {}".format(response.status))
