# YAML Record Review: bacterium enrichment culture clone En_UW_48

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_48.yaml`
- Started UTC: 2026-10-08T17:57:33Z
- Finished UTC: 2026-10-08T18:01:11Z
- Verdict: pass

## Target

Exactly one generated `TaxonRecord` was resolved and read completely: `NCBITaxon:1036434`, bacterium enrichment culture clone En_UW_48. It carries `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` status and zero associated strain records. The NCBI rank does not establish a formally named species or pure isolate.

The ignored-inclusive filename inventory of `data/taxa/`, `reports/yaml_record_review/` and `history/` found only this YAML for the identifier/label/slug pattern and no prior report for the stem. This is an individual review. No generated record, source, scope, history or status was edited.

## Validation

Focused commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_48.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_48.yaml --out /private/tmp/uw48-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The complete TSV contains only its header.
- Complete record-to-backbone, four-ancestor, attestation, scope, path-index and embedded seed-event comparisons: pass.
- Live primary taxonomy and full linked nucleotide/protein inspections: completed, with the limitations below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift and global statistics gates. Focused comparison is not proof of corpus reproduction. No undocumented per-record reproduction/history gate was invented. The embedded seed event was inspected against source and scope evidence; no matching standalone history artifact was found in the bounded search.

Graph grounding validation is not applicable because there is no curator-added graph. iModulonDB was not run: the record has no gene, regulator, pathway or expression-module claim, and this environmental clone was not resolved to a covered strain/dataset. This is not a finding of database absence.

## Identity and Grounding

Complete relevant evidence was inspected at `data/raw/ncbitaxon_taxa.tsv:222436`, `data/catalog/ncbi_names-0005.jsonl.gz:31980`, `data/taxa/PATHS.tsv:14943` and `curation/seed_scope.tsv:322683`. The identifier, scientific label, rank, parent, code, snapshot and empty synonym sets agree. All four root-first ancestors and their labels/ranks match the pinned backbone. A complete backbone scan found no direct children for the target.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036434&retmode=xml) confirms the name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036434) supplies ancestor IDs 1, 131567, 2 and 48479. EFetch's root omission from `LineageEx` is a response-format distinction, not lineage drift; its environmental-samples division is compatible with bacterial domain. No additional names appear in the response.

Exact scans of pinned type-material, merged-ID and dropped-record inventories found no target rows. `EXACT` describes supported NCBI name/identifier grounding, not a cultured-species identification. No neighboring clone, sequence similarity, broader taxon or deposit was substituted for this identity.

## Evidence

The sole `NCBITAXON` attestation traces to the scientific-name and backbone rows: one assertion, unit `NAME`. This counts a source assertion, not an organism, strain or genome. Its 2026-09-13 snapshot and the embedded seed event agree with the source and scope evidence. `SEEDED` is retained; this report is not a human review-status promotion.

The exact Nuccore query `txid1036434[Organism:noexp]` returned UID 336092412. The complete [HQ630172.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092412&rettype=gb&retmode=xml), including all features and sequence, identifies En_UW_48 and taxon 1036434. It contains 340 bases of partial `nosZ`, with both CDS ends partial, codon start 3 and translation table 11. The source is an environmental sample from an anode biofilm, with H2S-supplemented mineral medium. No strain, culture-deposit or geographic source qualifier appears. The study reference is unpublished and direct submission is dated 17 November 2010. These annotations describe a submitted fragment, not a pure isolate, measured reductase activity or whole-genome phenotype.

The explicitly linked [AEI00830.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00830.1&rettype=gb&retmode=xml) was separately read in full. It contains 112 amino acids, the same clone/taxon and an explicit partial CDS link to HQ630172.1. Actual and declared nucleotide/protein lengths agree, and the submitted CDS translation exactly matches this protein. No non-ACGT nucleotide or X/B/Z/J amino-acid ambiguity was detected. This checks annotation consistency, not independent translation, alignment or biochemical activity. Its computational PRK02888/CDD:235082 region spans less-than-1 through residue 112; the region's validation label does not prove experimentally measured function for the clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text match for HQ630172 or En_UW_48. Printed pages 54 and 92 were reread completely. Page 54's enrichment-sequence range includes this accession; page 92 warns that a single DGGE band does not establish purity. This is study context, not clone-to-species identification. Raster text and supplementary objects were not exhaustively audited.

Exact accession/clone searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. Exact web searches for HQ630172 and AEI00830, plus a clone query excluding the already inspected NCBI taxonomy listing, returned no results. Those bounded searches do not prove publication absence. No community phenotype or neighboring-clone protein archive was transferred to the target.

## Completeness

The supported taxonomy-seed fields are complete enough for their scope. Optional synonyms, nomenclature, mappings, strain/deposit records, genome links, traits and graphs do not require unsupported values. Zero associated strains agrees with the inventory, not a biological claim of unculturability.

Exact identifier scans of all seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The compressed-content search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned three rows: backbone, scientific name and scope. All were inspected completely.

An expanded search adding HQ630172, AEI00830, the submitted study title and the related PLOS DOI returned those same three rows. All five applicable `SOURCE.json` files, excluded from the content scan, were separately read without a target identity match. The ignored-independent history filename search found no target artifact. Absences are bounded to the stated roots and patterns.

The exact Assembly query returned zero items with a phrase-not-found warning. That is not proof of universal genome absence. No supported culture-deposit or whole-genome association emerged from the inspected sources. The partial gene is not a genome record and does not justify inferred traits.

## Findings

None found in the YAML's supported assertions.

Counts: 0 blocker, 0 major, 0 minor.

Unresolved organism-level identity and limited partial-sequence evidence constrain future enrichment but do not contradict the current taxonomy-only record. No invalid field, broken stored reference, source conflict, unsupported phenotype or status inflation was identified.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status.

Future taxonomy corrections belong first at NCBI and then in the pinned ingestion workflow in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. These are ownership routes, not proposed changes. Do not hand-edit generated records or add traits from the medium note, fragment annotation or adjacent clone evidence.

## Follow-up Checks

No blocker remains for this individual verdict. Future biological curation requires explicit clone-to-organism/deposit evidence and claim-specific support, preserving partial-sequence limits. Broader literature and supplementary-material searches are optional discovery work, not prerequisites for accepting this taxonomy seed.

After an authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun focused schema and strict validation, and then run applicable corpus reproduction, provenance, history and QC gates. No generation was run or global gate claimed as passed by this review.

## Additional Notes

One new timestamped Markdown report is the only repository write for this sequential individual review. Eukaryota, other record YAMLs and existing worktrees were untouched. No curation event, status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The target SHA-256 was unchanged before and after review: `fdfcd5b1797a70d2b0c0e7c2afd6886187464fda2b7482d0361893ed2d2d877c`.

The search outcomes above do not constitute an exhaustive census of external knowledge about the clone.
