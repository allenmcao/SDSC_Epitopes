SELECT COUNT(DISTINCT e.epitope_id) 
FROM tcell t, 
mhc_allele_restriction mar, 
curated_epitope ce, 
object o, 
epitope_object eo, 
epitope e,
organism org,
object obj
WHERE mar.DISPLAYED_RESTRICTION = t.MHC_ALLELE_NAME
AND t.CURATED_EPITOPE_ID = ce.CURATED_EPITOPE_ID
AND o.OBJECT_ID = ce.E_OBJECT_ID
AND o.OBJECT_ID = eo.OBJECT_ID
AND eo.EPITOPE_ID = e.EPITOPE_ID
AND org.organism_id = eo.source_organism_org_id
AND obj.OBJECT_ID = IV1_IMM_OBJECT_ID
AND mar.class = 'II'
AND e.linear_peptide_seq IS NOT NULL
AND org.path LIKE '1:10239%'
AND obj.object_sub_type ='Organism';