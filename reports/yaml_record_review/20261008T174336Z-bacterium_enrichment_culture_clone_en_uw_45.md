# YAML Record Review: bacterium enrichment culture clone En_UW_45

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_45.yaml`
- Started UTC: 2026-10-08T17:40:37Z
- Finished UTC: 2026-10-08T17:43:36Z
- Verdict: pass

## Target

One complete generated `TaxonRecord` was resolved and read before judgment: `NCBITaxon:1036431`, bacterium enrichment culture clone En_UW_45. It carries `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` status and zero associated strain records. NCBI's rank does not establish a formally named species or pure isolate.

The ignored-inclusive filename inventory of `data/taxa/`, `reports/yaml_record_review/` and `history/` found exactly this YAML for the identifier, label and slug pattern, and no earlier report for this stem. This is an individual read-only review, not a verdict on adjacent clones. Generated records, sources, scope, history and status were not edited.

## Validation

The focused validators ran in the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_45.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_45.yaml --out /private/tmp/uw45-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The complete TSV was read and contains only its header.
- Complete target-to-backbone, four-ancestor, attestation, path-index, scope and embedded seed-event comparisons: pass.
- Live primary taxonomy and linked nucleotide/protein inspection: completed with the evidence limits below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift and global statistics gates. No focused reproduction/history command was invented. The local comparisons do not prove corpus-wide reproducibility. The seed event was manually inspected against source and scope evidence; no matching standalone history artifact emerged from the bounded search.

Graph grounding validation is not applicable because there is no curator-added graph. iModulonDB was not run: the record has no gene, regulator, pathway or expression-module claim and this clone was not resolved to a covered strain/dataset. That does not establish absence of related data from iModulonDB.

## Identity and Grounding

Full relevant rows were read at `data/raw/ncbitaxon_taxa.tsv:222433`, `data/catalog/ncbi_names-0005.jsonl.gz:31977`, `data/taxa/PATHS.tsv:14940` and `curation/seed_scope.tsv:322680`. Identifier, scientific label, rank, parent, code, snapshot and empty synonym sets agree. The four-ancestor root-first lineage and each label/rank match the backbone. A complete backbone scan found no direct children for the target.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036431&retmode=xml) confirms the name, species rank, parent 48479 and code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036431) supplies ancestor IDs 1, 131567, 2 and 48479. EFetch omits root from `LineageEx`; this is a response-format distinction, not lineage drift. Its environmental-samples division does not conflict with bacterial domain placement. No additional names appear in the response.

Exact scans of pinned type-material, merged-ID and dropped-record inventories found no target entry. `EXACT` is supported for NCBI identifier/name grounding, not for a cultured-species assignment. No broader taxon, neighboring clone, sequence similarity or culture deposit was substituted for this target's identity.

## Evidence

The single `NCBITAXON` attestation traces to the scientific-name row and backbone: assertion count one, unit `NAME`. It counts an upstream assertion, not an organism, strain or genome. The 2026-09-13 snapshot and embedded seed event match the available source and scope evidence. `SEEDED` remains appropriate; this report does not confer human review status.

The exact query `txid1036431[Organism:noexp]` returned Nuccore UID 336092406. Its complete [HQ630169.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092406&rettype=gb&retmode=xml), including all features and sequence, identifies En_UW_45 and taxon 1036431. It contains 340 bases of partial `nosZ`; both CDS ends are partial, codon start is 3 and translation table is 11. The source is an environmental sample from an anode biofilm, with H2S-supplemented mineral medium. No strain, culture-deposit or geographic qualifier appears. The study reference is unpublished; direct submission is dated 17 November 2010. These are annotations of a submitted fragment, not proof of a pure culture, measured reductase activity or whole-genome phenotype.

The explicitly linked [AEI00827.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00827.1&rettype=gb&retmode=xml) was opened and read in full. It contains 112 amino acids, identifies the same clone/taxon and links back to the target's partial CDS. Actual and declared nucleotide/protein lengths agree, and the submitted CDS translation exactly equals the protein sequence. The character check found no non-ACGT base or X/B/Z/J amino-acid ambiguity. This verifies annotation consistency, not independent translation, alignment or biochemical activity. The computational PRK02888/CDD:235082 region extends from less-than-1 through residue 112; its validation label does not demonstrate experimental activity in this clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text hit for HQ630169 or the clone label. Printed pages 54 and 92 were reread completely. The accession lies within page 54's enrichment-sequence range; page 92 warns against treating a single DGGE band as evidence of culture purity. This establishes study context, not species identity. Rasterized text and supplements were not exhaustively audited.

Exact accession/clone searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. Exact web queries for HQ630169 and AEI00827, plus a clone query excluding the already checked NCBI taxonomy listing, returned no results. These discovery limits do not prove publication absence. No community phenotype or neighboring-clone protein archive was attributed to En_UW_45.

## Completeness

The populated taxonomy-seed assertions are complete enough for the supported scope. Optional synonyms, nomenclature, mappings, strain/deposit records, genome links, traits and graphs are appropriately unfilled without target-specific support. Zero associated strains agrees with the source inventory, not a biological claim of unculturability.

Exact identifier scans of all seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. A compressed-content search used `rg --no-ignore --hidden -n -z -i` over `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned three rows: backbone, scientific name and scope. Each complete row was read.

An expanded search adding HQ630169, AEI00827, the submitted study title and the related PLOS DOI returned the same three rows. All five applicable `SOURCE.json` files, excluded from that scan, were separately read without a target identity match. The ignored-independent history filename search found no matching artifact. These absences are bounded to the specified roots and patterns.

The exact Assembly query returned zero items with a phrase-not-found warning. It does not establish universal genome absence. No supported culture-deposit or whole-genome association was established from the inspected evidence. The partial gene was not treated as an assembly or used to infer traits.

## Findings

None found in the supported YAML claims.

Counts: 0 blocker, 0 major, 0 minor.

The clone's unresolved organism-level identity and limited fragment evidence constrain future enrichment but do not contradict this taxonomy record. No invalid field, broken stored reference, unsupported phenotype, source conflict or status inflation was identified.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status.

Future authoritative taxonomy corrections belong first at NCBI, followed by the pinned ingestion workflow in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. These are maintenance ownership routes, not proposed changes. Do not hand-edit generated records or infer a phenotype from a medium note or fragment annotation.

## Follow-up Checks

No unresolved blocker remains for this individual verdict. Future biological curation needs explicit clone-to-organism/deposit evidence and claim-specific support while retaining partial-sequence limitations. Additional supplementary-material or broader literature searches are optional discovery work, not prerequisites for accepting the current seed.

After an authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun the schema and strict validators, then execute applicable reproduction, provenance, history and QC gates. This review did not run generation or claim those global gates passed.

## Additional Notes

Exactly one timestamped Markdown report is the only repository write for this individual review. Eukaryota, other record YAMLs and existing worktrees were untouched. No curation event, review-status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The target SHA-256 was unchanged before and after review: `b376a28003269008eacb54b7b4b3db6239a6876b0629e92e86faeda02aebdce7`.

All absence statements refer to the named roots, exact queries and inspected responses, not a universal external knowledge census.
