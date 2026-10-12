# YAML Record Review: Pasteurellaceae bacterium Tulle1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_tulle1.yaml`
- Started UTC: 2026-10-04T01:47:21Z
- Finished UTC: 2026-10-04T01:48:15Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032633`, Pasteurellaceae bacterium Tulle1. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. It asserts no phenotype, gene function, causal graph or genome equivalence.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_tulle1.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_tulle1.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks verified all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was invented. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220880` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30187` support the YAML's identifier and label. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032633&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032633) confirm rank, parent, domain, code 11 and all nine root-first lineage IDs. The ancestry through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae is carried from NCBI.

Complete structured scans found no backbone synonyms or children and no own-ID type-material, merged-ID or dropped row. A strain-style suffix does not override the source species rank. EXACT describes source grounding, not formal nomenclatural validity or eligibility as a culture-collection accession.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13258` and `curation/seed_scope.tsv:321252` agree on ID, slug and NCBI-only scope reason. The seed event accurately records that reason without implying human review.

Exact-taxon Nuccore search returned two entries, both inspected as GenBank XML. [HM626598.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626598.1) is a 383-base partial RpoB coding sequence with strain Tulle1. [HM626620.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626620.1) is a 1,464-base partial 16S ribosomal RNA gene sequence whose strain qualifier is lowercase `tulle1`. Both explicitly identify taxon 1032633, genomic DNA, Denmark and a harbor-seal host. The shared taxon reference establishes source classification; case normalization of arbitrary strain names is not being used as a culture-collection join rule.

Both entries cite Christensen, Bisgaard and Hansen, direct submission on 2010-07-05, and an additional reference marked unpublished without a PMID or DOI. Its title discusses Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. That study-level title does not establish a synonym, type designation or species reassignment for every isolate. The YAML correctly refrains from those transfers.

Two partial marker records are not two complete genomes or direct physiological evidence. The NAME count is independent of the number of sequence accessions. Exact Assembly search returned zero with a phrase-not-found warning, which is a bounded query result rather than universal absence. Primary taxonomy and GenBank structured retrievals succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. There are no descendant taxa or classified BacDive strains in the checked backbone/inventory, supporting `strain_count: 0` under the repository's counting contract.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and Tulle1 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 22 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target collection deposit, assembly association, additional mapping or separate history record was found within those surfaces. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; externally inspected marker-gene annotations are context, not gene-function claims in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated-file ownership, separate source identity and SEEDED status. Future authority corrections belong to maintained inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. A culture or species crosswalk requires explicit isolate-level evidence, not a bare name or study title.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032633 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric matches include SAMEA1032633 for Streptococcus pneumoniae strain 42397/042397, unrelated Salmonella run identifiers containing 1032633, and Streptococcus pyogenes sample SAMN41032633. These do not supply Tulle1 taxonomy, strain or genome evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
