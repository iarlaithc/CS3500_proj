#---
# here is to be the code for our solar tracker simulation
# at first i am just going to work on it like i was coding a real one - and worry about the simulation part later
# #

from tracker import SolarTrackerArray
from Sun import Sun
from photodiode import Photodiode

def main():

  the_sun = Sun(270,18)
  
  array1 = SolarTrackerArray(1)

  n_sensor = Photodiode("N")
  s_sensor = Photodiode("S")
  e_sensor = Photodiode("E")
  w_sensor = Photodiode("W")

  w_sensor.set_surface_irradiation(10.0)
  e_sensor.set_surface_irradiation(8)

  w_sensor.check_diode_output_strength()
  e_sensor.check_diode_output_strength()

  print(w_sensor.get_output_voltage())
  print(e_sensor.get_output_voltage())

  

if __name__ == "__main__":
  main()