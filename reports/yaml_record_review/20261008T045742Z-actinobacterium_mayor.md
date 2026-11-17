# YAML Record Review: actinobacterium Mayor

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinobacterium_mayor.yaml`
- Started UTC: 2026-10-08T04:53:55Z
- Finished UTC: 2026-10-08T04:57:42Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036314`, actinobacterium Mayor, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:52018` (unclassified Actinomycetes), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 45 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14826` and `curation/seed_scope.tsv:322566` resolve the exact target. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. The record denotes the isolate-associated NCBI node, not an inferred genus or formally named species. There are no synonyms, nomenclature, taxonomy mappings, strain blocks, genome links, experimental evidence, or causal graphs in the record.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/actinobacterium_mayor.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/actinobacterium_mayor.yaml --out /private/tmp/amayor-strict.tsv` | Pass; one file, zero errors; the TSV was read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, genetic code, all seven ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All three matching rows/objects read completely. Five source-metadata JSON files and history filenames separately checked. |
| Current authority and primary publication | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, PubMed metadata, and relevant publisher article text inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded comparisons are diagnostics, not proof of corpus reproduction. No documented focused reference validator applies to this record. `just validate-products` is not applicable to the graph-free YAML. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history entry or review-status promotion was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222319` agrees with current NCBI Taxonomy XML on identifier 1036314, scientific name, species rank, parent 52018, bacterial division, and genetic code 11. Datasets supplies the same identifier, label, rank, and root-inclusive ancestry. The lowercase source label is preserved. NCBI assigns species rank to this node despite its unresolved lower-level classification; the record must not substitute a genus or formal binomial. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036314&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036314).

All seven ancestors match the pinned chain: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; unclassified Actinomycetes. The direct parent correctly retains `NO_RANK`. No order, family, or genus occurs in that source chain, so their omission is faithful source representation, not a missing-lineage finding. The full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31863` agrees with the identifier and label and has an empty unique-name field. All three backbone synonym columns are empty, and current Taxonomy XML supplies no other names. `EXACT` grounding concerns the identity of this node; it does not claim that its finer taxonomic placement is resolved.

## Evidence

**Attestation and history.** The sole attestation correctly names `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. The backbone and native name object support it. A name count is not a culture, genome, or experimental count. The scope reason and embedded seed explanation agree, including timestamp `2026-09-13T17:54:04Z`; neither implies human `REVIEWED` status.

**Primary sequence context.** The exact Nuccore query `txid1036314[Organism:noexp]` returned one record, UID 334302957. Complete top-level, source-feature, and reference metadata identifies `JF799090.1`, an 862-bp partial 16S rRNA sequence. The source explicitly names actinobacterium Mayor, strain Mayor, taxon 1036314, river water, and South Africa: Tyume River, Eastern Cape Province. It names no culture-deposit accession or genome assembly. Its references include the 2013 paper below and a direct submission dated 10 April 2011 by Okoh, Olaniran, and Agunbiade. The sequence was created on 5 June 2011 and updated on 30 August 2013. Sequence bases and non-source feature annotations were not evaluated. [JF799090.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799090.1).

**Primary publication context.** Luvuyo and colleagues' 2013 mixed-culture study is DOI `10.1186/1472-6750-13-62`, PMID `23915393`, PMCID `PMC3750929`, BMC Biotechnology 13:62. The publisher's abstract and bacterial-strain methods explicitly pair Mayor with JF799090, independently confirming the sequence link; the sequence also cites this paper. The methods describe Tyume River isolates, agreeing with the sequence source. The companion Methylobacterium sp. Obi has HQ537130, which must not be transferred to Mayor. Experimental results concern a mixed culture, not Mayor alone. The paper's Actinobacterium sp. wording and comparison to OR-221 do not supply a formal NCBI genus assignment or an exact synonym. Relevant identity, methods, and mixed-culture passages were inspected, along with PubMed metadata; figures, quantitative reproducibility, and the complete reference corpus were not audited. [Primary paper](https://link.springer.com/article/10.1186/1472-6750-13-62), [PubMed metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23915393&retmode=xml).

The YAML asserts no habitat, bioflocculation performance, culture conditions, gene function, or mechanism. These optional literature observations were not generalized to the taxon or represented as required missing fields. Other search results, including a conference-abstract lead, were not used as inspected evidence. iModulonDB is not applicable because no gene, locus, regulator, expression-module, or functional claim is present.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. It does not deny the existence of the studied isolate. A laboratory culture designation is not a registered culture-deposit accession, and a ribosomal marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, comprising backbone, scope, and native scientific name, were fully read. Expanded searches for JF799090, the paper DOI/PMID/PMCID, and Actinobacterium sp. Mayor naming variants returned only the same three target-name rows in those roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. This is a bounded result, not proof that no assembly exists elsewhere. Local checks establish pinned-source coverage, not exhaustive online absence. Optional synonyms, nomenclature, mappings, genome links, literature evidence, discussions, and graphs may correctly remain empty. Unresolved taxonomic placement is carried from NCBI rather than filled by inference.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's identity, lineage, genetic code, empty synonym fields, strain count, attestation, or seed-history assertions. The short lineage is source-faithful, and the primary paper does not demonstrate a required missing culture or genome relationship. Its mixed-culture results are not individual-isolate assertions in this YAML.

## Recommended Edits

None required for the generated record. Do not manufacture an order, family, genus, synonym, deposit, genome link, or single-isolate phenotype from the inspected publication.

Future taxonomy corrections belong upstream at NCBI and in pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, inspect the complete experimental evidence, retain the exact JF799090 identity link, and separate mixed-culture from axenic results. Verify proposed culture or genome identifiers directly.
- After an authorized source refresh, compare exact taxon 1036314, all seven ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary. Any finer placement must come from authority evidence, not an inferred name.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `6c3dc5eaea0803266c0f283acce0c533c882791dca214d4d7dbdd893613b5821`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or experimental replication was performed. The verdict does not confer human `REVIEWED` status.

The PubMed API abstract was shorter than the publisher's structured abstract and did not itself contain the accession-bearing passage; that passage was read directly on the publisher page. This report does not claim a complete assay, figure, or full-paper audit merely because the article's HTML was accessible.
