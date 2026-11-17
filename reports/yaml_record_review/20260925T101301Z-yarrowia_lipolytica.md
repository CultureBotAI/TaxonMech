# YAML Record Review: Yarrowia lipolytica

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_lipolytica.yaml`
- Identifier: `NCBITaxon:4952`

## Target

Reviewed the complete 85-line YAML record for Yarrowia lipolytica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_lipolytica.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_lipolytica.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_lipolytica.yaml data/taxa/eukaryota/yarrowia_osloensis.yaml data/taxa/eukaryota/yarrowia_phangngaensis.yaml data/taxa/eukaryota/yarrowia_porcina.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:2159` is `NCBITaxon:4952`, `Yarrowia lipolytica`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia lipolytica` entry, at `data/curated/seed_scope.tsv:51890`.
- NCBI synonym counts are 3 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 5 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:4952`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:37203` reports `organism_count` 267 for `NCBITaxon:4952`, matching the YAML GOLD assertion count of 267.
- Native GOLD evidence has 227 organism rows, 504 project rows, and 17 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 17 exact rows for `NCBITaxon:4952`: five `culture from type material` variants for `CBS 6124` and `NRRL YB-423`, plus 12 `type material` variants for `ATCC 18942`, `DBVPG 6053`, `IFO 1548`, `JCM 2320`, and `JCM 8060`.
- BacDive has 0 exact local rows for `NCBITaxon:4952`.
- StrainInfo has 396 exact direct strain rows and 597 exact deposit matches for `NCBITaxon:4952`.

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
