# YAML Record Review: Wolbachia endosymbiont of Lasioglossum zonulum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_zonulum.yaml`
- Started UTC: 2026-10-08T04:07:08Z
- Finished UTC: 2026-10-08T04:09:59Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036306`, Wolbachia endosymbiont of Lasioglossum zonulum, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT`, mapping status `SEEDED`. All 57 YAML lines were read before judgement.

`data/taxa/PATHS.tsv:14819` and `curation/seed_scope.tsv:322559` resolve this exact record. The scope row was added on 2026-09-13 under the one-source NCBI attestation rule. This is a bacterial source taxon, not its eukaryotic host or all Wolbachia associated with the host genus. It asserts no nomenclature, mapping, synonym, culture deposit, genome, experimental phenotype, or causal graph.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_zonulum.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_lasioglossum_zonulum.yaml --out /private/tmp/wlz-strict.tsv` | Pass; one file, zero errors; the TSV was read and contains only its header. |
| Structured pinned-source comparison | Identity, rank, parent, domain, genetic code, all eleven ancestors, empty synonym fields, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in the pinned type-material, merged-ID, or dropped-ID inventories; the backbone does not mark the node retired. |
| Ignored-inclusive source checks | All six candidate rows/objects read in full; three are unrelated numeric matches. Five source-metadata JSON files and history filenames were separately checked. |
| Current source checks | NCBI Taxonomy XML and Datasets confirm the target. Both sequences returned by the exact-taxonomy query had their complete top-level, source-feature, and reference metadata inspected. Primary publication context was also checked. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded comparisons are diagnostics, not a substitute for corpus reproduction. There is no documented focused reference validator for this record. `just validate-products` is not applicable to this graph-free record. Ignored-inclusive content and filename searches found no separate target history artifact; the embedded seed event was checked directly. No history event or review-status promotion was made.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:222312` agrees with live NCBI Taxonomy XML on taxon 1036306, label, species rank, parent 2640676, bacterial division, and genetic code 11. Datasets independently confirms the identifier, name, rank, and root-inclusive ancestry. Species rank is NCBI's rank for this node, not proof of a formally described bacterial species. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036306&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036306).

