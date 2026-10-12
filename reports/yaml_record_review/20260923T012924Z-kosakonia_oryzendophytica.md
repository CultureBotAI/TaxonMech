# YAML Record Review: Kosakonia oryzendophytica
- Repository: TaxonMech
- Record: data/taxa/bacteria/kosakonia_oryzendophytica.yaml
- Started UTC: 2026-09-23T01:29:24Z
- Finished UTC: 2026-09-23T01:29:24Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/kosakonia_oryzendophytica.yaml`
- Identifier: `NCBITaxon:1005665`
- Label: `Kosakonia oryzendophytica`
- Rank: `SPECIES`
- Parent: `NCBITaxon:1330547`
- Registry row: `data/taxa/PATHS.tsv:1816`
- Scope row: `curation/seed_scope.tsv:14810`
- A pre-write `find reports/yaml_record_review ... -name '*-kosakonia_oryzendophytica.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/pseudomonas_sp_afb_9.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_sapporensis.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_tyatiensis.yaml data/taxa/bacteria/kosakonia_oryzendophytica.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/kosakonia_oryzendophytica.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, authority-derived synonym, and NCBI related synonyms agree with `data/raw/ncbitaxon_taxa.tsv:210478`.
- `data/raw/lpsn_names.tsv:30905` confirms `Kosakonia oryzendophytica` as the validly published legitimate correct LPSN species name and links the GTDB `s__Kosakonia_oryzendophytica` species row.
- The stored lineage terminates at the asserted genus `NCBITaxon:1330547` / `Kosakonia`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210478` attests `NCBITaxon:1005665` as `Kosakonia oryzendophytica`, rank `SPECIES`, parent `NCBITaxon:1330547`, genetic code `11`, NCBI aliases, and NCBI snapshot `2026-09-13`.
- `data/raw/lpsn_names.tsv:30905` contributes LPSN name `lpsn:794362`, the `(Hardoim et al. 2015) Li et al. 2016` authority, type strain `kgmicrobe.strain:LMG-26432`, and sequence accession `INSDC:JF795011`; `data/raw/lpsn_names.tsv:30065` backs the related `Enterobacter oryzendophyticus` synonym.
- `data/raw/gtdb_mappings.tsv:1006` and `data/raw/gtdb_mappings.tsv:1007` map `GTDB:s__G002886105_sp002886105` and `GTDB:s__Kosakonia_oryzendophytica` to this species as `skos:broadMatch`; `data/raw/gtdb_species.tsv:65342` and `data/raw/gtdb_species.tsv:108251` provide their 3- and 6-genome cluster sizes.
- `data/raw/bacdive_strains.tsv:63087` contributes the BacDive `REICA_082` type-strain record and culture collection IDs `kgmicrobe.strain:LMG-26432` and `kgmicrobe.strain:NCCB-100390`, also present in `data/raw/culture_collection_strains.tsv:126432` and `data/raw/culture_collection_strains.tsv:137743`.
- `data/raw/strain_assemblies.tsv:46883`, `data/raw/strain_assemblies.tsv:46884`, and `data/raw/strain_genome_records.tsv:36754` through `data/raw/strain_genome_records.tsv:36756` back the BacDive/GOLD assembly and IMG/BV-BRC genome records for `REICA_082`.
- `data/raw/strain_related_records.tsv:135206` through `data/raw/strain_related_records.tsv:135210` back the GOLD BioProject, BioSample, analysis, organism, and project related records.
- The exact, gitignore-independent scan of `data/atb` and `data/straininfo` found the ATB assembly, ATB strain/genome links, and StrainInfo deposit links for the same BacDive strain at `data/atb/assemblies.tsv:3917`, `data/atb/strain_links.tsv:1645`, `data/atb/genome_links.tsv:7179`, `data/atb/genome_links.tsv:7180`, `data/straininfo/strain_links.tsv:27813`, and `data/straininfo/strain_links.tsv:27814`.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB mappings, NCBI/LPSN synonyms, xrefs, BacDive type strain, BacDive/GOLD assemblies and genome records, ATB assembly link, StrainInfo deposit links, source attestations, and seed history are complete for the pinned local rows.
- `GTDB:s__G002886105_sp002886105` is retained as a taxonomy mapping but not an `xref`, which matches its pooled broad-match status.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/kosakonia_oryzendophytica.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
