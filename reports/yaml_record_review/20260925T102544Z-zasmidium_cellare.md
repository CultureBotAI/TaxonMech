# YAML Record Review: Zasmidium cellare

- Verdict: pass
- Target: `data/taxa/eukaryota/zasmidium_cellare.yaml`
- Identifier: `NCBITaxon:395010`

## Target

Reviewed the complete 90-line YAML record for Zasmidium cellare. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zasmidium_cellare.

## Validation

- `just validate data/taxa/eukaryota/zasmidium_cellare.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zasmidium_cellare.yaml data/taxa/eukaryota/zasmidium_citrigriseum.yaml data/taxa/eukaryota/zasmidium_sp.yaml data/taxa/eukaryota/zhuliangomyces_illinitus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:84067` is `NCBITaxon:395010`, `Zasmidium cellare`, rank `SPECIES`, parent `NCBITaxon:395590`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zasmidium cellare` entry, at `data/curated/seed_scope.tsv:55496`.
- NCBI synonym counts are 2 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 4 synonym entries from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:395010`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:34278` reports `organism_count` 1 for `NCBITaxon:395010`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 15 exact rows for `NCBITaxon:395010`: 13 `culture from neotype` rows covering `ATCC 36951`, `IFO 4862`, `IMI 044943`, `IMI 44943`, `LCP 52.402`, `LSHB BB274`, and `MUCL 10089`, plus two `neotype` variants for `CBS 146.36`.
- BacDive has 0 exact local rows for `NCBITaxon:395010`.
- StrainInfo has 5 exact direct strain rows and 14 exact deposit matches for `NCBITaxon:395010`; all deposit matches are on the same five direct records, siIDs 74392, 107128, 111766, 183078, and 199792.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables all have 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
