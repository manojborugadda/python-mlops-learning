from abc import ABC, abstractmethod # importing the abstract base class module AND the abstractmethod decorator

class Vehicle(ABC): # creating an abstract class named Vehicle that inherits from ABC

    @abstractmethod # using the abstractmethod decorator to define an abstract method
    def start_engine(self): # defining an abstract method named start_engine
        pass # the method does not have any implementation, it is just a placeholder

# v1 = Vehicle() # trying to create an instance of the abstract class Vehicle will raise an error

class Car(Vehicle): # creating a concrete class named Car that inherits from the abstract class Vehicle

    def start_engine(self): # providing an implementation for the abstract method start_engine
        print("Car engine started!") # printing a message indicating that the car engine has started

c = Car() # creating an instance of the concrete class Car
c.start_engine() # calling the start_engine method on the instance of Car, which will print "Car engine started!"