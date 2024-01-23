import requests

ruble = []

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=USD_RUB&compact=ultra').json()
ruble.append(data['USD_RUB'])  

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=RUB_KZT&compact=ultra').json()
ruble.append(data['RUB_KZT']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=EUR_RUB&compact=ultra').json()
ruble.append(data['EUR_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=CNY_RUB&compact=ultra').json()
ruble.append(data['CNY_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=ILS_RUB&compact=ultra').json()
ruble.append(data['ILS_RUB'])

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=RUB_JPY&compact=ultra').json()
ruble.append(data['RUB_JPY']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=GBP_RUB&compact=ultra').json()
ruble.append(data['GBP_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=08daaf94b2a5a1affd49&q=INR_RUB&compact=ultra').json()
ruble.append(data['INR_RUB'])