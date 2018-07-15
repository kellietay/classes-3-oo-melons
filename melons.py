"""Classes for melon orders."""

class AbstractMelonOrder():

	def __init__(self, species, qty, country_code=None):
		"""Initialize melon order attributes."""
		self.species = species
		self.qty = qty
		self.shipped = False
		if country_code:
			self.country_code = country_code
		
	def get_total(self):
		"""Calculate price, including tax."""

		base_price = 5
		fee = 0
		
		if self.species.lower() == "christmas melons":
			base_price *= 1.5

		if self.order_type == "international" and self.qty < 10:
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
