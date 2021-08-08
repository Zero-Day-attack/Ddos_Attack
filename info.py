import requests
import socket
import json

damin = input("Enter the damin: ")
req = requests.get("https://"+damin)
print(req.headers,"\n")

ip = socket.gethostbyname(damin)
print(f"ip Address of {damin} is {ip}","\n")

req2 = requests.get("https://ipinfo.io/"+ip+"/json")
#print(req2)
data = json.loads(req2.text)
print("location of "+damin+"is "+data["loc"]+"\n")
print(data)
