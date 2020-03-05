from xmlrpc.server import SimpleXMLRPCServer

import serial

arduino = serial.Serial('/dev/cu.usbmodem14101', baudrate=9600, timeout=1.0)

def fan():

    temperatura = (arduino.readline()).decode()
    print(temperatura)
    return temperatura

server = SimpleXMLRPCServer(("192.168.43.91", 8000))
print("Listening on port 8000...")

server.register_function(fan, "fan")
server.serve_forever()


