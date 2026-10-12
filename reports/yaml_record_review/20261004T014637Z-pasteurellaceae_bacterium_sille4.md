# YAML Record Review: Pasteurellaceae bacterium Sille4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_sille4.yaml`
- Started UTC: 2026-10-04T01:45:45Z
- Finished UTC: 2026-10-04T01:46:37Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032632`, Pasteurellaceae bacterium Sille4. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. It asserts no phenotype, gene function, causal graph or genome equivalence.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_sille4.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_sille4.yaml` passed for one file with zero errors and refreshed the strict-validator TSV.

Read-only structured checks verified complete lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or independent history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220879` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30186` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032632&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032632) confirm identity, parent, rank, domain, code 11 and all nine root-first lineage IDs. NCBI's placement through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae is retained.

The full backbone scan found no synonyms or children. Complete type-material, merged-ID and dropped inventories contain no own-ID row. Sille4's strain-style name does not override the source's species rank. EXACT refers to NCBI grounding, not formal nomenclatural validity, a collection accession or a named-species assignment beyond the explicit source taxon.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note reproduce the raw inventory. `data/taxa/PATHS.tsv:13257` and `curation/seed_scope.tsv:321251` agree on identifier, slug and NCBI-only scope reason. The seed event correctly records that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HM626597.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626597.1) is a 474-base partial RpoB coding sequence, genomic DNA, strain Sille4 and taxon 1032632. Source qualifiers give Denmark and a harbor-seal host. Direct submission by Christensen, Bisgaard and Hansen occurred on 2010-07-05.

The entry's other reference is marked unpublished and has no PMID or DOI. Its title concerns Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. That study-level title does not establish an isolate-level synonym, type designation or species reassignment. The YAML appropriately makes none of those inferences. A short RpoB marker does not establish a complete genome or an experimentally demonstrated phenotype.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof of universal genome absence. Primary taxonomy and GenBank structured endpoints succeeded; the evidence above comes from inspected source responses rather than search snippets.

## Completeness

Complete BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventory scans found no exact target row. No descendant taxon or classified BacDive strain was found in the complete backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and Sille4 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 24 matches were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target collection deposit, assembly association, extra mapping or separate history record was found within those surfaces. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; externally inspected RpoB annotation is context, not a gene-function assertion in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source identity, generated-file ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. An explicit isolate-level crosswalk is required before adding a named-species synonym or culture-based genome association.

## Follow-up Checks

For an authorized refresh, inspect changed source evidence, regenerate one canary with `just seed-canary NCBITaxon:1032632 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric matches include SAMEA1032632 for Streptococcus pneumoniae R34-3203; IMG 2931032632 for Sphingobium sp. B2D3D; GCA_010326325.1 for Campylobacter jejuni; unrelated Salmonella run IDs; and Streptococcus pyogenes sample SAMN41032632. None supports Sille4 taxonomy, strain or genome identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
