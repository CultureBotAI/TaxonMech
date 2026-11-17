# YAML Record Review: Scytalidium lignicola

- Verdict: pass
- Target: `data/taxa/eukaryota/scytalidium_lignicola.yaml`
- Identifier: `NCBITaxon:5539`

## Target

Reviewed the complete 75-line YAML record for Scytalidium lignicola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for scytalidium_lignicola.

## Validation

- `just validate data/taxa/eukaryota/scytalidium_lignicola.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/scrippsiella_trochoidea.yaml data/taxa/eukaryota/scutellospora_calospora.yaml data/taxa/eukaryota/scyphosphaera_apsteinii.yaml data/taxa/eukaryota/scytalidium_lignicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:2461` has `taxon_id=NCBITaxon:5539`, `label=Scytalidium lignicola`, `rank=SPECIES`, `parent_id=NCBITaxon:5538`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:5539` at `data/seed_scope.tsv:52029`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 0 exact synonyms, 0 broad synonyms, and 1 related synonym, matching the 1 YAML synonym entry.
- All 14 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- `data/raw/ncbi_merged_ids.tsv:92175` maps old ID `NCBITaxon:685283` into `NCBITaxon:5539`, and an ignored-file-inclusive exact scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38667` reports `organism_count=1` for `NCBITaxon:5539`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 1 organism row, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` contains 10 exact type-material rows for `NCBITaxon:5539`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 54 direct exact rows plus 63 exact deposit cross-references for this taxon. The exact JSONL scan also found 1 non-direct record, `SI-ID 240630` for `Neofusicoccum mangiferae`, carrying a deposit cross-reference to `NCBITaxon:5539`.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:5539`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:5539`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:5539`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
