# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_sextelata.yaml`
- Taxon: `NCBITaxon:1174677` (`Morchella sextelata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1174677`, label `Morchella sextelata`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_sextelata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_septentrionalis.yaml ... morchella_sp.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58196` contains the seeded identifier with reason `attested rule: Morchella sextelata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:260863` matches the YAML parent, rank, exact synonym `Morchella sextelata M. Kuo, 2012`, and related synonym `Morchella sp. Mel-6`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:260863` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3865`, where `NCBITaxon:1174677` has `organism_count` 1.
- The native GOLD current-taxid scan returned zero organism, project, and analysis rows; an exact native organism scan across current `1174677` plus retired `746149` and `746169` also returned no rows.
- `data/raw/ncbi_type_material.tsv:11428-11429` has two holotype aliases, `F 07130403` and `F:07130403`.

## Completeness

- Exact StrainInfo has one direct record with one deposit, `ICMP 23687`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1174677`.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:746149` and `NCBITaxon:746169` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows, so those retired IDs are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The YAML GOLD assertion count follows the transformed aggregate in `data/raw/gold_organisms.tsv`; the local native JSONL exact scan did not find the row that contributed to that aggregate.
