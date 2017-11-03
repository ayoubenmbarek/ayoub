import csv
from StringIO import StringIO

quotedData = StringIO()

#with open('/home/databiz41/carsalesmobile/carsalesmobile/latest5_carsales_2017_09_v4.csv',"w") as f:
openfile = open("/home/databiz41/carsalesmobile/carsalesmobile/latest5_carsales_2017_09_v4.csv", "wb")
reader = csv.reader(openfile)
writer = csv.writer(openfile, quoting=csv.QUOTE_ALL)
for row in reader:
        writer.writerow(row)
