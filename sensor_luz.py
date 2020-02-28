#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import socket
import sys

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"

GPIO.setmode(GPIO.BOARD)
CLIENT_HOST, CLIENT_PORT = "192.168.43.80", 9999
#define the pin that goes to the circuit
pin_to_circuit = 11

def rc_time(pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        luz = rc_time(pin_to_circuit)
        #print(luz)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((CLIENT_HOST, CLIENT_PORT))
        sock.sendall((str(luz)).encode())
        sock.close()
                        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
