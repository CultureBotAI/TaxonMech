# YAML Record Review: Acetonema longum DSM 6540

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetonema_longum_dsm_6540.yaml
- Started UTC: 2026-09-23T16:15:31Z
- Finished UTC: 2026-09-23T16:16:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | TaxonRecord |
| Identifier | NCBITaxon:1009370 |
| Label | Acetonema longum DSM 6540 |
| Rank | STRAIN |
| Domain | BACTERIA |
| Parent | NCBITaxon:2374, Acetonema longum |
| Maintained inputs | data/raw/ncbitaxon_taxa.tsv, data/raw/gtdb_mappings.tsv, data/raw/gtdb_species.tsv, source inventories consumed by the seeder |
| YAML status | Generated from pinned source inventories |

The target was resolved by the exact `PATHS.tsv` row `NCBITaxon:1009370	acetonema_longum_dsm_6540` at line 3111. A `find` duplicate check over the ignored `reports/yaml_record_review` directory found no prior `*-acetonema_longum_dsm_6540.md` report before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/waddliaceae_bacterium_cve65.yaml data/taxa/bacteria/chlamydiales_bacterium_cve71.yaml data/taxa/bacteria/criblamydiaceae_bacterium_cve70.yaml data/taxa/bacteria/acetonema_longum_dsm_6540.yaml` | Passed: 4 files scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate data/taxa/bacteria/acetonema_longum_dsm_6540.yaml` | Passed: `linkml-validate` reported `No issues found`. |
| `just verify-corpus` | Skipped: this read-only review did not change `data/taxa/`, and the earlier full-corpus reproduction check over all 625,960 records was clean. |
| `just validate-history` | Skipped: no append-only `history/` record is created during this read-only review. |
| `just validate-products` | Skipped: this strain record has no `causal_graphs` grounding to validate. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211715` exactly supports the NCBI strain identifier, preferred label, rank, parent species, genetic code, seeded source set, and 2026-09-13 snapshot:

```text
NCBITaxon:1009370	Acetonema longum DSM 6540	STRAIN	NCBITaxon:2374	11	Acetonema longum APO-1|Acetonema longum str. DSM 6540|Acetonema longum strain DSM 6540			ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits		2026-09-13
```

The NCBI side of the record is a correctly grounded strain record. Its parent is the species `NCBITaxon:2374` (`Acetonema longum`), and its NCBI exact synonyms `Acetonema longum APO-1`, `Acetonema longum str. DSM 6540`, and `Acetonema longum strain DSM 6540` are copied directly from the exact NCBI row above.

GTDB support is narrower. The local GTDB source rows define `GTDB:s__Acetonema_longum` as a species cluster in `GTDB:g__Acetonema` with one genome, then map that species-cluster identifier to the strain-level NCBI taxon `NCBITaxon:1009370`:

```text
GTDB:s__Acetonema_longum	s__Acetonema_longum	GTDB:g__Acetonema	1
GTDB:s__Acetonema_longum	s__Acetonema_longum	GTDB:g__Acetonema	NCBITaxon:1009370	skos:closeMatch	1
```

The local GTDB genome rows and assembly rows that identify `RS_GCF_000219125.1`, `GCA_000219125.2`, and `GCF_000219125.1` as strain `DSM 6540` support the GTDB genome-level cross references in `strains`, `genome_records`, and `related_records`. They do not make the GTDB species-cluster identifier an exact strain synonym.

Live NCBI and GTDB browser lookups were unavailable in this environment; the committed NCBI, GTDB, BacDive, GOLD, BV-BRC, NCBI Assembly, and StrainInfo inventory rows were treated as the reproducible source of truth.

## Evidence

The record has seven source attestations:

| Source | Source ID | Source label | Count | Unit | Assessment |
|---|---|---|---:|---|---|
| NCBITAXON | NCBITaxon:1009370 | Acetonema longum DSM 6540 | 1 | NAME | Supported by `data/raw/ncbitaxon_taxa.tsv:211715`. |
| GTDB | GTDB:s__Acetonema_longum | s__Acetonema_longum | 1 | GENOME | Supported as a GTDB genome/species-cluster mapping by `data/raw/gtdb_species.tsv:3384` and `data/raw/gtdb_mappings.tsv:1119`, but over-promoted to strain identity in `taxonomy_mappings`, `synonyms`, and `xrefs`. |
| BACDIVE | NCBITaxon:1009370 | Acetonema longum DSM 6540 | 1 | STRAIN | Supported by exact BacDive-derived strain rows for `bacdive:17111`, culture collection IDs `ATCC-51454` and `DSM-6540`, and the `GCA_000219125` genome accession. |
| MEDIADIVE | NCBITaxon:1009370 | Acetonema longum DSM 6540 | 1 | MEDIUM | Supported by local MediaDive/BacDive inventory rows linked to `bacdive:17111`. |
| GOLD | NCBITaxon:1009370 | Acetonema longum DSM 6540 | 1 | ORGANISM | Supported by GOLD analysis, organism, and project rows for `Ga0027276`, `Go0011114`, and `Gp0011114` matched through `DSM 6540` or `APO-1, DSM 6540`. |
| MADIN | NCBITaxon:1009370 | Acetonema longum DSM 6540 | 4 | TRAIT_ASSERTION | Supported by local ATB trait source rows matched to this NCBI taxon. |
| BACTOTRAITS | NCBITaxon:1009370 | Acetonema longum DSM 6540 | 2 | TRAIT_ASSERTION | Supported by local ATB trait source rows matched to this NCBI taxon. |

The non-GTDB strain, genome, and related-record blocks are backed by BacDive, GOLD, BV-BRC, NCBI Assembly, and StrainInfo rows carrying matching strain labels, culture collection identifiers, assemblies, or BioProject/BioSample links. Exact plaintext and gzip-aware source searches over `data/raw`, `data/atb`, and `data/straininfo` found no evidence for additional same-taxon source rows that would change the review outcome.

## Completeness

Most generated slots are populated at the expected granularity for a strain record:

| Area | Assessment |
|---|---|
| Lineage | Complete root-first NCBI lineage is present from root through `Acetonema longum`. |
| NCBI synonyms | Complete for the aliases in the pinned NCBI row. |
| Taxonomy mappings | Incomplete by scope: `GTDB:s__Acetonema_longum` is present, but it is a species cluster and should not be promoted as a strain-level exact-looking xref or exact synonym. |
| Strains and genomes | `strain_count: 1` and strain `kgmicrobe.strain:bacdive_17111` are populated with BacDive, GOLD, BV-BRC, GTDB genome, NCBI Assembly, and StrainInfo support for the DSM 6540/APO-1/ATCC 51454 isolate. |
| Related records | BioProject, BioSample, GOLD, INSDC, and StrainInfo deposit links are present for the matched strain evidence. |
| Nomenclature | Correctly absent; no LPSN nomenclature row matched this strain-level NCBI taxon. |
| Causal graphs | Correctly absent; no curated mechanism overlay is present for this record. |

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The GTDB species-cluster identifier `GTDB:s__Acetonema_longum` is projected onto strain record `NCBITaxon:1009370` as if it were a strain identity. The mapping itself can remain a scoped GTDB note, but the generated `EXACT_SYNONYM` text `Acetonema longum` and bare `xrefs` entry make a species cluster look equivalent to `Acetonema longum DSM 6540`. | `data/raw/gtdb_species.tsv:3384` defines `GTDB:s__Acetonema_longum` as a GTDB species cluster with `genome_count: 1`, and `data/raw/gtdb_mappings.tsv:1119` maps that cluster to the NCBI strain taxon. In `src/taxonmech/seed.py`, every `skos:closeMatch` GTDB mapping is treated as identity; the seeder adds the GTDB ID to `xrefs` and emits the species-cluster label as an `EXACT_SYNONYM`. | `data/raw/gtdb_mappings.tsv` generation plus GTDB taxonomy mapping, synonym, and xref projection in `src/taxonmech/seed.py`. |

## Recommended Edits

1. In the GTDB mapping generation that writes `data/raw/gtdb_mappings.tsv`, prevent GTDB species clusters from being asserted as strain-level `skos:closeMatch` identities when the NCBI target rank is `STRAIN`; emit a scoped non-identity mapping, or keep the association only on genome-level evidence.
2. In `src/taxonmech/seed.py`, gate GTDB-to-`xrefs` and GTDB-to-`EXACT_SYNONYM` projection by NCBI rank so a GTDB species cluster cannot create a species-level exact synonym on a strain record even when an upstream mapping row says `skos:closeMatch`.
3. Regenerate `data/taxa/bacteria/acetonema_longum_dsm_6540.yaml` from the corrected maintained inputs and confirm the `taxonomy_mappings` block no longer presents `GTDB:s__Acetonema_longum` as strain identity while retaining the GTDB genome rows for `RS_GCF_000219125.1`.

## Follow-up Checks

- Re-run `just validate-strict data/taxa/bacteria/acetonema_longum_dsm_6540.yaml` after the GTDB mapping and seeder changes.
- Re-run `just validate data/taxa/bacteria/acetonema_longum_dsm_6540.yaml` to confirm LinkML still accepts the regenerated record.
- Re-run `just verify-corpus` after regeneration to prove the YAML reproduces from the maintained raw inputs.
- Manually inspect exact `GTDB:s__Acetonema_longum`, `NCBITaxon:1009370`, and `acetonema_longum_dsm_6540` searches in `data/raw`, `data/atb`, and `data/straininfo` to verify that only the species-cluster projection changed.

## Additional Notes

- The no-prior-report check used `find` so ignored Markdown reports in `reports/yaml_record_review` were included.
- Exact local searches used `rg --no-ignore --hidden` for plaintext source inventories and gzip-aware Ruby scans for compressed inventories, so ignored and compressed files under `data/raw`, `data/atb`, and `data/straininfo` were included.
