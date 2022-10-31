# coding: utf-8
# Author：quzard
import datetime
import sys
import time
import traceback
from time import sleep

from numpy import random

from Tui import *
from get_location import get_location
from read_inform import read_inform
from seu_clockin import seu_clockin

if __name__ == '__main__':
    inform = read_inform()
    username = inform.seu['username']
    password = inform.seu['password']
    name = inform.seu['name']
    enable_gps = inform.gps_inform['enable_gps']
    LAT = inform.gps_inform['LAT']  # 纬度
    LON = inform.gps_inform['LON']  # 经度
    serverchan = inform.serverchan
    ak = inform.api['ak']
    sk = inform.api['sk']
    province = '江苏省'
    city = '南京市'
    district = '玄武区'

        res = seu_clockin(username, password, province, city, district, LAT, LON)
        if res == "打卡成功!":
            person_msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n体温上报成功' + '\n\n' + "伪造地址：" + province + city + district
            server_post(name + '\t' + '体温上报\t成功', person_msg, serverchan)
        else:
            person_msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n' + res + '\n\n' + "伪造地址：" + province + city + district
            server_post(name + '\t' + '体温上报\t失败', person_msg, serverchan)
            sys.exit(1)

    except Exception as e:
        print(traceback.format_exc())
        server_post(name + '\t' + '体温上报\t失败', e, serverchan)
        sys.exit(1)
