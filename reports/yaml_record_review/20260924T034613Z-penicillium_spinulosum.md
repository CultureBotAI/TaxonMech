# Review: Penicillium spinulosum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_spinulosum.yaml`
- Target: `NCBITaxon:63822`

## Target

The record grounds `Penicillium spinulosum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 8022.

## Validation

- `just validate data/taxa/eukaryota/penicillium_spinulosum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sp_str_12.yaml data/taxa/eukaryota/penicillium_spathulatum.yaml data/taxa/eukaryota/penicillium_spinulosum.yaml data/taxa/eukaryota/penicillium_steckii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53069 with the expected reason: `attested rule: Penicillium spinulosum, 2 sources incl. NCBI`.
- The NCBI raw row has five exact synonyms, no broad synonyms, and four related synonyms; the YAML mirrors those nine synonym entries.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:1111108`, `NCBITaxon:1539488`, and `NCBITaxon:685546` into `NCBITaxon:63822` at lines 3721, 19372, and 92183; exact retained-row greps of `data/raw/ncbitaxon_taxa.tsv` found no remaining rows for those old IDs, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 8022.
- GOLD aggregate: line 40167 records `organism_count=1` for `NCBITaxon:63822`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: four exact rows at lines 243598-243601, all culture from neotype, covering `CBS 374.48` / `CBS:374.48` and `FRR 1750` / `FRR:1750`.
- StrainInfo: exact StrainInfo has 135 direct strains and 254 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:63822`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The large StrainInfo exact hit set is source-only for this generated record because none of the exact rows overlay onto BacDive-derived local strains.
