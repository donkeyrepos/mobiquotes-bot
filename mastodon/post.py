import requests
import random

lines = open('quotes.txt').read().splitlines()
myline =random.choice(lines)

#url = 'https://mstdn.social/api/v1/statuses'
url = 'https://mastodon.social/api/v1/statuses'
auth = {'Authorization': 'Bearer <token>'}
params = {'status': myline}

r = requests.post(url, data=params, headers=auth)

#print(r)
