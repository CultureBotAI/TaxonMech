# YAML Record Review: Kosakonia oryziphila
- Repository: TaxonMech
- Record: data/taxa/bacteria/kosakonia_oryziphila.yaml
- Started UTC: 2026-09-23T01:32:39Z
- Finished UTC: 2026-09-23T01:32:39Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/kosakonia_oryziphila.yaml`
- Identifier: `NCBITaxon:1005667`
- Label: `Kosakonia oryziphila`
- Rank: `SPECIES`
- Parent: `NCBITaxon:1330547`
- Registry row: `data/taxa/PATHS.tsv:1817`
- Scope row: `curation/seed_scope.tsv:14811`
- A pre-write `find reports/yaml_record_review ... -name '*-kosakonia_oryziphila.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/kosakonia_oryziphila.yaml data/taxa/bacteria/propionibacterium_sp_cc003_hc2.yaml data/taxa/bacteria/streptococcus_oralis_sk255.yaml data/taxa/bacteria/streptococcus_infantis_sk1076.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/kosakonia_oryziphila.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, authority-derived synonym, and NCBI related synonyms agree with `data/raw/ncbitaxon_taxa.tsv:210479`.
- `data/raw/lpsn_names.tsv:30904` confirms `Kosakonia oryziphila` as the validly published legitimate correct LPSN species name and links the GTDB `s__Kosakonia_oryziphila` species row.
- The stored lineage terminates at the asserted genus `NCBITaxon:1330547` / `Kosakonia`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210479` attests `NCBITaxon:1005667` as `Kosakonia oryziphila`, rank `SPECIES`, parent `NCBITaxon:1330547`, genetic code `11`, NCBI aliases, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv:30904` contributes LPSN name `lpsn:794361`, the `(Hardoim et al. 2015) Li et al. 2016` authority, type strain `kgmicrobe.strain:LMG-26429`, and sequence accession `INSDC:JF795013`; `data/raw/lpsn_names.tsv:30066` backs the related `Enterobacter oryziphilus` synonym.
- `data/raw/gtdb_mappings.tsv:1008` maps `GTDB:s__Kosakonia_oryziphila` to this species as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:108252` provides its one-genome cluster size.
- `data/raw/bacdive_strains.tsv:63086` contributes the BacDive `REICA_142` type-strain record and culture collection IDs `kgmicrobe.strain:LMG-26429` and `kgmicrobe.strain:NCCB-100393`, also present in `data/raw/culture_collection_strains.tsv:126431` and `data/raw/culture_collection_strains.tsv:137744`.
- `data/raw/strain_assemblies.tsv:46881`, `data/raw/strain_assemblies.tsv:46882`, and `data/raw/strain_genome_records.tsv:36751` through `data/raw/strain_genome_records.tsv:36753` back the BacDive/GOLD assembly and IMG/BV-BRC genome records for `REICA_142`.
- `data/raw/strain_related_records.tsv:135201` through `data/raw/strain_related_records.tsv:135205` back the GOLD BioProject, BioSample, analysis, organism, and project related records.
- The exact, gitignore-independent scan of `data/atb` and `data/straininfo` found the ATB assembly, ATB strain/genome links, and StrainInfo deposit links for the same BacDive strain at `data/atb/assemblies.tsv:3916`, `data/atb/strain_links.tsv:1644`, `data/atb/genome_links.tsv:7177`, `data/atb/genome_links.tsv:7178`, `data/straininfo/strain_links.tsv:27811`, and `data/straininfo/strain_links.tsv:27812`.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB mapping, NCBI/LPSN synonyms, xrefs, BacDive type strain, BacDive/GOLD assemblies and genome records, ATB assembly link, StrainInfo deposit links, source attestations, and seed history are complete for the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/kosakonia_oryziphila.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
