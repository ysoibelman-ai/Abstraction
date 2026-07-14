from abc import ABC, abstractmethod

# question 1
class DeliveryMethod(ABC):

    @abstractmethod
    def deliver(self,order_id):
        pass

class BikeDelivery (DeliveryMethod):
     def deliver(self,order_id):
        print (f"{order_id} Delivered by bike")
bike =BikeDelivery()
bike.deliver(101)





