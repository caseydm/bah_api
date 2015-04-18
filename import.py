import csv
from bah_api.models import withDependents
from django.contrib.auth.models import User

# open the CSV file
f = open("BAH2015/bahw15.txt")

# create CSV reader from the file
csv_f = csv.reader(f)

# print a row
#print(next(csv_f))

# print a model object
wdModel = withDependents()
#wdModel = (next(csv_f))
#for x in wdModel._meta.fields:
	#print(x.name)
#print(wdModel._meta.fields[1].name)

i = 1
for y in next(csv_f):
	print(wdModel._meta.fields[i].name, ':', y) 
	i += 1


# close the file
f.close()