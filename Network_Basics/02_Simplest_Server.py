from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)   #We make a socket, for our server
    try:
        serversocket.bind(('localhost',9000))     

        '''
        socket.bind(address)
        Bind the socket to address. The socket must not already be bound. 
        (The format of address depends on the address family — see above.)
        '''


        serversocket.listen(5)
        '''
        socket.listen([backlog])
        Enable a server to accept connections. If backlog is specified, it must be at least 0 
        (if it is lower, it is set to 0); 
        it specifies the number of unaccepted connections that the system will allow before refusing 
        new connections. 
        If not specified, a default reasonable value is chosen
        '''
        
        while (1):
            (clientsocket, address) = serversocket.accept()
            '''
            socket.accept()
            Accept a connection. The socket must be bound to an address and listening for connections. 
            The return value is a pair (conn, address) where conn is a new socket object usable to send 
            and receive data on the connection, and address is the address bound to the socket on the 
            other end of the connection.
            '''

            #print('serversocket.accept:', 'conn:',type(clientsocket), '.....Address:',type(address))
            

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)


    except KeyboardInterrupt:
        print("Shutting Down..");

    except Exception as exc:
        print('Error:\n');
        print(exc)
    
    serversocket.close()

print('Assess at --> http://localhost:9000')
createServer()





    

