import rtx_api_3_5 as rtx_api

while True:
    user_input = input("$ ")
    response = rtx_api.send_message(user_input)
    print(response)
