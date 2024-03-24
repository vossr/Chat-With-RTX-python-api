import requests
import random
import string
import json

def join_queue(session_hash, fn_index, port, chatdata):
    python_object = {
        "data": chatdata,
        "event_data": None,
        "fn_index": fn_index,
        "trigger_id": 46,
        "session_hash": session_hash
    }
    json_string = json.dumps(python_object)

    url = f"http://127.0.0.1:{port}/queue/join?__theme=dark"

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

def send_message(message, port):
    session_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    #fn_indexes are some gradio generated indexes from rag/trt/ui/user_interface.py

    join_queue(session_hash, 36, port, [])
    listen_for_updates(session_hash, port)

    join_queue(session_hash, 37, port, [])
    listen_for_updates(session_hash, port)

    chatdata = ["", [], "AI model default", None]
    join_queue(session_hash, 38, port, chatdata)
    listen_for_updates(session_hash, port)

    chatdata = ["", []]
    join_queue(session_hash, 39, port, chatdata)
    listen_for_updates(session_hash, port)

    #add chat history here -v
    chatdata = [[[message, None]], None]
    join_queue(session_hash, 40, port, chatdata)
    return listen_for_updates(session_hash, port)
