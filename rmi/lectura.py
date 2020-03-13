import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    
    idx, text = reader.read()
    print(idx)
    print(text)
    
finally:
    GPIO.cleanup()
    