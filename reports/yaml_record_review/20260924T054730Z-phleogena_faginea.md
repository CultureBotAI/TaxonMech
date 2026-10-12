# Review: Phleogena faginea

- Verdict: pass
- Record: `data/taxa/eukaryota/phleogena_faginea.yaml`
- Target: `NCBITaxon:5224`

## Target

The record grounds `Phleogena faginea` as an exact seeded NCBI species under `NCBITaxon:5223` (`Phleogena`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2297.

## Validation

- `just validate data/taxa/eukaryota/phleogena_faginea.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlegmacium_sp.yaml data/taxa/eukaryota/phleogena_faginea.yaml data/taxa/eukaryota/phlyctochytrium_arcticum.yaml data/taxa/eukaryota/phlyctochytrium_aureliae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 51954 with the expected reason: `attested rule: Phleogena faginea, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 2297.
- GOLD aggregate: line 37826 records `organism_count=2` for `NCBITaxon:5224`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 3 direct exact strains and 3 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
