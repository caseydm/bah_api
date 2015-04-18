import csv
from bah_api.models import withDependents
from django.contrib.auth.models import User

# open the CSV file
f = open("BAH2015/bahw15.txt")

# create CSV reader from the file
csv_f = csv.reader(f)

# print a row
print(next(csv_f))

# print a model object
users = User.objects.all()
print(users)

# close the file
f.close()