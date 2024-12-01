from http.client import HTTPConnection

def send_message_streaming(message):
    connection = HTTPConnection('localhost', 8000)
    connection.putrequest('POST', '/', skip_host=True)
    connection.putheader('Content-Type', 'text/plain')
    connection._http_vsn = 11
    connection._http_vsn_str = 'HTTP/1.1'
    encoded_message = message.encode('utf-8')
    connection.putheader('Content-Length', str(len(encoded_message)))
    connection.endheaders()
    connection.send(encoded_message)
    response = connection.getresponse()

    if response.status == 200:
        while True:
            chunk = response.readline().decode('utf-8')
            if not chunk:
                return
            yield chunk.strip()
    else:
        raise Exception(f"Error: Server responded with status {response.status}")

def send_message(message):
    response = ""
    for data in send_message_streaming(message):
        response += data + '\n'
    return response
