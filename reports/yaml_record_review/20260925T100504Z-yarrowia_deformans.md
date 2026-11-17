# YAML Record Review: Yarrowia deformans

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_deformans.yaml`
- Identifier: `NCBITaxon:1608523`

## Target

Reviewed the complete 84-line YAML record for Yarrowia deformans. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_deformans.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_deformans.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_alimentaria.yaml data/taxa/eukaryota/yarrowia_brassicae.yaml data/taxa/eukaryota/yarrowia_bubula.yaml data/taxa/eukaryota/yarrowia_deformans.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:415511` is `NCBITaxon:1608523`, `Yarrowia deformans`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia deformans` entry, at `data/curated/seed_scope.tsv:60564`.
- NCBI synonym counts are 2 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves all 5 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 1 redirect into `NCBITaxon:1608523`: `NCBITaxon:184778`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:13026` reports `organism_count` 2 for `NCBITaxon:1608523`, matching the YAML GOLD assertion count of 2.
- Native GOLD evidence has 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 16 exact rows for `NCBITaxon:1608523`: `culture from type material` designation variants for `ATCC 22969`, `CBS 2071`, `DBVPG 6137`, `IFO 1601`, `JCM 1694`, `NRRL Y-321`, and `VKM Y-1444`.
- BacDive has 0 exact local rows for `NCBITaxon:1608523`.
- StrainInfo has 8 exact direct strain rows and 12 exact deposit matches for `NCBITaxon:1608523`; two Yarrowia lipolytica records, siIDs 63304 and 118853, each contribute one deformans deposit match without changing the target identity.

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
