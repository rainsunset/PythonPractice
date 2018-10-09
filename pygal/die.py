# encoding:utf-8

from random import randint

class Die():
	""" 掷骰子"""

	def __init__(self, num_side=6):
		self.num_side = num_side

	def roll(self):
		""" 返回骰子随即面的值 """
		return randint(1,self.num_side)