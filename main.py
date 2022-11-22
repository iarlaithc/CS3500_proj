#---
# here is to be the code for our solar tracker simulation
# at first i am just going to work on it like i was coding a real one - and worry about the simulation part later
# #

from tracker import SolarTrackerArray
#from Sun import Sun
from photodiode import Photodiode

def main():

  #the_sun = Sun(270,18)
  n_sensor = Photodiode("N")
  s_sensor = Photodiode("S")
  e_sensor = Photodiode("E")
  w_sensor = Photodiode("W")

  array1 = SolarTrackerArray(1,30,300,[8660,4999,5352])
  array1.calc_angles_from_sunpoints()
  array1.set_sun_direction()
  print(array1.get_sun_direction())

if __name__ == "__main__":
  main()