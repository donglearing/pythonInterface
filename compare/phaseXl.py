# -*- coding: utf-8 -*-

import requests
import json


def post(user, pwd):
    url = "http://58.211.38.72:62080/backend/user/login"
    body = "{\n\"username\":user,\n\"password\":pwd\n}"
    #body = {"username":"super", "password":"Connext@0101"}
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    res = requests.request("POST", url, data=body, headers=headers)
    return res.text

if __name__ == "__main__":
    print(post("111", "111"))
