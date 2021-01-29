#!/usr/bin/python
import sys
import socket
import requests
import json

if len(sys.argv)<2:
   print("Recon:"+ sys.argv[0]+"<url>")
   sys.exit(1)

req = requests.get("http://"+sys.argv[1])
print("\n" + str(req.headers))

gethostname_ = socket.gethostbyname(sys.argv[1])
print("\n IP Address of" + sys.argv[1] +"is:" + gethostname_ + "\n")

req_two = requests.get("https://ipinfo.io" + gethostname_ +"/json")

response_ =json.loads(req_two.txt)

print("Location:" + resonse_["loc"])
print("Region:" + response_["region"])
print("City:" + response_["City"])
print("Country:" + response_["Country"])
