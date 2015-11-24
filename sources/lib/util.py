import time


def get_formated_time():
    struct_time = time.localtime()
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day = struct_time.tm_mday
    hour = struct_time.tm_hour
    min = struct_time.tm_min
    sec = struct_time.tm_sec
    formated_time = str(year) + "-" + str(month) + "-" + str(day) + "T" + str(hour) + ":" + str(min) + ":" + str(sec) + "+08:00"
    return formated_time


if __name__ == "__main__":
    print(get_formated_time())
