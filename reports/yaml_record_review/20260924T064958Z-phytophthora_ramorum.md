# Review: Phytophthora ramorum

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_ramorum.yaml`
- Target: `NCBITaxon:164328`

## Target

The record grounds `Phytophthora ramorum` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 33708.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_ramorum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_quininea.yaml data/taxa/eukaryota/phytophthora_ramorum.yaml data/taxa/eukaryota/phytophthora_rubi.yaml data/taxa/eukaryota/phytophthora_sojae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 54203 with the expected reason: `attested rule: Phytophthora ramorum, 2 sources incl. NCBI`.
- The NCBI raw row has three related synonyms and no exact or broad synonyms; the YAML mirrors those three synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:332201` into this identifier at line 67849; an exact retained-row check found no `NCBITaxon:332201` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 33708.
- GOLD aggregate: line 14087 records `organism_count=22` for `NCBITaxon:164328`, matching the YAML GOLD attestation count; native GOLD has 22 exact organism rows, 24 exact project rows, and 23 exact analysis rows for this target.
- NCBI type material: 11 exact rows were found at lines 49238-49248.
- StrainInfo: 62 direct exact strains and 62 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora ramorum` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
