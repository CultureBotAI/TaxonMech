# YAML Record Review: bromate-reducing bacterium AUS24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_aus24.yaml`
- Started UTC: 2026-10-04T02:20:38Z
- Finished UTC: 2026-10-04T02:23:44Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032699`, bromate-reducing bacterium AUS24. This is a SPECIES-rank placeholder in BACTERIA under unclassified Bacteria (49928), with four lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. The functional wording belongs to the source taxon label. The YAML contains no separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_aus24.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_aus24.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the full lineage, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded; all 28 returned rows were inspected and no organism/dataset resolved AUS24.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220891` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30197` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032699&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032699) confirm identity, exact label, species rank, parent, bacterial domain, code 11 and all four root-first lineage IDs.

The short lineage reflects the authority's unresolved classification, not omitted YAML ancestry. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT denotes identity with NCBI, not formal nomenclatural validity or independent experimental verification of every word in the name. Other study isolates do not establish a phylum or genus for AUS24.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13275` and `curation/seed_scope.tsv:321262` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF951736.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951736.1) is a 1,347-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain AUS24 and explicit taxon 1032699. Its isolation-source qualifier describes a biologically active carbon filter receiving dechlorinated tap water. Direct submission was on 2011-05-12. This is a marker sequence, not a genome assembly or a bromate-metabolism assay.

The sequence cites Davidson and colleagues' 2011 Water Research paper, volume 45, issue 18, pages 6051-6062. Inspected [PubMed XML for PMID 21943884](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref DOI metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) confirm the title, authors and DOI `10.1016/j.watres.2011.09.001`. PubMed explicitly includes JF951736 among the deposited GenBank accessions.

The inspected abstract describes 15 bromate-reducing isolates from three sources, heterogeneous nitrate/perchlorate behavior, and no significant filter-performance improvement from the tested bioaugmentation. Those aggregate results do not assign AUS24 a particular nitrate/perchlorate phenotype, kinetic rate, reductase, respiratory mechanism or treatment outcome. The [USDA ARS author-institution publication page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) supplies consistent study context but not isolate-specific tables. The inspected ScienceDirect article URL returned 403; structured PubMed and Crossref retrieval succeeded. Search snippets were not used as isolate-specific experimental proof.

Exact Assembly search returned zero with a phrase-not-found warning. This is a bounded query result, not universal genome-absence evidence. No additional biological claim is needed to support the current NAME-only record.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules. That count does not assert that the publication lacked a cultured isolate.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded AUS24/AUS 24/AUS-24 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 12 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. Bare AUS24 is not a collection accession. Optional nomenclature, strains and causal/phenotype slots may remain empty. The external study is a future curation lead, not evidence of a missing required YAML slot. iModulonDB was not applicable because no listed organism/dataset resolves this isolate; its absence is not negative phenotype evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the current taxonomy-only record. Isolate-specific experimental detail remains unverified for future functional enrichment.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Before separately authorized functional curation, inspect the full paper's AUS24-specific rows and conditions, then use a maintained evidence input supported by the generator. Do not hand-edit generated YAML, infer a reductase from the label, or transfer group-level assay results to AUS24.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032699 --force`, inspect its YAML and rerun both focused validators. Future functional enrichment must first resolve the experimental-table access limit and retain isolate/condition scope. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the retained taxonomy-only claims.

## Additional Notes

Numeric search collisions include SAMEA1032699 for Streptococcus pneumoniae R34-3074, assembly GCA/GCF_001148925, and SAMN41032699 for Streptococcus pyogenes 23GA0210, assembly GCA_044061535. Associated ATB rows retain those unrelated identities and do not support a target genome link.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
