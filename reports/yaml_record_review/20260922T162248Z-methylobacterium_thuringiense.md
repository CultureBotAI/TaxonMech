# YAML Record Review: Methylobacterium thuringiense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/methylobacterium_thuringiense.yaml
- Started UTC: 2026-09-22T16:22:49Z
- Finished UTC: 2026-09-22T16:22:49Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/methylobacterium_thuringiense.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003091` / `Methylobacterium thuringiense`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003091`
- Label: `Methylobacterium thuringiense`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:407` / `Methylobacterium`
- Maintained owner: source rows under `data/raw/`, `data/atb/`, and `data/straininfo/`; do not patch `data/taxa/bacteria/methylobacterium_thuringiense.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/methylobacterium_thuringiense.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/methylobacterium_thuringiense.yaml data/taxa/bacteria/methylobacterium_trifolii.yaml data/taxa/bacteria/bacterium_bjsm1.yaml data/taxa/bacteria/bacterium_bjsm2.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003091` to label `Methylobacterium thuringiense`, rank `SPECIES`, parent `NCBITaxon:407`, genetic code `11`, NCBI synonyms `Methylobacterium sp. C34` and `Methylobacterium thuringiense Wellner et al. 2013`, source bundle `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:407` through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, and `Methylobacteriaceae`. Each checked ancestor had an exact local NCBI source row.
- The LPSN block is supported by `data/raw/lpsn_names.tsv` row `lpsn:790953`, including species status, authority `Wellner et al. 2013`, URL `https://lpsn.dsmz.de/species/methylobacterium-thuringiense`, parent `lpsn:516060`, NCBI cross-reference `NCBITaxon:1003091`, GTDB cross-reference `GTDB:s__Methylobacterium_thuringiense`, type strain `kgmicrobe.strain:LMG-25777`, publications `PMID:23291886`, `doi:10.1099/ijs.0.047787-0`, `doi:10.1099/ijs.0.056119-0`, and sequence `INSDC:MT760178`.
- The GTDB mapping to `GTDB:s__Methylobacterium_thuringiense` with predicate `skos:closeMatch` and genome count `2` is supported by `data/raw/gtdb_mappings.tsv`; `data/raw/gtdb_species.tsv` also carries genome count `2` for that GTDB species.

## Evidence

- `strain_count: 2` matches the two same-taxon BacDive strain rows in `data/raw/bacdive_strains.tsv`: `bacdive_133947` / `C34` with `CCM-7787` and `LMG-25777`, and `bacdive_24172` / `T19+3-5, T5` with `CCM-7790` and `DSM-23631`.
- The type-strain assertion on `kgmicrobe.strain:bacdive_133947` is corroborated by NCBI type-material aliases for `C34`, `CCM 7787`, and `LMG 25777`, and by the LPSN type-strain row naming `LMG-25777`.
- Culture-collection identifiers on both strains resolve in `data/raw/culture_collection_strains.tsv`.
- The StrainInfo deposit and strain related records in the YAML exactly trace to `data/straininfo/strain_links.tsv` and `data/straininfo/related_records.tsv.gz`: deposits `855621` and `889756` for `bacdive_133947` / `straininfo.strain:370468`, and deposit `907083` for `bacdive_24172` / `straininfo.strain:400233`.
- The `INSDC:MT760178` and `INSDC:FR847846` nucleotide-sequence related records trace to StrainInfo rows for `bacdive_133947` and `bacdive_24172`, respectively.
- Source attestations match the inspected inventory rows: NCBI `1 NAME`, LPSN `1 NAME`, GTDB `2 GENOME`, BacDive `2 STRAIN`, MediaDive `2 MEDIUM`, GOLD `1 ORGANISM`, MADIN `14 TRAIT_ASSERTION`, and BactoTraits `4 TRAIT_ASSERTION`.
- No unsupported evidence placement, over-scoped source, or mismatched source identifier was found.

## Completeness

- The record correctly leaves causal-graph slots absent; no causal graph was attested in the reviewed raw rows.
- Optional LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, culture-collection, and StrainInfo surfaces that have same-taxon evidence are represented.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo`, plus exact `zgrep` checks of compressed StrainInfo records, found no same-taxon source that would force an additional `Methylobacterium thuringiense` strain into this species record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If upstream Methylobacterium source inventories are refreshed, rerun the taxon generation step that owns `data/taxa/bacteria/methylobacterium_thuringiense.yaml`, then rerun `just validate data/taxa/bacteria/methylobacterium_thuringiense.yaml` and a strict validation over the regenerated file.
- For a live authority audit beyond the pinned `2026-09-13` snapshot, manually compare current NCBI Taxonomy, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, and StrainInfo pages against the local rows before changing maintained inputs.

## Additional Notes

- `data/raw/gtdb_mappings.tsv` also maps `GTDB:s__Methylobacterium_thuringiense` to `NCBITaxon:2603898` / `Methylobacterium sp. WL9`; that second mapping is materialized in `data/taxa/bacteria/methylobacterium_sp_wl9.yaml` and does not invalidate the exact `NCBITaxon:1003091` mapping reviewed here.
- BacDive-derived assembly rows for `bacdive_130982` / `DSM 23674` carry assembly-level `NCBITaxon:1003091`, but the BacDive strain row itself is under `NCBITaxon:409`; those rows are owned by `data/taxa/bacteria/methylobacterium_sp.yaml`, not by this species record.
