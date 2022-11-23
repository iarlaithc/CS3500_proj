import unittest
from Sun import Sun
from tracker import SolarTrackerArray
from photodiode import Photodiode

#this is unit testing with the python standard test framework unittest unit testing package
# The analysis and description of the required tests should also be included in the report

class TestSun(unittest.TestCase):
	def setUp(self):
		self.sun1 = Sun(85,290)

	def test_init(self):
		self.assertIsNone(self.sun1.__init__())

	def test_set_sun_radiation(self):
		self.assertRaises(Exception)

	def test_set_sun_direction(self):
		self.assertListEqual(self.sun1.set_sun_direction(),[85,290])

	def test_convert_degs_to_rads(self):
		self.assertEqual(self.sun1.convert_degs_to_rads(10),0.17453292519943295)

	def test_convert_rads_to_degs(self):
		self.assertEqual(self.sun1.convert_rads_to_degs(0.17453292519943295),10)

	def test_decrement_sun_alt_angle(self):
		self.assertRaises(Exception)

	def test_move_sun(self):
		min_max = [10,40,270,30,1]
		self.assertTrue(self.sun1.move_sun(min_max))

class TestTracker(unittest.TestCase):
	def setUp(self):
		self.t1 = SolarTrackerArray(1,89.5,0)
		self.t2 = SolarTrackerArray(2,100.0,400.0) #bad

	def test_init(self):
		self.assertIsNone(self.t1.__init__(1))
		assert self.t1.array_number == 1
		assert self.t1.radius == 10000

	def test_safety_state(self):
		self.assertTrue(self.t1.safety_state())

	def test_check_anenometer(self):
		self.assertFalse(self.t1.check_anenometer(5000))
		self.assertTrue(self.t1.check_anenometer(50))

	def test_sun_radiation_level(self):
		self.assertFalse(self.t1.check_sun_radiation_level(50))
		self.assertTrue(self.t1.check_sun_radiation_level(100))

	def test_incerement_array_azi_angle(self):
		self.assertRaises(Exception)

	def test_decerement_array_azi_angle(self):
		self.assertRaises(Exception)

	def test_move_altitude_motor(self):
		self.assertTrue(self.t1.move_altitude_motor(1))

	def test_calc_sun_point(self):
		self.assertEqual(self.t1.sun_coords, [0,0,0])

class TestPhotoDiode(unittest.TestCase):
	def setUp(self):
		self.d1 = Photodiode("N")

	def test_get_output_voltage(self):
		self.assertEqual(self.d1.get_output_voltage(), 0)
		

if __name__ == '__main__':
	unittest.main()

#its testing