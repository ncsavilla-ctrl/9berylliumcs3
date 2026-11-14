class Car: # This creates the car class
  def move(self): # This defines the move method
    print("The car drives on the road.") # This displays how the car moves

class Boat: # This creates the boat class
  def move(self): # This defines the move method
    print("The boat sails on water.") # This displays how the boat moves


class Drone: # THis creates the drone class
  def move(self): # This defines the move method
    print("The drone flies in the sky.") # This displays how the drone moves


def start_trip(vehicle): # This defines a function that is name start_trip()
    vehicle.move() # This calls the move method of the given object


car = Car() # This creates an object of the car class
boat = Boat() # This creates an object of the boat class
drone = Drone() # This creates an object of the drone class

start_trip(car) # This calls start_trip() using the car object
start_trip(boat) # This calls start_trip() using the boat object
start_trip(drone) # This calls start_trip() using the drone object

