SELECT org.path, name_txt, COUNT(DISTINCT e.epitope_id)
FROM bcell b, curated_epitope ce, epitope_object eo, epitope e, organism org, object obj, organism_names orgn
WHERE b.curated_epitope_id = ce.curated_epitope_id
AND ce.e_object_id = eo.object_id
AND eo.epitope_id = e.epitope_id
AND org.organism_id = eo.source_organism_org_id
AND obj.object_id = iv1_imm_object_id
AND org.organism_id = orgn.organism_id
AND linear_peptide_seq IS NOT NULL
AND org.path LIKE '1:10239:%'
AND iv1_imm_type IN ('Source Organism', 'Source Antigen')
GROUP BY org.path
ORDER BY COUNT(DISTINCT e.epitope_id) DESC;