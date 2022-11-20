#---
# here is to be the code for our solar tracker simulation
# at first i am just going to work on it like i was coding a real one - and worry about the simulation part later
# #

from tracker import SolarTrackerArray
from Sun import Sun

def main():

  array1 = SolarTrackerArray(1)
  the_sun = Sun(270,18)

  # #day cycle
  # for i in range(0,1439):
  #   the_sun.update_sun_pos()
  #   if i % 10 == 0:
  #     print(f"check{i}: ",the_sun.get_sun_pos())

if __name__ == "__main__":
  main()