import socket

HOST = "192.168.0.205"   # telefon IP
PORT = 5050

s = socket.socket()
s.connect((HOST, PORT))

# CLICK
s.send(b"click:500,800")

# SWIPE
# s.send(b"swipe:300,800,300,200")

s.close()

print("command sent")
