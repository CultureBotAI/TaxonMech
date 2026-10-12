# YAML Record Review: Chryseobacterium sp. TS35

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_ts35.yaml`
- Started UTC: 2026-10-04T02:47:41Z
- Finished UTC: 2026-10-04T02:48:33Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032718`, Chryseobacterium sp. TS35. It carries SPECIES rank, BACTERIA domain, parent unclassified Chryseobacterium (2593645), thirteen lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No curated phenotype, host interaction, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/chryseobacterium_sp_ts35.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/chryseobacterium_sp_ts35.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked every lineage entry, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220902` and `data/catalog/ncbi_names-0005.jsonl.gz:30208` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032718&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032718) confirm exact label, species rank, parent, code 11, bacterial domain and all thirteen root-first lineage IDs.

Weeksellaceae, the two clades and the unranked Chryseobacterium group are source-carried lineage entries, not extra curated taxa. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder; it neither formally names the species nor equates it with other isolates designated TS35.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13288` and `curation/seed_scope.tsv:321273` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ647281.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ647281.1) is a 1,423-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain TS35 and explicit taxon 1032718. Source qualifiers identify rhizosphere material, host wild rice and China: Dongxiang, Jiangxi.

The references comprise an unpublished study by Fei and a direct submission on 2010-11-21. No PMID or DOI is supplied. These metadata do not establish a scientific host-species grounding, beneficial host interaction, transcriptomic response or another strain-specific function. The YAML makes none of those extrapolations.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query does not prove universal genome absence, and the partial marker is not an assembly. Browser retrieval of the Nuccore page failed; both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and bounded TS35/TS 35/TS-35/TS_35 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 26 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. TS35 is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; the unrelated metatranscriptome name collision does not make it a transcriptomics record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific evidence for functions and host interactions and an explicit authority crosswalk before attaching culture, genome or transcriptomic evidence.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032718 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Pusillimonas sp. TS35 (2695269) has its own backbone, name, scope, GOLD and genome entries, including GCA_009857885.1 and historical GCF_009857885.1. Comamonas sp. TS35 (477208) is another authority entry. Neither name collision establishes identity with Chryseobacterium TS35. Other exclusions include Klebsiella pneumoniae TS-35 (GCA_045318975.1), Salmonella Sal_TS_35 (GCA_056131215.1), and a tomato-rhizosphere metatranscriptome from Haddat ash Sham, Saudi Arabia, labeled TS35. No inspected synonym, merge or explicit crosswalk supports transfer.

SAMEA1032718 belongs to Streptococcus pneumoniae 323485 (1313), including GCA_001300775.1/.2, GCF_001300775.1 and ATB run ERR069819. A BioSample number is not the NCBI taxonomy identifier with the same digits and supplies no target genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
