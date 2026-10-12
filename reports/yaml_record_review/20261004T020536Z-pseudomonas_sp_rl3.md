# YAML Record Review: Pseudomonas sp. RL3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_rl3.yaml`
- Started UTC: 2026-10-04T02:04:51Z
- Finished UTC: 2026-10-04T02:05:36Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032654`, Pseudomonas sp. RL3. It is a SPECIES-rank placeholder in BACTERIA under unclassified Pseudomonas (196821), with ten lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. No gene-function, phenotype, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_rl3.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pseudomonas_sp_rl3.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the complete lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220886` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30193` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032654&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032654) confirm identifier, label, species rank, parent, bacterial domain, code 11 and all ten root-first lineage IDs. The Pseudomonadales/Pseudomonadaceae/Pseudomonas chain is retained from the authority.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT denotes the specific NCBI placeholder, not formal nomenclatural validity. The strain-style label does not override NCBI's species rank. RL3 is not automatically identical to RL1, RL2 or any organism bearing RL-3.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13266` and `curation/seed_scope.tsv:321258` confirm identifier, slug and the NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ625019.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ625019.1) is a 1,502-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain RL3 and taxon 1032654. Its source qualifiers explicitly identify soil and China. The only reference is Rao's direct submission on 2010-11-12; no PMID or DOI is supplied.

The sequence accession and source qualifiers were checked for RL3 itself. Similarity of name, sequence length or submission history to the neighboring Pseudomonas entries does not establish strain equivalence. The marker does not demonstrate a whole genome, physiological trait or type designation.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than universal genome-absence evidence. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded RL3/RL 3/RL-3 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 67 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

No independently supported target culture deposit, genome association, extra source mapping or separate history record was found within those surfaces. Bare RL3 is not a registered collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; external marker context is not a record gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit isolate/deposit evidence before transferring RL-3 genome links or metadata from neighboring RL records.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032654 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

The prominent RL-3 genome matches concern Sphingobium ummariense: species 420994, strain 1346791, BacDive 14190, GCA/GCF_000447205.1, IMG 2571042663 and BV-BRC 1346791.3. Its GOLD chain Go0044672/Gp0044672/Ga0042186 and CCM 7431 deposit do not support a link to Pseudomonas RL3. The unversioned BacDive GCA accession was not rewritten or transferred.

Other name collisions include Streptomyces RL3, Neurospora RL3-8A, Leptolyngbya RL_3_1, other RL_3_* metagenome isolates and community studies. Numeric exclusions include SAMEA1032654 for Streptococcus pneumoniae R34-3204, SAMN41032654 for Streptococcus pyogenes, Salmonella run SRR11032654, Campylobacter assembly GCA_010326545.1 and an unrelated SeqKit checksum. These are not target identity links.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
