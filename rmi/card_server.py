from tinydb import TinyDB, Query
import Pyro4
@Pyro4.expose
class GreetingMaker(object):
    def __init__(self):
        self.db = TinyDB('cards.json')

    def create(self, id, name, area):
        self.db.insert({'id': id, 'name': name, 'area': area})
    
    def search(self, id):
        card = Query()
        return self.db.search(card.id == id)


Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Greeting',
}, host="192.168.43.80", port=9090, ns=False, verbose=True)