#!/usr/bin/python

import socket


class webApp:

    def parse(self, request):

        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

    def __init__(self, hostname, port):

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))
        mySocket.listen(5)


        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to parse and process):'
            request = recvSocket.recv(2048)
            print request
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n")
            recvSocket.close()

if __name__ == "__main__":
    testWebApp = webApp("localhost", 1234)
