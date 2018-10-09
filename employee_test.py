# encoding:utf-8
import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
	""" 员工类测试 """

	def setUp(self):
		self.salary = 7000
		self.my_employee = Employee('gangwei','li',666)

	def test_give_default_raise(self):
		""" 测试默认年薪 """
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.salary,5000)

	def test_give_custom_raise(self):
		""" 测试自定义年薪 """
		self.my_employee.give_raise(self.salary)
		self.assertEqual(self.my_employee.salary,self.salary)
		
unittest.main()