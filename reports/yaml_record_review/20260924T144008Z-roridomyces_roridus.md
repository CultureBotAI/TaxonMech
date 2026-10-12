# YAML Record Review: Roridomyces roridus

- Verdict: pass
- Target: `data/taxa/eukaryota/roridomyces_roridus.yaml`
- Identifier: `NCBITaxon:1738132`

## Target

Reviewed the complete 90-line YAML record for Roridomyces roridus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for roridomyces_roridus.

## Validation

- `just validate data/taxa/eukaryota/roridomyces_roridus.yaml` ran LinkML validation against `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/rogerpetersonia_torreyae.yaml data/taxa/eukaryota/roridomyces_roridus.yaml data/taxa/eukaryota/rosellinia_corticium.yaml data/taxa/eukaryota/rosellinia_necatrix.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` retains `NCBITaxon:1738132` at line 454237 with label `Roridomyces roridus`, rank `SPECIES`, parent `NCBITaxon:230760`, genetic code `1`, and an empty `retired_into` field.
- `data/raw/ncbitaxon_seed_scope.tsv` includes the target at line 61178 with reason `attested rule: Roridomyces roridus, 2 sources incl. NCBI`.
- The YAML preserves the NCBI synonym columns exactly: 2 exact synonyms, 4 related synonyms, and 0 broad synonyms.
- The 14 YAML lineage entries all match the NCBI snapshot; no lineage entries were missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:182005` to `NCBITaxon:1738132` at line 29129. An exact retained-row search of `data/raw/ncbitaxon_taxa.tsv` found no `NCBITaxon:182005` row, so no generated `replaces` value is expected.

## Evidence

- The GOLD source attestation matches the aggregate `data/raw/gold_organisms.tsv` row at line 15095 for `NCBITaxon:1738132`, whose `organism_count` is `1`.
- Native GOLD support was 1 analysis row, 1 organism row, and 2 project rows; the generated YAML follows the aggregate organism count.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:1738132`, matching the absence of type-material-derived strain entries.
- BacDive had 0 exact rows for `NCBITaxon:1738132`; StrainInfo had 2 direct exact JSONL rows and 2 exact deposits, but no local generated StrainInfo overlay rows materialized for this target.

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
