from person import Person
from enroll import Enroll

class Student(Person):
	def __init__(self, first, last, dob, phone, address, international=False):
		super().__init__(self, first, last, dob, phone, address)
		self.international = international
		self.enrolled = []

	def add_enrollment(self, enroll):
		if not isinstance(enroll, Enroll):
			raise TypeError("Invalid Enroll...")

		self.enrolled.append(enroll)