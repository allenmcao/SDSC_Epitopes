import os
import csv
import json
origin = 'c:\\Users\\Allen\\Documents\\11th-12th_Grade'
path = os.path.join(origin, 'Proteomes')
bacteriadict = {}
f = open(os.path.join(path, 'bacteria.csv'))
reader = csv.reader(f)
for row in reader:
    if row:
        bacteriadict[row[0]] = row[2]
f.close()
with open(os.path.join(path, 'bacteria.json'), 'w') as f_new:
    json.dump(bacteriadict, f_new)
