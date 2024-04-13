import requests
import random
import string
import psutil
import json

port = None

def find_chat_with_rtx_port():
    global port
    connections = psutil.net_connections(kind='inet')
    for host in connections:
        try:
            if host.pid:
                process = psutil.Process(host.pid)
                if "ChatWithRTX" in process.exe():
                    test_port = host.laddr.port
                    url = f"http://127.0.0.1:{test_port}/queue/join"
                    response = requests.post(url, data="", timeout=0.05)
                    if response.status_code == 422:
                        port = test_port
                        return
        except:
            pass

def join_queue(session_hash, fn_index, port, chatdata):
    #fn_indexes are some gradio generated indexes from rag/trt/ui/user_interface.py
    python_object = {
        "data": chatdata,
        "event_data": None,
        "fn_index": fn_index,
        "session_hash": session_hash
    }
    json_string = json.dumps(python_object)

    url = f"http://127.0.0.1:{port}/queue/join"
    response = requests.post(url, data=json_string)
    # print("Join Queue Response:", response.json())

def listen_for_updates(session_hash, port):
    url = f"http://127.0.0.1:{port}/queue/data?session_hash={session_hash}"

    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line[5:])
                # if data['msg'] == 'process_generating':
                #     print(data['output']['data'][0][0][1])
                if data['msg'] == 'process_completed':
                    return data['output']['data'][0][0][1]
            except Exception as e:
                pass
    return ""

def send_message(message):
    if not port:
        find_chat_with_rtx_port()
    if not port:
        raise Exception("Failed to find a server port for 'Chat with RTX'. Ensure the server is running.")

    session_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    #add chat history here -v
    chatdata = [[[message, None]], None]
    join_queue(session_hash, 34, port, chatdata)
    return listen_for_updates(session_hash, port)
