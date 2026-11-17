# YAML Record Review: Enterococcus sp. CIFRI D-TSB15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_sp_cifri_d_tsb15.yaml`
- Started UTC: 2026-10-08T05:17:03Z
- Finished UTC: 2026-10-08T05:22:28Z
- Verdict: pass with minor issues

## Target

One generated `TaxonRecord`, `NCBITaxon:1036317`, Enterococcus sp. CIFRI D-TSB15. All 54 YAML lines were read before judgement. It is `SPECIES`, `BACTERIA`, parent `NCBITaxon:2608891` (unclassified Enterococcus), genetic code 11, grounding `EXACT`, mapping status `SEEDED`, with zero strain entries and one NCBI name attestation.

`data/taxa/PATHS.tsv:14829` and `curation/seed_scope.tsv:322569` resolve the exact record. It contains no synonyms, nomenclature, taxonomy mappings, genome links, literature assertions, discussions, or causal graphs. This review distinguishes correct source reproduction from a remaining biological classification discrepancy.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/enterococcus_sp_cifri_d_tsb15.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/enterococcus_sp_cifri_d_tsb15.yaml --out /private/tmp/ed15-strict.tsv` | Pass; one file, zero errors; output TSV read and contains only its header. |
| Pinned-source comparison | Identity, parent, genetic code, ten ancestors, empty synonyms, attestation, scope/index membership, and seed explanation agree. |
| Identifier lifecycle | No target row in pinned type-material, merged-ID, or dropped-ID inventories; backbone retirement field empty. |
| Ignored-inclusive source inspection | Three candidate rows/objects read completely; five source-metadata JSON files parsed and history filenames checked. |
| Current sources | NCBI Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, marker source/reference metadata, relevant primary article text, and PubMed metadata inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded source comparison is not a corpus-reproduction check. No documented focused reference validator applies; `just validate-products` is inapplicable to the graph-free record. Ignored-inclusive searches found no target-specific separate history artifact; the embedded seed event was checked. No history or review-status mutation was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222322` agrees with live NCBI Taxonomy XML for identifier 1036317, exact scientific name, species rank, parent 2608891, bacterial division, and genetic code 11. Datasets supplies the same identifier, label, rank, and root-inclusive ancestry. Taxonomy XML supplies no other names. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036317&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036317).

The ten ancestors are root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Lactobacillales; Enterococcaceae; Enterococcus; unclassified Enterococcus. All identifiers, labels, ranks, and positions match the pinned chain and current authority. The direct parent correctly has `NO_RANK`. A full backbone scan found no immediate children.

The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31866` agrees, with an empty unique-name field. All three backbone synonym columns are empty. `EXACT` identifies this NCBI node; it does not resolve the external genus discrepancy described below or authorize a replacement taxon identifier.

## Evidence

**Attestation and history.** The sole attestation correctly gives `NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and the 2026-09-13 snapshot. This counts an authority name, not cultures, genomes, or experiments. The scope date/reason and embedded seed explanation agree, including timestamp `2026-09-13T17:54:04Z`. No human `REVIEWED` status is implied by this report.

**Primary sequence identity.** Exact query `txid1036317[Organism:noexp]` returns Nuccore UID 334303317, accession `JF799879.1`, a 1,448-bp partial 16S rRNA sequence. Complete top-level, source-feature, and reference metadata names Enterococcus sp. CIFRI D-TSB15, strain CIFRI D-TSB15, taxon 1036317, marine soil sediment, and location `India: W.B.`. No culture-deposit or genome-assembly accession occurs in its source feature. Its references are an unpublished salt-tolerant-bacteria study and an 11 April 2011 direct submission by Behera, Sharma, Das, Chanda, and Patra. Creation and update dates are both 5 June 2011. Bases and non-source feature annotations were not evaluated. [JF799879.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799879.1).

**Accession-linked classification discrepancy.** Behera and colleagues' Table 2 links D-TSB-15 to JF799879 and lists Vagococcus fluvialis as the nearest-strain identification; Table 1 gives Digha soil. These passages were read in the author-uploaded primary text. This is a different genus, not merely a more specific Enterococcus name. It conflicts with the current authority placement but does not itself supply a corrected NCBI mapping. [Primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis). Publisher metadata and abstract confirm DOI `10.1007/s40011-014-0440-6`, online publication in 2014 and volume 85, pages 957-964 (2015). [Publisher](https://link.springer.com/article/10.1007/s40011-014-0440-6).

