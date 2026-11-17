# YAML Record Review: bacterium enrichment culture clone En_UW_47

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_47.yaml`
- Started UTC: 2026-10-08T17:50:49Z
- Finished UTC: 2026-10-08T17:54:39Z
- Verdict: pass

## Target

Exactly one complete generated `TaxonRecord` was resolved and read: `NCBITaxon:1036433`, bacterium enrichment culture clone En_UW_47. Its fields are rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479`, code 11, grounding `EXACT`, mapping status `SEEDED` and zero associated strain records. The rank is NCBI's classification of this environmental clone, not proof of a formally named species or pure isolate.

The ignored-inclusive filename search of `data/taxa/`, `reports/yaml_record_review/` and `history/` found only the target YAML for the identifier/label/slug pattern and no prior report for the stem. This individual review does not judge neighboring records or change generated YAML, sources, scope, history or status.

## Validation

The existing environment was used with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_47.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_47.yaml --out /private/tmp/uw47-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The complete TSV contains only its header.
- Complete target-to-backbone, four-ancestor, attestation, scope, path-index and embedded seed-event comparisons: pass.
- Current primary taxonomy and full linked nucleotide/protein inspections: completed, with the evidence limitations below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift and global statistics gates. Focused comparisons do not establish corpus reproduction or publication readiness. No undocumented per-record reproduction/history gate was invented. The embedded seed event was manually checked against source/scope evidence; no matching standalone history artifact was found in the bounded searches.

Graph grounding validation is not applicable because the record has no curator-added graph. iModulonDB was not run: the YAML contains no gene, regulator, pathway or expression-module claim and this clone has not been resolved to a covered strain/dataset. This is not a claim that the database lacks related evidence.

## Identity and Grounding

Complete relevant rows were inspected at `data/raw/ncbitaxon_taxa.tsv:222435`, `data/catalog/ncbi_names-0005.jsonl.gz:31979`, `data/taxa/PATHS.tsv:14942` and `curation/seed_scope.tsv:322682`. Identifier, scientific label, rank, parent, genetic code, snapshot and empty synonym sets agree. The root-first lineage's four ancestors, labels and ranks match the pinned backbone. The complete backbone scan found no direct children.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036433&retmode=xml) agrees on the name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036433) confirms ancestor IDs 1, 131567, 2 and 48479. EFetch omits root from `LineageEx`; that representation difference does not establish drift. Its environmental-samples division is compatible with bacterial domain placement. No additional names appear in the inspected response.

Exact scans of pinned type-material, merged-ID and dropped-record inventories found no target rows. `EXACT` is supported for the NCBI name/identifier, not for a cultured-species assignment. No broader taxon, similar sequence, culture deposit or adjacent clone was substituted for the reviewed identity.

## Evidence

The sole `NCBITAXON` attestation traces to the scientific-name and backbone rows: one assertion with unit `NAME`, not one organism, strain or genome. The 2026-09-13 snapshot and embedded seed event agree with source and scope evidence. `SEEDED` remains appropriate; this report does not confer human review status.

The exact Nuccore query `txid1036433[Organism:noexp]` returned UID 336092410. The complete [HQ630171.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092410&rettype=gb&retmode=xml), including features and sequence, identifies this clone and taxon. It contains 341 bases of partial `nosZ`, with both CDS ends partial, codon start 3 and translation table 11. The source is an environmental sample from an anode biofilm, with H2S-supplemented mineral medium. No strain, culture-deposit or geographic qualifier is supplied. Its study reference is unpublished and direct submission is dated 17 November 2010. These annotations support a submitted fragment, not a pure isolate, measured reductase activity or whole-genome phenotype.

The explicitly linked [AEI00829.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00829.1&rettype=gb&retmode=xml) was opened and read completely. It contains 113 amino acids, the same clone/taxon and an explicit partial CDS link to HQ630171.1. Actual nucleotide/protein lengths match the declarations, and the submitted CDS translation exactly equals the protein sequence. The DNA contains S at base 2 and Y at base 108; the protein contains X at residue 36. These ambiguities were not silently resolved. This is annotation-consistency checking, not independent translation, alignment or biochemical validation. The computational PRK02888/CDD:235082 region spans less-than-1 through residue 113; its validation label does not prove experimental activity for this clone. The YAML does not store a sequence or phenotype claim affected by these limitations.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text match for HQ630171 or the clone label. Printed pages 54 and 92 were reread in full. Page 54's enrichment-sequence range includes HQ630171; page 92 warns that a single DGGE band does not establish culture purity. This supports study context, not a clone-to-species assignment. It is not an exhaustive raster-text or supplement audit.

Exact accession/clone searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. Exact web queries for HQ630171 and AEI00829, plus a clone query excluding the already checked NCBI taxonomy listing, returned no results. These bounded discovery outcomes do not prove publication absence. No community phenotype or neighboring-clone archive membership was transferred.

## Completeness

The populated taxonomy-seed assertions are complete enough for their supported scope. Optional synonyms, nomenclature, mappings, strain/deposit records, genome links, traits and graphs do not need unsupported entries. Zero associated strains agrees with the available inventory, not a claim of biological unculturability.

Exact identifier scans of all seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The compressed-content search used `rg --no-ignore --hidden -n -z -i` over `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned three rows: backbone, scientific name and scope. All three complete rows were read.

The expanded search adding HQ630171, AEI00829, the submitted study title and the related PLOS DOI returned the same three rows. All five applicable `SOURCE.json` files, excluded from that content scan, were separately read without finding a target identity match. The ignored-independent history filename search found no matching artifact. Those absences are bounded to the specified roots and patterns.

The exact Assembly query returned zero items with a phrase-not-found warning. It does not prove universal genome absence. No supported culture-deposit or whole-genome association was established from the inspected sources. The partial gene was not treated as a genome or used to infer traits.

## Findings

None found in the YAML's supported assertions.

Counts: 0 blocker, 0 major, 0 minor.

The external sequence ambiguities and unresolved organism-level identity constrain future biological enrichment but do not contradict the current taxonomy-only record. No invalid shape, broken stored reference, unsupported phenotype, source conflict or status inflation was identified.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status.

Future authoritative taxonomy corrections belong first at NCBI and then in the pinned ingestion workflow in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope changes belong in `curation/seed_scope.tsv`. These are ownership routes, not requested changes. Do not hand-edit generated records or infer traits from the medium note, partial annotation or neighboring clones.

## Follow-up Checks

No blocker remains for this record-level verdict. Before sequence-based biological curation, resolve the ambiguous bases against primary sequence evidence without guessing and preserve all partial-sequence qualifiers. A clone-to-organism/deposit link and claim-specific experimental support are needed for strain or phenotype enrichment. Additional literature/supplement searches are optional discovery work, not prerequisites for accepting the taxonomy seed.

After an authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun focused schema and strict validators, and then execute applicable reproduction, provenance, history and QC gates. This read-only review did not run generation or claim those global gates passed.

## Additional Notes

One new timestamped Markdown report is the only repository write for this sequential individual review. Eukaryota, other record YAMLs and existing worktrees were untouched. No curation event, status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The target SHA-256 was unchanged before and after review: `906627935bf117be21c2aa4b21a53f271e84d89fa4389e8e93a9201f7fa40102`.

All absence findings refer to the stated roots, queries and source responses, not a universal census of external knowledge.
