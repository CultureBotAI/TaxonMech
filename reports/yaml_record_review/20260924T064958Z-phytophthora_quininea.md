# Review: Phytophthora quininea

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_quininea.yaml`
- Target: `NCBITaxon:134455`

## Target

The record grounds `Phytophthora quininea` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 26554.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_quininea.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_quininea.yaml data/taxa/eukaryota/phytophthora_ramorum.yaml data/taxa/eukaryota/phytophthora_rubi.yaml data/taxa/eukaryota/phytophthora_sojae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53960 with the expected reason: `attested rule: Phytophthora quininea, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:980179` into this identifier at line 100238; an exact retained-row check found no `NCBITaxon:980179` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 26554.
- GOLD aggregate: line 8389 records `organism_count=1` for `NCBITaxon:134455`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: 18 exact rows were found at lines 24389-24406.
- StrainInfo: two direct exact strains and four exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora quininea` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
