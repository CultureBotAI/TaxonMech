# YAML Record Review: bromate-reducing bacterium WC20

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_wc20.yaml`
- Started UTC: 2026-10-04T02:29:08Z
- Finished UTC: 2026-10-04T02:30:38Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032701`, bromate-reducing bacterium WC20. This is a SPECIES-rank placeholder in BACTERIA under unclassified Bacteria (49928), with four lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. Functional wording belongs to the source label; the YAML contains no separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_wc20.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_wc20.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the complete lineage, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded. All 28 returned rows were inspected; none resolved an organism/dataset for the target WC20.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. The cited paper's isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220893` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30199` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032701&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032701) confirm identity, exact label, species rank, parent, bacterial domain, code 11 and all four root-first lineage IDs.

The short lineage reflects unresolved authority classification, not omitted YAML ancestry. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT denotes identity with the NCBI placeholder, not formal nomenclatural validity or independent verification of every word in the name. Matching WC20 designations do not supply a taxonomic crosswalk.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13278` and `curation/seed_scope.tsv:321264` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF951738.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951738.1) is a 1,217-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain WC20 and explicit taxon 1032701. Its isolation-source qualifier identifies Waller Creek water. Direct submission was on 2011-05-12. This marker is not a genome assembly or a bromate-metabolism assay.

The sequence cites Davidson and colleagues' 2011 Water Research paper, volume 45, issue 18, pages 6051-6062. Inspected [PubMed XML for PMID 21943884](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref DOI metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) confirm title, authors and DOI `10.1016/j.watres.2011.09.001`. PubMed explicitly lists JF951738 among the study's GenBank accessions.

The abstract reports 15 bromate-reducing isolates from three sources, differing nitrate/perchlorate behavior and no significant filter-performance improvement from tested bioaugmentation. These aggregate results cannot assign WC20 an individual nitrate/perchlorate phenotype, kinetic rate, reductase, respiratory mechanism or treatment outcome. The inspected [USDA ARS publication page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) provides study context, not the isolate-specific tables. ScienceDirect returned 403; structured PubMed and Crossref retrieval succeeded. No search snippet was treated as isolate-specific experimental evidence.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query does not establish universal genome absence. No extra biological claim is needed to support the current NAME-only record.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules, not an absence of cultured isolates in the study.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and bounded WC20/WC 20/WC-20/WC_20 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 19 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains and causal/phenotype slots may remain empty. The paper is a future curation lead, not evidence of an omitted required YAML slot. iModulonDB was not applicable because no listed organism/dataset resolves this isolate; absence is not negative phenotype evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the retained taxonomy-only record. Isolate-specific experimental detail remains unverified for future functional enrichment.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Before separately authorized functional curation, inspect WC20-specific experimental rows and conditions, then use a maintained evidence input supported by the generator. Do not hand-edit generated YAML, infer a reductase from the label, or transfer other WC20 isolates' genes and phenotypes.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032701 --force`, inspect its YAML and rerun both focused validators. Future functional enrichment must first resolve experimental-table access and retain isolate/condition scope. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects retained taxonomy-only claims.

## Additional Notes

Pseudomonas sp. WC20 is a separate authority entry, 1526644, in `data/raw/ncbitaxon_taxa.tsv:392943`, `data/catalog/ncbi_names-0009.jsonl.gz:23024` and `curation/seed_scope.tsv:462413`. Live taxonomy and Datasets independently resolve that ID under unclassified Pseudomonas. Its two inspected Nuccore entries are KJ784469.1 (1,456-base partial 16S) and KM234124.1 (430-base partial phaC), both explicitly assigned to 1526644 with wastewater and Pakistan: Lahore qualifiers. Their direct submissions are in 2014, with an unpublished bioplastic-production study. These differ from the target's source context and do not establish synonymy, a missing phaC claim or a Pseudomonas placement for 1032701. Separate IDs alone are not proof of biological distinctness; no inspected authority crosswalk justifies transfer.

Planctomycetota bacterium WC_20 (2026780), assembly GCA_020059145.1, is another designation match, represented as Planctomycetes in BV-BRC. SAMEA1032701 instead belongs to Streptococcus pneumoniae 306435 (1313), including GCA_001101385.1/.2, GCF_001101385.1 and ATB run ERR069816. Their source chains do not support a target genome link.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
