# Review: Phaeoannellomyces elegans

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeoannellomyces_elegans.yaml`
- Target: `NCBITaxon:66226`

## Target

The record grounds `Phaeoannellomyces elegans` as an exact seeded NCBI species under `NCBITaxon:66225` (`Phaeoannellomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 8661.

## Validation

- `just validate data/taxa/eukaryota/phaeoannellomyces_elegans.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeoannellomyces_elegans.yaml data/taxa/eukaryota/phaeococcomyces_sp.yaml data/taxa/eukaryota/phaeocystis_antarctica.yaml data/taxa/eukaryota/phaeocystis_cf_globosa.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53132 with the expected reason: `attested rule: Phaeoannellomyces elegans, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that pattern.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 8661.
- GOLD aggregate: line 40688 records `organism_count=1` for `NCBITaxon:66226`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: lines 246651-246654 record four exact rows for this target.
- StrainInfo: 3 direct exact strains and 3 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
