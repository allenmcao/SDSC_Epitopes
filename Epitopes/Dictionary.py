import os
import csv
import json
from Bio import SeqIO

viruses = open("C:\\Users\\Lynn\\Desktop\\Blast\\viruses\\viruses.csv", "r")
reader = csv.reader(viruses)
bacteria = open("C:\\Users\\Lynn\\Desktop\\Blast\\bacteria\\bacteria.csv", "r")

vd = dict()
bd = dict()

for row in reader:
    if row:
        vd[row[0]] = row[2]

reader = csv.reader(bacteria)

for row in reader:
    if row:
        bd[row[0]] = row[2]


handle = open("C:\\Users\\Lynn\\Desktop\\Blast\\mhcII.fasta", "r")
mhcII = list(SeqIO.parse(handle, "fasta"))
for record in mhcII:
    description = record.description
    sourceid = description[description.index("org") + 12:-1]
    if sourceid in vd:
        proteomeid = vd[sourceid]
        with open("C:\\Users\\Lynn\\Documents\\SDSC_2013\\mhcII_virus\\" + proteomeid + ".fasta", "a") as f:
            f.write('>' + description + '\n')
            f.write(str(record.seq + '\n'))
        #file = open("C:\\Users\\Lynn\\Documents\\SDSC_2013\\mhcII_virus\\" + proteomeid + ".fasta", "w")
        #file.write(">" + description + "\n" + str(record.seq) + "\n")
    elif sourceid in bd:
        proteomeid = bd[sourceid]
        with open("C:\\Users\\Lynn\\Documents\\SDSC_2013\\mhcII_bacteria\\" + proteomeid + ".fasta", "a") as f:
            f.write('>' + description + '\n')
            f.write(str(record.seq + '\n'))
        #file = open("C:\\Users\\Lynn\\Documents\\SDSC_2013\\mhcII_bacteria\\" + proteomeid + ".fasta", "w")
        #file.write(">" + description + "\n" + str(record.seq) + "\n")
    else:
        continue


#json.dump(vd, open("C:\\Users\\Lynn\\Desktop\\Blast\\viruses\\viruses.json", "w"))

#json.dump(bd, open("C:\\Users\\Lynn\\Desktop\\Blast\\bacteria\\bacteria.json", "w"))



