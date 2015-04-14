from django.db import models

# BAH model
class BAH(models.Model):
	rank = models.CharField(max_length = 4)
	dependents = models.BooleanField()
	MHA = models.CharField(max_length = 5)

		
