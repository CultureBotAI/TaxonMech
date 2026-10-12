# YAML Record Review: Anaerocolumna xylanovorans
## Target
- Path: `data/taxa/bacteria/anaerocolumna_xylanovorans.yaml`
- Identifier: `NCBITaxon:100134`
- Label: `Anaerocolumna xylanovorans`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/anaerocolumna_xylanovorans.yaml`
- PASS: `just validate-strict data/taxa/bacteria/pseudomonas_sp_br_9131.yaml data/taxa/bacteria/pseudomonas_sp_br_9133.yaml data/taxa/bacteria/sporobacterium_olearium.yaml data/taxa/bacteria/anaerocolumna_xylanovorans.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, exact synonym, authority synonyms, and four direct source families match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:100134	Anaerocolumna xylanovorans	SPECIES	NCBITaxon:1843210	11	Clostridium xylanovorans	...	ncbitaxon|lpsn|gold|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the raw rows that seed the species.
- `mapping_status: SEEDED` accurately reflects a generated seed from local NCBI, LPSN, BacDive, GOLD, and MADIN inputs.
- `parent_taxon: NCBITaxon:1843210` is represented in the lineage as `Anaerocolumna`.
- The lineage is internally coherent for an Anaerocolumna species:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Clostridia` -> `Lachnospirales` -> `Lachnospiraceae` -> `Anaerocolumna`
- `data/raw/lpsn_names.tsv` links `lpsn:794359`, `NCBITaxon:100134`, `GTDB:s__Anaerocolumna_xylanovorans`, and basionym `lpsn:775027`; the YAML carries the LPSN xref, GTDB xref, and LPSN `Clostridium xylanovorans` synonym.
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI `NAME`, LPSN `NAME`, BacDive `STRAIN`, GOLD `ORGANISM`, and MADIN `TRAIT_ASSERTION` entries.
- Local source counts agree with the top-level attestation counts: `data/raw/gold_organisms.tsv` reports two direct organisms and `data/raw/madin_taxa.tsv` reports two direct trait assertions.
- The LPSN nomenclature block matches `data/raw/lpsn_names.tsv`, including authority `(Mechichi et al. 2000) Ueki et al. 2016`, PMID `27126251`, both publication DOIs, sequence accession `INSDC:AF116920`, type strain designations `DSM-12503` and `JCM-31057`, and basionym synonym `Clostridium xylanovorans`.
- The descendant BacDive strain `bacdive:2797` is filed under `NCBITaxon:1121345`, which is a strain under `NCBITaxon:100134`; the YAML records that with `classified_as: NCBITaxon:1121345`.
- Most nested DSM 12503/JCM 31057 GOLD, GTDB, NCBI Assembly, StrainInfo, and AllTheBacteria records are backed by exact rows in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/straininfo/strain_links.tsv`, `data/straininfo/assemblies.tsv`, and `data/atb/`.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested four-source seed on `2026-09-12`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 1` is consistent with the one same-species descendant BacDive strain row.
- The record includes the local LPSN nomenclature, BacDive strain, GOLD and MADIN attestations, StrainInfo rows, AllTheBacteria assembly, and source-related genome/project/sample rows visible in the inspected raw inputs.
- No causal graphs are present in the record or required by the inspected seed evidence.

## Findings
- No blocking findings.
- Major: the generated `strains` section imports `Anaerocolumna cellulosilytica SN021` records into `Anaerocolumna xylanovorans`.
  - Evidence: `genome_assemblies`, `genome_records`, and `related_records` contain `GCA_014218335`, `GCA_014218335.1`, `img.taxon:8064407441`, `patric:433286.4`, `bioproject:PRJDB9873`, and `biosample:SAMD00229170` rows with `taxon_id: NCBITaxon:433286` and names containing `Anaerocolumna cellulosilytica SN021`.
  - Maintained owner: the BacDive/BV-BRC strain genome matching that emits `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` rows for `kgmicrobe.strain:bacdive_2797` should reject or quarantine genome links whose `taxon_id` is neither `NCBITaxon:100134` nor a descendant such as `NCBITaxon:1121345`.
- No minor findings.

## Recommended Edits
- Fix the raw strain genome matching for `kgmicrobe.strain:bacdive_2797` so `NCBITaxon:433286` / `Anaerocolumna cellulosilytica SN021` rows are not emitted under the `Anaerocolumna xylanovorans` strain.
- Re-run `scripts/seed_from_sources.py` after the raw source rows are corrected so `data/taxa/bacteria/anaerocolumna_xylanovorans.yaml` drops the cross-taxon genome, IMG, BV-BRC, BioProject, and BioSample entries.
- Add a regression check that prevents a descendant-strain rollup from importing source-related rows whose `taxon_id` is outside the target taxon's descendant set.

## Follow-up Checks
- Re-run `just validate data/taxa/bacteria/anaerocolumna_xylanovorans.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/anaerocolumna_xylanovorans.yaml`.
- Re-run the exact `NCBITaxon:433286|GCA_014218335|patric:433286.4|SAMD00229170|PRJDB9873` scan against `data/taxa/bacteria/anaerocolumna_xylanovorans.yaml` and verify no same-species `Anaerocolumna xylanovorans` record carries those cross-taxon rows.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.
