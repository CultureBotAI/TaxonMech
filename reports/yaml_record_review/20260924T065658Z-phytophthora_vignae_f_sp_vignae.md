# Review: Phytophthora vignae f. sp. vignae

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_vignae_f_sp_vignae.yaml`
- Target: `NCBITaxon:2501433`

## Target

The record grounds `Phytophthora vignae f. sp. vignae` as an exact seeded NCBI forma specialis under `NCBITaxon:67595` (`Phytophthora vignae`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 528070.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_vignae_f_sp_vignae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_vignae_f_sp_adzukicola.yaml data/taxa/eukaryota/phytophthora_vignae_f_sp_vignae.yaml data/taxa/eukaryota/phytophthora_x_alni.yaml data/taxa/eukaryota/phytophthora_x_cambivora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 11 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 62642 with the expected reason: `attested rule: Phytophthora vignae f. sp. vignae, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 528070.
- GOLD aggregate: line 22647 records `organism_count=1` for `NCBITaxon:2501433`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this forma-specialis target.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora vignae f. sp. vignae` is a forma-specialis NCBI taxon under the `Phytophthora vignae` species lineage entry.
