#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from config import *

proxy = '96.9.90.90:8080'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}

print(TEST_URL)
response = requests.get(TEST_URL, proxies=proxies, verify=False)
if response.status_code == 200:
    print('Successfully')
    print(response.text)