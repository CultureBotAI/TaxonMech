# YAML Record Review: bromate-reducing bacterium AUS11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_aus11.yaml`
- Started UTC: 2026-10-04T02:13:16Z
- Finished UTC: 2026-10-04T02:14:56Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032696`, bromate-reducing bacterium AUS11. This is a SPECIES-rank placeholder in BACTERIA under unclassified Bacteria (49928), with four lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. The functional wording is part of the source taxon label; the YAML contains no separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_aus11.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_aus11.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded and its complete returned list was inspected; no covered organism/dataset resolved AUS11.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. The cited study's full isolate-specific experimental tables were not accessible through the inspected publisher pages.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220888` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30194` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032696&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032696) confirm identity, exact label, species rank, parent, bacterial domain, code 11 and all four root-first lineage IDs.

The short lineage is the authority's unresolved classification, not missing YAML ancestry. Bromate-reduction wording does not justify inferring a phylum, genus or a placement based on other members of a study. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT denotes NCBI identity, not formal nomenclatural validity or independent experimental verification of every word in the name.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13272` and `curation/seed_scope.tsv:321259` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF951733.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951733.1) is a 1,441-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain AUS11 and taxon 1032696. The isolation-source qualifier describes a biologically active carbon filter receiving dechlorinated tap water. Direct submission was on 2011-05-12. This marker is not a genome assembly or an assay of bromate metabolism.

The sequence cites Davidson and colleagues' 2011 Water Research paper, volume 45, issue 18, pages 6051-6062. Inspected [PubMed XML for PMID 21943884](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref DOI metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) confirm the title, authors and DOI `10.1016/j.watres.2011.09.001`. PubMed explicitly includes JF951733 among the study's deposited GenBank accessions.

The inspected abstract reports 15 bromate-reducing isolates from three sources and heterogeneous nitrate/perchlorate behavior. It also reports no significant filter-performance improvement from the tested bioaugmentation. These aggregate statements cannot assign AUS11 an individual nitrate/perchlorate phenotype, kinetic rate, reductase or respiratory mechanism. The [author institution's USDA ARS publication page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) supplies a consistent study summary but not the missing isolate-specific tables. Browser PubMed access encountered a challenge and the DOI/publisher pages failed or returned 403; structured PubMed/Crossref retrieval succeeded. Search snippets were not used as proof of an isolate-specific experiment.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than universal genome-absence evidence. No additional biological claim is needed to support the record's current NAME-only scope.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules; it does not mean no isolate was cultured in the publication.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded AUS11/AUS 11/AUS-11 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 14 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. Bare AUS11 is not a collection accession. Optional nomenclature, strains and causal/phenotype slots may remain empty. The external study is a future curation lead, not evidence that a required YAML slot was omitted. iModulonDB is not applicable because no listed organism/dataset resolves this unclassified isolate; that result is not negative phenotype evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the current taxonomy-only record. Isolate-specific experimental detail remains unverified for any future functional enrichment.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Before any separately authorized functional curation, inspect the full paper's AUS11-specific rows and conditions, then use a maintained evidence input supported by the generator. Do not hand-edit the generated YAML, infer a reductase from the label, or transfer group-level assay results to AUS11.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032696 --force`, inspect its YAML and rerun both focused validators. Future functional enrichment must first resolve the experimental-table access limit and keep evidence at isolate/condition scope. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the retained taxonomy-only claims.

## Additional Notes

Xanthomonas perforans Aus11, assembly GCA_041647055.1 and taxon 442694, is not this AUS11 merely because the designation matches. Numeric exclusions include SAMEA1032696 for Streptococcus pneumoniae 379678, SAMN41032696 for Streptococcus pyogenes, and Campylobacter jejuni assembly GCA_010326965.1. Their associated genome and ATB rows do not support a target link.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
