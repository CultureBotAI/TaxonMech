# YAML Record Review: Podila minutissima

- Verdict: pass
- Target: `data/taxa/eukaryota/podila_minutissima.yaml`
- Identifier: `NCBITaxon:64525`

## Target

Reviewed the complete 81-line YAML record for `Podila minutissima`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podila_minutissima`.

## Validation

- `just validate data/taxa/eukaryota/podila_minutissima.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podila_epigama.yaml data/taxa/eukaryota/podila_horticola.yaml data/taxa/eukaryota/podila_humilis.yaml data/taxa/eukaryota/podila_minutissima.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8183` is the exact retained NCBITaxon row for `NCBITaxon:64525`: label `Podila minutissima`, rank `SPECIES`, parent `NCBITaxon:2779937`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53093` contains the seeded in-scope row for `NCBITaxon:64525` with the reason `attested rule: Podila minutissima, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:979715` to `NCBITaxon:64525`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:40326` is the aggregate GOLD row for `NCBITaxon:64525` and reports `organism_count=7`, matching the YAML GOLD source attestation.
- Native GOLD has five exact organism rows, six linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has four exact culture-from-syntype rows for `NCBITaxon:64525`, all filed under `Mortierella minutissima var. dubia`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 14 exact local JSONL records covering 16 deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:64525`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:64525`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The generated GOLD source attestation uses the aggregate GOLD row rather than the smaller local native GOLD organism row count.
