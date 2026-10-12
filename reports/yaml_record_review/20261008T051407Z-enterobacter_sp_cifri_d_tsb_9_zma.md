# YAML Record Review: Enterobacter sp. CIFRI D-TSB-9-ZMA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_cifri_d_tsb_9_zma.yaml`
- Started UTC: 2026-10-08T05:08:53Z
- Finished UTC: 2026-10-08T05:14:07Z
- Verdict: pass

## Target

One generated `TaxonRecord`: `NCBITaxon:1036316`, Enterobacter sp. CIFRI D-TSB-9-ZMA. All 54 YAML lines were read before judgement. The record is `SPECIES`, `BACTERIA`, parent `NCBITaxon:2608935` (unclassified Enterobacter), genetic code 11, grounding `EXACT`, mapping status `SEEDED`, with zero listed strains and one NCBI name attestation.

`data/taxa/PATHS.tsv:14828` and `curation/seed_scope.tsv:322568` identify this exact target. It contains no synonyms, nomenclature, taxonomy mappings, genome links, literature assertions, discussions, or causal graphs. It denotes the isolate-associated NCBI node, not an inferred formal species, culture deposit, or similarly named strain.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/enterobacter_sp_cifri_d_tsb_9_zma.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/enterobacter_sp_cifri_d_tsb_9_zma.yaml --out /private/tmp/ecifri-strict.tsv` | Pass; one file, zero errors; TSV read and contains only its header. |
| Structured pinned-source comparison | Identity, parent, genetic code, all ten ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target rows in pinned type-material, merged-ID, or dropped-ID inventories; backbone retirement field empty. |
| Ignored-inclusive source inspection | All three candidates read completely; five source-metadata JSON files parsed and history filenames checked. |
| Live identity and evidence | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, full marker source/reference metadata, primary article passages, and PubMed metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. Bounded comparisons do not prove corpus reproduction. No documented focused reference validator applies. `just validate-products` is inapplicable to this graph-free YAML. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded event was checked. No curation event, history entry, or review-status promotion was made.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:222321` matches live NCBI Taxonomy XML for identifier 1036316, exact label, species rank, parent 2608935, bacterial division, and genetic code 11. Datasets confirms the same taxon, name, rank, and root-inclusive ancestry. Taxonomy XML supplies no other names. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036316&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036316).

All ten ancestors match the pinned chain and live authority: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Enterobacter; unclassified Enterobacter. The direct parent correctly has `NO_RANK`. A complete backbone scan found no immediate children.

