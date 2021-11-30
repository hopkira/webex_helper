import requests
import time

base_url = 'http://octopi.local:8123/api/webhook/'
myobj = {'dummykey': 'dummyvalue'}

on = 'webex_start'
off = 'webex_finish'

url_on = base_url + on
url_off = base_url + off

requests.post(url_on, data = myobj)
time.sleep(1)
requests.post(url_off, data = myobj)
