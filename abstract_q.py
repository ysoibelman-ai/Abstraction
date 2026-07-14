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
class DeliveryMethod(ABC):
    
    @abstractmethod
    def deliver (self, order_id):
        pass

    @abstractmethod
    def get_eta():
        pass

class WalkingDelivery (DeliveryMethod):
    
    def deliver (self, order_id):
        pass

    def get_eta(self):
        return 60

class ExpressDelivery (DeliveryMethod):
    
    def deliver (self, order_id):
        pass

    def get_eta(self):
        return 10

class DeliveryHelper:
    @staticmethod
    def faster (d1,d2):
        if d1.get_eta() < d2.get_eta():
            return d1
        else:
            return d2

print (f"Faster Option: {DeliveryHelper.faster(WalkingDelivery(),ExpressDelivery()).__class__.__name__}")