**Name-matched resistance study, identity unresolved.** Liu and colleagues' paper, DOI `10.1128/AAC.01605-12`, PMID `23070165`, PMCID `PMC3535926`, mentions one CIFRI D-TSB15-labelled isolate among samples collected in Shandong, China. Its abstract identifies the three cfr-positive isolates as E. thailandicus 3-38 and W3 and E. faecalis W9-2, not this CIFRI-labelled isolate. The inspected methods do not establish a deposit or accession chain to the Indian sediment isolate. Name reuse does not justify importing its cohort's resistance context or the other isolates' genes/plasmids. The abstract and relevant methods were read from the institutional PDF text; PubMed metadata and full abstract were separately verified. [Primary PDF](https://www.openagrar.de/servlets/MCRFileNodeServlet/Document_derivate_00001298/SD201329.pdf), [PubMed metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23070165&retmode=xml).

The YAML asserts no habitat, salt tolerance, antimicrobial resistance, gene function, or mechanism. None of those optional claims was added. iModulonDB is not applicable because the target record contains no gene, locus, regulator, expression-module, or functional assertion. Other search leads were not treated as inspected evidence.

## Completeness

No source-owned strain or genome omission was established. Exact scans returned no target rows in the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, or BactoTraits inventories. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. This does not deny the existence of the sequenced isolate. Laboratory names and marker sequences do not supply registered culture deposits or assemblies.

Identifier, label, and slug resolution included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`, finding one target and no prior target report. Source searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, backbone, scope, and native name, were fully read. Expanded searches for JF799879, both paper DOIs, PMID 23070165, PMCID PMC3535926, and designation variants returned only the same three target-name rows. Five `SOURCE.json` files and history filenames were separately checked without ignoring files.

The exact live Assembly query returned zero results with a phrase-not-found warning. This is bounded evidence, not proof of genome absence everywhere. The unresolved external classification is a follow-up caveat, not permission to invent a synonym, genus replacement, deposit, or genome relationship.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: unresolved cross-source genus discrepancy.** The accession-linked study identifies a nearest match in Vagococcus, whereas NCBI and the faithful generated record retain Enterococcus. The evidence above establishes a discrepancy requiring clarification, not which classification is correct. This is a non-blocking biological/provenance caveat: the identifier still denotes the intended source node, no unsupported phenotype is present, and no seeder defect or definitive wrong grounding was proved. Do not interpret the pass of source/schema checks as resolution of this discrepancy.

The authority-level owner is NCBI taxonomy/sequence curation. In this repository, an accepted correction would enter through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`, then `src/taxonmech/seed.py`; the generated YAML is not the correction surface. The discrepancy is preserved in this report rather than silently choosing a genus.

## Recommended Edits

No immediate generated-file edit. Prioritize human review of the conflicting identification before biological reuse or literature enrichment. Retain the exact marker link and both source interpretations; do not add Vagococcus fluvialis as an exact synonym or replace the NCBI parent without an accepted authority correction.

If a supported correction is accepted upstream, refresh the pinned authority input through the maintained ingestion paths above and regenerate with focused tests. Any future persistent discussion/evidence representation must be implemented through an authorized maintained seeder or overlay design, not hand-written into generated YAML. Scope decisions remain owned by `curation/seed_scope.tsv`.

Do not transfer the Chinese cohort's resistance results or other isolates' plasmid identifiers through the CIFRI label alone. That is an enrichment boundary, not an additional defect in the current graph-free YAML.

## Follow-up Checks

- Resolve the genus discrepancy using authoritative sequence/taxonomy evidence and the primary study's original table/figure context. No independent sequence alignment, type-strain comparison, or definitive reclassification was performed here.
- Before any resistance enrichment, verify the Chinese isolate's exact identifier/deposit chain and isolate-specific results; the current name match is insufficient.
- After an authorized source correction, recheck taxon 1036317, all ten ancestors, aliases, lifecycle status, and eligible strain evidence; inspect a one-record seed canary, rerun schema/strict validation, and run corpus, provenance, rendering, documentation, and QC gates before publication. Validate append-only history if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `fe8aa2cdb3d489c1f3e3a7d6cae1913ad699efaa69e1ec1c40f2e0ae9894c2b9`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, previous report, GitHub item, or worktree was modified. Eukaryota was not re-reviewed or edited. No paid research, outreach, source refresh, or experimental replication was performed.

The PMC browser page presented an access check. The institutional PDF initially supplied readable metadata, abstract, and methods text, but later requests returned a security check, so no complete PDF or visual audit is claimed. The Behera publisher figure request and a bounded direct download timed out; the figure was not visually inspected. Its relevant table text was accessible through the author-uploaded transcription, whose garbled growth symbols were not converted to numeric phenotypes. Full-paper, figure, and assay-reproducibility audits were not performed.
