import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('127.0.0.1',8000))

#http://127.0.0.1:8000/

cmd = 'http://127.0.0.1:8000/talk_to_pi/get_data/'.encode()

mysock.send(cmd)



while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
print('Done')