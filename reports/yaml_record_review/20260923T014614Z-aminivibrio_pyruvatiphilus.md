# YAML Record Review: Aminivibrio pyruvatiphilus
- Repository: TaxonMech
- Record: data/taxa/bacteria/aminivibrio_pyruvatiphilus.yaml
- Started UTC: 2026-09-23T01:46:14Z
- Finished UTC: 2026-09-23T01:46:14Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/aminivibrio_pyruvatiphilus.yaml`
- Identifier: `NCBITaxon:1005740`
- Label: `Aminivibrio pyruvatiphilus`
- Rank: `SPECIES`
- Parent: `NCBITaxon:1427172`
- Registry row: `data/taxa/PATHS.tsv:1834`
- Scope row: `curation/seed_scope.tsv:4026`
- A pre-write `find reports/yaml_record_review ... -name '*-aminivibrio_pyruvatiphilus.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/bacteroidetes_bacterium_6e.yaml data/taxa/bacteria/aminivibrio_pyruvatiphilus.yaml data/taxa/bacteria/saprospiraceae_bacterium_kmm_9006.yaml data/taxa/bacteria/bradyrhizobium_sp_semia_6002.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/aminivibrio_pyruvatiphilus.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, NCBI related synonyms, LPSN nomenclature, and GTDB species mapping agree with the pinned NCBI, LPSN, and GTDB rows.
- `data/raw/lpsn_names.tsv:28028` marks `Aminivibrio pyruvatiphilus` as legitimate, validly published, and the correct name, and links it to `NCBITaxon:1005740`, `GTDB:s__Aminivibrio_pyruvatiphilus`, DSM 25964, and JCM 18417.
- The stored lineage terminates at the asserted genus `NCBITaxon:1427172` / `Aminivibrio`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210498` attests `NCBITaxon:1005740` as `Aminivibrio pyruvatiphilus`, rank `SPECIES`, parent `NCBITaxon:1427172`, genetic code `11`, two related synonyms, eight attesting sources, and NCBI snapshot `2026-09-13`.
- `data/raw/gtdb_mappings.tsv:1013` maps `GTDB:s__Aminivibrio_pyruvatiphilus` to `NCBITaxon:1005740` as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:8962` confirms the GTDB species has two genomes.
- `data/raw/bacdive_strains.tsv:24301` contributes BacDive strain `bacdive:24744` for isolate `4F6E` with DSM 25964 and JCM 18417 culture collection IDs; `data/raw/mediadive_taxa.tsv:33`, `data/raw/madin_taxa.tsv:339`, and `data/raw/bactotraits_taxa.tsv:22` back the MediaDive, Madin, and BactoTraits source-attestation counts.
- `data/raw/gold_organisms.tsv:150` contributes three GOLD organism assertions; `data/raw/strain_genome_records.tsv:93006` through `data/raw/strain_genome_records.tsv:93012`, `data/raw/strain_assemblies.tsv:115794` through `data/raw/strain_assemblies.tsv:115802`, and `data/raw/strain_related_records.tsv:333584` through `data/raw/strain_related_records.tsv:333605` back the generated GTDB, GOLD, BV-BRC, NCBI Assembly, and related-record links.
- Exact, gitignore-independent scans of `data/atb` and `data/straininfo` found same-taxon rows for `NCBITaxon:1005740` in the AllTheBacteria assembly/link tables and StrainInfo assembly/link tables, all tying the generated strain material to `kgmicrobe.strain:DSM-25964`.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB species mapping, NCBI synonyms, BacDive type strain, culture collection IDs, strain assemblies, genome records, related records, ATB genome, StrainInfo evidence, source attestations, and seed history are complete for the local source rows.
- The `GTDB:s__Aminivibrio_pyruvatiphilus` mapping is species-level and is also asserted by LPSN for this species, so it is not the strain-level species-cluster projection issue seen elsewhere.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/aminivibrio_pyruvatiphilus.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
