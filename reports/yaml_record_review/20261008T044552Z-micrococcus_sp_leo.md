# YAML Record Review: Micrococcus sp. Leo

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micrococcus_sp_leo.yaml`
- Started UTC: 2026-10-08T04:41:41Z
- Finished UTC: 2026-10-08T04:45:52Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036312`, Micrococcus sp. Leo, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2620948` (unclassified Micrococcus), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 53 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14824` and `curation/seed_scope.tsv:322564` resolve the exact record. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. This is the NCBI taxon bearing the Leo isolate designation, not an inferred named Micrococcus species, a culture deposit, or an entire experimental consortium. The record has no synonyms, nomenclature, mappings, strain blocks, genome links, experimental evidence, or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/micrococcus_sp_leo.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/micrococcus_sp_leo.yaml --out /private/tmp/mleo-strict.tsv` | Pass; one file, zero errors; the TSV was read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all ten ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All three matching rows/objects read completely. Five source-metadata JSON files and history filenames separately checked. |
| Live identity and publication checks | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, and two publication abstracts/metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded comparisons are diagnostics, not proof of corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to the graph-free YAML. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or status promotion was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222317` agrees with current NCBI Taxonomy XML on identifier 1036312, scientific name, species rank, parent 2620948, bacterial division, and genetic code 11. Datasets supplies the same identifier, label, rank, and root-inclusive ancestry. Species rank is NCBI's rank for this isolate-associated node; no formal species name or different rank was inferred. The source spelling is Leo, not an invented uppercase alias. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036312&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036312).

All ten ancestors match the pinned chain: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales; Micrococcaceae; Micrococcus; unclassified Micrococcus. The direct parent correctly retains `NO_RANK`. The full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31861` agrees with the exact taxon and label and has an empty unique-name field. All three backbone synonym columns are empty, and current Taxonomy XML supplies no other names. `EXACT` grounding is supported for this node, not for neighboring isolates or experimental partners.

## Evidence

**Attestation and history.** The sole attestation names `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The complete backbone and native name object support it. A taxonomic-name assertion does not count cultures, genomes, or experiments. The scope reason and embedded seed explanation agree, including timestamp `2026-09-13T17:54:04Z`; neither implies human `REVIEWED` status.

**Primary sequence context.** The exact Nuccore query `txid1036312[Organism:noexp]` returned one record, UID 334302958. Its complete top-level, source-feature, and reference metadata identifies `JF799091.1`, an 855-bp partial 16S rRNA sequence. The source explicitly names Micrococcus sp. Leo, strain Leo, taxon 1036312, ocean water, and South Africa: Algoa Bay, Eastern Cape Province. No culture-deposit accession or genome assembly is named in that source block. The sole reference is a direct submission dated 10 April 2011 by Okoh, Olaniran, Mabinya, and Cosa; creation and last update are both 5 June 2011. Sequence bases and non-source feature annotations were not evaluated. [JF799091.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799091.1).

**Publication context, with scope limits.** Two primary abstracts explicitly name Micrococcus sp. Leo:

- The publisher page for Okaiyeto and colleagues' 2014 study verifies DOI `10.1134/S000368381406012X`, Applied Biochemistry and Microbiology 50:601-608, and describes a Leo bioflocculant study. The complete abstract and publication metadata were inspected; full subscription text was not. [Publisher article](https://link.springer.com/article/10.1134/S000368381406012X).
- PubMed API metadata and the complete abstract verify the 2013 paper, PMID `24135818`, DOI `10.3390/ijerph10105097`, PMCID `PMC3823338`. Its subject is a consortium of Halomonas sp. Okoh and Micrococcus sp. Leo. Those results cannot be attributed to Leo alone. Full text and figures were not inspected. [PubMed source](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24135818&retmode=xml).

Neither inspected abstract establishes the exact JF799091 accession link, and the sequence record cites neither paper. These publications are relevant name-matched context, not a substitute for the direct sequence-to-taxon assertion. An exact publication-to-accession connection remains unverified. No assay values, sample-origin statements from search snippets, consortium properties, or genus-wide phenotype were imported into the verdict.

The YAML asserts no bioflocculation performance, habitat, growth condition, gene function, or mechanism. Optional literature therefore does not demonstrate a missing required trait or graph. iModulonDB is not applicable because no gene, locus, regulator, expression-module, or functional claim is present. Secondary pages and search-index excerpts were leads only.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. It does not deny that the Leo isolate exists or was studied. A bare isolate designation is not a registered culture accession, and a partial ribosomal marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, comprising backbone, scope, and native scientific name, were fully read. Expanded searches for JF799091, PMID 24135818, both paper DOIs, and Micrococcus Leo naming variants returned only the same three target-name rows within those roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. This is a bounded result, not proof that no assembly exists elsewhere. These local checks establish pinned-source coverage, not exhaustive online absence. Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and graphs may correctly remain empty under the documented model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, genetic code, empty synonym fields, strain count, attestation, or seed-history assertions. Unverified publication-to-accession correspondence and unavailable full papers limit optional enrichment, not the independently verified identity asserted by this YAML.

## Recommended Edits

None required for the generated record. Do not turn a marker into a genome link, silently change the source label, or transfer consortium properties to an individual strain.

Future taxonomy corrections belong upstream at NCBI and in pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, inspect complete primary papers, establish the exact publication-to-accession connection, and preserve individual-isolate versus consortium scope. Verify any proposed culture, genome, or habitat assertion directly.
- After an authorized source refresh, compare taxon 1036312, all ten ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `ed9c835e47fa8989327fd077a6a5e81febb5cba65746bfc96b3cf917e007a9c3`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed. The verdict does not confer human `REVIEWED` status.

The 2013 study's PubMed and PMC browser pages presented access checks, and the MDPI publisher page returned HTTP 429. The public PubMed API supplied its complete abstract and explicit DOI/PMID/PMCID mapping. This is bibliographic verification through source metadata, not inspection of the full paper or independent DOI redirection. The 2014 publisher abstract was accessible, but its full text was subscription content. No payment, access-control workaround, or full-paper review was performed.
