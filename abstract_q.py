from abc import ABC, abstractmethod

# # question 1
# class DeliveryMethod(ABC):

#     @abstractmethod
#     def deliver(self,order_id):
#         pass

# class BikeDelivery (DeliveryMethod):
     
#      def deliver(self,order_id):
#         print (f"{order_id} Delivered by bike")

# bike =BikeDelivery()
# bike.deliver(101)

# # question 2
# class DeliveryMethod(ABC):

#     @abstractmethod
#     def deliver(self,order_id):
#         pass

# class DroneDelivery (DeliveryMethod):
     
#      def deliver(self,order_id):
#         print (f"{order_id} dropped by dron at your door")

        
# class CarDelivery (DeliveryMethod):
     
#      def deliver(self,order_id):
#         print (f"{order_id} brought to your building by car")

# car = CarDelivery()
# car.deliver(202)
# drone = DroneDelivery()
# drone.deliver(202)

# # question 3
# class DeliveryMethod(ABC):
#     def __init__(self, compony_name):
#         self.compony_name = compony_name

#     @abstractmethod
#     def deliver(self,order_id):
#         pass

# class BikeDelivery (DeliveryMethod):
#      def __init__(self, compony_name):
#          super().__init__(compony_name)
     
#      def deliver(self,order_id):
#         print (f"{self.compony_name} Order: {order_id} - Bike delivery")

# class DroneDelivery (DeliveryMethod):
#      def __init__(self, compony_name):
#          super().__init__(compony_name)

#      def deliver(self,order_id):
#         print (f"{self.compony_name} Order: {order_id} - Drone delivery")


# dron = DroneDelivery("drony")
# bike = BikeDelivery("bikey")
# dron.deliver(101)
# bike.deliver(102)

# # question 4
# class DeliveryMethod(ABC):

#     @abstractmethod
#     def deliver(self,order_id):
#         pass

#     @abstractmethod
#     def get_eta(self):
#         pass
    
# class BikeDelivery (DeliveryMethod):
#      def __init__(self, compony_name):
#          self.compony_name = compony_name
     
#      def deliver(self,order_id):
#         print (f"{self.compony_name} Order: {order_id} - Bike delivery")

#      def get_eta(self):
#          return 30

# # class DroneDelivery (DeliveryMethod):
# #      def __init__(self, compony_name):
# #          super().__init__(compony_name)

# #      def deliver(self,order_id):
# #         print (f"{self.compony_name} Order: {order_id} - Drone delivery")

# #      def get_eta(self):
# #         return 15
     
# # bike = BikeDelivery("bikey")
# # bike.deliver(1)
# # bike.get_eta

# # question 5
# class DeliveryMethod(ABC):

#     @abstractmethod
#     def deliver(self,order_id):
#         pass

# class BrokenDelivery(DeliveryMethod):
#     def deliver(self,order_id):
#         pass
    

# roken = BrokenDelivery()

# # question 6
# class DeliveryFee:
#     @staticmethod
#     def calculate(distance_km, rate_per_km):
#         return distance_km * rate_per_km
    
#     @staticmethod
#     def with_surcharge(base_fee, surcharge_percent):
#         return base_fee * (1 + surcharge_percent / 100)
    
#     @staticmethod
#     def is_free(distance_km):
#         return True if distance_km <= 2.0 else None
    
# print (DeliveryFee.calculate(5, 3.0))
# print (DeliveryFee.with_surcharge(15.0,10))
# print(DeliveryFee.is_free(1.5))

# question 7
# class DeliveryMethod(ABC):
    
#     @abstractmethod
#     def deliver (self, order_id):
#         pass

#     @abstractmethod
#     def get_eta():
#         pass

# class WalkingDelivery (DeliveryMethod):
    
#     def deliver (self, order_id):
#         pass

#     def get_eta(self):
#         return 60

# class ExpressDelivery (DeliveryMethod):
    
#     def deliver (self, order_id):
#         pass

#     def get_eta(self):
#         return 10

# class DeliveryHelper:
#     @staticmethod
#     def faster (d1,d2):
#         if d1.get_eta() < d2.get_eta():
#             return d1
#         else:
#             return d2

