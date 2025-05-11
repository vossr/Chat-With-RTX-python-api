import subprocess
import shutil
import os


def copy_self_to_another_directory(target_directory):
    current_script = os.path.realpath(__file__)
    target_file = os.path.join(target_directory, os.path.basename(current_script))
    if os.path.exists(target_file):
        os.remove(target_file)
    shutil.copy(current_script, target_file)


# copy & run self in the nvidia virtual env
python_bin = (
    "C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\env_nvd_rag\\Scripts\\python.exe"
)
target_directory = "C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\RAG\\trt-llm-rag-windows-ChatRTX_0.5.0\\ChatRTXUI\\engine"
if os.getcwd() != target_directory:
    copy_self_to_another_directory(target_directory)
    os.chdir(target_directory)
    subprocess.run([python_bin, target_directory + "\\" + os.path.basename(__file__)])
    exit(0)


from http.server import BaseHTTPRequestHandler, HTTPServer
from configuration import Configuration
from backend import Backend, Mode

data_path = os.path.expandvars("%programdata%\\NVIDIA Corporation\\chatrtx")
backend = Backend(model_setup_dir=data_path)

backend.init_model(model_id="mistral_7b_AWQ_int4_chat")
# backend.init_model(model_id="llama2_13b_AWQ_INT4_chat")
# backend.init_model(model_id="chatglm3_6b_AWQ_int4")
# backend.init_model(model_id="gemma_7b_int4")
# backend.init_model(model_id="clip_model")

# dataset_dir = '{directory_to_your_dataset}'
# status = backend.ChatRTX(chatrtx_mode=Mode.RAG, data_dir=dataset_dir)
status = backend.ChatRTX(chatrtx_mode=Mode.AI)


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        input_string = post_data.decode("utf-8")
        answer_stream = backend.query_stream(query=input_string)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()

        for part in answer_stream:
            print(part)
            chunk = part.encode("utf-8")
            if not chunk:
                continue
            # HTTP/1.1 chunked transfer encoding standard
            chunk_size = len(chunk)
            self.wfile.write(f"{chunk_size:x}\r\n".encode("utf-8"))
            self.wfile.write(chunk + b"\r\n")
            self.wfile.flush()
        self.wfile.flush()


httpd = HTTPServer(("", 8000), RequestHandler)
httpd.serve_forever()
