from django.db import models

class withDependents(models.Model):
	MHA = models.CharField(max_length = 5)

	def __str__(self):
		return self.MHA

class withOutDependents(models.Model):
	MHA = models.CharField(max_length = 5)
	
	def __str__(self):
		return self.MHA

class ZipMHA(models.Model):
	ZipCode = models.CharField(max_length = 5)
	MHA = models.CharField(max_length = 5)

# add rank fields to withDependents and withOutDependents
rank_fields = [
	'E1', 'E2','E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
	'W1', 'W2', 'W3', 'W4', 'W5', 'O1E', 'O2E', 'O3E', 'O1',
	'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10'
	]

for rank in rank_fields:
		withDependents.add_to_class(rank, models.DecimalField(max_digits = 10, decimal_places = 2))
		withOutDependents.add_to_class(rank, models.DecimalField(max_digits = 10, decimal_places = 2))