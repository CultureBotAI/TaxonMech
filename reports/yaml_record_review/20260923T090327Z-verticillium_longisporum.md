# YAML Record Review: Verticillium longisporum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/verticillium_longisporum.yaml
- Started UTC: 2026-09-23T09:02:15Z
- Finished UTC: 2026-09-23T09:03:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100787 |
| label | Verticillium longisporum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1036719 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/eukaryota/verticillium_longisporum.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-verticillium_longisporum.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact anchored `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found the expected NCBI, GOLD, merged-ID, and NCBI type-material rows for `NCBITaxon:100787` / `Verticillium longisporum`; no same-taxon GTDB, LPSN, BacDive, AllTheBacteria, StrainInfo, Madin, MediaDive, or BactoTraits row was found. |
| `just validate data/taxa/eukaryota/verticillium_longisporum.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/verticillium_longisporum.yaml data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml data/taxa/bacteria/chlamydia_trachomatis_rc_j_971.yaml data/taxa/bacteria/curtobacterium_sp_tn4w_19.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI fungal species `NCBITaxon:100787`, with label `Verticillium longisporum`, direct parent `NCBITaxon:1036719`, and eukaryotic genetic code `1` matching `data/raw/ncbitaxon_taxa.tsv:17326`.

The root-first lineage is internally coherent for a fungal record. It reaches `Verticillium` through `Eukaryota`, `Opisthokonta`, `Fungi`, `Dikarya`, `Ascomycota`, `saccharomyceta`, `Pezizomycotina`, `leotiomyceta`, `sordariomyceta`, `Sordariomycetes`, `Hypocreomycetidae`, `Glomerellales`, and `Plectosphaerellaceae`.

The four emitted NCBI synonyms are all present on the pinned NCBI row: two exact synonyms, `Verticillium dahliae var. longisporum` and `Verticillium longisporum var. longisporum`, plus two related authority strings.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17326` supports the NCBI identifier, label, rank, parent, genetic code, and synonym set.
- `data/raw/gold_organisms.tsv:188` supports the GOLD source attestation with five `ORGANISM` assertions keyed to `NCBITaxon:100787`.
- `data/raw/ncbi_merged_ids.tsv:21697` preserves the obsolete-to-current merge from `NCBITaxon:1608296` to `NCBITaxon:100787`.
- `data/raw/ncbi_type_material.tsv:611` through `data/raw/ncbi_type_material.tsv:620` preserve the local NCBI `typematerial.dmp` holotype and culture-from-holotype aliases.

## Completeness

The generated record is complete for the pinned source set: it carries NCBI identity, the complete NCBI synonym set, the GOLD source attestation, and no unsupported GTDB, LPSN, BacDive, StrainInfo, MediaDive, Madin, BactoTraits, or AllTheBacteria claims.

The NCBI type-material rows are not missing from the YAML by accident; TaxonMech currently derives `nomenclature` and type-strain fields from LPSN, and no local LPSN row is present for this fungal species.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI and GOLD lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
