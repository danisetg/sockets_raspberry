import xmlrpc.client
from time import sleep
import RPi.GPIO as GPIO
import random

GPIO.setwarnings(False)

#GPIO.output(21, True)


with xmlrpc.client.ServerProxy("http://192.168.43.91:8000/") as proxy:
    GPIO.setmode(GPIO.BOARD)
    while True:
        
        GPIO.setup(26, GPIO.OUT)
        temp = proxy.fan()
        
        print(temp)
        try:
            temp = float(temp)
            print("Temp: ", temp)
        
            if temp >= 21:
                #v = proxy.fan(True)
                GPIO.output(26,False)
                print("entro")
                sleep(5)
            else:
                #v = proxy.fan(False)
                GPIO.output(26,True)
                #GPIO.cleanup()
                sleep(5)
        except:
            print(proxy.fan())
        #print("fan: ", v)
        
