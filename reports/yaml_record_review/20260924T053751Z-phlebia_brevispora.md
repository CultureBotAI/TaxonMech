# Review: Phlebicolorata brevispora

- Verdict: pass
- Record: `data/taxa/eukaryota/phlebia_brevispora.yaml`
- Target: `NCBITaxon:194682`

## Target

The record grounds `Phlebicolorata brevispora` as an exact seeded NCBI species under `NCBITaxon:3817995` (`Phlebicolorata`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 38574.

## Validation

- `just validate data/taxa/eukaryota/phlebia_brevispora.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phialocephala_subalpina.yaml data/taxa/eukaryota/phialomyces_arenicola.yaml data/taxa/eukaryota/phialophora_verrucosa.yaml data/taxa/eukaryota/phlebia_brevispora.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54421 with the expected reason: `attested rule: Phlebia brevispora, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Phlebia brevispora`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 6981 and 86799 map retired `NCBITaxon:1191688` and `NCBITaxon:571426` to this identifier; exact retained-row greps found neither old ID in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 38574.
- GOLD aggregate: line 17903 records `organism_count=1` for `NCBITaxon:194682`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 4 direct exact strains and 5 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
