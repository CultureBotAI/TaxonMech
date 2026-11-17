# YAML Record Review: Nocardiopsis sp. SRh8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_srh8.yaml`
- Started UTC: 2026-10-04T03:01:25Z
- Finished UTC: 2026-10-04T03:02:00Z
- Verdict: pass

## Target

Read the full generated TaxonRecord for `NCBITaxon:1032723`, Nocardiopsis sp. SRh8. It carries SPECIES rank, BACTERIA domain, parent unclassified Nocardiopsis (2649073), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, gene-function, host-interaction, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/nocardiopsis_sp_srh8.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/nocardiopsis_sp_srh8.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220907` and `data/catalog/ncbi_names-0005.jsonl.gz:30213` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032723&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032723) confirm exact identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Bacillati, Actinomycetota, Actinomycetes, Streptosporangiales and Nocardiopsidaceae agree with the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the NCBI source placeholder, not a formally named species or an equivalence to another Nocardiopsis isolate.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13294` and `curation/seed_scope.tsv:321278` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443221.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443221.1) is a 1,444-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain SRh8 and explicit taxon 1032723. Its source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

The references comprise an unpublished actinomycete study by Fei and a direct submission on 2010-10-24; no PMID or DOI is supplied. The marker supports this source identity but is not a genome. Neither the genus nor the collection context establishes an antimicrobial, plant-growth-promoting or other strain-specific function. The common host label does not ground a scientific host species. None of these stronger claims appears in the YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded SRh8 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All ten matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those bounded surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. SRh8 is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; external marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific evidence for functions and explicit authority crosswalks for culture and genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032723 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

SAMEA1032723 belongs to Streptococcus pneumoniae 18044 (1313), including GCA_001085645.1/.2, GCF_001085645.1, BV-BRC 1313.6841 and ATB run ERR069735. GOLD spells that other strain 018044. The source-specific leading zero and assembly versions are retained, not normalized into target identity. None of these numeric matches provides an SRh8 genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
