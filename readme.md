## Python api for calling Chat With RTX local server

### Usage
```python
import rtx_api

localhost_port = "set_port_number"
message = rtx_api.send_message("explain preprompt", localhost_port)
print(message)
```


### Speed
```
Chat With RTX builds int4 (W4A16 AWQ) tensortRT engines for mistral 7b and llama2 13b

On my 4090
  mistral 110 tok/s
  lama 69 tok/s
```


LICENSE: CC0
