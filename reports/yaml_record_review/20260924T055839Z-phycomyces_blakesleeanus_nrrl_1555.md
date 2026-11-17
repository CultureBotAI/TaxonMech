# Review: Phycomyces blakesleeanus NRRL 1555(-)

- Verdict: pass
- Record: `data/taxa/eukaryota/phycomyces_blakesleeanus_nrrl_1555.yaml`
- Target: `NCBITaxon:763407`

## Target

The record grounds `Phycomyces blakesleeanus NRRL 1555(-)` as an exact seeded NCBI strain under `NCBITaxon:4837` (`Phycomyces blakesleeanus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 177173.

## Validation

- `just validate data/taxa/eukaryota/phycomyces_blakesleeanus_nrrl_1555.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phycomyces_blakesleeanus_nrrl_1555.yaml data/taxa/eukaryota/phycomyces_nitens.yaml data/taxa/eukaryota/phycomyces_sp_jgi_2019a.yaml data/taxa/eukaryota/phyllachora_maydis.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56676 with the expected reason: `attested rule: Phycomyces blakesleeanus NRRL 1555(-), 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms, matching the absence of YAML synonyms.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 177173.
- GOLD aggregate: line 42510 records `organism_count=1` for `NCBITaxon:763407`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this target.
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

None.
