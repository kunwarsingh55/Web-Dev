import socket

'''
A Socket - A network socket is a software structure within a network node 
            of a computer network that serves as an endpoint for sending 
            and receiving data across the network

'''
#Setup a socket, acts like end point of our side 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


"""
AF_INET is an address family that is used to designate the type of addresses 
that your socket can communicate with (in this case, Internet Protocol v4 addresses).

TCP (SOCK_STREAM) is a connection-based protocol. The connection is established and 
the two parties have a conversation until the connection is terminated by one of the 
parties or by a network error.
"""



#Connect to a URL and a port
mysock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

#.encode() converts python Unicode to UTF-8 format

#Client always talks first
mysock.send(cmd)

print(type(cmd))

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())


'''
socket.recv(bufsize[, flags])
Receive data from the socket. 
The return value is a string representing the data received. 
The maximum amount of data to be received at once is specified 
by bufsize. 

'''

mysock.close()
print('Done')

