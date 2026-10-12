# Review: Phaeococcomyces sp.

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeococcomyces_sp.yaml`
- Target: `NCBITaxon:2040901`

## Target

The record grounds `Phaeococcomyces sp.` as an exact seeded NCBI species under `NCBITaxon:2635909` (`unclassified Phaeococcomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 513195.

## Validation

- `just validate data/taxa/eukaryota/phaeococcomyces_sp.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeoannellomyces_elegans.yaml data/taxa/eukaryota/phaeococcomyces_sp.yaml data/taxa/eukaryota/phaeocystis_antarctica.yaml data/taxa/eukaryota/phaeocystis_cf_globosa.yaml`: exited successfully
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 62150 with the expected reason: `attested rule: Phaeococcomyces sp., 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 513195.
- GOLD aggregate: line 19349 records `organism_count=1` for `NCBITaxon:2040901`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: no exact rows were found for this target.
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
