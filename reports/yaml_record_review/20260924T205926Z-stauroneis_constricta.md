# YAML Record Review: Stauroneis constricta

- Verdict: pass
- Target: `data/taxa/eukaryota/stauroneis_constricta.yaml`
- Identifier: `NCBITaxon:265584`

## Target

Reviewed the complete 69-line YAML record for Stauroneis constricta. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stauroneis_constricta`.

## Validation

- `just validate data/taxa/eukaryota/stauroneis_constricta.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_sirachaensis.yaml data/taxa/eukaryota/starmerella_stellata.yaml data/taxa/eukaryota/starmerella_vitae.yaml data/taxa/eukaryota/stauroneis_constricta.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:265584`, `label: Stauroneis constricta`, `rank: SPECIES`, `parent: NCBITaxon:265583`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:265584`; the YAML carries the same related synonym and no extra exact or broad synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:265584` in `data/seed/scope.tsv`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:265584` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:24381` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0368876`; no GOLD project or analysis rows used `NCBITaxon:265584`.
- No exact type-material rows for `NCBITaxon:265584` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 1 direct exact record and 1 exact deposit placement for `NCBITaxon:265584`; the exact JSONL search found 1 record carrying `"ncbi":265584`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:265584`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:265584` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
