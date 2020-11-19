import requests
import json


clientt = requests.session()


clientt.get('http://127.0.0.1:8000/talk_to_pi/get_data/')
# Django would like the csrf token passed with the data, so we do need to save it off seperately.
csrftoken = clientt.cookies['csrftoken']






# '{"cookies": {"sessioncookie": "123456789"}}'

x = clientt.get('http://127.0.0.1:8000/talk_to_pi/get_data/')

stuff = str(x.content, 'utf-8')


y = json.loads(stuff)

# the result is a Python dictionary:
t_dict = y[0]
url = 'http://127.0.0.1:8000/talk_to_pi/get_data/'
payload = {'sensor':'343434','csrfmiddlewaretoken':csrftoken}
# We use client.post (not requests.post) so that we pass on the cookies that our session stored.
r2 = clientt.post(url, data=payload)



print(r2)