#---
# here is to be the code for our solar tracker simulation
# at first i am just going to work on it like i was coding a real one - and worry about the simulation part later
# #

from tracker import SolarTrackerArray
from Sun import Sun
from photodiode import Photodiode
from time import time,sleep

sun_path_dict = {
  "key":["min alt","max alt","min azi","max azi","speed multiplyer"],
  "january" : [10,40,270,30,1],
  "march" : [10,45,280,40,1], 
  "may" : [10,70,282,50,2], 
  "july" : [10,75,280,60,2], 
  "september" : [10,55,275,70,1], 
  "november" : [10,40,270,80,1], 
}

def run_routine():
  counter = 0
  sleep(0.005)
  #start
  #init instances of tracker and diodes
  user_choice_month = sun_path_dict["july"]
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
    counter += 1
    if counter%10 == 0:
      the_sun.move_sun(user_choice_month)
    #check windspeed
    wind_safe = array1.check_anenometer(wind_input_speed)

    if wind_safe == True:
      #check sun level
      daytime = array1.check_sun_radiation_level()

      if daytime == True:
        state_tracker = 0
        end = time()
        #check all 4 diodes and compare them
        e1 = e_sensor.check_diode_output_strength()
        w1 = w_sensor.check_diode_output_strength()
        s1 = s_sensor.check_diode_output_strength()
        n1 = n_sensor.check_diode_output_strength()

        if end-routine_start >= 40: #600 actually, shortened for demo #resets system
          daytime = False
          wind_safe = False
          running_init = False
        
        elif array1.sun_direction[0] < the_sun.sun_pos_angles[0]:
          #tilt up
          array1.move_altitude_motor(1)

        elif array1.sun_direction[0] > the_sun.sun_pos_angles[0]:
          #tilt down
          array1.move_altitude_motor(-1)
        
        #issues

        elif 270 < array1.sun_direction[1] < 360 and 270 < the_sun.sun_pos_angles[1] < 360:
          if array1.sun_direction[1] < the_sun.sun_pos_angles[1]:
          #turn clockwise in quadrant
            array1.increment_array_azi_angle()

          elif array1.sun_direction[1] > the_sun.sun_pos_angles[1]:
            array1.decrement_array_azi_angle()
            #turn antclockwise in quadrant

        elif 0 < array1.sun_direction[1] < 90 and 0 < the_sun.sun_pos_angles[1] < 90:
          if array1.sun_direction[1] < the_sun.sun_pos_angles[1]:
          #turn clockwise in quadrant
            array1.increment_array_azi_angle()

          elif array1.sun_direction[1] > the_sun.sun_pos_angles[1]:
            array1.decrement_array_azi_angle()
            #turn antclockwise in quadrant

        elif 270 < array1.sun_direction[1] < 360 and 0 < the_sun.sun_pos_angles< 90:
          array1.increment_array_azi_angle()
          #move forward across axis
        
        elif 0 < array1.sun_direction[1] < 90 and 270 < the_sun.sun_pos_angles< 360:
          array1.decrement_array_azi_angle()
          #move back across axis

        else:
          daytime = False
          wind_safe = False

        #print(array1.sun_direction)
        print(the_sun.sun_pos_angles)
        #sleep(180) # 2mins realistically, shortened for test
        #sleep(0.5)
      
    elif wind_safe!= True:
      state_tracker = 2
      array1.safety_state()
      #sleep(180) # realistically, shortened for test
      sleep(0.5)
    
    state_tracker = 1
    #sleep(180) # realistically, shortened for test
    sleep(0.025)


def main():
  counter = 0
  # while True:
  #   run_routine()
  run_routine()

if __name__ == "__main__":
  main()
