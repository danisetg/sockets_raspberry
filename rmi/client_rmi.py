import Pyro4
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

ipAddressServer = "192.168.1.135"

reader = SimpleMFRC522()
while True:
    try:
        idx, text = reader.read()
        greetingMaker = Pyro4.core.Proxy('PYRO:Greeting@' + ipAddressServer + ':9090')
        print(greetingMaker.search(idx))
    except:
        print("An exception has occurerd")
                