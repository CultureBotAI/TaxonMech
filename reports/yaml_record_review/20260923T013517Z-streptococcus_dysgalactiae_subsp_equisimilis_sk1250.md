# YAML Record Review: Streptococcus dysgalactiae subsp. equisimilis SK1250
- Repository: TaxonMech
- Record: data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml
- Started UTC: 2026-09-23T01:35:17Z
- Finished UTC: 2026-09-23T01:35:17Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml`
- Identifier: `NCBITaxon:1005706`
- Label: `Streptococcus dysgalactiae subsp. equisimilis SK1250`
- Rank: `STRAIN`
- Parent: `NCBITaxon:119602`
- Registry row: `data/taxa/PATHS.tsv:1821`
- Scope row: `curation/seed_scope.tsv:26032`
- A pre-write `find reports/yaml_record_review ... -name '*-streptococcus_dysgalactiae_subsp_equisimilis_sk1250.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml data/taxa/bacteria/pseudanabaena_belizensis.yaml data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml data/taxa/bacteria/komvophoron_apiculatum.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, and NCBI strain synonyms agree with `data/raw/ncbitaxon_taxa.tsv:210483`.
- The stored lineage terminates at the asserted parent subspecies `NCBITaxon:119602` / `Streptococcus dysgalactiae subsp. equisimilis`.
- `grounding_status: EXACT` is appropriate for the NCBI strain taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210483` attests `NCBITaxon:1005706` as `Streptococcus dysgalactiae subsp. equisimilis SK1250`, rank `STRAIN`, parent `NCBITaxon:119602`, genetic code `11`, NCBI aliases, and NCBI snapshot `2026-09-13`.
- `data/raw/madin_taxa.tsv:338` contributes one Madin trait assertion for `NCBITaxon:1005706`.
- `data/raw/gtdb_mappings.tsv:1012` maps `GTDB:s__Streptococcus_dysgalactiae` to `NCBITaxon:1005706` as `skos:closeMatch`.
- `data/raw/gtdb_species.tsv:168765` identifies `GTDB:s__Streptococcus_dysgalactiae` as a 268-genome GTDB species cluster.
- `data/raw/gold_organisms.tsv:147` contributes one GOLD organism; `data/raw/strain_assemblies.tsv:59471`, `data/raw/strain_genome_records.tsv:46084`, and `data/raw/strain_related_records.tsv:185793` through `data/raw/strain_related_records.tsv:185797` back the generated GOLD assembly, genome, BioProject, BioSample, analysis, organism, and project links for `SK1250`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005706`, `Streptococcus dysgalactiae subsp. equisimilis SK1250`, or `streptococcus_dysgalactiae_subsp_equisimilis_sk1250`.

## Completeness

- The generated NCBI identity, lineage, NCBI synonyms, Madin attestation, GOLD attestation, source attestations, and seed history are complete for the local source rows.
- The GTDB mapping and synonym material are present but belong to the broader `Streptococcus dysgalactiae` species cluster, not this subspecies-level strain.

## Findings

- **Major:** the record represents `GTDB:s__Streptococcus_dysgalactiae`, a GTDB species-cluster ID, as a close match, xref, exact synonym source, and genome-count attestation for NCBI strain `Streptococcus dysgalactiae subsp. equisimilis SK1250`. A species cluster with 268 genomes should not be attached as equivalent to this single strain.

## Recommended Edits

- Repair the GTDB mapping source or the `src/taxonmech/seed.py` projection so species clusters are not emitted onto strain records.
- Regenerate `data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml` after the shared fix and confirm that `GTDB:s__Streptococcus_dysgalactiae` is gone from `taxonomy_mappings`, `source_attestations`, `synonyms`, and `xrefs`.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml` after regeneration.
- Re-run an exact source scan for `NCBITaxon:1005706` to confirm no strain-specific GTDB source row has replaced the species-cluster row.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
