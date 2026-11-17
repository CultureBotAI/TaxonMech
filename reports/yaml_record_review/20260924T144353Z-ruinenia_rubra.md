# YAML Record Review: Ruinenia rubra

- Verdict: pass
- Target: `data/taxa/eukaryota/ruinenia_rubra.yaml`
- Identifier: `NCBITaxon:4986`

## Target

Reviewed the complete 81-line YAML record for Ruinenia rubra. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ruinenia_rubra.

## Validation

- `just validate data/taxa/eukaryota/ruinenia_rubra.yaml` ran LinkML validation against `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/rostrohypoxylon_terebratum.yaml data/taxa/eukaryota/rozella_allomycis.yaml data/taxa/eukaryota/ruinenia_rubra.yaml data/taxa/eukaryota/russula_abietina.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` retains `NCBITaxon:4986` at line 2173 with label `Ruinenia rubra`, rank `SPECIES`, parent `NCBITaxon:1798879`, genetic code `1`, and an empty `retired_into` field.
- `data/raw/ncbitaxon_seed_scope.tsv` includes the target at line 51899 with reason `attested rule: Ruinenia rubra, 2 sources incl. NCBI`.
- The YAML preserves the NCBI synonym columns exactly: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- The 12 YAML lineage entries all match the NCBI snapshot; no lineage entries were missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:86681` to `NCBITaxon:4986` at line 97088. An exact retained-row search of `data/raw/ncbitaxon_taxa.tsv` found no `NCBITaxon:86681` row, so no generated `replaces` value is expected.

## Evidence

- The GOLD source attestation matches the aggregate `data/raw/gold_organisms.tsv` row at line 37267 for `NCBITaxon:4986`, whose `organism_count` is `1`.
- Native GOLD support was 0 analysis rows, 0 organism rows, and 0 project rows; the generated YAML follows the aggregate organism count.
- `data/raw/ncbi_type_material.tsv` has 6 exact rows for `NCBITaxon:4986` at lines 224377-224382, all naming `Ballistosporomyces ruber` type material.
- BacDive had 0 exact rows for `NCBITaxon:4986`; StrainInfo had 2 direct exact JSONL rows and 8 exact deposits, but no local generated StrainInfo overlay rows materialized for this target.

## Completeness

- Generated raw strain tables had 0 exact rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source scans all returned 0 exact rows across `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 exact rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No YAML edits were made during this read-only generated-record review.
