# YAML Record Review: bacterium enrichment culture clone En_UW_46

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_46.yaml`
- Started UTC: 2026-10-08T17:46:24Z
- Finished UTC: 2026-10-08T17:49:28Z
- Verdict: pass

## Target

Exactly one generated `TaxonRecord` was resolved and read completely: `NCBITaxon:1036432`, bacterium enrichment culture clone En_UW_46. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` status and zero associated strain records. NCBI's species rank does not establish a formally named species or pure isolate.

The ignored-inclusive filename inventory of `data/taxa/`, `reports/yaml_record_review/` and `history/` found only the target YAML for the identifier, label and slug pattern and no previous report for this stem. No other target was judged in this individual review. Generated YAML, sources, scope, history and status were not edited.

## Validation

The existing environment was used with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_46.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_46.yaml --out /private/tmp/uw46-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The complete TSV contains only its header.
- Complete target comparison with the pinned backbone, four ancestors, attestation, scope, path index and embedded seed event: pass.
- Current primary taxonomy and full linked nucleotide/protein inspection: completed, with scope limits below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, global statistics and generated-site drift. Focused source comparison does not prove corpus reproduction. No undocumented per-record reproduction/history gate was invented. The embedded seed event was checked manually against source and scope evidence; no matching standalone history artifact was identified in the bounded searches.

Graph grounding validation is not applicable because the record has no curator-added graph. iModulonDB was not run: the YAML has no gene, regulator, pathway or expression-module claim, and this environmental clone has not been resolved to a covered strain/dataset. That is not negative evidence about database contents.

## Identity and Grounding

Complete relevant evidence was inspected at `data/raw/ncbitaxon_taxa.tsv:222434`, `data/catalog/ncbi_names-0005.jsonl.gz:31978`, `data/taxa/PATHS.tsv:14941` and `curation/seed_scope.tsv:322681`. The identifier, scientific label, rank, parent, genetic code, snapshot and empty synonym sets agree. The four root-first ancestor labels/ranks match the pinned backbone. A complete backbone scan found no direct children for the target.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036432&retmode=xml) confirms the name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036432) supplies all four ancestor IDs: 1, 131567, 2 and 48479. EFetch's root omission from `LineageEx` is a response-format distinction rather than drift. Its environmental-samples division is compatible with bacterial domain placement. No additional names appear in the response.

Exact scans of pinned type-material, merged-ID and dropped-record inventories found no target rows. `EXACT` describes supported NCBI identifier/name grounding, not a cultured-species identification. A neighboring clone, similar sequence, broader taxon or culture-deposit identity was not substituted for the target.

## Evidence

The single `NCBITAXON` attestation is supported by the scientific-name row and backbone: one assertion, unit `NAME`. It does not count organisms, strains or genomes. The 2026-09-13 snapshot and embedded seed event agree with the source and scope evidence. `SEEDED` remains appropriate; this report does not confer human review status.

The exact Nuccore query `txid1036432[Organism:noexp]` returned UID 336092408. The full [HQ630170.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092408&rettype=gb&retmode=xml), including features and sequence, identifies En_UW_46 and taxon 1036432. It contains 340 bases of partial `nosZ`, with both CDS ends partial, codon start 3 and translation table 11. The source is an environmental sample from an anode biofilm, with H2S-supplemented mineral medium. No strain, culture-deposit or geographic qualifier is supplied. The study reference remains unpublished; direct submission is dated 17 November 2010. These annotations describe a submitted fragment, not a pure culture, measured enzyme activity or whole-genome phenotype.

The explicitly linked [AEI00828.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00828.1&rettype=gb&retmode=xml) was separately opened and read in full. It contains 112 amino acids, the same clone/taxon and an explicit partial CDS link to HQ630170.1. Actual and declared lengths agree, and the submitted translation exactly matches the protein sequence. No non-ACGT nucleotide or X/B/Z/J amino-acid ambiguity was detected. This is annotation consistency, not an independent translation, alignment or assay. The computational PRK02888/CDD:235082 region spans less-than-1 through residue 112; its validation label does not demonstrate experimental function for this clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text match for HQ630170 or En_UW_46. Printed pages 54 and 92 were reread in full. Page 54's enrichment-sequence range includes HQ630170; page 92 explains why a single DGGE band does not establish purity. This is study context, not clone-to-species identification. Rasterized text and supplementary objects were not exhaustively audited.

Exact target accession/clone searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. Exact web searches for HQ630170 and AEI00828, and a clone query excluding the already inspected NCBI taxonomy listing, returned no results. Those bounded queries do not prove publication absence. No community phenotype or neighboring-clone archive membership was transferred.

## Completeness

The supported taxonomy-seed assertions are complete enough for their scope. Optional synonyms, nomenclature, mappings, strain/deposit records, genome links, traits and graphs do not need unsupported values. Zero associated strains agrees with the inventory evidence, not a claim of biological unculturability.

Exact scans of the seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The compressed-content search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned three rows: backbone, scientific name and scope. All three complete rows were read.

An expanded search adding HQ630170, AEI00828, the submitted study title and the related PLOS DOI returned the same three rows. All five applicable `SOURCE.json` files, excluded from the content scan, were separately read without a target identity match. Ignored-independent history filename searches found no target artifact. Absence claims are bounded to these named surfaces and patterns.

The exact Assembly query returned zero items with a phrase-not-found warning. That is not proof of universal genome absence. No supported culture-deposit or whole-genome association emerged from the inspected evidence. The partial gene was not treated as an assembly or used to infer traits.

## Findings

None found in the YAML's supported assertions.

Counts: 0 blocker, 0 major, 0 minor.

Unresolved organism identity and limited partial-sequence evidence constrain future enrichment but do not contradict this taxonomy-only record. No invalid field, broken stored reference, unsupported phenotype, source conflict or status inflation was identified.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status.

Future taxonomy corrections belong first at NCBI and then in the pinned ingestion workflow owned by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. These are maintenance routes, not proposed changes. Do not hand-edit generated records or add traits from a medium note, fragment annotation or adjacent clone.

## Follow-up Checks

No blocker remains for this individual verdict. Future biological curation needs an explicit clone-to-organism/deposit connection and claim-specific evidence while retaining partial-sequence limitations. Broader literature and supplement searches are optional discovery work, not prerequisites for the current taxonomy seed.

Following an authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun focused schema and strict validation, then execute applicable corpus reproduction, provenance, history and QC gates. This review did not run generation or claim those global gates passed.

## Additional Notes

One new timestamped Markdown report is the only repository write for this sequential individual review. Eukaryota, other record YAMLs and existing worktrees were untouched. No curation event, status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The record SHA-256 was unchanged before and after review: `6828b85fcc1e5512e04831c090395fc4a0729a00091c77ebc47126c59770e094`.

The stated search outcomes are not an exhaustive census of external knowledge about this clone.
