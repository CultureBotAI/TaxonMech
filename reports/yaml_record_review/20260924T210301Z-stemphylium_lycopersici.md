# YAML Record Review: Stemphylium lycopersici

- Verdict: pass
- Target: `data/taxa/eukaryota/stemphylium_lycopersici.yaml`
- Identifier: `NCBITaxon:183478`

## Target

Reviewed the complete 126-line YAML record for Stemphylium lycopersici. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stemphylium_lycopersici`.

## Validation

- `just validate data/taxa/eukaryota/stemphylium_lycopersici.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/staurosirella_guenter_grassii.yaml data/taxa/eukaryota/steccherinum_ochraceum.yaml data/taxa/eukaryota/stellarima_microtrias.yaml data/taxa/eukaryota/stemphylium_lycopersici.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:183478`, `label: Stemphylium lycopersici`, `rank: SPECIES`, `parent: NCBITaxon:95729`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 7 exact synonyms, 0 broad synonyms, and 8 related synonyms for `NCBITaxon:183478`; the YAML carries the same 15 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:183478` in `data/seed/scope.tsv`.
- All 17 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps 6 retired IDs into `NCBITaxon:183478`: `NCBITaxon:183481`, `NCBITaxon:2005014`, `NCBITaxon:2005015`, `NCBITaxon:2005016`, `NCBITaxon:2005017`, and `NCBITaxon:2005018`. The exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:16261` reports `organism_count=3`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 3 organism rows, 3 project rows, and 3 analysis rows for `NCBITaxon:183478`, covering `CIDEFI 212`, `CIDEFI 213`, and `CIDEFI 216`.
- `data/raw/ncbi_type_material.tsv` contains 16 exact `NCBITaxon:183478` rows spanning `Stemphylium oblongum`, `S. plantaginis`, `S. pruni`, `S. pyrina`, `S. sophorae`, `S. xanthosomatis`, and `Thyrospora lycopersici` type-material designations from `typematerial.dmp`.
- Local StrainInfo records contained 15 direct exact records and 18 exact deposit placements for `NCBITaxon:183478`; the exact JSONL search found 15 records carrying `"ncbi":183478`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:183478`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:183478` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- Auxiliary bacterial source tables had no rows for this eukaryotic taxon in BactoTraits, GTDB, LPSN, Madin, or MediaDive inputs.
- Generated StrainInfo overlay tables had no target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The review ran from the detached worktree at `/private/tmp/taxonmech-codex-review`; the seeded YAML record was left unchanged.
