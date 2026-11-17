# YAML Record Review: Streptomyces sp. PM7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_pm7.yaml`
- Started UTC: 2026-10-04T01:58:20Z
- Finished UTC: 2026-10-04T01:59:27Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032647`, Streptomyces sp. PM7. The record is a SPECIES-rank placeholder in BACTERIA, parent unclassified Streptomyces (2593676), with ten lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. It makes no gene-function, phenotype, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_pm7.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/streptomyces_sp_pm7.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared the full lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. The record has no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220883` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30190` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032647&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032647) confirm the identifier, label, species rank, parent, domain, code 11 and all ten root-first lineage IDs. Kitasatosporales is the source order and is not replaced with an inferred alternative hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT means identity with this NCBI entry, not formal nomenclatural validity or equivalence with every isolate called PM7. The species rank follows NCBI despite the strain-style label.

## Evidence

The NCBITAXON NAME count of one and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13262` and `curation/seed_scope.tsv:321255` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF766235.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766235.1) is a 1,492-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain PM7 and taxon 1032647. Its source qualifiers identify a coral-reef isolation source in India's Gulf of Mannar Biosphere Reserve. Deepa, Hemalatha, Karuppiah and Sivakumar submitted it on 2011-03-31; the other reference is an unpublished taxonomic investigation and supplies no PMID or DOI.

This marker supports the submitted isolate's identity and stated collection context, not a complete genome, type designation, physiological trait or biosynthetic activity. Exact Assembly search returned zero with a phrase-not-found warning, which is a bounded result rather than proof of genome absence everywhere. The browser sequence view failed, but both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded PM7/PM 7/PM-7 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 66 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. Bare PM7 is not a culture-collection accession. Empty optional nomenclature, strain, phenotype and graph slots are appropriate. iModulonDB is not applicable to the taxonomy-only YAML; external marker context is not a record gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, SEEDED status and the target's full taxon identity. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv`. Require an explicit isolate/deposit crosswalk before attaching any source record sharing only PM7.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate a single canary with `just seed-canary NCBITaxon:1032647 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

The PM7 name matches include unrelated Escherichia, Proteus, Weissella, Klebsiella, Synechococcus, Colletotrichum and archaeal records. BacDive 138739 and StrainInfo 67492 concern Bacillus subtilis PM 7 (taxon 1423), not this Streptomyces. Their grouping and designation do not authorize evidence transfer. Ban-PM7 is a Pasteurella strain. SAMEA1032647 belongs to Streptococcus pneumoniae R34-3072, SAMN41032647 to Streptococcus pyogenes, and SRR11032647 to Salmonella; numeric substrings are not taxon identity links.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
