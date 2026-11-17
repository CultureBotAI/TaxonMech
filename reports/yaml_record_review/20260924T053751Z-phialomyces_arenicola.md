# Review: Phialomyces arenicola

- Verdict: pass
- Record: `data/taxa/eukaryota/phialomyces_arenicola.yaml`
- Target: `NCBITaxon:168477`

## Target

The record grounds `Phialomyces arenicola` as an exact seeded NCBI species under `NCBITaxon:1131489` (`Phialomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 34412.

## Validation

- `just validate data/taxa/eukaryota/phialomyces_arenicola.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phialocephala_subalpina.yaml data/taxa/eukaryota/phialomyces_arenicola.yaml data/taxa/eukaryota/phialophora_verrucosa.yaml data/taxa/eukaryota/phlebia_brevispora.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54244 with the expected reason: `attested rule: Phialomyces arenicola, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 24413 maps retired `NCBITaxon:168587` to this identifier; an exact retained-row grep found no `NCBITaxon:168587` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 34412.
- GOLD aggregate: line 14526 records `organism_count=8` for `NCBITaxon:168477`, matching the YAML GOLD attestation count; native GOLD has eight exact organism rows and no exact project or analysis rows for this target.
- NCBI type material: lines 52114-52115 record `CBS 220.66` and `CBS:220.66` as `Penicillium arenicola` isotypes.
- StrainInfo: 16 direct exact strains and 44 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
