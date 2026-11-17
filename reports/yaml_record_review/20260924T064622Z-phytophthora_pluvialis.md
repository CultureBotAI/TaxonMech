# Review: Phytophthora pluvialis

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_pluvialis.yaml`
- Target: `NCBITaxon:1330343`

## Target

The record grounds `Phytophthora pluvialis` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 318171.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_pluvialis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_pluvialis.yaml data/taxa/eukaryota/phytophthora_podocarpi.yaml data/taxa/eukaryota/phytophthora_pseudosyringae.yaml data/taxa/eukaryota/phytophthora_quercina.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 59505 with the expected reason: `attested rule: Phytophthora pluvialis, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 318171.
- GOLD aggregate: line 8040 records `organism_count=2` for `NCBITaxon:1330343`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have two exact rows for this target.
- NCBI type material: nine exact rows were found at lines 23199-23207.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora pluvialis` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
