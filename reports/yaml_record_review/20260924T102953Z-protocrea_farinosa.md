# YAML Record Review: Protocrea farinosa

- Verdict: pass
- Target: `data/taxa/eukaryota/protocrea_farinosa.yaml`
- Identifier: `NCBITaxon:399278`

## Target

Reviewed the complete 87-line YAML record for `Protocrea farinosa`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protocrea_farinosa`.

## Validation

- `just validate data/taxa/eukaryota/protocrea_farinosa.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/proteomonas_sulcata.yaml data/taxa/eukaryota/protoceratium_reticulatum.yaml data/taxa/eukaryota/protocrea_farinosa.yaml data/taxa/eukaryota/protocrea_pallida.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:85384` is the exact retained NCBITaxon row for `NCBITaxon:399278`: label `Protocrea farinosa`, rank `SPECIES`, parent `NCBITaxon:555849`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55516` contains the seeded in-scope row for `NCBITaxon:399278` with the reason `attested rule: Protocrea farinosa, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:555850` to `NCBITaxon:399278`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:34408` is the aggregate GOLD row for `NCBITaxon:399278` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:203517` through `data/raw/ncbi_type_material.tsv:203522` provide six exact type-material aliases, split between four `culture from epitype` rows and two `epitype` rows.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:399278`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:399278`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

`NCBITaxon:555850` appears only as a retired old ID in `data/raw/ncbi_merged_ids.tsv` and not as a retained row in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of a generated `replaces` value. The GOLD source attestation is backed by the aggregate GOLD row; exact native GOLD organism, project, and analysis scans returned 0 rows for `NCBITaxon:399278`.
