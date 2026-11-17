# YAML Record Review: Azospirillum sp. TTI

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/azospirillum_sp_tti.yaml
- Started UTC: 2026-09-23T08:51:24Z
- Finished UTC: 2026-09-23T08:52:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100762 |
| label | Azospirillum sp. TTI |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2630922 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/` and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: all 59 lines of `data/taxa/bacteria/azospirillum_sp_tti.yaml` were read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-azospirillum_sp_tti.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks found the expected NCBI and Madin rows for `NCBITaxon:100762` across `data/raw/`, `data/atb/`, and `data/straininfo/`. No same-taxon LPSN, GTDB, BacDive, AllTheBacteria, StrainInfo, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/azospirillum_sp_tti.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/stenotrophomonas_sp_hob1.yaml data/taxa/bacteria/streptomyces_sp_aoa1.yaml data/taxa/bacteria/azospirillum_sp_tti.yaml data/taxa/bacteria/dechloromonas_sp_cl.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species placeholder `NCBITaxon:100762`. Its label, `SPECIES` rank, parent `NCBITaxon:2630922`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:17321`.

The root-first lineage through `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Rhodospirillales`, `Azospirillaceae`, `Azospirillum`, and `unclassified Azospirillum` is consistent with the corresponding pinned NCBI inventory rows.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17321` supports the NCBI identifier, label, rank, parent, bacterial genetic code, and raw source list `ncbitaxon|madin_etal`.
- `data/raw/madin_taxa.tsv:380` supports the Madin source attestation with five `TRAIT_ASSERTION` rows.
- No evidence is over-applied from GTDB, LPSN, BacDive, GOLD, MediaDive, AllTheBacteria, StrainInfo, or NCBI type-material rows.

## Completeness

The record is complete for the source evidence currently attached to this placeholder. It includes the source-attestation counts from NCBI and Madin, and it correctly omits synonyms, nomenclature, taxonomy mappings, strain records, genome links, and a causal graph because exact gitignore-independent searches over the scoped local source files found no same-taxon auxiliary rows beyond those two source inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories later add GTDB, LPSN, BacDive, ATB, StrainInfo, or NCBI type-material evidence for `NCBITaxon:100762`, rerun `just seed-canary NCBITaxon:100762`, inspect `data/taxa/bacteria/azospirillum_sp_tti.yaml`, and rerun `just validate-strict data/taxa/bacteria/azospirillum_sp_tti.yaml`.

## Additional Notes

- External live NCBI Taxonomy and Madin lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
