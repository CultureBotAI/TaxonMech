# YAML Record Review: Micromonospora maris

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/micromonospora_maris.yaml
- Started UTC: 2026-09-22T16:27:53Z
- Finished UTC: 2026-09-22T16:27:53Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/micromonospora_maris.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003110` / `Micromonospora maris`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003110`
- Label: `Micromonospora maris`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1873` / `Micromonospora`
- Maintained owner: source rows under `data/raw/`, `data/atb/`, and `data/straininfo/`; do not patch `data/taxa/bacteria/micromonospora_maris.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/micromonospora_maris.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/bacterium_bjsm7.yaml data/taxa/bacteria/bacterium_bjsm8.yaml data/taxa/bacteria/bacterium_bjsm9.yaml data/taxa/bacteria/micromonospora_maris.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003110` to label `Micromonospora maris`, rank `SPECIES`, parent `NCBITaxon:1873`, genetic code `11`, exact synonym `Verrucosispora maris`, NCBI related synonyms for the original `Verrucosispora maris` authority forms, source bundle `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:1873` through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Micromonosporales`, and `Micromonosporaceae`. Each checked ancestor had an exact local NCBI source row.
- The LPSN block is supported by `data/raw/lpsn_names.tsv` row `lpsn:798650`, including species status, authority `(Goodfellow et al. 2012) Nouioui et al. 2018`, URL `https://lpsn.dsmz.de/species/micromonospora-maris`, parent `lpsn:516092`, NCBI cross-reference `NCBITaxon:1003110`, type strains `DSM-45365`, `JCM-31040`, and `NRRL-B-24793`, publications `PMID:30186281`, `doi:10.1099/ijsem.0.003071`, `doi:10.3389/fmicb.2018.02007`, and sequence `INSDC:AY528866`.
- The LPSN synonym `Verrucosispora maris` resolves to `lpsn:789672`, and the record keeps it as a related LPSN synonym while separately preserving NCBI's exact `Verrucosispora maris` synonym.
- The GTDB mapping to `GTDB:s__Micromonospora_gifhornensis` with predicate `skos:closeMatch` and genome count `12` is supported by `data/raw/gtdb_mappings.tsv`; `data/raw/gtdb_species.tsv` also carries genome count `12` for that GTDB species.

## Evidence

- `strain_count: 1` matches the one same-taxon BacDive strain row in `data/raw/bacdive_strains.tsv`: `bacdive_8032` / `AB-18-032` with `DSM-15899`, `DSM-45365`, `JCM-31040`, `NBRC-109089`, and `NRRL-B-24793`.
- The type-strain assertion on `kgmicrobe.strain:bacdive_8032` is corroborated by NCBI type-material aliases for `AB-18-032`, `DSM 45365`, and `NRRL B-24793`, and by the LPSN type-strain row naming `DSM-45365`, `JCM-31040`, and `NRRL-B-24793`.
- Culture-collection identifiers on the strain resolve in `data/raw/culture_collection_strains.tsv`.
- The BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly rows for `GCA_000204155`, `GCA_001507315`, `GCA_001507315.1`, and `GCF_001507315.1` in `data/raw/strain_assemblies.tsv` support the record's `genome_assemblies`.
- The GTDB, BacDive, GOLD, and BV-BRC rows in `data/raw/strain_genome_records.tsv` support the record's `genome_records` for `RS_GCF_001507315.1`, `img.taxon:2772190706`, `img.taxon:650716103`, `patric:1003110.4`, and `patric:263358.5`.
- The BioProject, BioSample, GOLD analysis, GOLD organism, GOLD project, and StrainInfo related records trace to `data/raw/strain_related_records.tsv`, `data/straininfo/strain_links.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Source attestations match the inspected inventory rows: NCBI `1 NAME`, LPSN `1 NAME`, GTDB `12 GENOME`, BacDive `1 STRAIN`, MediaDive `4 MEDIUM`, GOLD `5 ORGANISM`, MADIN `4 TRAIT_ASSERTION`, and BactoTraits `1 TRAIT_ASSERTION`.
- No unsupported evidence placement, over-scoped source, or mismatched source identifier was found.

## Completeness

- The record correctly leaves causal-graph slots absent; no causal graph was attested in the reviewed raw rows.
- Optional LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, culture-collection, genome, assembly, StrainInfo, and related-record surfaces that have same-taxon evidence are represented.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo`, plus an exact `zgrep` check of compressed StrainInfo related records, found no same-taxon source that would force an additional `Micromonospora maris` BacDive strain into this species record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If upstream `Micromonospora` source inventories are refreshed, rerun the taxon generation step that owns `data/taxa/bacteria/micromonospora_maris.yaml`, then rerun `just validate data/taxa/bacteria/micromonospora_maris.yaml` and a strict validation over the regenerated file.
- For a live authority audit beyond the pinned `2026-09-13` snapshot, manually compare current NCBI Taxonomy, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, BV-BRC, NCBI Assembly, and StrainInfo pages against the local rows before changing maintained inputs.

## Additional Notes

- BacDive assembly and genome rows for the `AB-18-032` genome use strain taxon `NCBITaxon:263358`, which is a child of `NCBITaxon:1003110`; including those under the species-level `bacdive_8032` strain is consistent with the local NCBI row for `Micromonospora maris AB-18-032`.
- `GTDB:s__Micromonospora_gifhornensis` has close or broad mapping rows to several NCBI taxa in `data/raw/gtdb_mappings.tsv`; the reviewed YAML uses only the exact row that maps that GTDB species to `NCBITaxon:1003110`.
