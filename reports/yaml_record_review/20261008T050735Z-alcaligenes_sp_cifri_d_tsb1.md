# YAML Record Review: Alcaligenes sp. CIFRI D-TSB1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alcaligenes_sp_cifri_d_tsb1.yaml`
- Started UTC: 2026-10-08T05:01:41Z
- Finished UTC: 2026-10-08T05:07:35Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036315`, Alcaligenes sp. CIFRI D-TSB1. All 54 YAML lines were read before judgement. It is a bacterial `SPECIES` node under `NCBITaxon:259357` (unclassified Alcaligenes), with genetic code 11, grounding `EXACT`, mapping status `SEEDED`, zero strain entries, and one NCBI name attestation.

The exact target resolves at `data/taxa/PATHS.tsv:14827` and `curation/seed_scope.tsv:322567`. There are no synonyms, nomenclature, taxonomy mappings, genome links, record-level literature assertions, discussions, or causal graphs. The isolate designation is not itself a registered culture-deposit accession or a formal species name.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/alcaligenes_sp_cifri_d_tsb1.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/alcaligenes_sp_cifri_d_tsb1.yaml --out /private/tmp/acifri-strict.tsv` | Pass; one file, zero errors; output TSV read and contains only its header. |
| Structured pinned-source comparison | Identifier, label, rank, parent, genetic code, all ten ancestors, empty synonym columns, attestation, scope/index membership, and seed explanation agree. |
| Exact identifier status | No target row in pinned type-material, merged-ID, or dropped-ID inventories; no retirement flag in the backbone. |
| Ignored-inclusive source checks | All three source candidates fully read; five source-metadata JSON files parsed and history filenames checked. |
| Live authority and literature | Taxonomy XML, Datasets taxonomy, exact sequence/assembly queries, sequence source/reference metadata, and relevant primary publication passages inspected. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, and whole-corpus history validation. The bounded source comparison is not a corpus-reproduction gate. No documented focused reference validator applies here; `just validate-products` is inapplicable to the graph-free record. Ignored-inclusive content and filename searches found no target-specific separate history artifact; the embedded seed event was checked directly. No history or review-status mutation was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222320` agrees with current NCBI Taxonomy XML: taxon 1036315, Alcaligenes sp. CIFRI D-TSB1, species rank, parent 259357, bacterial division, and genetic code 11. Datasets independently returns the same taxon, name, rank, and root-inclusive ancestry. No other names are supplied in the Taxonomy XML. [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036315&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036315).

The ten source ancestors are root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Burkholderiales; Alcaligenaceae; Alcaligenes; unclassified Alcaligenes. Every identifier, label, rank, and position agrees with the pinned parent chain; the unclassified direct parent correctly has `NO_RANK`. The full backbone scan found no immediate children.

The native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31864` was read completely and agrees, with an empty unique-name field. All three backbone synonym columns are empty. `EXACT` grounding identifies this NCBI node, not a resolved formal species assignment. The publication identification discussed below must not silently replace NCBI's classification.

## Evidence

**Attestation and history.** The sole attestation correctly records `NCBITAXON`, the exact identifier and source label, count 1, unit `NAME`, and the 2026-09-13 snapshot. That unit counts an authority name, not cultures, genomes, or experiments. The 2026-09-13 scope reason and embedded seed explanation agree; the seed timestamp is `2026-09-13T17:54:04Z`. This read-only review does not promote the record to human `REVIEWED` status.

**Primary sequence.** The exact Nuccore query `txid1036315[Organism:noexp]` returns UID 334303316, accession `JF799878.1`, a 1,419-bp partial 16S rRNA sequence. Complete top-level, source-feature, and reference metadata explicitly identify the target taxon and strain CIFRI D-TSB1, with marine soil sediment and location `India: W.B.`. No culture-deposit or assembly accession occurs in that source feature. The references are an unpublished salt-tolerant-bacteria study and an 11 April 2011 direct submission by Behera, Sharma, Das, Chanda, and Patra. Creation and update dates are both 5 June 2011. Sequence bases and non-source annotations were not audited. [JF799878.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799878.1).

