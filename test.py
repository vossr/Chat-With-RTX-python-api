from time import time_ns
import rtx_api_3_5 as rtx_api

if __name__ == '__main__':
    port = your port number

    current_time_ns = time_ns()
    start_sec = current_time_ns / 1_000_000_000

    out = rtx_api.send_message("Write essay on: War, Famine, and Pestilence", port)

    current_time_ns = time_ns()
    end_sec = current_time_ns / 1_000_000_000

    average_characters_in_token = 4
    took = end_sec - start_sec
    tokens_per_second = len(out) / took / average_characters_in_token
    print("tokens/s:", int(tokens_per_second))

    print(out + "\n")
    out = rtx_api.send_message("Write single sentence sumary of: " + out, port)
    print("SUMMARY: " + out)
