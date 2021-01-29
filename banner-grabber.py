#!/usr/bin/python

import socket

host_name = str(raw_input("Enter the host name: "))
host_port = int(raw_input("Enter the host Port: "))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host_name,host_port))
s.send('GET HTTP/1.1 \r\n')

received_data = s.recv(1024)
print  str(received_data)