The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31865` agrees, with an empty unique-name field. All three backbone synonym columns are empty. `EXACT` refers to identity at this NCBI node, not a claim that its species-level placement has been resolved. The paper's narrower identification below is kept distinct from the carried NCBI classification.

## Evidence

**Attestation and history.** The sole attestation correctly gives `NCBITAXON`, the target identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. It does not count cultures or genomes. The scope date/reason and embedded seed explanation agree; the event timestamp is `2026-09-13T17:54:04Z`. An external review report does not confer human `REVIEWED` status.

**Primary marker metadata.** Exact Nuccore query `txid1036316[Organism:noexp]` returned UID 334303324. The full top-level, source-feature, and reference metadata identifies `JF799886.1`, a 1,430-bp partial 16S rRNA sequence, organism Enterobacter sp. CIFRI D-TSB-9-ZMA, strain CIFRI D-TSB-9-ZMA, and taxon 1036316. Its source is marine water, location `India: W.B.`; no culture-deposit or assembly accession is supplied in the source feature. References comprise an unpublished salt-tolerant-bacteria study and a direct submission dated 11 April 2011 by Behera, Sharma, Das, Chanda, and Patra. Creation and update dates are both 5 June 2011. Bases and non-source feature annotations were not evaluated. [JF799886.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799886.1).

**Accession-linked study.** The Behera paper's Table 2 pairs D-TSB-9-ZMA with JF799886 and a nearest-strain identification of Enterobacter hormaechei; Table 1 gives Digha water. These inspected author-uploaded passages establish the study link, not an NCBI reclassification. [Primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Publisher metadata confirms DOI `10.1007/s40011-014-0440-6`, online publication in 2014 and volume 85, pages 957-964 (2015). [Publisher](https://link.springer.com/article/10.1007/s40011-014-0440-6).

**Excluded phenotype transfer.** Wong-Villarreal and colleagues' 2016 biosurfactant study, DOI `10.5604/17331331.1204478`, PMID `30015442`, concerns isolates from Jatropha rhizosphere in Chiapas, Mexico. Its methods describe sequence comparison against GenBank; results call LS1 related to the CIFRI taxon, and Table III gives 95% identity. Thus LS1 is not established as the same isolate, and its biosurfactant results cannot be transferred to CIFRI D-TSB-9-ZMA. The author-uploaded methods, results, and table transcription were inspected; PubMed independently confirms article metadata and abstract. [Primary text](https://www.researchgate.net/publication/303851965_Characterization_of_Bacteria_Isolation_of_Bacteria_from_Pinyon_Rhizosphere_Producing_Biosurfactants_from_Agro-Industrial_Waste), [PubMed metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30015442&retmode=xml).

The YAML asserts no habitat, salinity, biosurfactant phenotype, gene function, or mechanism. Optional literature context is therefore not a missing mandatory field or an unsupported claim in this record. iModulonDB is not applicable: there is no gene, locus, regulator, expression-module, or functional assertion. Other search leads were not treated as inspected evidence.

## Completeness

No consequential source-owned omission was established. Exact taxon scans found no rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. No descendants were found. Consequently `strain_count: 0` agrees with the pinned eligible inventory, without denying the existence of the sequenced isolate. Neither a bare laboratory designation nor a related strain in another paper supplies a valid culture-deposit join. A partial 16S marker is not a genome assembly.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`, locating one record and no previous target report. Source searches used `rg --no-ignore --hidden -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, backbone, scope, and scientific-name object, were read losslessly. Expanded searches for JF799886, the two publication DOIs, and CIFRI D-TSB-9-ZMA/D-TSB-9-ZMA variants yielded only those same three name rows. A separate ignored-inclusive search for PMID 30015442 in the same roots returned no match. Five `SOURCE.json` files and history filenames were separately checked.

The exact live Assembly query returned zero results with a phrase-not-found warning. That is bounded evidence, not an exhaustive claim that no genome exists online. Empty optional nomenclature, synonyms, mappings, literature, strain, and genome fields remain defensible under the current model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in identity, lineage, genetic code, synonym handling, strain count, attestation, or seed history. The primary study's finer identification is retained as external context rather than silently replacing NCBI's node. The LS1 study is a near match, not proof of a missing strain relationship or phenotype for this record.

## Recommended Edits

None required. Do not relabel the record as Enterobacter hormaechei from marker similarity alone or assign LS1's identity, habitat, or phenotype to it. Do not create genome or deposit links from the CIFRI prefix.

Taxonomy corrections belong upstream at NCBI and then in pinned ingestion through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Supported enrichment or emission changes belong in the maintained source adapter and `src/taxonmech/seed.py`, with focused tests; scope changes belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages must not be patched independently.

## Follow-up Checks

- Before optional enrichment, verify proposed identifiers and exact study-to-isolate links; independently inspect assay/table layouts before adding quantitative phenotypes. No assay reproducibility or independent sequence analysis was performed here.
- After an authorized source refresh, recheck taxon 1036316, the ten ancestors, names, lifecycle rows, and eligible strain evidence before a one-record seed canary.
- Rerun schema and strict validation after authorized regeneration, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate append-only history if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `f7a176af19f5cf3b527287bb623a3d0753dbfdc5bfebbb83acc0901852bc35ad`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, page, earlier report, GitHub item, or worktree was changed. Eukaryota was not re-reviewed or edited. No paid research, outreach, source refresh, or experimental replication was performed.

The biosurfactant publisher page, PDF, and DOI redirect failed in the browser fetcher; the author-uploaded primary text and public PubMed API were available. The Behera publisher page exposed metadata and abstract, with subscription access for the full article; the inspected body passages came from its author-uploaded text. No protected download was attempted. Garbled growth symbols in that text were not converted into salt-tolerance numbers. These targeted source reads do not constitute full-paper, full-figure, or quantitative assay audits.
