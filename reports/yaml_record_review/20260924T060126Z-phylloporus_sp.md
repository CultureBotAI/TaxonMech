# Review: Phylloporus sp.

- Verdict: pass
- Record: `data/taxa/eukaryota/phylloporus_sp.yaml`
- Target: `NCBITaxon:1916375`

## Target

The record grounds `Phylloporus sp.` as an exact seeded NCBI species under `NCBITaxon:2645115` (`unclassified Phylloporus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 494765.

## Validation

- `just validate data/taxa/eukaryota/phylloporus_sp.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phylloporia_minima.yaml data/taxa/eukaryota/phylloporus_rhodoxanthus.yaml data/taxa/eukaryota/phylloporus_sp.yaml data/taxa/eukaryota/phyllosticta_ampelicida.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 61604 with the expected reason: `attested rule: Phylloporus sp., 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms, matching the absence of YAML synonyms.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 494765.
- GOLD aggregate: line 17480 records `organism_count=1` for `NCBITaxon:1916375`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
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
