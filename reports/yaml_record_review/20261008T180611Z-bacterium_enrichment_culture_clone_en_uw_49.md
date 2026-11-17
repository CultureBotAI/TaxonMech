# YAML Record Review: bacterium enrichment culture clone En_UW_49

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_49.yaml`
- Started UTC: 2026-10-08T18:02:35Z
- Finished UTC: 2026-10-08T18:06:11Z
- Verdict: pass

## Target

One complete generated `TaxonRecord` was resolved and read: `NCBITaxon:1036435`, bacterium enrichment culture clone En_UW_49. Its fields are `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` status and zero associated strain records. The NCBI rank does not establish a formally named species or pure isolate.

An ignored-inclusive filename inventory of `data/taxa/`, `reports/yaml_record_review/` and `history/` found only this YAML for the identifier/label/slug pattern and no previous report for the stem. This individual review did not edit generated records, sources, scope, history or status.

## Validation

Focused commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_49.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_49.yaml --out /private/tmp/uw49-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The full TSV contains only its header.
- Complete record-to-backbone, four-ancestor, attestation, scope, path-index and embedded seed-event comparisons: pass.
- Live primary taxonomy and complete linked nucleotide/protein inspections: completed, with scope limits below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift and global statistics gates. Focused comparisons do not establish corpus reproduction. No undocumented per-record reproduction/history gate was invented. The embedded seed event was manually checked against source and scope evidence; no matching standalone history artifact was found in the bounded searches.

Graph grounding validation is not applicable because the YAML has no curator-added graph. iModulonDB was not run: there is no stored gene, regulator, pathway or expression-module claim, and this clone was not resolved to a covered strain/dataset. This is not evidence of database absence.

## Identity and Grounding

Complete relevant rows were inspected at `data/raw/ncbitaxon_taxa.tsv:222437`, `data/catalog/ncbi_names-0005.jsonl.gz:31981`, `data/taxa/PATHS.tsv:14944` and `curation/seed_scope.tsv:322684`. Identifier, scientific label, rank, parent, code, snapshot and empty synonym sets agree. All four root-first ancestor labels/ranks match the pinned backbone. A complete backbone scan found no direct children for the target.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036435&retmode=xml) agrees on name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036435) supplies ancestor IDs 1, 131567, 2 and 48479. EFetch's root omission from `LineageEx` is a format difference, not lineage drift. Its environmental-samples division is compatible with bacterial domain. No additional names appear in the response.

Exact scans of pinned type-material, merged-ID and dropped-record inventories found no target rows. `EXACT` describes supported NCBI name/identifier grounding, not a cultured-species assignment. No adjacent clone, similar fragment, broader taxon or culture deposit was substituted for this identity.

## Evidence

The sole `NCBITAXON` attestation traces to the scientific-name and backbone rows: one assertion with unit `NAME`. This is a source-assertion count, not an organism, strain or genome count. Its 2026-09-13 snapshot and the embedded seed event match the source and scope evidence. `SEEDED` remains appropriate; this report does not confer human review status.

The exact Nuccore query `txid1036435[Organism:noexp]` returned UID 336092414. Its complete [HQ630173.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092414&rettype=gb&retmode=xml), including all features and sequence, identifies En_UW_49 and taxon 1036435. It contains 346 bases of partial `nosZ`, with both CDS ends partial, codon start 3 and translation table 11. The source is an environmental sample from an anode biofilm, with H2S-supplemented mineral medium. No strain, culture-deposit or geographic qualifier is supplied. The study reference is unpublished; direct submission is dated 17 November 2010. These annotations describe a submitted fragment, not a pure isolate, measured reductase activity or whole-genome phenotype.

The explicitly linked [AEI00831.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00831.1&rettype=gb&retmode=xml) was separately read in full. It contains 114 amino acids, the same clone/taxon and an explicit partial CDS link to HQ630173.1. Actual and declared nucleotide/protein lengths agree, and the submitted translation exactly matches the protein sequence. No non-ACGT nucleotide or X/B/Z/J amino-acid ambiguity was detected. This checks annotation consistency, not independent translation, alignment or biochemical activity. The computational PRK02888/CDD:235082 region ends at residue 109, not 114; its validation label does not demonstrate experimental activity for this clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text hit for HQ630173 or the clone label. Printed pages 54 and 92 were reread completely. Page 54's enrichment-sequence range includes HQ630173; page 92 warns that a single DGGE band cannot establish purity. This supports study context, not species identity. Rasterized text and supplements were not exhaustively audited.

Exact accession/clone searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. Exact web queries for HQ630173 and AEI00831, plus a clone query excluding the already inspected NCBI taxonomy listing, returned no results. These bounded queries do not prove publication absence. No community phenotype or neighboring-clone archive membership was transferred.

## Completeness

The taxonomy-seed assertions are complete enough for the supported scope. Optional synonyms, nomenclature, mappings, strain/deposit records, genome links, traits and graphs do not require invented values. Zero associated strains agrees with the inventory, not a biological claim of unculturability.

Exact scans of all seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The compressed-content search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned four rows, all read completely. Adding HQ630173, AEI00831, the submitted study title and the related PLOS DOI returned the same four rows. All five applicable `SOURCE.json` files, excluded from the content scan, were separately read without a target identity match. Ignored-independent history filename searches found no matching artifact.

Three matches are the backbone, scientific-name and scope rows. The fourth, `data/catalog/ncbi_genbank-0054.jsonl.gz:17264`, is not a target genome: GCA_058711085.1 is a Streptococcus pneumoniae assembly, taxon/species taxon 1313, with isolate code 1036435 and genome size 2010306. Its isolate string is a numerical collision with the reviewed NCBI identifier. The unrelated assembly's sample, project and publication references were not attributed to En_UW_49.

The exact NCBI Assembly query returned zero items with a phrase-not-found warning. This is not universal genome absence. No supported culture-deposit or whole-genome connection emerged from the inspected sources. The partial gene is not a genome record and does not justify organism-level traits.

## Findings

None found in the supported YAML assertions.

Counts: 0 blocker, 0 major, 0 minor.

Unresolved organism-level identity and limited fragment evidence constrain future enrichment but do not contradict this taxonomy-only record. No invalid field, broken stored reference, unsupported phenotype, source conflict or status inflation was identified.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status.

Future taxonomy corrections belong first at NCBI and then in the pinned ingestion workflow maintained in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. These are ownership routes, not proposed changes. Do not hand-edit generated records or add a phenotype from the medium note, fragment annotation or unrelated assembly.

## Follow-up Checks

No blocker remains for this individual verdict. Future biological curation requires explicit clone-to-organism/deposit evidence and claim-specific support, preserving partial-sequence limitations. Broader literature and supplementary-material searches are optional discovery work, not prerequisites for accepting the current seed.

After an authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun schema and strict validators, and then execute applicable corpus reproduction, provenance, history and QC gates. This review did not run generation or claim those global gates passed.

## Additional Notes

One new timestamped Markdown report is the only repository write for this sequential individual review. Eukaryota, other record YAMLs and existing worktrees were untouched. No curation event, status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The target SHA-256 was unchanged before and after review: `08c166c6598cd61a1b2e051acb6cf736aa2b517df363cd4d74895f5e0228c961`.

All absence statements are limited to the named roots, queries and inspected responses, not an exhaustive external knowledge census.
