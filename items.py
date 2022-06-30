

class Item():
	def __init__(self, number_tag, equipable, x, y):
		self.equipable = equipable
		self.number_tag = number_tag 
		self.x = x
		self.y = y

	def gain_ID(self, ID):
		self.ID = ID

	def get_number_tag(self):
		return self.number_tag

class Weapon():
	def __init__(self, melee):
		self.melee = melee
