## Python API for Chat With RTX

### Usage

Run `python3 rtx_server_july_2024.py` as administrator

```python
import rtx_api_july_2024 as rtx_api

response = rtx_api.send_message("write fire emoji")
print(response)
```


### Speed
Chat With RTX builds int4 (W4A16 AWQ) tensortRT engines for LLMs

| Model | On 4090 |
|-|-|
| Mistral | 457 char/sec |
| Llama2 | 315 char/sec |
| ChatGLM3 | 385 char/sec |
| Gemma | 407 char/sec |
 
<br>
<br>
<br>

```
Update History of Chat With RTX
3.2024  Removed youtube video transcript fetch
4.2024  Added Whisper Speech to text model
7.2024  Electron app ui
```
LICENSE: CC0
