import csv
from bah_api.models import withDependents, ZipMHA

# with Dependents
def LoadWithDep(file_location):
	f = open(file_location)
	csv_f = csv.reader(f)
	for row in csv_f:
		i = 1
		# create a model instance	
		wdModel = withDependents()
		#loop through the rows
		for y in row:
			setattr(wdModel, wdModel._meta.fields[i].name, y)
			i += 1
		# save each row
		wdModel.save()
	f.close()

# ZipMHA
def LoadZipMHA(file_location):
	f = open(file_location)
	csv_f = csv.reader(f, delimiter=' ')
	for row in csv_f:
		i = 1
		# create a model instance	
		zipModel = ZipMHA()
		#loop through the rows
		for y in row:
			setattr(zipModel, zipModel._meta.fields[i].name, y)
			i += 1
		# save each row
		zipModel.save()
	f.close()

# run functions
# LoadWithDep("BAH2015/bahw15.txt")
LoadZipMHA("BAH2015/sorted_zipmha15.txt")