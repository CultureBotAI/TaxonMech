# YAML Record Review: Pasteurellaceae bacterium Delphsu4b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_delphsu4b.yaml`
- Started UTC: 2026-10-04T01:37:43Z
- Finished UTC: 2026-10-04T01:38:29Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032629`, Pasteurellaceae bacterium Delphsu4b. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It contains no phenotype, gene-function, causal-graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_delphsu4b.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_delphsu4b.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons verified the full lineage, inventory matches, source attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused equivalent was substituted. There are no curator-added graph terms or independent history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220876` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30183` support the YAML's identifier and scientific name. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032629&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032629) confirm rank, parent, domain, code 11 and all nine root-first lineage identifiers. Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae retain NCBI's placement.

The full backbone scan found no synonyms or children, and complete structured scans of type-material, merged-ID and dropped inventories found no own-ID row. Delphsu4b is not Delphsu4a (1032624): the separately inspected live source taxa and their sequence qualifiers retain both labels and identifiers. Similar strain labels, a shared host/location and common study context are not an identity crosswalk. EXACT does not imply formal nomenclatural validity, and the strain-style suffix does not override NCBI's SPECIES rank.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13253` and `curation/seed_scope.tsv:321248` confirm ID, slug and NCBI-only scope reason. The seed event repeats that reason while preserving SEEDED status.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HM626594.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626594.1) is a 466-base partial RpoB coding sequence with genomic DNA molecule type, strain Delphsu4b and taxon 1032629. Source qualifiers give Canada and a harbor-seal host. This differs from Delphsu4a's separately inspected HM626589.1 and its explicit taxon 1032624; no sequence identity or biological equivalence between the two was inferred.

Christensen, Bisgaard and Hansen directly submitted the sequence on 2010-07-05. Its other reference is marked unpublished and supplies no PMID or DOI. That reference's title discusses Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. A study title cannot transfer the proposed species name or type status to every sampled isolate; the record correctly asserts neither transfer.

A short RpoB fragment is not a complete genome or direct physiological evidence. Exact Assembly search returned zero with a phrase-not-found warning, which is a bounded query result rather than proof of genome absence everywhere. The browser sequence view failed, but the structured taxonomy and GenBank endpoints succeeded.

## Completeness

Complete BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventory scans found no exact target row. There are no descendants in the full backbone or classified BacDive strains in the checked inventory, supporting `strain_count: 0` under the source-counting contract.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier, label, slug and Delphsu4b spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 23 matching lines were inspected in context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independent target collection deposit, supported genome association, extra source mapping or separate history record was found within those searched surfaces. Bare Delphsu4b is not a registered collection accession. Optional nomenclature, strain, phenotype and graph slots need not be fabricated. iModulonDB is not applicable to the taxonomy-only YAML; external RpoB sequence context is not a record-level gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the generated-file boundary, separate source identity and SEEDED status. Future corrections belong in maintained authority inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not merge Delphsu4b with Delphsu4a or a named species without an explicit authoritative reassignment.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032629 --force`, inspect its YAML and rerun both focused validators. Run the documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Unrelated numeric hits were excluded using structured source context: SAMEA1032629 describes Streptococcus pneumoniae R34-3220; PDT001032629.1 names another assembly; SRR10326290 through SRR10326299 are Salmonella runs; and SAMN41032629 describes Streptococcus pyogenes. Identifier substrings do not provide taxon or strain support.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
