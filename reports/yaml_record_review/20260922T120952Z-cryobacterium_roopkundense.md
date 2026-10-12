# YAML Record Review: Cryobacterium roopkundense
## Target
- Path: `data/taxa/bacteria/cryobacterium_roopkundense.yaml`
- Identifier: `NCBITaxon:1001240`
- Label: `Cryobacterium roopkundense`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/cryobacterium_roopkundense.yaml`
- PASS: `just validate-strict data/taxa/bacteria/cryobacterium_roopkundense.yaml data/taxa/bacteria/exiguobacterium_sp_sbh81.yaml data/taxa/bacteria/pseudomonas_sp_br_9130.yaml data/taxa/bacteria/pseudomonas_sp_br_9132.yaml`
  - `files scanned: 4`
  - `files with ERROR: 0`
  - `total ERROR rows: 0`
- SKIPPED: `just validate-history`
  - This was a read-only review of a generated record and did not add a `history/` decision.
- SKIPPED: `just verify-corpus`
  - The record was unchanged; full-corpus verification was not rerun for this four-record review batch.
- NOT APPLICABLE: `just validate-products`
  - The record has no `causal_graphs`.

## Identity and Grounding
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, authority synonym, and six-source coverage match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1001240	Cryobacterium roopkundense	SPECIES	NCBITaxon:69578	11		Cryobacterium roopkundense Reddy et al. 2010		ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the raw rows that seed the species.
- `mapping_status: SEEDED` accurately reflects a generated seed from local NCBI, LPSN, GTDB, BacDive, GOLD, and MADIN inputs.
- `parent_taxon: NCBITaxon:69578` is represented in the lineage as `Cryobacterium`.
- The lineage is internally coherent for a Cryobacterium species:
  - `Bacteria` -> `Bacillati` -> `Actinomycetota` -> `Actinomycetes` -> `Micrococcales` -> `Microbacteriaceae` -> `Cryobacterium`
- `data/raw/lpsn_names.tsv` links `lpsn:788461`, `NCBITaxon:1001240`, and `GTDB:s__Cryobacterium_roopkundense`; the YAML carries both xrefs and the GTDB `skos:closeMatch` with the expected two-genome count.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI `NAME`, LPSN `NAME`, GTDB `GENOME`, BacDive `STRAIN`, GOLD `ORGANISM`, and MADIN `TRAIT_ASSERTION` entries.
- Local source counts agree with the attestation counts:
  - `data/raw/gtdb_mappings.tsv` reports `genome_count: 2`.
  - `data/raw/gold_organisms.tsv` reports `2` organisms.
  - `data/raw/madin_taxa.tsv` reports `11` trait assertions.
  - `data/raw/bacdive_strains.tsv` contains one strain row for `kgmicrobe.strain:bacdive_7304`.
- The LPSN nomenclature block matches `data/raw/lpsn_names.tsv`, including authority `Reddy et al. 2010`, all three publication IDs, sequence accession `INSDC:EF467640`, and type strain designations `DSM-21065` and `JCM-15131`.
- `data/raw/ncbi_merged_ids.tsv` contains old `NCBITaxon:1001241` and `NCBITaxon:1001242` identifiers merged into `NCBITaxon:1001240`; the YAML correctly uses the current NCBITaxon identifier.
- The nested `strain_assemblies`, `strain_genome_records`, and `strain_related_records` entries for BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, IMG, BioProject, BioSample, GOLD analysis, GOLD organism, GOLD project, and StrainInfo are backed by exact rows in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/strain_links.tsv`.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested six-source seed on `2026-09-12`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 1` is consistent with the one same-taxon BacDive strain row.
- The record includes the local LPSN nomenclature, GTDB species mapping, BacDive strain, GOLD and MADIN attestations, StrainInfo related records, and source-related genome/project/sample rows visible in the inspected raw inputs.
- No causal graphs are present in the record or required by the inspected seed evidence.

## Findings
- No blocking findings.
- No major findings.
- No minor findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds or removes assemblies, GTDB genomes, GOLD organisms, MADIN trait assertions, or LPSN nomenclature for `NCBITaxon:1001240`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
