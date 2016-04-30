from Bio.Blast.Applications import NcbiblastpCommandline
import os
import json
root = 'c:\\Users\\Allen\\Documents\\11th-12th_Grade'
path = os.path.join(root, 'sdsc_rehs_2013', 'fasta_files')
epath = os.path.join(path, 'epitope')
dbpath = os.path.join(root, 'sdsc_rehs_2013', 'blast_dbs', 'bacteria')
opath = os.path.join(root, 'sdsc_rehs_2013', 'blast_results', 'bcellbacteria')
data_file = open(os.path.join(root, 'sdsc_rehs_2013', 'fasta_files', 'bacteria.json'))
bacteriadict = json.load(data_file)
for root, _, files in os.walk(os.path.join(epath, 'bcell')):
    for f in files:
        if f[:-6] in bacteriadict:
            if os.path.isfile(os.path.join(path, 'proteome', 'bacteria', f[:-6] + '.fasta')):
                print ('hi')
                blastp_cline = NcbiblastpCommandline(query = os.path.join(epath, 'bcell', f), db = os.path.join(dbpath, bacteriadict[f[:-6]] + '.db'), outfmt = "\"10 qlen qseqid qstart qend sstart send gaps pident length \"", out = os.path.join(opath, f[:-6] + '.csv'), gapopen = 9, gapextend = 1, word_size = 2, matrix = "BLOSUM90")
                stdout, stderr = blastp_cline()
