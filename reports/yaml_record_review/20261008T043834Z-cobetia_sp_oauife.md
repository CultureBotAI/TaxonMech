# YAML Record Review: Cobetia sp. OAUIFE

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cobetia_sp_oauife.yaml`
- Started UTC: 2026-10-08T04:33:15Z
- Finished UTC: 2026-10-08T04:38:34Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036311`, Cobetia sp. OAUIFE, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2609414` (unclassified Cobetia), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 53 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14823` and `curation/seed_scope.tsv:322563` resolve the exact record. Its scope row was added on 2026-09-13 under the one-source NCBI attestation rule. This is the NCBI taxon bearing the OAUIFE isolate designation, not a named Cobetia species inferred from sequence similarity or another member of a studied consortium. The record has no synonyms, nomenclature, mappings, strain blocks, genome links, experimental evidence, or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/cobetia_sp_oauife.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/cobetia_sp_oauife.yaml --out /private/tmp/coauife-strict.tsv` | Pass; one file, zero errors; TSV read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all ten ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All four candidate rows/objects read completely, including an unrelated numerical hit. Five source-metadata JSON files and history filenames separately checked. |
| Current authority and publication checks | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, and PubMed publication metadata and abstract inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded comparisons are diagnostics, not substitutes for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to the graph-free YAML. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or review-status promotion was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222316` agrees with live NCBI Taxonomy XML on identifier 1036311, scientific name, species rank, parent 2609414, bacterial division, and genetic code 11. Datasets supplies the same identifier, label, rank, and root-inclusive ancestry. The species rank is NCBI's rank for this node; the isolate wording is not grounds for inventing a formal species name or changing the rank. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036311&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036311).

All ten ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Oceanospirillales; Halomonadaceae; Cobetia; unclassified Cobetia. The direct parent correctly retains `NO_RANK`. The full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31860` agrees with this exact identifier and label and has an empty unique-name field. All three backbone synonym columns are empty, and current Taxonomy XML supplies no other names. `EXACT` grounding is supported for this NCBI node, not for a neighboring isolate or formally named species.

## Evidence

**Attestation and seed history.** The sole attestation correctly records `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The backbone and native scientific-name object support it. This count concerns a name, not a strain deposit, genome, or experiment. The scope reason and embedded seed explanation agree, including timestamp `2026-09-13T17:54:04Z`; neither implies human `REVIEWED` status.

**Primary sequence context.** The exact Nuccore query `txid1036311[Organism:noexp]` returned one record, UID 334302959. Its complete top-level, source-feature, and reference metadata identifies `JF799092.1`, an 849-bp partial 16S rRNA sequence. The source explicitly names Cobetia sp. OAUIFE, strain OAUIFE, taxon 1036311, ocean water, and South Africa: Algoa Bay, Eastern Cape Province. It supplies no culture-deposit accession or genome assembly. The references include the 2012 study below and a direct submission dated 10 April 2011 by Okoh, Olaniran, Cosa, and Mabinya. The sequence was created on 5 June 2011 and updated on 30 June 2015. Sequence bases and non-source feature annotations were not evaluated. [JF799092.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799092.1).

**Primary publication context.** The sequence explicitly cites Ugbenyen and colleagues' 2012 thermostable-bioflocculant study, PMID `22829793`, DOI `10.3390/ijerph9062108`, International Journal of Environmental Research and Public Health 9(6):2108-2120. PubMed API metadata and the complete abstract were inspected. The abstract explicitly pairs OAUIFE with JF799092, confirming the accession-based identity connection; sequence similarity to Cobetia sp. L222 does not establish isolate equivalence. The paper's abstract describes sediment from Algoa Bay, whereas the nucleotide source field says ocean water. That sample-context discrepancy is unresolved and must be preserved before any habitat enrichment. The YAML makes neither assertion, so this is not an internal record inconsistency. Full text, figures, assay reproducibility, and mechanistic interpretation were not audited. [PubMed source](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22829793&retmode=xml).

The YAML asserts no bioflocculation performance, habitat, growth condition, gene function, or causal mechanism. Optional literature therefore does not establish a missing required trait or graph. Other publication and consortium search results were leads only; their experimental claims were not attributed to OAUIFE. iModulonDB is not applicable because the reviewed YAML has no gene, locus, regulator, expression-module, or functional assertion requiring that adapter.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned source inventory. It does not deny the existence of the studied isolate. OAUIFE alone is not a registered culture accession, and a partial ribosomal marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target report or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All four candidates were fully read. Three are the target's backbone, scope, and native scientific-name rows. The fourth, `data/catalog/ncbi_genbank-0065.jsonl.gz:2052`, is `GCA_977532945.1`, an uncultured bacterium classified as taxon 77133: its genome-size field equals 1036311. This numerical coincidence supplies no OAUIFE identity or genome relationship.

Expanded ignored-inclusive searches for OAUIFE, JF799092, PMID 22829793, PMCID PMC3397367, and the primary DOI found only the same three target-name rows within those ten roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files. The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning; this is a bounded result, not proof that no assembly exists elsewhere. Local checks establish pinned-source coverage, not exhaustive online absence.

Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and graphs may correctly remain empty under the documented model. The environmental-source discrepancy needs resolution only before a later workflow asserts that particular habitat or sample claim; it does not undermine the accession-linked taxon identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, genetic code, empty synonym fields, source count, attestation, or seed-history assertions. External water-versus-sediment descriptions remain unresolved source context, not a finding against an unasserted YAML habitat field. Neither the marker nor the unrelated metagenome establishes a required missing strain-genome link.

## Recommended Edits

None required for the generated record. Do not transfer a neighboring isolate's identity, count the numerical assembly-search hit as a genome link, or add habitat or functional claims without authorized evidence-backed curation.

Future taxonomy corrections belong upstream at NCBI and in the pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature or habitat enrichment, inspect the complete primary paper and reconcile its sediment description with the nucleotide record's ocean-water field. Preserve the exact JF799092 identity link and distinguish individual-isolate from consortium results.
- After an authorized source refresh, compare exact taxon 1036311, all ten ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary. Verify any proposed culture or genome identifier directly.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `613eefa393f7023f6e54d3ff5d962e200ffe50b732c4c752820fe469802618aa`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed. The verdict does not confer human `REVIEWED` status.

PMC and PubMed browser pages presented access checks, and the publisher page returned HTTP 429. Direct DOI opening was unavailable. The public PubMed API nevertheless returned the complete abstract and explicit DOI/PMID/PMCID mapping, which agrees with the marker's cited reference. This verifies the bibliographic identifiers through source metadata, not successful independent DOI resolution or inspection of the full article. Search-index excerpts were not substituted for inspected primary text.
