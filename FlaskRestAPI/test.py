import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":100,"name":"tim","views":100},
		{"likes":00,"name":"kim","views":300},
		{"likes":500,"name":"cim","views":200}]

for i in range(len(data)):
	response =requests.put(BASE + "video/6")
	print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())