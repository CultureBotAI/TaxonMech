# YAML Record Review: Pasteurellaceae bacterium Svante2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_svante2.yaml`
- Started UTC: 2026-10-04T01:36:09Z
- Finished UTC: 2026-10-04T01:36:58Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032628`, Pasteurellaceae bacterium Svante2. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and a single seed event. No phenotype, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_svante2.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_svante2.yaml` passed for one file with zero errors and refreshed the validator TSV.

Read-only structured checks compared the entire lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220875` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30182` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032628&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032628) confirm ID, label, rank, parent, domain, code 11 and all nine root-first lineage identifiers. The Pseudomonadati/Pseudomonadota/Gammaproteobacteria/Pasteurellales/Pasteurellaceae ancestry is carried from NCBI.

The full backbone has no synonyms or children for the target. Complete type-material, merged-ID and dropped inventories contain no own-ID row. The label's strain-like suffix does not override NCBI's SPECIES rank. EXACT records source grounding, not formal nomenclatural validity or an inferred assignment to a named species.

## Evidence

The NCBITAXON attestation correctly counts one NAME from the 2026-09-13 snapshot. `data/taxa/PATHS.tsv:13252` and `curation/seed_scope.tsv:321247` agree on ID, slug and NCBI-only scope reason. The seed event faithfully records that reason without implying human review.

Exact-taxon Nuccore search returned two records, both inspected as GenBank XML. [HM626593.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626593.1) is a 466-base partial RpoB coding sequence with strain Svante2. [HM626618.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626618.1) is a 1,401-base partial 16S sequence whose strain qualifier is lowercase `svante2`. Both explicitly identify taxon 1032628, genomic DNA, Denmark and a harbor-seal host. The taxon identity rests on those explicit references, not a general rule that arbitrary strain names can be case-normalized into collection identifiers.

Both entries cite Christensen, Bisgaard and Hansen, direct submission on 2010-07-05, and an additional reference marked unpublished with no PMID or DOI. The study title concerns Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. It does not assign every sample to that proposed species. The YAML properly retains Svante2's separate source identity and does not manufacture a synonym or type-strain designation.

Partial marker sequences are not whole-genome or physiological evidence. The single NAME assertion is correctly independent of the two sequence records. Exact Assembly search returned zero with a phrase-not-found warning; this is a bounded query outcome, not universal genome absence. The browser sequence view was unavailable, but structured taxonomy and GenBank endpoints succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. There are no descendant taxa or classified BacDive strains in the checked backbone/inventory, supporting `strain_count: 0` under repository rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and Svante2 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 23 matching lines were inspected in context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independent target deposit, genome association, extra mapping or separate history record was found within those surfaces. Bare Svante2/svante2 is not an eligible collection accession, and short sequence records cannot supply a missing genome join. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; external marker-gene context is not a record-level gene-function assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated-file ownership and SEEDED status. Future source corrections belong to maintained authority inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not infer a culture accession or species reassignment from a bare strain label or study title.

## Follow-up Checks

For an authorized source refresh, inspect the changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032628 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric matches include SAMEA1032628 for Streptococcus pneumoniae R34-3054, GCA_010326285.1 for Campylobacter jejuni, an unrelated assembly name PDT001032628.1, Salmonella run IDs beginning SRR1032628, and Streptococcus pyogenes sample SAMN41032628. None supports target taxonomy, strain or genome identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
