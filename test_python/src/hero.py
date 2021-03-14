#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from typing import List
def log(func):
	"""
	func =winner
	:param func:
	:return:
	"""
	def wrapper(*args, **kwargs):
		print(func.__name__)
		return func(*args, **kwargs)
	return wrapper




class Hero:
	hp = 100
	power = 10
	magic_hp = 200
	speed = 1
	tools = []

	@log
	def fight(self, hero: 'Hero'):
		while True:
			self.hp -= hero.power
			if self.winner(self, hero):
				return True
			hero.hp -= self.power
			if self.winner(hero, self):
				return False

	def winner(self, hero1, hero2):
		print(f'{hero1} VS {hero2}')
		if hero1.hp <= 0:
			print('False')
			return False
		if hero2.hp <= 0:
			print('Ture')
			return True

	@log
	def fight_many(self, heros: list['Hero']):
		pass