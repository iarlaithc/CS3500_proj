#The Sun
#in our atmoshphere power is about 1380 watts per square meter (W/m2). This value is known as the Solar Constant.
#Atmospheric conditions can reduce direct beam radiation by 10% on clear, dry days and by 100% during thick, cloudy days.
#weather features?????
#90% of solar constant is 1242 w/m2 at ground level - aka on our panel ish

#just going to treat the sun like a 2d object on the edge of our hemisphere above the array

#----
# Altitude is the angular distance of an object above the local horizon. It ranges from 0 degrees at the horizon to 90 degrees at the zenith, the spot directly overhead.  theta
# #Azimuth is the angular distance of an object from the local North, measured along the horizon. 0, 360 . phi
#
################################
#15degs per hour movement for now
#update every min
#.25 degs / min on the suns path
#horizon is 10000m away
#############################

class Sun:
  solar_constant = 1380 #Watts/m^2
  avg_horizon_dist = 10000 #metres

  ##this doesnt work
  speed_const = 0.15 #degs/min
  neg_speed_const = -0.15

  def __init__(self,starting_azimuth:float, starting_altitude:float):
    self.__sun_altitude_angle = starting_altitude
    self.__sun_azimuth_angle = starting_azimuth
    self.sun_pos = []
    self.centre_check = False

    self.weather_effect = 1.0
    self.output_radiation_power = float
    #altitude can technically be negative as it goes below the horizon

  def add_weather_effect(self):
    self.output_radiation_power = self.solar_constant * self.weather_effect 

  def update_sun_pos(self): ###this doesnt work
    #per minute
    self.__sun_azimuth_angle += self.speed_const
    
    if self.__sun_azimuth_angle >= 359:
      self.__sun_azimuth_angle = 0
      self.centre_check = True
      
    if self.centre_check == True:
      self.__sun_altitude_angle += self.neg_speed_const
    else:
      self.__sun_altitude_angle += self.speed_const

    self.sun_pos = [self.__sun_altitude_angle,self.__sun_azimuth_angle]

  def get_sun_pos(self):
    return self.sun_pos
