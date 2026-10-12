# Review: Phytophthora rubi

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_rubi.yaml`
- Target: `NCBITaxon:129364`

## Target

The record grounds `Phytophthora rubi` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 24751.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_rubi.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_quininea.yaml data/taxa/eukaryota/phytophthora_ramorum.yaml data/taxa/eukaryota/phytophthora_rubi.yaml data/taxa/eukaryota/phytophthora_sojae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53921 with the expected reason: `attested rule: Phytophthora rubi, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, two related synonyms, and no broad synonyms; the YAML mirrors those three synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 24751.
- GOLD aggregate: line 6899 records `organism_count=4` for `NCBITaxon:129364`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have four exact rows for this target.
- NCBI type material: 22 exact rows were found at lines 20017-20038.
- StrainInfo: five direct exact strains and seven exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora rubi` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
