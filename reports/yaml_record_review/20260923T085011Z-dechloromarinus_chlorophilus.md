# YAML Record Review: Dechloromarinus chlorophilus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/dechloromarinus_chlorophilus.yaml
- Started UTC: 2026-09-23T08:48:51Z
- Finished UTC: 2026-09-23T08:50:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100761 |
| label | Dechloromarinus chlorophilus |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:100668 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/` and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: all 62 lines of `data/taxa/bacteria/dechloromarinus_chlorophilus.yaml` were read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-dechloromarinus_chlorophilus.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks found the expected NCBI, GOLD, and Madin rows for `NCBITaxon:100761` across `data/raw/`, `data/atb/`, and `data/straininfo/`. No same-taxon LPSN, BacDive, AllTheBacteria, StrainInfo, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/dechloromarinus_chlorophilus.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/dechloromarinus_chlorophilus.yaml data/taxa/bacteria/ochrobactrum_sp_hob2.yaml data/taxa/bacteria/salimicrobium_sp_hob6.yaml data/taxa/bacteria/salinicoccus_sp_hob5.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species `NCBITaxon:100761`. Its label, `SPECIES` rank, parent `NCBITaxon:100668`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:17320`.

The root-first lineage through `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Gammaproteobacteria incertae sedis`, and `Dechloromarinus` is consistent with the corresponding pinned NCBI inventory rows.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17320` supports the NCBI identifier, label, rank, parent, bacterial genetic code, exact NCBI synonym `'Dechloromarinus chlorophilus'`, and raw source list `ncbitaxon|gold|madin_etal`.
- `source_attestations[0]` is correctly limited to the NCBITAXON name assertion from `data/raw/ncbitaxon_taxa.tsv:17320`.
- `data/raw/gold_organisms.tsv:186` supports the GOLD source attestation with one `ORGANISM`.
- `data/raw/madin_taxa.tsv:379` supports the Madin source attestation with two `TRAIT_ASSERTION` rows.
- No evidence is over-applied from GTDB, LPSN, BacDive, MediaDive, AllTheBacteria, StrainInfo, or NCBI type-material rows.

## Completeness

The record is complete for the source evidence currently attached to this species. It includes the NCBI exact synonym and the source-attestation counts from NCBI, GOLD, and Madin, and it correctly omits nomenclature, taxonomy mappings, strain records, genome links, and a causal graph because exact gitignore-independent searches over the scoped local source files found no same-taxon auxiliary rows beyond those three source inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories later add GTDB, LPSN, BacDive, ATB, StrainInfo, or NCBI type-material evidence for `NCBITaxon:100761`, rerun `just seed-canary NCBITaxon:100761`, inspect `data/taxa/bacteria/dechloromarinus_chlorophilus.yaml`, and rerun `just validate-strict data/taxa/bacteria/dechloromarinus_chlorophilus.yaml`.

## Additional Notes

- External live NCBI Taxonomy, GOLD, and Madin lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
