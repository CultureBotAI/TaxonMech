# Review: Phialophora verrucosa

- Verdict: pass
- Record: `data/taxa/eukaryota/phialophora_verrucosa.yaml`
- Target: `NCBITaxon:39412`

## Target

The record grounds `Phialophora verrucosa` as an exact seeded NCBI species under `NCBITaxon:5600` (`Phialophora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 4443.

## Validation

- `just validate data/taxa/eukaryota/phialophora_verrucosa.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phialocephala_subalpina.yaml data/taxa/eukaryota/phialomyces_arenicola.yaml data/taxa/eukaryota/phialophora_verrucosa.yaml data/taxa/eukaryota/phlebia_brevispora.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52404 with the expected reason: `attested rule: Phialophora verrucosa, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym, `Phialophora verrucosa Medlar, 1915`, and no exact or broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 4443.
- GOLD aggregate: line 34233 records `organism_count=1` for `NCBITaxon:39412`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 202288-202291 record four cultures from epitype, covering `BMU 07506`, `BMU:07506`, `CBS 140325`, and `CBS:140325`.
- StrainInfo: 26 direct exact strains and 34 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
