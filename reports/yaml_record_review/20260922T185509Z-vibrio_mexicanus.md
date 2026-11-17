# YAML Record Review: Vibrio mexicanus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/vibrio_mexicanus.yaml`
- Started UTC: 2026-09-22T18:53:31Z
- Finished UTC: 2026-09-22T18:55:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004326` |
| Label | `Vibrio mexicanus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:662` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated bacterial species record for the NCBI taxon, enriched by LPSN, GTDB, BacDive, MediaDive, GOLD, Madin et al., BactoTraits, NCBI Assembly, BV-BRC, and StrainInfo rows.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/vibrio_mexicanus.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/vibrio_mexicanus.yaml data/taxa/bacteria/vibrio_sp_caim_1559.yaml data/taxa/bacteria/vibrio_sp_caim_190.yaml data/taxa/bacteria/vibrio_sp_caim_363.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004326` is the pinned NCBI row for `Vibrio mexicanus`, rank `SPECIES`, parent `NCBITaxon:662`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadota`, `Gammaproteobacteria`, `Vibrionales`, `Vibrionaceae`, and `Vibrio`.

The LPSN row `lpsn:793375` maps the same name to `NCBITaxon:1004326`, marks it as validly published, legitimate, and the correct name, and links `GTDB:s__Vibrio_mexicanus`. The GTDB row maps `s__Vibrio_mexicanus` to this same NCBI taxon by `skos:closeMatch` with one genome.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, rank, parent, genetic code, and NCBI synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004326`, label `Vibrio mexicanus`, rank `SPECIES`, parent `NCBITaxon:662`, genetic code `11`, related synonyms `Vibrio mexicanus Gonzlez-Castillo et al. 2015` and `Vibrio sp. CAIM 1540`, and the expected eight-source source set. |
| LPSN nomenclature | `data/raw/lpsn_names.tsv` has `lpsn:793375` for `Vibrio mexicanus` with the same authority, correct-name status, DOI/PMID list, INSDC sequence accession, and `GTDB:s__Vibrio_mexicanus` cross-reference shown in the record. |
| GTDB taxonomy and genome mapping | `data/raw/gtdb_mappings.tsv` has `GTDB:s__Vibrio_mexicanus` mapped to `NCBITaxon:1004326` by `skos:closeMatch` with `1` genome, and `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` carry the `RS_GCF_001012815.1` genome links through `CAIM 1540`. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:131484` / `CulC12 3(4)` classified under `NCBITaxon:1004326` with deposits `CAIM-1540`, `CECT-8828`, and `DSM-100338`; `data/raw/culture_collection_strains.tsv` maps all three deposit CURIEs to this NCBI taxon. |
| Genome and related records | The single BacDive strain has the 9 genome assemblies, 8 genome records, and 26 related records present in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/strain_links.tsv`, including NCBI Assembly, BV-BRC, GTDB, GOLD organism/project/analysis, BioSample, BioProject, and StrainInfo DSM 100338 links. |
| Source attestation counts | `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` provide the MediaDive count `1`, GOLD count `4`, Madin count `5`, and BactoTraits count `1`; the other attestation rows trace to the checked NCBI, LPSN, GTDB, and BacDive rows. |

## Completeness

The nomenclature entry, GTDB mapping, xrefs, two NCBI synonyms, single BacDive strain, genome assemblies, genome records, GOLD/BioSample/BioProject related records, StrainInfo deposit records, source attestations, and seed history are populated from the inspected maintained inputs. The empty record-level `evidence`, `causal_graphs`, and discussion sections are appropriate because no curator-authored mechanism graph or literature overlay is present.

AllTheBacteria has BioSample `SAMN03339753` only in `data/atb/exclusions.tsv` and `data/atb/assemblies.tsv` as unavailable/not processed, so there is no supported ATB genome link to add.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004326`, `lpsn:793375`, `GTDB:s__Vibrio_mexicanus`, or the BacDive/NCBI Assembly/BV-BRC/GOLD/StrainInfo source rows for CAIM 1540, CECT 8828, or DSM 100338.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-vibrio_mexicanus.md'` check, which includes ignored report files, found no prior local report before this one was written.

The local NCBI type-material inventory has `CAIM 1540`, `CECT 8828`, and `DSM 100338` type-strain rows for this taxon. The current seeder and corpus invariant derive `is_type_strain` only from LPSN `type_strain_designations`, and the pinned `lpsn:793375` row has no type-strain IDs, so the BacDive strain is unflagged under the current projection rule. Live source lookups were unavailable during this run, so identity and evidence were checked against the pinned committed source snapshots under `data/raw/` and `data/straininfo/`.
