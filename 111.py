# -*- coding: utf-8 -*- 
# @Time : 2019/1/24 17:20 
# @Author : taojian 
# @File : 111.py

#### 关联用例 作为全局变量的使用
import unittest
from uu import test

class login(unittest.TestCase):
	name = None
	@classmethod
	def setUpClass(self):
		self.phone=test()
	
	def test_1(self):
		global name
		data={"username":"tj","password":123456}
		name=(data["username"])
		print(name)
		return name

	def test_2(self):
		pp={'user':name,'phone':self.phone}
		print(pp)
		
if __name__=='__main_ s_':
	unittest.main()
