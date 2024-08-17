import rtx_api_july_2024 as rtx_api
from time import time_ns

if __name__ == '__main__':
    current_time_ns = time_ns()
    start_sec = current_time_ns / 1_000_000_000

    out = ""
    for i in range(10):
        print('iteration', i)
        tmp = rtx_api.send_message("Write essay on: War, Famine, and Pestilence")
        print(tmp)
        out += tmp

    current_time_ns = time_ns()
    end_sec = current_time_ns / 1_000_000_000

    took = end_sec - start_sec
    char_per_second = len(out) / took
    print("char/sec:", int(char_per_second))

    # print(out + "\n")
    # out = rtx_api.send_message("Write single sentence sumary of: " + out)
    # print("SUMMARY: " + out)
