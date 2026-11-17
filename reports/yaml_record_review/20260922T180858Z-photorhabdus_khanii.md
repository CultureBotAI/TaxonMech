# YAML Record Review: Photorhabdus khanii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photorhabdus_khanii.yaml`
- Started UTC: 2026-09-22T18:06:02Z
- Finished UTC: 2026-09-22T18:08:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004150` |
| Label | `Photorhabdus khanii` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:29487` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated TaxonMech species record. Its seeded identity, lineage, LPSN nomenclature, GTDB mapping, gathered BacDive strains, source attestations, genome links, and related records must be changed through the source inventories or seeder rather than through a direct YAML edit.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/photorhabdus_khanii.yaml` | Pass; `linkml-validate` exited 0. |
| `just validate-strict data/taxa/bacteria/mesoflavibacter_zeaxanthinifaciens_s86.yaml data/taxa/bacteria/photorhabdus_khanii.yaml data/taxa/bacteria/photorhabdus_khanii_nc19.yaml data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004150` is the pinned NCBI species row for `Photorhabdus khanii`, with genus parent `NCBITaxon:29487` and genetic code `11`; the YAML lineage carries the NCBI path to `Photorhabdus`. The record is species-level, bacterial, and eligible for `data/taxa/bacteria/`.

The LPSN nomenclature entry `lpsn:798521` maps the correct species name `Photorhabdus khanii` to this NCBI taxon and lists type designations `kgmicrobe.strain:CIP-109947` and `kgmicrobe.strain:DSM-3369`, which match deposits on the BacDive NC19 strain. The GTDB species `GTDB:s__Photorhabdus_khanii` appears in `data/raw/gtdb_mappings.tsv` as a `skos:closeMatch` with genome count `11`, and the LPSN row links that GTDB species to this species name, so the `taxonomy_mappings`, `xrefs`, GTDB synonym, and GTDB source attestation are appropriate here.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI species identity and NCBI synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004150`, label `Photorhabdus khanii`, rank `SPECIES`, parent `NCBITaxon:29487`, genetic code `11`, and the NCBI synonym spellings present in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:798521` carries `Photorhabdus khanii`, rank `SPECIES`, the correct-name status, the same DOI/PMID and INSDC accessions, and the CIP/DSM type-strain designations. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Photorhabdus_khanii` to `NCBITaxon:1004150` with `skos:closeMatch` and count `11`; the same GTDB species is the LPSN-linked mapping for `lpsn:798521`. |
| Direct source counts | Exact rows support the `MEDIADIVE` count of `1` in `data/raw/mediadive_taxa.tsv`, `GOLD` count of `1` in `data/raw/gold_organisms.tsv`, and `BACTOTRAITS` count of `1` in `data/raw/bactotraits_taxa.tsv`. |
| Gathered BacDive strains | `data/raw/bacdive_strains.tsv` has `bacdive:5051` filed directly under `NCBITaxon:1004150` and `bacdive:167546` filed under descendant `NCBITaxon:2100166`; the YAML's `strain_count: 2` and `classified_as: NCBITaxon:2100166` on MEX20-17 match that source split. |
| NC19 genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/strain_links.tsv` support the NC19 NCBI assembly, IMG, PATRIC, GOLD organism, StrainInfo deposit, SI-ID, and nucleotide-sequence related records. |
| MEX20-17 genome and related records | Exact `bacdive:167546` / `NCBITaxon:2100166` rows support `GCA_004348755`, `img.taxon:2897716086`, `patric:2100166.3`, `straininfo.strain:265640`, and `straininfo.deposit:20863`. |

## Completeness

The record has one species-level LPSN name, one GTDB mapping, two BacDive strain entries, and all exact direct source attestations found for `NCBITaxon:1004150`. Its descendant BacDive subspecies strain is present despite being filed under `NCBITaxon:2100166`, which is the intended asymmetry for species records.

The same gitignore-independent searches also found LPSN subspecies rows `lpsn:800148` and `lpsn:800272`; those are tied to descendant subspecies concepts rather than to the species-level `NCBITaxon:1004150`, so they are not missing from this species record's `nomenclature`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run focused validation plus an exact `rg --no-ignore --hidden` scan for `NCBITaxon:1004150`, `bacdive:5051`, `bacdive:167546`, `lpsn:798521`, and `GTDB:s__Photorhabdus_khanii` after the next upstream refresh to confirm the same two BacDive strains and direct source counts still project to the species.

## Additional Notes

Some NC19 related records preserve source taxon IDs from old or adjacent names, such as `NCBITaxon:574560` on GOLD and StrainInfo rows. They remain typed related records with explicit culture-deposit matches and do not change the `Photorhabdus khanii` record identity.
