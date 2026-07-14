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

# question 2
class DeliveryMethod(ABC):

    @abstractmethod
    def deliver(self,order_id):
        pass

class DroneDelivery (DeliveryMethod):
     
     def deliver(self,order_id):
        print (f"{order_id} dropped by dron at your door")

        
class CarDelivery (DeliveryMethod):
     
     def deliver(self,order_id):
        print (f"{order_id} brought to your building by car")

car = CarDelivery()
car.deliver(202)
drone = DroneDelivery()
drone.deliver(202)



