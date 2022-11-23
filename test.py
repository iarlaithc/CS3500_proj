import unittest
from Sun import Sun

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

	def test_decrement_sun_alt_angle(self):
		self.assertRaises(Exception)

	def test_move_sun(self):
		min_max = [10,40,270,30,1]
		self.assertTrue(self.sun1.move_sun(min_max))

if __name__ == '__main__':
	unittest.main()