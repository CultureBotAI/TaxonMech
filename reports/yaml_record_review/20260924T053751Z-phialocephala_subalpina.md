# Review: Phialocephala subalpina

- Verdict: pass
- Record: `data/taxa/eukaryota/phialocephala_subalpina.yaml`
- Target: `NCBITaxon:576137`

## Target

The record grounds `Phialocephala subalpina` as an exact seeded NCBI species under `NCBITaxon:576134` (`Phialocephala fortinii species complex`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 136345.

## Validation

- `just validate data/taxa/eukaryota/phialocephala_subalpina.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phialocephala_subalpina.yaml data/taxa/eukaryota/phialomyces_arenicola.yaml data/taxa/eukaryota/phialophora_verrucosa.yaml data/taxa/eukaryota/phlebia_brevispora.yaml`: exited successfully
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56090 with the expected reason: `attested rule: Phialocephala subalpina, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym, `Phialocephala subalpina Grunig & T.N. Sieber, 2008`, and no exact or broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 136345.
- GOLD aggregate: line 39289 records `organism_count=1` for `NCBITaxon:576137`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 237843-237844 record `CBS 119280` and `CBS:119280` as cultures from holotype.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

None.
