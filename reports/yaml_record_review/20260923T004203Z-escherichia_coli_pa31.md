# YAML Record Review: Escherichia coli PA31
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_pa31.yaml
- Started UTC: 2026-09-23T00:42:03Z
- Finished UTC: 2026-09-23T00:42:03Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_pa31.yaml`
- Identifier: `NCBITaxon:1005502`
- Label: `Escherichia coli PA31`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1736`
- Scope row: `curation/seed_scope.tsv:35985`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_pa31.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_pa24.yaml data/taxa/bacteria/escherichia_coli_pa25.yaml data/taxa/bacteria/escherichia_coli_pa28.yaml data/taxa/bacteria/escherichia_coli_pa31.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/escherichia_coli_pa31.yaml` passed with no LinkML issues.

## Identity and Grounding

- The record's identifier, label, rank, bacterial domain, parent taxon, and genetic code agree with the pinned NCBI source row at `data/raw/ncbitaxon_taxa.tsv:210398`.
- The lineage terminates at the asserted parent species, `NCBITaxon:562` / `Escherichia coli`, which is coherent for an NCBI strain entry named `Escherichia coli PA31`.
- The `grounding_status: EXACT` assertion is appropriate for the NCBI taxon itself.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210398` attests `NCBITaxon:1005502` as strain `Escherichia coli PA31`, parent `NCBITaxon:562`, genetic code `11`, and a `2026-09-13` NCBI snapshot.
- `data/raw/madin_taxa.tsv:270` contributes one Madin trait assertion for `NCBITaxon:1005502`.
- `data/raw/gtdb_mappings.tsv:942` maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1005502` with `skos:closeMatch` and genome count `36408`.
- `data/raw/gtdb_species.tsv:59219` shows that `GTDB:s__Escherichia_coli` is the GTDB species cluster `s__Escherichia_coli` under genus `GTDB:g__Escherichia`, with `36408` genomes.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005502`, `Escherichia coli PA31`, and `escherichia_coli_pa31` found no same-taxon auxiliary ATB or StrainInfo rows.

## Completeness

- The generated record carries the expected NCBI identity, lineage, genetic code, Madin source attestation, GTDB mapping, xref, and curation history for the three-source seed row.
- The record is over-complete semantically: it inherits species-cluster GTDB metadata onto a narrower NCBI strain node.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` is a GTDB species cluster, not a strain-level identifier for `Escherichia coli PA31`. Projecting it onto this strain as `taxonomy_mappings`, `xrefs`, a GTDB source attestation, and the exact synonym `Escherichia coli` makes the strain record look interchangeable with the entire GTDB species cluster.

## Recommended Edits

- Correct the GTDB seed or projection logic in `data/raw/gtdb_mappings.tsv` generation and `src/taxonmech/seed.py` so species-cluster mappings do not become strain-level `skos:closeMatch`, xrefs, or exact synonyms.
- After that upstream fix, regenerate this record so `GTDB:s__Escherichia_coli` is absent from `taxonomy_mappings`, `xrefs`, `synonyms`, and `source_attestations` unless a strain-specific GTDB accession supports this exact NCBI strain.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_pa31.yaml` after regeneration.
- Confirm no regenerated synonym says `Escherichia coli` is an exact synonym of the narrower `Escherichia coli PA31` strain node.

## Additional Notes

- Live NCBI and GTDB lookups were not used for this read-only review; the pinned local rows in `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
- `just validate-history` was not applicable because this review did not create a `history/` decision.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

