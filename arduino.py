import serial
arduino = serial.Serial('COM7', baudrate=9600, timeout=1.0)
while True:
    try:
        temperatura = int(intarduino.readline())
        print(temperatura.decode())
    except:
        print("temperatura inválida")