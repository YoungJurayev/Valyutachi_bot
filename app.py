
import requests
import json
inputs=str(input('malumot kiriting: '))
url='https://v6.exchangerate-api.com/v6/056edfc7e154317e02b8f85c/latest/'+inputs
response=requests.get(url)
rest=json.loads(response.text)
print(rest['conversion_rates']['UZS'])
