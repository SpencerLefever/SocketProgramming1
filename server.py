from socket import *
import sys

#Create socket
#assign port number
#bind socket to server address and server port
#listen to at most one connection at a time

serverPort = 12503
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('Server is up')
while True:

    print('Ready to serve')

    #set up new connection
    connectionSocket, addr = serverSocket.accept()

    try:
        #set up new connection
        #connectionSocket, addr = serverSocket.accept()
        #receive request message
        message = connectionSocket.recv(12503).decode()
        #extract path
        filename = message.split()[1]
        #read path
        f = open(filename[1:])
        #store data
        outputdata = f.read()       
        #send http response header line
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #send content to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()


    except IOError:
        #throw 404 error for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

#Close the server socket
connectionSocket.close()
#terminate program
sys.exit()


