import socket

HOST = "192.168.1.45"  # <-- IDE A SAJÁT IP-D
PORT = 5050

s = socket.socket()
s.connect((HOST, PORT))

s.send(b"click:500,800")

s.close()

print("sent")
