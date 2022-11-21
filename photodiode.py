# photodiode produces current when it absorbs photons
# there will be 4 instances of a photodiode 
# one for each corner of compass on sensor

class Photodiode:
  photodiode_surface_area = 0.000625 #biggg sensor surface area tbh

  def __init__(self,polar_name):
    self.__surface_irradiation = 0.0 #float #unit for irradiance is watt/m^2
    self.__output_voltage = float
    self.name = polar_name

  def check_diode_output_strength(self):
    #function to take power/area input and generate voltage output
    #based on graph ig
    #1kOHM load
    #when 1w/m2 on sensor 0.025m x 0.025m
    #P=(V^2)/R and stuff but the load and size are constant
    #theoretically linear function so
    # 1m/m2 -> 2.8125mV output
    self.__output_voltage = self.__surface_irradiation*0.0028125

  def set_surface_irradiation(self, irr_value:float):
    self.__surface_irradiation = irr_value

  def get_output_voltage(self):
    return self.__output_voltage
