from Bio.Blast import NCBIXML

result_handle = open("MHCxUNI-X.xml")
blast_records = NCBIXML.parse(result_handle)

counter = 0
positions = []
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print (hsp.query)
                
result_handle.close()
