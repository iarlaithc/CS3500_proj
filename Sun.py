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

from math import cos,sin,tan,pi

class Sun:
  solar_constant = 1380 #Watts/m^2
  radius = 10000 #metres
  limits_azimuth_angles = [0.0,360.0]
  limits_altitude_angles = [0.0,90.0]

  ##this doesnt work
  speed_const = 0.15 #degs/min

  def __init__(self, starting_altitude:float=270.0,starting_azimuth:float=30.0):
    if starting_altitude > 90 or starting_azimuth > 360:
      raise Exception("init out of bounds, impossible angle")

    self.__altitude_angle = starting_altitude
    self.__azimuth_angle = starting_azimuth
    self.sun_pos_angles = [self.__altitude_angle,self.__azimuth_angle]
    self.sun_coords = []

    self.weather_effect = 1.0
    self.output_radiation_power = float
    #altitude can technically be negative as it goes below the horizon

  def add_weather_effect(self):
    self.output_radiation_power = self.solar_constant * self.weather_effect 

  def set_sun_pos(self): ###this doesnt work
    #per minute
    sx = self.radius*cos(self.convert_degs_to_rads(self.__altitude_angle))
    sy = self.radius*sin(self.convert_degs_to_rads(self.__altitude_angle))
    sz = sx/(tan(self.convert_degs_to_rads((2*pi)-self.__azimuth_angle)))
    self.sun_coords = [sx,sy,sz]

  def set_sun_direction(self):
    self.sun_pos_angles = [self.__altitude_angle, self.__azimuth_angle]

  def convert_degs_to_rads(self,in_degrees):
    radians = in_degrees*(pi/180)
    return radians

  def convert_rads_to_degs(self,in_rads):
    degrees = in_rads/(pi/180)
    return degrees

  def set_sun_angles(self,alt_in, azi_in):
    self.__altitude_angle = alt_in
    self.__azimuth_angle = azi_in

  def increment_sun_alt_angle(self,speed_mult):
    alt = self.sun_pos_angles[0] + (0.5*speed_mult)
    return alt

  def increment_sun_azi_angle(self,speed_mult):
    azi = self.sun_pos_angles[1] + (0.5*speed_mult)
    return azi

  def decrement_sun_alt_angle(self,speed_mult):
    alt = self.sun_pos_angles[0] - (0.5*speed_mult)
    return alt

  def decrement_sun_azi_angle(self,speed_mult):
    azi = self.sun_pos_angles[1] - (0.5*speed_mult)
    return azi

  def move_sun(self,min_max):
    pass
    #takes list input from dict in form "key":["min alt","max alt","min azi","max azi"],
    

