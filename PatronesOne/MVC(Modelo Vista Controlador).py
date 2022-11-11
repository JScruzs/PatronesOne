# Este patron se utiliza para hacer interfaces de usuario el cual se divide en partes logicas del programa.

class MVC(object):
    services = {
        'email': {'number': 1, 'price': 12},
        'sms': {'number': 1, 'price': 10},
        'voice': {'number': 1, 'price': 5},
    }
 
class Vista(object):
    def list_services(self, services):
        for svc in services:
            print(svc, " ")
 
    def list_pricing(self, services):
        for svc in services:
            print("For", MVC.services[svc]['number'],
                  svc, "message you pay $",
                  MVC.services[svc]['price'])
 
class Controller(object):
    def __init__(self):
        self.model = MVC()
        self.view = Vista()
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
 
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)
class Cliente(object):
    con = Controller()
    print("Services Provided:")
    con.get_services()
    print("Pricing for Services:")
    con.get_pricing()