#----
# Altitude is the angular distance of an object above the local horizon. It ranges from 0 degrees at the horizon to 90 degrees at the zenith, the spot directly overhead. 
# #Azimuth is the angular distance of an object from the local North, measured along the horizon.
#
from math import pi,sin,cos,tan,acos,atan

class SolarTrackerArray:

  #class vars
  min_light_levels = 100.0 #W/m2
  limits_azimuth_angles = [0.0,360.0]
  limits_altitude_angles = [0.0,90.0]
  windspeed_safety_threshold = 30.0 #this is in kmph, realisticially we would have a rpm check so convert this over
  radius = 10000

  def __init__(self,array_number:int, start_altitude_angle:float, start_azimuth_angle:float,suncoords = [0,0,0]):
    #system setup & instance vars
    self.array_number = array_number
    self.__altitude_angle = start_altitude_angle
    self.__azimuth_angle = start_azimuth_angle
    self.sun_direction = [self.__altitude_angle, self.__azimuth_angle]

    self.anenometer_rpm = float
    self.sun_coords = suncoords

  def __repr__(self):
    return f"instance {self.array_number} of whole array class"

  def system_setup(self):
    #first time setup only on every reset ~10 mins
    pass

  def calibrate_sensors(self):
    pass

  def check_anenometer(self,anenometer_rpm):
    #You can use a “shortcut” method in calculating the anemometer speed. #Multiply the rpm by 0.03 to obtain your anemometer speed in km/hr.
    anenometer_windspeed = anenometer_rpm * 0.03 # conversion
    if anenometer_windspeed < self.windspeed_safety_threshold:
      return True
    elif anenometer_windspeed >= self.windspeed_safety_threshold:
      return False

  def check_sun_radiation_level(self, test_sensor):
    if test_sensor >= self.min_light_levels: #W/m2
      return True
    if test_sensor < self.min_light_levels:
      return False

  def move_azimuth_motor(self):
    #check against minmaxes
    self.__azimuth_angle += 0.5
    if self.__azimuth_angle >= self.limits_azimuth_angles[0] or self.__azimuth_angle < self.limits_altitude_angles[1]:
      return True
    elif self.__azimuth_angle >= self.limits_azimuth_angles[1]:
      self.__azimuth_angle -= self.limits_azimuth_angles[1]
      return True
    else:
      raise Exception("Number out of mechanical bounds")

  def move_altitude_motor(self):
    #check against minmaxes
    self.__altitude_angle += 0.125
    if self.__altitude_angle >= self.limits_altitude_angles[0] or self.__altitude_angle < self.limits_altitude_angles[1]:
      return True
    elif self.__altitude_angle > self.limits_altitude_angles[1] or self.__altitude_angle < self.limits_altitude_angles[0]:
      raise Exception("Number out of mechanical bounds") 

  def get_sun_direction(self):
    return self.sun_direction

  def set_sun_direction(self):
    self.sun_direction = [self.__altitude_angle, self.__azimuth_angle]

  def convert_degs_to_rads(self,in_degrees):
    radians = in_degrees*(pi/180)
    return radians

  def convert_rads_to_degs(self,in_rads):
    degrees = in_rads/(pi/180)
    return degrees

  def calc_sun_point(self):
    sx = self.radius*cos(self.convert_degs_to_rads(self.__altitude_angle))
    sy = self.radius*sin(self.convert_degs_to_rads(self.__altitude_angle))
    sz = sx/(tan(self.convert_degs_to_rads((2*pi)-self.__azimuth_angle)))

    self.sun_coords = [sx,sy,sz]

  def calc_angles_from_sunpoints(self):
    self.__altitude_angle = self.convert_rads_to_degs(acos(self.sun_coords[0]/self.radius))
    self.__azimuth_angle = self.convert_rads_to_degs((2*pi)-atan(self.sun_coords[0]/self.sun_coords[2]))
