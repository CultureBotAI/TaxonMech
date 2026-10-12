# YAML Record Review: Mesoflavibacter zeaxanthinifaciens S86

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mesoflavibacter_zeaxanthinifaciens_s86.yaml`
- Started UTC: 2026-09-22T18:06:02Z
- Finished UTC: 2026-09-22T18:08:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004149` |
| Label | `Mesoflavibacter zeaxanthinifaciens S86` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:393060` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated TaxonMech taxon record under `data/taxa/`. The file is owned by the seeder plus `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; future corrections must be made in those maintained inputs or in `src/taxonmech/seed.py`, not by hand-editing this YAML.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mesoflavibacter_zeaxanthinifaciens_s86.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/mesoflavibacter_zeaxanthinifaciens_s86.yaml data/taxa/bacteria/photorhabdus_khanii.yaml data/taxa/bacteria/photorhabdus_khanii_nc19.yaml data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004149` denotes the strain `Mesoflavibacter zeaxanthinifaciens S86` in the pinned NCBI taxonomy inventory. Its parent is the species `NCBITaxon:393060` (`Mesoflavibacter zeaxanthinifaciens`), and the root-first lineage in the YAML carries the pinned NCBI parent chain through `Bacteria`, `Bacteroidota`, `Flavobacteriia`, `Flavobacteriales`, `Flavobacteriaceae`, `Mesoflavibacter`, and the parent species.

The two exact synonyms in the record, `Mesoflavibacter zeaxanthinifaciens str. S86` and `Mesoflavibacter zeaxanthinifaciens strain S86`, are the exact NCBI synonyms on the local `data/raw/ncbitaxon_taxa.tsv` row. The `EXACT` grounding and `SEEDED` status are therefore internally consistent.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and two exact synonyms | `data/raw/ncbitaxon_taxa.tsv` has the exact row for `NCBITaxon:1004149`, label `Mesoflavibacter zeaxanthinifaciens S86`, rank `STRAIN`, parent `NCBITaxon:393060`, genetic code `11`, and both NCBI synonyms. |
| Parent species identity | `data/raw/ncbitaxon_taxa.tsv` has the exact parent row for `NCBITaxon:393060`, label `Mesoflavibacter zeaxanthinifaciens`, rank `SPECIES`, parent `NCBITaxon:444051`, genetic code `11`. |
| Madin attestation | `data/raw/madin_taxa.tsv` has `NCBITaxon:1004149` with count `1`, matching the `MADIN` `TRAIT_ASSERTION` attestation. |
| Seed provenance | The sole `curation_history` entry records `seed_from_sources`, `SEEDED_FROM_SOURCES`, and the expected `MADIN` plus `NCBITAXON` sources. |

## Completeness

The strain has no `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, or discussions. That is complete for the local inputs inspected: a gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1004149`, the label, and the slug found the NCBI and Madin rows but no same-taxon LPSN, GTDB, BacDive, MediaDive, GOLD, BactoTraits, StrainInfo, or AllTheBacteria rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the same focused `just validate` and `just validate-strict` commands after the next seed refresh if any upstream row for `NCBITaxon:1004149` changes. No manual curation follow-up is required from this review.

## Additional Notes

The live NCBI lookup was unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot that seeds the record.
