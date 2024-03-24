## Python api for calling Chat With RTX local server

### Usage
```python
import rtx_api_3_5 as rtx_api

your_localhost_port = "set_port_number"
response = rtx_api.send_message("explain preprompt", your_localhost_port)
print(response)
```


### Speed
```
Chat With RTX builds int4 (W4A16 AWQ) tensortRT engines for mistral 7b and llama2 13b

On my 4090
  mistral 130 tok/s
  lama 75 tok/s
```


LICENSE: CC0
