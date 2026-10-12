# YAML Record Review: bacterium enrichment culture clone En_UW_44

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_44.yaml`
- Started UTC: 2026-10-08T17:35:28Z
- Finished UTC: 2026-10-08T17:39:04Z
- Verdict: pass

## Target

One generated `TaxonRecord` was resolved and read completely: `NCBITaxon:1036430`, bacterium enrichment culture clone En_UW_44. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` status and zero associated strain records. The species rank comes from NCBI; it does not establish a formally named species or pure isolate.

An ignored-inclusive filename search of `data/taxa/`, `reports/yaml_record_review/` and `history/` resolved only this YAML for the identifier/label/slug pattern and found no prior report for the stem. No generated record, source inventory, scope entry, status or history was edited.

## Validation

Focused commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_44.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_44.yaml --out /private/tmp/uw44-strict.tsv`: pass, one file, zero files with errors and zero error rows. The complete TSV was read and contains only its header.
- Complete target-to-backbone comparison, all four ancestor checks, attestation, path index, scope and embedded seed-event comparisons: pass.
- Live primary taxonomy and linked nucleotide/protein inspection: completed as described below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift and global statistics gates. These individual comparisons do not prove corpus reproduction or publication readiness. No undocumented focused reproduction/history gate was invented. The embedded seed event was manually checked; no matching standalone history artifact was found in the bounded searches.

Graph grounding validation is not applicable because the record has no curator-added graph. iModulonDB was not run: the YAML has no gene, regulator, pathway or expression-module claim, and the clone has not been resolved to a covered strain/dataset. This is not a finding of database absence.

## Identity and Grounding

Complete relevant evidence was inspected at `data/raw/ncbitaxon_taxa.tsv:222432`, `data/catalog/ncbi_names-0005.jsonl.gz:31976`, `data/taxa/PATHS.tsv:14939` and `curation/seed_scope.tsv:322679`. Identifier, scientific name, rank, parent, code, snapshot date and empty synonym sets agree with the YAML. Its four root-first ancestors and their ranks match the pinned backbone. The complete backbone scan found no direct children.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036430&retmode=xml) agrees on the name, species rank, parent 48479 and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036430) confirms ancestor IDs 1, 131567, 2 and 48479. EFetch's root omission from `LineageEx` is a response-format difference, not lineage drift; environmental-samples division does not conflict with bacterial domain. No additional names appear in that response.

Exact searches of pinned type-material, merged-ID and dropped-record inventories found no target rows. `EXACT` correctly describes NCBI name/identifier grounding, not a cultured-species identification. No taxonomic merge, broader placement or strain equivalence is inferred from neighboring clones.

## Evidence

The sole `NCBITAXON` attestation traces to the scientific-name row and backbone: one assertion with unit `NAME`, not one organism, strain or genome. Its 2026-09-13 snapshot matches the source. The embedded seed event and scope reason agree, and `SEEDED` is retained; this review is not a human status promotion.

The exact query `txid1036430[Organism:noexp]` returned Nuccore UID 336092404. The complete [HQ630168.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092404&rettype=gb&retmode=xml), including all features and sequence, identifies this clone and taxon. It contains 340 bases of partial `nosZ`, with both CDS ends partial, codon start 3 and translation table 11. Source qualifiers specify an environmental sample from an anode biofilm and H2S-supplemented mineral medium. No strain, culture-deposit or geographic qualifier is supplied. The reference is unpublished; direct submission is dated 17 November 2010. The accession and medium were obtained from this record, not inferred from adjacent clone numbers. The fragment does not establish culture purity, measured enzyme activity or whole-genome phenotype.

The explicitly linked [AEI00826.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00826.1&rettype=gb&retmode=xml) was separately opened and read in full. It has 112 amino acids, the same clone/taxon and an explicit partial CDS link to HQ630168.1. Actual and declared lengths match, and the submitted CDS translation equals the protein sequence. No non-ACGT nucleotide or X/B/Z/J amino-acid ambiguity was detected. This checks annotation consistency, not independent translation, alignment or biochemical activity. The computational PRK02888/CDD:235082 region spans less-than-1 through 112; its validation label does not prove experimental activity in this clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text match for HQ630168 or En_UW_44. Printed pages 54 and 92 were reread completely. The accession falls within the enrichment-sequence range on page 54; page 92 warns that a single DGGE band does not establish purity. This supports study context, not species identity. It is not an exhaustive raster-text or supplement audit.

Exact clone/accession searches in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. Exact web searches for HQ630168 and AEI00826, and for the clone excluding the already inspected NCBI taxonomy listing, returned no results. These bounded searches do not prove literature absence. No community phenotype or neighboring-clone archive evidence was transferred.

## Completeness

The taxonomy-seed assertions are complete enough for the supported scope. Optional synonyms, nomenclature, mappings, strain/deposit records, genome links, traits and graphs do not require unsupported values. Zero strains agrees with the source inventory, not a claim of biological unculturability.

Exact scans of all seven raw inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The compressed-content search used `rg --no-ignore --hidden -n -z -i` over `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label patterns returned four rows, all inspected completely. Adding HQ630168, AEI00826, the submitted study title and the related PLOS DOI returned the same four rows. All five applicable `SOURCE.json` files were separately read, without a target identity match; ignored-independent history filename searches found no matching artifact.

Three matches are the backbone, scientific-name and scope rows. The fourth, `data/catalog/ncbi_genbank-0051.jsonl.gz:19539`, is a numerical identifier collision: GCA_055615595.1 is a Streptococcus pneumoniae assembly with taxon/species taxon 1313 and isolate code 1036430. Its genome size is 1970458. Its isolate string is not the target NCBI taxon and cannot supply a strain/genome association. No project, sample or publication link from that unrelated assembly was attributed to En_UW_44.

The exact NCBI Assembly query returned zero items with a phrase-not-found warning. That is a bounded query result, not universal assembly absence. No culture-deposit or whole-genome connection was established from the inspected sources, and the partial gene is not a genome record.

## Findings

None found in the supported YAML assertions.

Counts: 0 blocker, 0 major, 0 minor.

The environmental clone's unresolved organism identity and limited fragment evidence constrain future enrichment but do not contradict the present record. No invalid shape, broken stored reference, unsupported phenotype, source conflict or status inflation was identified.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status.

Future taxonomy corrections belong first at NCBI, followed by the pinned ingestion workflow in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope changes belong in `curation/seed_scope.tsv`. These are ownership routes, not requested changes. Do not hand-edit YAML or add a phenotype from the medium note, fragment annotation or unrelated assembly.

## Follow-up Checks

No blocker remains for this record-level verdict. Future biological curation requires explicit clone-to-organism/deposit links and claim-specific experimental evidence, preserving partial-sequence scope. Additional literature or supplement searches are optional discovery work, not required to accept the supported taxonomy seed.

After any authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun its schema and strict validators, then execute applicable reproduction, provenance, history and QC gates. This read-only review did not run generation or claim those global gates passed.

## Additional Notes

One new timestamped Markdown report is the only repository write for this individual review. Eukaryota, other records and existing worktrees were untouched. No curation event, status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The target SHA-256 was unchanged before and after review: `8e66bc6f134d18aedbf34a76ec984a0e51f0e4fd7200fc3fa5e236b1ba63c064`.

All absence statements are limited to the specified roots, source responses and queries, not an exhaustive external knowledge census.