All eleven ancestors match the pinned parent chain: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria; Rickettsiales; Anaplasmataceae; Wolbachieae; Wolbachia; unclassified Wolbachia. The tribe and unranked direct parent are preserved. The full backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31856` supplies the same label and identifier, with an empty unique-name field. The backbone's three synonym columns are empty, and the live XML supplies no other names. No unsupported synonym or neighboring host-associated taxon was imported.

## Evidence

**Attestation and seed history.** The sole attestation correctly records `NCBITAXON`, source ID 1036306, the exact label, count 1, unit `NAME`, and the 2026-09-13 snapshot. It counts a taxonomic name, not a genome, culture, infection assay, or host specimen. The scope reason and embedded seed explanation agree. The seed event timestamp `2026-09-13T17:54:04Z` follows the newest extraction time among the raw, ATB, and StrainInfo manifests, as implemented by `_seed_timestamp` in `src/taxonmech/seed.py:139`.

**Sequence context.** An exact Nuccore query, `txid1036306[Organism:noexp]`, returned two records. Both explicitly identify the target taxon and host Lasioglossum zonulum:

- `KP183307.1` is a 446-bp partial `ftsZ` coding sequence from isolate `LaZo`. Its source/reference metadata names Gerth and colleagues' endosymbiont-screen study and a November 2014 submission. The assembly-data comment identifies Sanger sequencing technology; it does not turn this marker into a genome assembly. [KP183307.1](https://www.ncbi.nlm.nih.gov/nuccore/KP183307.1).
- `JF902299.1` is a 623-bp partial COI coding sequence with voucher `BIOUG<CAN>:LASNA393-08.w`, BOLD cross-reference `ASEND062-09.COI-5P`, and source locality Oregon, USA. Its source block gives a collection date of 23 July 2001 and a May 2011 submission in the reference metadata. The specimen voucher is not a microbial culture-collection accession. [JF902299.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902299.1).

Neither inspected source block supplies a registered microbial culture deposit or genome assembly. No equivalence between the two specimens is asserted. Sequence bases, translations, and non-source feature annotations were not evaluated; BOLD was checked only as a GenBank cross-reference, not through an independent BOLD retrieval.

**Publication context.** The bibliography of KP183307.1 retains an unpublished status, but its title identifies Gerth et al.'s published 2015 study, DOI `10.1093/femsec/fiv047`, PMID `25914139`. Publisher metadata, abstract, and relevant methods were inspected. The methods describe a PCR screen using `ftsZ` and sequencing to confirm detections; accession-level details are assigned to supplementary Table S1. This supports interpreting KP183307.1 as marker evidence, not a genome or a demonstrated host-manipulation phenotype. The exact supplementary row was not inspected. [Primary endosymbiont-screen paper](https://academic.oup.com/femsec/article/91/6/fiv047/2594561), [PubMed metadata](https://pubmed.ncbi.nlm.nih.gov/25914139/).

The COI record cites Smith's barcoding study, also with an unpublished status retained in its source metadata. The inspected publisher article, DOI `10.1371/journal.pone.0036514`, explains in its methods that `.w` labels identify bacterial samples associated with host BOLD process IDs. This is specimen context, not evidence for a cultured-strain accession or an ecological mechanism. [Primary barcoding paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514).

The barcoding paper's full Table S2 specimen row was not inspected; its XLS was not retrievable by the web tool during this review session, and the checked local environment lacked a suitable XLS reader. No result here depends on uninspected table cells. The YAML has no literature-backed phenotype or snippet requiring additional support. iModulonDB is not applicable because this record makes no gene, regulator, expression-module, or mechanism claim; the optional marker context does not create one.

## Completeness

No consequential gap was established under the current source-owned model. Exact target scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` is supported as an inventory count. Neither a host-derived isolate name nor a COI voucher establishes a required strain-to-genome relationship. Optional nomenclature, mappings, cross-references, literature evidence, discussion, and causal graphs may correctly remain empty.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`; it resolved one target and found no prior target review or separate history artifact. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All six candidate rows/objects were read completely. The target matches are the backbone, scope, and scientific-name object.

The other three matches are false numeric matches: GenBank objects `ncbi_genbank-0063.jsonl.gz:29437` and `ncbi_genbank-0066.jsonl.gz:30542` have genome size 1036306 but organism uncultured archaeon and taxon 115547; `allthebacteria.tsv.xz:76179` contains the number in a SeqKit checksum and describes Escherichia coli sample SAMEA104040320. None supports a target genome link. Expanded searches for both sequence accessions, the voucher/BOLD codes, and bounded isolate label `LaZo` found no further rows within those roots. All five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The live exact-taxonomy Assembly query returned zero entries with a phrase-not-found warning. That result is not proof that no assembly exists anywhere. The local searches establish bounded pinned-source coverage, not exhaustive online absence or a claim that the bacterium has never been sampled.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the identity, lineage, genetic code, empty synonym fields, source count, attestation, or seed-history assertions. The available marker records do not demonstrate a missing required genome or cultured-strain representation. External study-level findings were not generalized to this entire taxon.

## Recommended Edits

None required for the current generated record. Do not import the numeric catalog matches or turn specimen vouchers and partial gene sequences into culture or genome identities.

Any future taxonomy correction belongs upstream at NCBI and in the pinned ingestion governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A supported enrichment or emission change belongs in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated YAML or append an unearned review event.

## Follow-up Checks

- Before future specimen-level enrichment, inspect Gerth et al.'s complete Table S1 row, Smith et al.'s Table S2 row, and BOLD ASEND062-09 independently. Preserve distinctions between host, taxon, specimen, marker, culture deposit, and genome.
- After an authorized source refresh, compare exact taxon 1036306, all eleven ancestors, genetic code, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `032d58300440f10af0ba6faa474e35a818485625594f46cc77dd73177da9f43f`. Only this new report was written for this target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent sequence analysis, or phenotypic inference was performed. The verdict does not confer human `REVIEWED` status.
