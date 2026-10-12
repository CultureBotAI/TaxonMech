# Review: Phlegmacium cistoglaucopus

- Verdict: pass
- Record: `data/taxa/eukaryota/phlegmacium_cistoglaucopus.yaml`
- Target: `NCBITaxon:1440158`

## Target

The record grounds `Phlegmacium cistoglaucopus` as an exact seeded NCBI species under `NCBITaxon:2339270` (`Phlegmacium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 361329.

## Validation

- `just validate data/taxa/eukaryota/phlegmacium_cistoglaucopus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlebopus_sp.yaml data/taxa/eukaryota/phlegmacium_cistoglaucopus.yaml data/taxa/eukaryota/phlegmacium_glaucopus.yaml data/taxa/eukaryota/phlegmacium_glaucopus_at_2004_276.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60142 with the expected reason: `attested rule: Phlegmacium cistoglaucopus, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 361329.
- GOLD aggregate: line 10500 records `organism_count=1` for `NCBITaxon:1440158`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: lines 31150-31154 record `LIP JVG 1081108P`, `LIP:JVG:1081108P`, and `LIP_JVG_1081108P_HOLOTYPE` holotype designations plus `GDA 59131` and `GDA:59131` isotype designations.
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
