from Bio.Blast.Applications import NcbiblastpCommandline
import os
import json
origin = 'c:\\Users\\Allen\\Documents\\11th-12th_Grade'
epath = os.path.join(origin, 'Epitopes', 'TcellBactSorted')
dbpath = os.path.join(origin, 'Proteomes', 'Bacteria', 'Databases')
outpath = os.path.join(origin, 'Epitopes', 'TcellBactBLAST')
for root, _, files in os.walk(os.path.join(origin, 'Epitopes', 'TcellBactSorted')):
    for f in files:
        if os.path.isfile(os.path.join(dbpath, f[:-6] + '.db')):
            blastp_cline = NcbiblastpCommandline(query = os.path.join(epath, f), db = os.path.join(dbpath, f[:-6] + '.db'), out = os.path.join(outpath, f[:-6] + '.xml'), gapopen = 9, gapextend = 1, word_size = 2, matrix = "BLOSUM90", outfmt = 5)
            stdout, stderr = blastp_cline()
