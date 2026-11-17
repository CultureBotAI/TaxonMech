# YAML Record Review: Pasteurellaceae bacterium baikas1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_baikas1.yaml`
- Started UTC: 2026-10-04T01:49:28Z
- Finished UTC: 2026-10-04T01:50:43Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032637`, Pasteurellaceae bacterium baikas1. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and a single seed event. It makes no phenotype, gene-function, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_baikas1.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_baikas1.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220881` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30188` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032637&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032637) confirm identity, label spelling, species rank, parent, domain, code 11 and all nine root-first lineage IDs. The ancestry through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae is preserved from NCBI.

Complete structured scans found no backbone synonyms or children and no own-ID type-material, merged-ID or dropped entry. The lowercase name `baikas1`, including its letter s, is the source spelling; it must not be silently normalized to the previously reviewed Baika1 type-strain designation of Otariodibacter oris. EXACT describes NCBI grounding, not formal nomenclatural validity, and the strain-style name does not override NCBI's species rank.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13259` and `curation/seed_scope.tsv:321253` confirm ID, slug and NCBI-only scope reason. The seed event records that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HM626602.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626602.1) is a 520-base partial RpoB coding sequence with genomic DNA molecule type, strain baikas1 and taxon 1032637. Its source qualifiers identify Denmark and a California-sea-lion host. Direct submission by Christensen, Bisgaard and Hansen was on 2010-07-05.

The entry's other reference is marked unpublished and supplies no PMID or DOI. Its title discusses Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. The title, host and similar isolate names do not establish an isolate-level synonym or type designation. The target's own source identity is retained, and the YAML correctly does not import Baika1's deposit or genome evidence.

A partial RpoB marker is not a complete genome or experimentally demonstrated phenotype. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than universal genome-absence evidence. The browser sequence view failed, but structured GenBank and both taxonomy requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and baikas1 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 13 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target culture deposit, assembly association, extra source mapping or separate history record was found within those surfaces. Bare baikas1 is not a registered collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; the external marker annotation is context, not a gene-function claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve exact source spelling, generated-file ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require an explicit isolate-level authority crosswalk before transferring any Baika1/Otariodibacter association to baikas1.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032637 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric matches include SAMEA1032637 for Streptococcus pneumoniae strain 255210, Salmonella run SRR11032637, and Streptococcus pyogenes sample SAMN41032637. These unrelated accession strings do not establish target taxon, strain or genome identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
