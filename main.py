#---
# here is to be the code for our solar tracker simulation
# at first i am just going to work on it like i was coding a real one - and worry about the simulation part later
# #

from tracker import SolarTrackerArray
#from Sun import Sun
from photodiode import Photodiode
import time

def run_routine():
  #start
  #init instances of tracker and diodes and clock
  clock = time.clock()
  n_sensor = Photodiode("N")
  s_sensor = Photodiode("S")
  e_sensor = Photodiode("E")
  w_sensor = Photodiode("W")

  array1 = SolarTrackerArray(1,30,300)

  wind_input_speed = 0
  wind_safe = False
  daytime = False
  state_tracker = 0# 0-default, 1-safety, 2-sleep
  
  array1.calibrate_sensors()
  #overall loop begins
  running_init = True
  while running_init == True:
    #check windspeed
    windspeed_test = array1.check_anenometer(wind_input_speed)
    wind_safe = windspeed_test

    while wind_safe == True:
      #check sun level
      enough_sun = array1.check_sun_radiation_level()
      daytime = enough_sun

      while daytime == True:
        state_tracker = 0
        #check all 4 diodes and compare them
        e1 = e_sensor.check_diode_output_strength()
        w1 = w_sensor.check_diode_output_strength()
        s1 = s_sensor.check_diode_output_strength()
        n1 = n_sensor.check_diode_output_strength()

        if e1 > w1:
          #turn anticlockwise
          array1.move_azimuth_motor(-1)
          #moved

        elif e1 < w1:
          #turn clockwise
          array1.move_azimuth_motor(1)

        elif n1 > s1:
          #tilt up
          array1.move_altitude_motor(1)

        elif s1 > n1:
          #tilt down
          array1.move_altitude_motor(-1)

        else:
          daytime = False
          wind_safe = False
      
      state_tracker = 2
    
    state_tracker = 1
    array1.safety_state()



def main():
  run_routine()

if __name__ == "__main__":
  main()
