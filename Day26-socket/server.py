import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 8012)


sk.bind(address)


sk.listen(3)


conn = sk.accept()

print(conn)

