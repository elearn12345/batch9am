import json
import requests

res=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data=res.json()
print('AS PER: ', data['time']['updatedISO'])
print('Bitcoin price in USD: ', data['bpi']['USD']['rate'])
