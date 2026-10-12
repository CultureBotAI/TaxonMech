# YAML Record Review: Pseudomonas sp. RL2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_rl2.yaml`
- Started UTC: 2026-10-04T02:03:23Z
- Finished UTC: 2026-10-04T02:04:04Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032653`, Pseudomonas sp. RL2. This is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pseudomonas (196821), with ten lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. No gene-function, phenotype, causal-graph or genome-equivalence claim is made.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_rl2.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pseudomonas_sp_rl2.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220885` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30192` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032653&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032653) confirm the identifier, label, species rank, parent, bacterial domain, code 11 and all ten root-first lineage IDs. The Pseudomonadales/Pseudomonadaceae/Pseudomonas chain remains source-carried.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder; it does not assert formal nomenclatural validity. RL2 remains distinct from Pseudomonas RL1 and from unrelated RL-2 strain designations. The species rank follows NCBI despite the strain-style label.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13265` and `curation/seed_scope.tsv:321257` confirm identifier, slug and the NCBI-only scope reason. The seed event at 2026-09-13T17:54:04Z records that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ625018.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ625018.1) is a 1,500-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain RL2 and taxon 1032653. Its source qualifiers explicitly identify soil and China. The only reference is Rao's direct submission on 2010-11-12; it supplies no PMID or DOI.

RL2's accession, sequence length, country qualifier and submission date were checked independently. The explicit China qualifier is present here, whereas the previously reviewed RL1 entry supplied only a soil qualifier and a submitter address. Shared authorship does not justify transferring collection metadata between them.

A partial marker is not a genome assembly, phenotype result or type designation. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than universal genome-absence evidence. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded RL2/RL 2/RL-2 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 99 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

No independently supported target culture deposit, genome association, extra source mapping or separate history record was found within those surfaces. Bare RL2 is not a culture-collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; the external marker is not a record gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the source identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit isolate/deposit evidence before transferring metadata from RL1 or any unrelated RL-2 designation.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032653 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded name matches include Kandleria vitulina RL 2 (BacDive 5378, StrainInfo 10473) and Paraperlucidibaca baekdonensis RL-2 (taxon 748120, BacDive 8210, StrainInfo 407422). The latter's old Moraxellaceae name, type-material rows and GOLD Go0031602 refer to that separate taxon. Bacillus RL2, Gordonia YC-RL2, Ec-RL2-1X, RL_2_* metagenome isolates and community-study labels also do not identify this Pseudomonas.

Numeric exclusions include SAMEA1032653 for Streptococcus pneumoniae 40241, SAMN41032653 for Streptococcus pyogenes, Salmonella run SRR11032653, and unrelated SeqKit checksums. No matching substring supplies a target genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
