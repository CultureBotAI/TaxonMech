# YAML Record Review: Scedosporium apiospermum

- Verdict: pass
- Target: `data/taxa/eukaryota/scedosporium_apiospermum.yaml`
- Identifier: `NCBITaxon:563466`

## Target

Reviewed the complete 93-line YAML record for Scedosporium apiospermum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for scedosporium_apiospermum.

## Validation

- `just validate data/taxa/eukaryota/scedosporium_apiospermum.yaml` ran LinkML validation for `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saxomyces_penninicus.yaml data/taxa/eukaryota/saxophila_tyrrhenica.yaml data/taxa/eukaryota/scedosporium_apiospermum.yaml data/taxa/eukaryota/scedosporium_aurantiacum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI Taxonomy row at `data/raw/ncbitaxon_taxa.tsv:132482` has `taxon_id=NCBITaxon:563466`, `label=Scedosporium apiospermum`, `rank=SPECIES`, `parent_id=NCBITaxon:41687`, `genetic_code=1`, an empty `retired_into`, and `attested_by=gold` in the 2026-09-13 snapshot, matching the YAML identity fields.
- The seed-scope inventory contains exactly 1 row for `NCBITaxon:563466` at `data/seed_scope.tsv:56047`, matching the seeded `mapping_status` and GOLD plus NCBITAXON source attestations.
- The NCBI row contributes 2 exact synonyms, 0 broad synonyms, and 3 related synonyms, matching the 5 YAML synonym entries.
- All 16 lineage entries were checked against NCBI; no expected lineage rows were missing and no labels or ranks mismatched.
- NCBI merged-ID rows retire `NCBITaxon:1186050` into `NCBITaxon:563466`, but exact old-ID checks found no retained rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38894` reports `organism_count=2` for `NCBITaxon:563466`, matching the YAML GOLD `assertion_count`.
- Native GOLD rows for this taxon include 2 organism rows, 2 project rows, and 2 analysis rows.
- `data/raw/ncbi_type_material.tsv` contains 7 exact type-material rows for `NCBITaxon:563466`.
- BacDive contributes 0 exact rows, and local StrainInfo contributes 117 direct exact rows plus 121 exact deposit cross-references for this taxon.

## Completeness

- Generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contain 0 rows for `NCBITaxon:563466`, matching `strain_count: 0`.
- Auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` each contain 0 rows for `NCBITaxon:563466`.
- Generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` each contain 0 rows for `NCBITaxon:563466`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
