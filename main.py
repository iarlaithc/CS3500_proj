#---
# here is to be the code for our solar tracker simulation
# at first i am just going to work on it like i was coding a real one - and worry about the simulation part later
# #

from tracker import SolarTrackerArray
from Sun import Sun
from photodiode import Photodiode
from time import time,sleep

sun_path_dict = {
  "key":["min alt","max alt","min azi","max azi"],
  "january" : [10,40,270,30],
  "march" : [10,45,280,40], 
  "may" : [10,70,282,50], 
  "july" : [10,75,280,60], 
  "september" : [10,55,275,70], 
  "novemeber" : [10,40,270,80], 
}

def run_routine():
  #start
  #init instances of tracker and diodes
  user_choice_month = sun_path_dict["march"]
  print(user_choice_month)
  routine_start = time()
  #alt,azi
  the_sun = Sun(user_choice_month[0],user_choice_month[2])
  n_sensor = Photodiode("N")
  s_sensor = Photodiode("S")
  e_sensor = Photodiode("E")
  w_sensor = Photodiode("W")

  array1 = SolarTrackerArray(1,89.5,0)
  
  wind_input_speed = 0
  wind_safe = False
  daytime = False
  state_tracker = 0# 0-default, 1-safety, 2-sleep
  
  array1.calibrate_sensors()
  #overall loop begins
  running_init = True
  while running_init == True:
    the_sun.move_sun(user_choice_month)
    #check windspeed
    windspeed_test = array1.check_anenometer(wind_input_speed)
    wind_safe = windspeed_test

    if wind_safe == True:
      #check sun level
      enough_sun = array1.check_sun_radiation_level()
      daytime = enough_sun

      if daytime == True:
        state_tracker = 0
        end = time()
        #check all 4 diodes and compare them
        e1 = e_sensor.check_diode_output_strength()
        w1 = w_sensor.check_diode_output_strength()
        s1 = s_sensor.check_diode_output_strength()
        n1 = n_sensor.check_diode_output_strength()
        check_180 = array1.sun_direction[1]-the_sun.sun_pos_angles[1]

        if end-routine_start >= 60: #600 actually, shortened for demo
          daytime = False
          wind_safe = False
          running_init = False

        elif array1.sun_direction[1] > the_sun.sun_pos_angles[1]:
          #turn anticlockwise
          if abs(check_180) >= 180:
            array1.move_azimuth_motor(1)
          elif abs(check_180) < 180:
            array1.move_azimuth_motor(-1)

        elif array1.sun_direction[1] < the_sun.sun_pos_angles[1]:
          #turn clockwise
          array1.move_azimuth_motor(1)

        elif array1.sun_direction[0] < the_sun.sun_pos_angles[0]:
          #tilt up
          array1.move_altitude_motor(1)

        elif array1.sun_direction[0] > the_sun.sun_pos_angles[0]:
          #tilt down
          array1.move_altitude_motor(-1)

        else:
          daytime = False
          wind_safe = False

        print(array1.sun_direction)
        #sleep(180) # 2mins realistically, shortened for test
        sleep(0.5)
      
    elif wind_safe!= True:
      state_tracker = 2
      array1.safety_state()
      #sleep(180) # realistically, shortened for test
      sleep(0.5)
    
    state_tracker = 1
    #sleep(180) # realistically, shortened for test
    sleep(0.5)


def main():
  #t0 = time.clock()
  while True:
    run_routine()

if __name__ == "__main__":
  main()
