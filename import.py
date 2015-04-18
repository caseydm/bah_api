import csv
from bah_api.models import withDependents

# open the CSV file
f = open("BAH2015/bahw15.txt")

# create CSV reader from the file
csv_f = csv.reader(f)

# assign model


# loop through each row and assign to the model fields
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

# close the file
f.close()