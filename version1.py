from Bio.Blast import NCBIXML
import csv

result_handle = open("MHCxUNI-X.xml")
blast_records = NCBIXML.parse(result_handle)
outputfile = "C:/Users/Allen/Documents/11th-12th_Grade/SDSC_Epitopes/MHCxUNI.csv"

outfile = open(outputfile,"wb")
writer = csv.writer(outfile)

epitopeInfo = ""

identities = []
maxident = 0
maxcount = 0

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            epitopeInfo = blast_record.query
            if ((hsp.identities*100)/len(hsp.sbjct)) >= 80 and hsp.gaps<2 and len(hsp.query)>=blast_record.query_length:
                identities.append(hsp)
                if hsp.identities>maxident:
                    maxident = hsp.identities
                    maxcount = 0
                elif hsp.identities==maxident:
                    maxcount+1;
        if maxcount>2:
            for i in identities:
                if i.identities==maxident:
                    writer.writerow([epitopeInfo])
        identities = []
        maxident = 0
        maxcount = 0
        epitopeInfo = ""
                
result_handle.close()
