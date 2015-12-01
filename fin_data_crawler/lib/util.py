import time
import math
import copy
from mysql_driver import MySQLdriver


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


def get_formated_time_mysql():
    struct_time = time.localtime()
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day = struct_time.tm_mday
    hour = struct_time.tm_hour
    min = struct_time.tm_min
    sec = struct_time.tm_sec
    formated_time = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(min) + ":" + str(sec)
    return formated_time


def toshare_null_handle(my_dict):
    for key in my_dict.keys():
        try:
            if math.isnan(my_dict[key]):
                del my_dict[key]
        except:
            pass
    return my_dict


def json_to_mysql(json_obj, table, sql_type="insert"):
    local_copy = copy.deepcopy(json_obj)
    if sql_type == "insert":
        sql_part1 = "insert into " + table
        keys = local_copy.keys()

        sql_part2 = "("
        for key in keys:
            sql_part2 += key
            sql_part2 += ","
        sql_part2 = sql_part2.rstrip(",")
        sql_part2 += ")"

        sql_part3 = "("
        for key in keys:
            sql_part3 += "'" + str(local_copy[key]) + "'"
            sql_part3 += ","
        sql_part3 = sql_part3.rstrip(",")
        sql_part3 += ")"

        sql = sql_part1 + " " + sql_part2 + " values " + sql_part3

    elif sql_type == "select":
        del local_copy["id"]
        del local_copy["fetchtime"]
        del local_copy["crawler"]
        sql_part1 = "select count(*) from " + table + " where"
        keys = local_copy.keys()

        sql_part2 = "("
        for key in keys:
            sql_part2 += key
            sql_part2 += ","
        sql_part2 = sql_part2.rstrip(",")
        sql_part2 += ")"

        sql_part3 = "("
        for key in keys:
            sql_part3 += "'" + str(local_copy[key]) + "'"
            sql_part3 += ","
        sql_part3 = sql_part3.rstrip(",")
        sql_part3 += ")"

        sql = sql_part1 + " " + sql_part2 + " = " + sql_part3

    return sql


if __name__ == "__main__":
    json = {"a": 1, "b": 2}
    table = "table_1"
    sql = json_to_mysql(json, table, "select")
    print(sql)

