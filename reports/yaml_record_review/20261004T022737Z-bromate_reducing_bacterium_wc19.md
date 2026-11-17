# YAML Record Review: bromate-reducing bacterium WC19

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_wc19.yaml`
- Started UTC: 2026-10-04T02:26:31Z
- Finished UTC: 2026-10-04T02:27:37Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032700`, bromate-reducing bacterium WC19. This is a SPECIES-rank placeholder in BACTERIA under unclassified Bacteria (49928), with four lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. Functional wording is part of the source label; no separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion appears in the YAML.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_wc19.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_wc19.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded. All 28 returned rows were inspected; none resolved an organism/dataset for WC19.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220892` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30198` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032700&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032700) confirm identity, exact label, species rank, parent, bacterial domain, code 11 and all four root-first lineage IDs.

The short lineage reflects unresolved authority classification, not omitted YAML ancestry. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT denotes identity with this NCBI placeholder, not formal nomenclatural validity or independent verification of every word in the name. Matching WC19 or WC_19 designations in other taxa do not supply a taxonomic crosswalk.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13277` and `curation/seed_scope.tsv:321263` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF951737.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951737.1) is a 1,437-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain WC19 and explicit taxon 1032700. Its isolation-source qualifier says Waller Creek water; it does not identify a carbon-filter isolate. Direct submission was on 2011-05-12. This marker is neither a genome assembly nor a bromate-metabolism assay.

The sequence cites Davidson and colleagues' 2011 Water Research paper, volume 45, issue 18, pages 6051-6062. Inspected [PubMed XML for PMID 21943884](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref DOI metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) confirm title, authors and DOI `10.1016/j.watres.2011.09.001`. PubMed explicitly lists JF951737 among the deposited GenBank accessions.

The inspected abstract describes 15 bromate-reducing isolates from three sources, heterogeneous nitrate/perchlorate behavior, and no significant filter-performance improvement from tested bioaugmentation. Those aggregate results do not assign WC19 an individual nitrate/perchlorate phenotype, kinetic rate, reductase, respiratory mechanism or treatment outcome. The [USDA ARS author-institution publication page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) provides consistent study context but not the isolate-specific tables. The ScienceDirect article URL returned 403; structured PubMed and Crossref retrieval succeeded. Search snippets were not used as isolate-specific experimental proof.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query result does not establish universal genome absence. No extra biological claim is needed to support the current NAME-only record.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules. That value does not assert that no isolate was cultured in the study.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and bounded WC19/WC 19/WC-19/WC_19 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 23 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. A short strain designation is not a collection accession. Optional nomenclature, strains and causal/phenotype slots may remain empty. The study is a future curation lead, not evidence of an omitted required YAML slot. iModulonDB was not applicable because no listed organism/dataset resolves this isolate; absence from it is not negative phenotype evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the retained taxonomy-only record. Isolate-specific experimental detail remains unverified for any future functional enrichment.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Before separately authorized functional curation, inspect the full paper's WC19-specific rows and conditions, then use a maintained evidence input supported by the generator. Do not hand-edit generated YAML, infer a reductase from the label, or transfer other isolates' sources or group-level assay results to WC19.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032700 --force`, inspect its YAML and rerun both focused validators. Future functional enrichment must first resolve the experimental-table access limit and retain isolate/condition scope. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the retained taxonomy-only claims.

## Additional Notes

Burkholderia pseudomallei WC19 (28450), assembly GCA/GCF_018228345.1, occurs in NCBI, GTDB, BV-BRC and GOLD sources but is not this taxon merely because the designation matches. Candidatus Peribacterales bacterium WC_19 (2711152), assembly GCA_020059285.1, is another unrelated designation match. No inspected authority merge, synonym or explicit crosswalk supports transferring either genome.

SAMEA1032700 belongs to Streptococcus pneumoniae 268660 (1313), including GCA_001147305.1/.2, GCF_001147305.1 and ATB run ERR069806. A BioSample number is not an NCBI taxonomy identifier. Its ATB sample and assembly evidence remain attached to that source chain, not WC19.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
