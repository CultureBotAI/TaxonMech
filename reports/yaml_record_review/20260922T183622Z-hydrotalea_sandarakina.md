# YAML Record Review: Hydrotalea sandarakina

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/hydrotalea_sandarakina.yaml`
- Started UTC: 2026-09-22T18:35:04Z
- Finished UTC: 2026-09-22T18:36:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004304` |
| Label | `Hydrotalea sandarakina` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1004300` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated bacterial species record for the NCBI taxon, enriched by LPSN, GTDB, BacDive, MediaDive, GOLD, Madin et al., BactoTraits, AllTheBacteria, and StrainInfo rows.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/hydrotalea_sandarakina.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/hydrotalea_sandarakina.yaml data/taxa/bacteria/aphanothece_stagnina.yaml data/taxa/bacteria/aphanothece_stagnina_h5.yaml data/taxa/bacteria/nostoc_sp_r5.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004304` is the pinned NCBI row for `Hydrotalea sandarakina`, rank `SPECIES`, parent `NCBITaxon:1004300`, and genetic code `11`. The lineage follows NCBI through `Bacteroidota`, `Chitinophagia`, `Chitinophagales`, `Chitinophagaceae`, and `Hydrotalea`.

The LPSN row `lpsn:789993` maps the same name to `NCBITaxon:1004304`, marks it as validly published, legitimate, and the correct name, and names DSM 23241 and LMG 25526 as type-strain designations. The GTDB row `GTDB:s__Hydrotalea_sandarakina` maps to the same NCBI taxon with `skos:closeMatch` and `genome_count: 1`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, rank, parent, genetic code, and NCBI synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004304`, label `Hydrotalea sandarakina`, rank `SPECIES`, parent `NCBITaxon:1004300`, genetic code `11`, related synonyms `Hydrotalea sandarakina Albuquerque et al. 2012` and `Hydrotalea sp. AF-51`, and the expected source set. |
| LPSN nomenclature | `data/raw/lpsn_names.tsv` has `lpsn:789993` for `Hydrotalea sandarakina` with the same authority, correct-name status, DOI/PMID list, INSDC sequence accession, GTDB cross-reference, and DSM 23241 / LMG 25526 type-strain designations shown in the record. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` has `GTDB:s__Hydrotalea_sandarakina` mapped to `NCBITaxon:1004304` by `skos:closeMatch` with `1` genome. |
| BacDive strains | `data/raw/bacdive_strains.tsv` has exactly the two rows represented here: `bacdive:17765` / AF-51 with DSM 23241 and LMG 25526, and `bacdive:17766` / AF-50 with DSM 23242 and LMG 25527. |
| Genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/atb/*.tsv`, and `data/straininfo/*.tsv` provide the DSM 23241 genome links, BioSample `SAMN05660754`, GOLD organism/project/analysis rows, AllTheBacteria `202505.SAMN05660754` row, and StrainInfo deposit rows projected under `kgmicrobe.strain:bacdive_17765` and `kgmicrobe.strain:bacdive_17766`. |
| Source attestation counts | `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` provide the MediaDive count `1`, GOLD count `3`, Madin count `24`, and BactoTraits count `20`; the other attestation rows trace to the checked NCBI, LPSN, GTDB, and BacDive rows. |

## Completeness

The nomenclature, GTDB mapping, xrefs, two NCBI synonyms, two BacDive strains, genome assemblies, genome records, AllTheBacteria evidence, StrainInfo deposits, source attestations, and seed history are populated from the inspected maintained inputs. The empty record-level `evidence`, `causal_graphs`, and discussion sections are appropriate because no curator-authored mechanism graph or literature overlay is present.

An exact, gitignore-independent `find` found no prior local review for this stem. The exact `rg --no-ignore --hidden` searches over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` found the expected Hydrotalea rows in NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, BactoTraits, AllTheBacteria, StrainInfo, strain genome, and strain related-record inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004304`, `lpsn:789993`, `GTDB:s__Hydrotalea_sandarakina`, or the BacDive/StrainInfo/GOLD/ATB source rows for DSM 23241, LMG 25526, DSM 23242, or LMG 25527.

## Additional Notes

Live source lookups were unavailable during this run, so identity and evidence were checked against the pinned committed source snapshots under `data/raw/`, `data/atb/`, and `data/straininfo/`.
