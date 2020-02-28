import socketserver
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
led_pin = 10
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH)
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
        print(self.data)
        if self.data == "encender_luz":
            GPIO.output(led_pin,GPIO.HIGH)
        
        elif self.data == "apagar_luz":
            GPIO.output(led_pin,GPIO.LOW)

if __name__ == "__main__":
    HOST, PORT = "192.168.43.20", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()