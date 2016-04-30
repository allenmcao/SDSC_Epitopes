'''
Created on Jul 18, 2013

@author: anita
'''
from Bio.Blast import NCBIXML

result_handle = open("output3.xml")
blast_records = NCBIXML.parse(result_handle)

counter = 0
positions = []
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if (hsp.identities*100)/len(hsp.sbjct) >= 80: #percent of matches, I think
                counter += 1
                positions.append(hsp.sbjct_start) #hopefully this is the actual starting position
            if counter > 1:
                for i in range (0, counter):
                    positions.pop()
        counter = 0
print (positions)
                
result_handle.close()
