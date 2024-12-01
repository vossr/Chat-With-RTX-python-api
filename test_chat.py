import rtx_api_july_2024 as rtx_api

while True:
    user_input = input("$ ")
    for data in rtx_api.send_message_streaming(user_input):
        print(data)
