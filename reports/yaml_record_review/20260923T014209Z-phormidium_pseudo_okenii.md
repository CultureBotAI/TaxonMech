# YAML Record Review: Phormidium pseudo-okenii
- Repository: TaxonMech
- Record: data/taxa/bacteria/phormidium_pseudo_okenii.yaml
- Started UTC: 2026-09-23T01:42:09Z
- Finished UTC: 2026-09-23T01:42:09Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/phormidium_pseudo_okenii.yaml`
- Identifier: `NCBITaxon:1005727`
- Label: `Phormidium pseudo-okenii`
- Rank: `SPECIES`
- Parent: `NCBITaxon:1198`
- Registry row: `data/taxa/PATHS.tsv:1829`
- Scope row: `curation/seed_scope.tsv:311211`
- A pre-write `find reports/yaml_record_review ... -name '*-phormidium_pseudo_okenii.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/phormidium_pseudo_okenii.yaml data/taxa/bacteria/geitlerinema_serpens.yaml data/taxa/bacteria/schizothrix_tenebrosa.yaml data/taxa/bacteria/bacteroidetes_bacterium_4f6b.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/phormidium_pseudo_okenii.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, exact synonyms, and NCBI related synonym agree with `data/raw/ncbitaxon_taxa.tsv:210492`.
- The stored lineage terminates at the asserted genus `NCBITaxon:1198` / `Phormidium`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210492` attests `NCBITaxon:1005727` as `Phormidium pseudo-okenii`, rank `SPECIES`, parent `NCBITaxon:1198`, genetic code `11`, exact synonyms `Phormidium pseudo-okeni` and `Phormidium pseudookenii`, a nomenclatural related synonym, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` found no same-taxon rows for `NCBITaxon:1005727`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005727`, `Phormidium pseudo-okenii`, `Phormidium pseudo-okeni`, `Phormidium pseudookenii`, or `phormidium_pseudo_okenii`.

## Completeness

- The generated NCBI identity, lineage, NCBI synonyms, source attestation, and seed history are complete for the local source row.
- The record has no GTDB mapping, xref, Madin, GOLD, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/phormidium_pseudo_okenii.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
