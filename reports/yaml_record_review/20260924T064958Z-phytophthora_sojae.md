# Review: Phytophthora sojae

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_sojae.yaml`
- Target: `NCBITaxon:67593`

## Target

The record grounds `Phytophthora sojae` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 8968.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_sojae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_quininea.yaml data/taxa/eukaryota/phytophthora_ramorum.yaml data/taxa/eukaryota/phytophthora_rubi.yaml data/taxa/eukaryota/phytophthora_sojae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53146 with the expected reason: `attested rule: Phytophthora sojae, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:4789` into this identifier at line 80822; an exact retained-row check found no `NCBITaxon:4789` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 8968.
- GOLD aggregate: line 41070 records `organism_count=1` for `NCBITaxon:67593`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, three exact project rows, and one exact analysis row for this target.
- NCBI type material: 20 exact rows were found at lines 253519-253538.
- StrainInfo: 64 direct exact strains and 57 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora sojae` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
