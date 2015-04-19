from django.db import models

class withDependents(models.Model):
	MHA = models.CharField(max_length = 5)
	E1 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E2 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E3 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E4 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E5 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E6 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E7 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E8 = models.DecimalField(max_digits = 10, decimal_places = 2)
	E9 = models.DecimalField(max_digits = 10, decimal_places = 2)
	W1 = models.DecimalField(max_digits = 10, decimal_places = 2)
	W2 = models.DecimalField(max_digits = 10, decimal_places = 2)
	W3 = models.DecimalField(max_digits = 10, decimal_places = 2)
	W4 = models.DecimalField(max_digits = 10, decimal_places = 2)
	W5 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O1E = models.DecimalField(max_digits = 10, decimal_places = 2)
	O2E = models.DecimalField(max_digits = 10, decimal_places = 2)
	O3E = models.DecimalField(max_digits = 10, decimal_places = 2)
	O1 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O2 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O3 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O4 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O5 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O6 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O7 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O8 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O9 = models.DecimalField(max_digits = 10, decimal_places = 2)
	O10 = models.DecimalField(max_digits = 10, decimal_places = 2)

	def __str__(self):
		return self.MHA

class ZipMHA(models.Model):
	ZipCode = models.CharField(max_length = 5)
	MHA = models.CharField(max_length = 5)
