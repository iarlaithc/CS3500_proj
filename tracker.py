#----
# Altitude is the angular distance of an object above the local horizon. It ranges from 0 degrees at the horizon to 90 degrees at the zenith, the spot directly overhead. 
# #Azimuth is the angular distance of an object from the local North, measured along the horizon.
#

class SolarTrackerArray:

  #class vars
  min_light_levels = 100.0 #W/m2
  limits_azimuth_angles = [0.0,360.0]
  limits_altitude_angles = [0.0,90.0]
  windspeed_safety_threshold = 30.0 #this is in kmph, realisticially we would have a rpm check so convert this over

  def __init__(self,array_number:int, start_altitude_angle = 0, start_azimuth_angle = 270 ):
    #system setup & instance vars
    self.array_number = array_number
    self.__altitude_angle = float
    self.__azimuth_angle = float
    self.sun_direction = [self.__altitude_angle, self.__azimuth_angle]

    self.anenometer_rpm = float

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

  # def check_solar_sensor_X(self, input_sensor:object):
  #   input_sensor.check_diode_output_strength

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

  def set_sun_direction(self,altitude,azimuth):
    self.__altitude_angle = altitude
    self.__azimuth_angle = azimuth
