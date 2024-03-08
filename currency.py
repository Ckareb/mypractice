import requests

ruble = []

data = requests.get('https://free.currconv.com/api/v7/convert?q=USD_RUB&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['USD_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?q=RUB_KZT&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['RUB_KZT']) 

data = requests.get('https://free.currconv.com/api/v7/convert?q=EUR_RUB&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['EUR_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?q=CNY_RUB&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['CNY_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?q=ILS_RUB&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['ILS_RUB'])

data = requests.get('https://free.currconv.com/api/v7/convert?q=RUB_JPY&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['RUB_JPY']) 

data = requests.get('https://free.currconv.com/api/v7/convert?q=GBP_RUB&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['GBP_RUB']) 

data = requests.get('https://free.currconv.com/api/v7/convert?q=INR_RUB&compact=ultra&apiKey=d9371a2ba6535eab179c').json()
ruble.append(data['INR_RUB'])