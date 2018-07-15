"""Classes for melon orders."""

from random import randint
import datetime 

class AbstractMelonOrder():

	def __init__(self, species, qty, country_code=None):
		"""Initialize melon order attributes."""
		self.species = species
		self.qty = qty

		if self.qty > 100:
#			raise TooManyMelonsError("Cannot buy more than 100 melons. \
#You have bought {} melons".format(self.qty))
			raise TooManyMelonsError("Error",self.qty)
		self.shipped = False
		if country_code:
			self.country_code = country_code
		

	def get_base_price(self):

		base_price = randint(5,9)
		hour_now = int(datetime.datetime.now().strftime("%H"))


		if hour_now > 8 and hour_now < 11:
			base_price += 4  
			print("Rush Hour")

		print(base_price,hour_now)

		return base_price

	def get_total(self):
		"""Calculate price, including tax."""



		fee = 0
		base_price = self.get_base_price()

		if self.species.lower() == "christmas melons":
			base_price *= 1.5

		if self.order_type == "international" and self.qty < 11:
			fee = 3

		total = (1 + self.tax) * self.qty * base_price + fee

		return total

	def mark_shipped(self):
		"""Record the fact than an order has been shipped."""

		self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
	"""A melon order within the USA."""

	
	order_type = "domestic"
	tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
	"""An international (non-US) melon order."""

	order_type = "international"
	tax = 0.17

	def get_country_code(self):
		"""Return the country code."""

		return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
	
	tax = 0
	order_type = "government"
	passed_inspection = False

	def mark_inspection(self,passed):
		
		self.passed_inspection = passed

		return passed


class TooManyMelonsError(ValueError):


    def __init__(self,message,qty):
    	self.message = message
    	self.qty = qty
    	self.display_error()
    	
    def display_error(self):
    	print("Cannot buy more than 100 melons\
You have bought {} melons".format(self.qty))