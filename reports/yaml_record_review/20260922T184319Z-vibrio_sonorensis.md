# YAML Record Review: Vibrio sonorensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_sonorensis.yaml`
- Started UTC: 2026-09-22T18:41:48Z
- Finished UTC: 2026-09-22T18:43:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004316` |
| Label | `Vibrio sonorensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:662` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated bacterial species record for the NCBI taxon, enriched by LPSN, GTDB, BacDive, MediaDive, GOLD, Madin et al., BactoTraits, and StrainInfo rows.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/vibrio_sonorensis.yaml` | Pass; `linkml-validate` exited 0. |
| `just validate-strict data/taxa/bacteria/vibrio_sp_caim_1039.yaml data/taxa/bacteria/vibrio_sp_caim_1067.yaml data/taxa/bacteria/vibrio_sonorensis.yaml data/taxa/bacteria/vibrio_sp_caim_1180.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004316` is the pinned NCBI row for `Vibrio sonorensis`, rank `SPECIES`, parent `NCBITaxon:662`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadota`, `Gammaproteobacteria`, `Vibrionales`, `Vibrionaceae`, and `Vibrio`.

The LPSN row `lpsn:795017` maps the same name to `NCBITaxon:1004316`, marks it as validly published, legitimate, and the correct name, and names DSM 102190 as a type-strain designation. The GTDB row `GTDB:s__Vibrio_sonorensis` maps to the same NCBI taxon with `skos:closeMatch` and `genome_count: 1`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, rank, parent, genetic code, and NCBI synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004316`, label `Vibrio sonorensis`, rank `SPECIES`, parent `NCBITaxon:662`, genetic code `11`, related synonyms `Vibrio sonorensis Gonzalez-Castillo et al. 2017` and `Vibrio sp. CAIM 1076`, and the expected source set. |
| LPSN nomenclature | `data/raw/lpsn_names.tsv` has `lpsn:795017` for `Vibrio sonorensis` with the same authority, correct-name status, DOI/PMID list, INSDC sequence accession, GTDB cross-reference, and DSM 102190 type-strain designation shown in the record. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` has `GTDB:s__Vibrio_sonorensis` mapped to `NCBITaxon:1004316` by `skos:closeMatch` with `1` genome. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:132001` / PP5(1) classified under `NCBITaxon:1004316` with deposits CAIM 1076, CECT 9100, and DSM 102190. |
| Genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/strain_links.tsv` provide the CAIM 1076 genome links, BioSample `SAMN04029016`, GOLD organism/project/analysis rows, and StrainInfo DSM 102190 deposit rows projected under `kgmicrobe.strain:bacdive_132001`. |
| Source attestation counts | `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` provide the MediaDive count `1`, GOLD count `4`, Madin count `2`, and BactoTraits count `1`; the other attestation rows trace to the checked NCBI, LPSN, GTDB, and BacDive rows. |

## Completeness

The nomenclature, GTDB mapping, xrefs, two NCBI synonyms, single BacDive type strain, genome assemblies, genome records, StrainInfo deposit, source attestations, and seed history are populated from the inspected maintained inputs. The empty record-level `evidence`, `causal_graphs`, and discussion sections are appropriate because no curator-authored mechanism graph or literature overlay is present.

An exact, gitignore-independent `find` found no prior local review for this stem. The exact `rg --no-ignore --hidden` searches over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` found the expected Vibrio sonorensis rows in NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, BactoTraits, StrainInfo, strain genome, and strain related-record inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004316`, `lpsn:795017`, `GTDB:s__Vibrio_sonorensis`, or the BacDive/StrainInfo/GOLD source rows for CAIM 1076, CECT 9100, or DSM 102190.

## Additional Notes

Live source lookups were unavailable during this run, so identity and evidence were checked against the pinned committed source snapshots under `data/raw/` and `data/straininfo/`.
