CREATE OR REPLACE VIEW epi AS
(SELECT DISTINCT e.epitope_id
FROM bcell b, curated_epitope ce, epitope_object eo, epitope e, organism org
WHERE b.curated_epitope_id = ce.curated_epitope_id
AND ce.e_object_id = eo.object_id
AND eo.epitope_id = e.epitope_id
AND org.organism_id = eo.source_organism_org_id
AND linear_peptide_seq IS NOT NULL
AND org.path LIKE '1:10239%');

CREATE OR REPLACE VIEW pos AS 
(SELECT DISTINCT e.epitope_id
FROM bcell b, curated_epitope ce, epitope_object eo, epitope e, organism org
WHERE b.curated_epitope_id = ce.curated_epitope_id
AND ce.e_object_id = eo.object_id
AND eo.epitope_id = e.epitope_id
AND org.organism_id = eo.source_organism_org_id
AND linear_peptide_seq IS NOT NULL
AND org.path LIKE '1:10239%'
AND as_char_value LIKE 'Positive%');

SELECT (SELECT COUNT(*) FROM pos) AS Positives, COUNT(*) AS Negatives
FROM epi
WHERE epi.epitope_id NOT IN (SELECT pos.epitope_id FROM pos)