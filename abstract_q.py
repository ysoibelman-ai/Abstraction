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

# class DroneDelivery (DeliveryMethod):
#      def __init__(self, compony_name):
#          super().__init__(compony_name)

#      def deliver(self,order_id):
#         print (f"{self.compony_name} Order: {order_id} - Drone delivery")

#      def get_eta(self):
#         return 15
     
# bike = BikeDelivery("bikey")
# bike.deliver(1)
# bike.get_eta



