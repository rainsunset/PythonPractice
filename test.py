# encoding:utf-8
import unittest
from name_function import get_formatter_name

class NamesTestCase(unittest.TestCase):
	"""测试name_funcation.py"""

	def test_formater_name(self):
		formatted_naem = get_formatter_name('li','gang')
		self.assertEqual(formatted_naem,"Li Gang")

	def test_formater_middle_name(self):
		formatted_naem = get_formatter_name('guo','hong','jia')
		self.assertEqual(formatted_naem,"Guo Jia Hong")

	def test_notEuual(self):
		end_val = 1 + 1
		self.assertNotEqual(end_val,3)

	def test_true(self):
		end_val = True
		self.assertTrue(end_val)

	def test_false(self):
		end_val = False
		self.assertFalse(end_val)

	def test_in(self):
		sixx = 6
		list_demo = [6,7]
		self.assertIn(sixx,list_demo)
		
	def test_not_in(self):
		sixx = 6
		list_demo = [7,8]
		self.assertNotIn(sixx,list_demo)

unittest.main()