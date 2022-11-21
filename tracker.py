#----
# Altitude is the angular distance of an object above the local horizon. It ranges from 0 degrees at the horizon to 90 degrees at the zenith, the spot directly overhead. 
# #Azimuth is the angular distance of an object from the local North, measured along the horizon.
#

class SolarTrackerArray:

  #class vars
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
      return 

  def check_sun_radiation_level(self):
    pass

  def check_solar_sensor_X(self, input_sensor):
    pass

  def move_azimuth_motor(self):
    #check against minmaxes
    pass

  def move_altitude_motor(self):
    #check against minmaxes
    pass

  def get_sun_direction(self):
    return self.sun_direction

  def set_sun_direction(self,altitude,azimuth):
    self.__altitude_angle = altitude
    self.__azimuth_angle = azimuth