**Accession-linked primary study.** Behera and colleagues' paper, DOI `10.1007/s40011-014-0440-6`, was published online in October 2014 and assigned to volume 85, pages 957-964 (2015). Publisher metadata and abstract were inspected; relevant methods and Tables 1-2 were read in the author-uploaded full-text transcription. Table 2 explicitly links D-TSB-1 and JF799878, listing Alcaligenes faecalis as the nearest-strain identification. Table 1 places D-TSB-1 in Digha soil. This narrower, marker-based identification is retained as literature context, distinct from NCBI's unresolved label. It supplies neither an NCBI merger nor an exact taxonomic synonym. Garbled growth symbols in the transcription were not interpreted as quantitative tolerance data; no numerical phenotype is asserted here. [Publisher](https://link.springer.com/article/10.1007/s40011-014-0440-6), [Author-uploaded primary text](https://www.researchgate.net/publication/267156636_Functional_Screening_and_Molecular_Characterization_of_Halophilic_and_Halotolerant_Bacteria_by_16S_rRNA_Gene_Sequence_Analysis).

**Closest-relative context, not isolate recovery.** Trivedi and colleagues' citrus-rhizosphere study, DOI `10.1038/ismej.2011.100`, uses CIFRI D-TSB1/JF799878 as a closest-relative entry for clone group BP4 in Figure 4, with 99.2% identity. The relevant methods and figure page were inspected, including a visual rendering of PDF page 10. This is not evidence that the same Indian isolate was recovered in the citrus study or that its community-level functional results belong to this taxon. [Primary PDF](https://swfrec.ifas.ufl.edu/hlb/database/pdf/00002854.pdf).

The YAML makes no habitat, salinity, gene-function, or mechanism claim. The inspected publication context therefore does not reveal an unsupported phenotype in the record. iModulonDB is not applicable because no gene, locus, regulator, expression-module, or functional assertion is present. Genomes from other CIFRI-designated organisms were not transferred by shared name fragments.

## Completeness

No consequential gap was established under the source-owned model. Exact target scans of the seven raw BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin, and BactoTraits inventories returned no rows. With no descendants or eligible BacDive entries found, `strain_count: 0` agrees with the pinned inventory. This does not mean the biological isolate does not exist. A marker sequence is not a genome assembly, and a study designation is not a verified collection deposit.

Identifier, label, and slug searches included ignored files under `data/taxa`, `reports/yaml_record_review`, `history`, and `curation`, resolving one target with no previous target report. Source scans used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three candidates, backbone, scope, and scientific-name object, were fully read. Expanded searches for JF799878, both publication DOIs, and CIFRI D-TSB1/D-TSB-1 variants returned only those same three target-name rows. Five `SOURCE.json` files were separately parsed and history filenames checked without ignoring files.

The live exact-taxonomy Assembly query returned zero results with a phrase-not-found warning. This is a bounded query result, not proof that no assembly exists elsewhere. Optional literature, nomenclature, mappings, deposits, and genome links need not be manufactured from nearby organisms or sequence-similarity results.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated record's identity, lineage, genetic code, empty synonyms, strain count, attestation, or seed-history assertions. The external paper's narrower identification is recorded above without reconciling it into NCBI's carried lineage; it is not a demonstrated seeder defect or a required missing mapping.

## Recommended Edits

None required for this record. Do not replace the label with Alcaligenes faecalis, infer a culture deposit, add a genome from a shared CIFRI prefix, or transfer citrus-community observations to this isolate.

Any supported taxonomy correction belongs upstream at NCBI, then in pinned ingestion through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Enrichment or emission changes belong in the responsible maintained adapter and `src/taxonmech/seed.py`, with focused tests; scope decisions belong in `curation/seed_scope.tsv`. Generated YAML, catalogs, and pages are not independent correction surfaces.

## Follow-up Checks

- Before optional literature enrichment, verify complete table layouts and assay evidence in the Behera paper, retain the accession link, and distinguish its marker-based identification from NCBI taxonomy. Quantitative tolerance was not validated here.
- For a future source refresh, recheck taxon 1036315, all ten ancestors, names, lifecycle rows, and eligible strain evidence before a one-record seed canary. New culture or genome links require explicit identity evidence.
- After authorized regeneration, rerun schema and strict validation, then corpus, provenance, rendering, documentation, and QC gates before publication. Validate separate append-only history only if later curation creates an event.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Initial and pre-report SHA-256: `036240baa7a590aa12e0e4ecafdca4e4d05163804367140de589ae90ed2c9137`. Only this new report was written for the target. No YAML, source, scope, lifecycle, history, generated page, prior report, GitHub item, or worktree was modified. Eukaryota was neither re-reviewed nor edited. No paid research, outreach, source refresh, independent phylogeny, or experimental replication was performed.

The Behera publisher page offered subscription access; no purchase or protected download was attempted. Its author-uploaded text was inspected directly, not treated as a search snippet. The citrus PDF was publicly available. `pdftoppm` was unavailable, so native PDFKit rendered its relevant page successfully for visual inspection. The web screenshot calls did not expose inspectable image payloads. These targeted reads are not a full-paper, complete-figure, or assay-reproducibility audit.
