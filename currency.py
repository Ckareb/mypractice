import requests

ruble = []

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=USD_RUB&compact=ultra').json()
ruble.append(data['USD_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=RUB_KZT&compact=ultra').json()
ruble.append(data['RUB_KZT']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=EUR_RUB&compact=ultra').json()
ruble.append(data['EUR_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=CNY_RUB&compact=ultra').json()
ruble.append(data['CNY_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=ILS_RUB&compact=ultra').json()
ruble.append(data['ILS_RUB'])

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=RUB_JPY&compact=ultra').json()
ruble.append(data['RUB_JPY']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=GBP_RUB&compact=ultra').json()
ruble.append(data['GBP_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=d9371a2ba6535eab179c=INR_RUB&compact=ultra').json()
ruble.append(data['INR_RUB'])