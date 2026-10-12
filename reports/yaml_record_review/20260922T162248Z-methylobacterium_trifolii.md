# YAML Record Review: Methylobacterium trifolii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/methylobacterium_trifolii.yaml
- Started UTC: 2026-09-22T16:22:49Z
- Finished UTC: 2026-09-22T16:22:49Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/methylobacterium_trifolii.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003092` / `Methylobacterium trifolii`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003092`
- Label: `Methylobacterium trifolii`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:407` / `Methylobacterium`
- Maintained owner: source rows under `data/raw/`, `data/atb/`, and `data/straininfo/`; do not patch `data/taxa/bacteria/methylobacterium_trifolii.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/methylobacterium_trifolii.yaml` | Passed; `linkml-validate` exited 0. |
| `just validate-strict data/taxa/bacteria/methylobacterium_thuringiense.yaml data/taxa/bacteria/methylobacterium_trifolii.yaml data/taxa/bacteria/bacterium_bjsm1.yaml data/taxa/bacteria/bacterium_bjsm2.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003092` to label `Methylobacterium trifolii`, rank `SPECIES`, parent `NCBITaxon:407`, genetic code `11`, NCBI synonyms `Methylobacterium sp. TA73` and `Methylobacterium trifolii Wellner et al. 2013`, source bundle `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:407` through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, and `Methylobacteriaceae`. Each checked ancestor had an exact local NCBI source row.
- The LPSN block is supported by `data/raw/lpsn_names.tsv` row `lpsn:790952`, including species status, authority `Wellner et al. 2013`, URL `https://lpsn.dsmz.de/species/methylobacterium-trifolii`, parent `lpsn:516060`, NCBI cross-reference `NCBITaxon:1003092`, GTDB cross-reference `GTDB:s__Methylobacterium_trifolii`, type strain `kgmicrobe.strain:LMG-25778`, publications `PMID:23291886`, `doi:10.1099/ijs.0.047787-0`, `doi:10.1099/ijs.0.056119-0`, and sequence `INSDC:FR847848`.
- The GTDB mapping to `GTDB:s__Methylobacterium_trifolii` with predicate `skos:closeMatch` and genome count `1` is supported by `data/raw/gtdb_mappings.tsv`; `data/raw/gtdb_species.tsv` also carries genome count `1` for that GTDB species.

## Evidence

- `strain_count: 1` matches the one same-taxon BacDive strain row in `data/raw/bacdive_strains.tsv`: `bacdive_133946` / `TA73` with `CCM-7786` and `LMG-25778`.
- The type-strain assertion on `kgmicrobe.strain:bacdive_133946` is corroborated by NCBI type-material aliases for `TA73`, `CCM 7786`, and `LMG 25778`, and by the LPSN type-strain row naming `LMG-25778`.
- Culture-collection identifiers on the strain resolve in `data/raw/culture_collection_strains.tsv`.
- The assembly, genome, BioProject, and BioSample related records for `kgmicrobe.strain:bacdive_133946` trace to `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` rows for `GCA_042677185.1`, `patric:1003092.4`, `PRJNA595761`, and `SAMN43284412`.
- The StrainInfo deposit and strain related records in the YAML exactly trace to `data/straininfo/strain_links.tsv` and `data/straininfo/related_records.tsv.gz`: deposits `856797` and `889758` for `bacdive_133946` / `straininfo.strain:371133`.
- Source attestations match the inspected inventory rows: NCBI `1 NAME`, LPSN `1 NAME`, GTDB `1 GENOME`, BacDive `1 STRAIN`, GOLD `1 ORGANISM`, and MADIN `7 TRAIT_ASSERTION`.
- No unsupported evidence placement, over-scoped source, or mismatched source identifier was found.

## Completeness

- The record correctly leaves causal-graph slots absent; no causal graph was attested in the reviewed raw rows.
- Optional LPSN, GTDB, BacDive, GOLD, MADIN, culture-collection, genome, assembly, and StrainInfo surfaces that have same-taxon evidence are represented.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo`, plus exact `zgrep` checks of compressed StrainInfo records, found no same-taxon source that would force an additional `Methylobacterium trifolii` strain into this species record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If upstream Methylobacterium source inventories are refreshed, rerun the taxon generation step that owns `data/taxa/bacteria/methylobacterium_trifolii.yaml`, then rerun `just validate data/taxa/bacteria/methylobacterium_trifolii.yaml` and a strict validation over the regenerated file.
- For a live authority audit beyond the pinned `2026-09-13` snapshot, manually compare current NCBI Taxonomy, LPSN, GTDB, BacDive, GOLD, MADIN, and StrainInfo pages against the local rows before changing maintained inputs.

## Additional Notes

- BacDive-derived assembly rows for `bacdive_130981` / `DSM 23632` carry assembly-level `NCBITaxon:1003092`, but the BacDive strain row itself is under `NCBITaxon:409`; those rows are owned by `data/taxa/bacteria/methylobacterium_sp.yaml`, not by this species record.
