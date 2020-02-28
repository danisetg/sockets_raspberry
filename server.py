import socketserver
import socket
import sys
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode()
        print (format(self.client_address[0]), "wrote: ", self.data)
        luz = int(self.data)
        if luz > 10000:
            print("si entra aca")
            self.sendCommand2Server("encender_luz")
            #self.luz_encendida = True
        else:
            self.sendCommand2Server("apagar_luz")
            #self.luz_encendida = False
    
    #Client Part
    HOST, PORT = "192.168.43.20", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
    def sendCommand2Server(self, command):
        SERVER_HOST = "192.168.43.20"
        SERVER_PORT = 9999
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((SERVER_HOST, SERVER_PORT))       
            sock.sendall(command.encode())

        finally:
            sock.close()
        

if __name__ == "__main__":
    HOST, PORT = "192.168.43.80", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()