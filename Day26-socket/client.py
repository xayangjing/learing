import socket


address = ("127.0.0.1", 8012)

sk = socket.socket()

sk.connect(address)

sk.send("Hello server....")

