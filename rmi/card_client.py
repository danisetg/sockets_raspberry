# saved as greeting-client.py
import Pyro4

ipAddressServer = "192.168.43.80"
greetingMaker = Pyro4.core.Proxy('PYRO:Greeting@' + ipAddressServer + ':9090')
command = input()
if command == "create":
    print("Id:")
    id = input()
    print("Name:")
    name = input()
    print("Area:")
    area = input()
    greetingMaker.create(id,name,area)