# print (f"Faster Option: {DeliveryHelper.faster(WalkingDelivery(),ExpressDelivery()).__class__.__name__}")

# # question 8 
# class Notifier (ABC):
#     @abstractmethod
#     def send (self,recipient,message):
#         pass

# class PushNotifier(Notifier):

#     def send (self,recipient,message):
#         return f"Push to {recipient}: {message}"

# class WhatsAppNotifier(Notifier):
#     def send (self,recipient,message):
#         return f"WhatsApp to {recipient}: {message}"

# class InAppNotifier (Notifier):
#     def send (self,recipient,message):
#         return f"In-App banner for {recipient}: {message}"

# notifier_list = [PushNotifier(),WhatsAppNotifier(),InAppNotifier()]

# for notification in notifier_list:
#     print (notification.send ("customer_42", "Your order is under way"))

# # question 9
# class Restaurant (ABC):
#     @abstractmethod
#     def get_menu() -> list:
#         pass
#     @abstractmethod
#     def prepare_order (item_name):
#         pass

# class ItalianRestaurant (Restaurant):
#     menu = ['pasta', 'pizza', 'tiramisu']
#     def get_menu(menu) -> list:
#         return menu
#     def prepare_order (self, item_name):
#         return f"Sto preparando questo cibo per te: {item_name}"

# class SushiRestaurant (Restaurant):
#     menu = ['maki', 'nigiri', 'ramen']
#     def get_menu(menu) -> list:
#         return menu
#     def prepare_order (self, item_name):
#         return f"Kiminotameni kono ryōri o tsukutte iru nda: {item_name}"

# class BurgerJoint (Restaurant):
#     menu = ['burger', 'fries', 'shake']
#     def get_menu(menu) -> list:
#         menu
#     def prepare_order (self, item_name):
#         return f"Were are preparing {item_name} in the speed of light"

# for rest in [ItalianRestaurant(), SushiRestaurant(), BurgerJoint()]:
#     print (f"Menu: {rest.menu}\nPreparing: {rest.prepare_order(rest.menu[0])}\n")

# question 10
class DeliveryMethod (ABC):
    @abstractmethod
    def deliver(order_id):
        pass
    @abstractmethod
    def get_eta():
        pass
    @abstractmethod
    def get_cost(distance_km):
        pass

class BikeDelivery(DeliveryMethod):
    def __init__(self):
        self.cost_per_km = 10
    def deliver(order_id):
        print ("Deliver by bike")
    
    def get_eta(self):
        return 60
    
    def get_cost(self,distance_km):
        return distance_km * self.cost_per_km

class DroneDelivery(DeliveryMethod):
    def __init__(self):
        self.cost_per_km = 11
    def deliver(order_id):
        print ("Deliver by Drone")
    
    def get_eta(self):
        return 40
    
    def get_cost(self,distance_km):
        return distance_km * self.cost_per_km

class CarDelivery(DeliveryMethod):
    def __init__(self):
        self.cost_per_km = 12
    def deliver(order_id):
        print ("Deliver by car")
    
    def get_eta(self):
        return 50
    
    def get_cost(self,distance_km):
        return distance_km * self.cost_per_km

class WalkingDelivery(DeliveryMethod):
    def __init__(self):
        self.cost_per_km = 5

    def deliver(order_id):
        print ("Deliver by foot")
    
    def get_eta(self):
        return 100
    
    def get_cost(self, distance_km):
        return distance_km * self.cost_per_km



class Platform:
    
    delivery_options = [WalkingDelivery(),CarDelivery(), BikeDelivery(),DroneDelivery()]

    def cheapest_option (distance_km):

        cheapest = float('inf')
        method = None

        for option in Platform.delivery_options:

            cost = option.get_cost(distance_km)
            if cost < cheapest:
                cheapest = cost
                method = option
        return method
    
    def fastest_option ():
        
        fastest = float('inf')
        method = None

        for option in Platform.delivery_options:
            speed = option.get_eta() 
            if speed < fastest:
                fastest = speed
                method = option

        return method
    

print (f"The cheapest option is: {Platform.cheapest_option(10).__class__.__name__} | The fastest option is: {Platform.fastest_option().__class__.__name__}")

