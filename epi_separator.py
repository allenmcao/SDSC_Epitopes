from Bio import SeqIO
import os
import json

original = 'c:\\Users\\Allen\\Documents\\11th-12th_Grade'
path = os.path.join(original, 'Epitopes') 
for seq_record in SeqIO.parse(os.path.join(path, 'mhcII.fasta'), 'fasta'):
    id = seq_record.description[seq_record.description.index('organism_id')+12:-1]
    data_file = open(os.path.join(original, 'Proteomes', 'bacteria.json'))
    data_file2 = open(os.path.join(original, 'Proteomes', 'viruses.json'))
    bacteriadict = json.load(data_file)
    virusdict = json.load(data_file2)
    specieid = 0
    if id in bacteriadict:
        specieid = bacteriadict[id]
    elif id in virusdict:
        specieid = virusdict[id]
    if specieid==0:
        print ("no match")
    with open(os.path.join(path, "TcellSorted",specieid + '.fasta'), 'a') as f:
              f.write('>' + seq_record.description + '\n')
              f.write(str(seq_record.seq + '\n'))
