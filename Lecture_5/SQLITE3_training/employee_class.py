class employee:
	
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def email(self):
		return "{}_{}@naver.com".format(self.first, self.last)


