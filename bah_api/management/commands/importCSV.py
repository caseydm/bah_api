from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from bah_api.models import withDependents, withOutDependents, ZipMHA

class Command(BaseCommand):
	def handle(self, *args, **options):
		# Populate CSV file into model
		def LoadCSV(file_location, my_model, delim):
			f = open(file_location)
			csv_f = csv.reader(f, delimiter=delim)
			for row in csv_f:
				i = 1
				# create a model instance	
				target_model = my_model()
				#loop through the rows
				for y in row:
					setattr(target_model, target_model._meta.fields[i].name, y)
					i += 1
				# save each row
				target_model.save()
			f.close()

		# run functions
		LoadCSV(settings.PROJECT_PATH + "/BAH2015/bahw15.txt", withDependents, ',')
		LoadCSV(settings.PROJECT_PATH + "/BAH2015/bahwo15.txt", withOutDependents, ',')
		LoadCSV(settings.PROJECT_PATH + "/BAH2015/sorted_zipmha15.txt", ZipMHA, ' ')