# YAML Record Review: Methylobacterium sp. T7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t7.yaml`
- Started UTC: 2026-10-06T15:44:36Z
- Finished UTC: 2026-10-06T15:46:39Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035212`, label `Methylobacterium sp. T7`, SPECIES / BACTERIA. The complete YAML was read before judgement and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. An ignored-independent filename search found the exact target and no prior report for its stem.

EXACT grounding, SEEDED status, ten root-first ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event are present. Synonyms, equivalent xrefs, nomenclature, mappings, genome links, definition, citations, phenotype and causal graph are not asserted.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t7.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t7.yaml --out /private/tmp/mt7-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: identity, complete lineage, code, attestation, scope and seed-event content match pinned inputs. This does not replace corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus pass is claimed.
- No curator-added graph nodes need term validation. The product-check configuration excludes taxonomy fields; their inventory agreement was manually checked.
- No separate target history artifact was found by the ignored-independent filename check. Inline history passed record validation; no external validator was run against an invented artifact.
- No PMID, DOI or quotation is asserted by the YAML. The marker-linked publication below was inspected as completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221933`, [live NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035212&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035212) agree on the exact identifier, label and SPECIES rank. Both live responses were read in full. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm all ten root-inclusive ancestor IDs; the pinned labels and ranks match the YAML.

The no-rank grouping `unclassified Methylobacterium`, below genus 407, belongs in the carried NCBI lineage. A sequence strain qualifier does not authorize changing NCBI's rank. EXACT identifies the source concept, not a validly published binomial.

The [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was previously inspected in full and rechecked for T7 in this review. No target formal-name or type-deposit attribution was established, and no genus-level nomenclature was inherited. The legacy taxonomy-browser route was unavailable; successful NCBI structured responses supplied the identity check.

Exact pinned scans found no children, type-material row, merged-ID row or dropped row for T7.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221933` supports identity, rank, parent, code, empty synonyms and NCBI-only provenance.
- Full native `data/catalog/ncbi_names-0005.jsonl.gz:31401` contains the exact scientific name and taxid with an empty unique-name field.
- `data/taxa/PATHS.tsv:14424` resolves the slug; `curation/seed_scope.tsv:322208` adds it on 2026-09-13 under its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with that scope and source list. One NAME is a source assertion, not a genome or culture-deposit count.

Two numeric hits represent the same unrelated assembly: `data/catalog/gtdb_genomes-0002.jsonl.gz:16841` and `data/catalog/ncbi_genbank-0017.jsonl.gz:12240`. Both native rows were read fully. GCA_018819405.1 / GB_GCA_018819405.1, isolate OS_PC_MetaG.mb.1, has NCBI taxid 2052139, Patescibacteria group bacterium, BioSample SAMN19298392 and project PRJNA627556. The single-contig metagenome-derived assembly has length and ungapped length 1035212; GTDB also carries that number as contig N50. GTDB classifies it as XYD1-37-29 sp018819405 within Patescibacteriota. None of these matching length statistics identifies T7 or supplies a genome link to it.

Exact Entrez `txid1035212[Organism:noexp]` returned zero assemblies with phrases-not-found / no-items diagnostics, and one Nuccore UID, 347300709. The complete nucleotide ID list equals the query count. The assembly no-hit is bounded to that exact query, not universal proof of absence.

Complete [GenBank metadata for FR869808.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869808.1) identify a 1,335-nt partial 16S rRNA sequence, strain T7, exact taxon 1035212, host Trifolium repens and host leaf surface as isolation source. Submission was 18 May 2011, creation 18 September 2011 and update 6 December 2011. Every feature, source qualifier and reference was read; bases were omitted. No culture-collection qualifier, BioSample, BioProject or assembly is supplied. This is a marker, not a genome.

The explicit reference is Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched earlier in this turn, were reread against T7's sequence reference. They confirm a phyllosphere-community study across hosts, sites and land-use types. The abstract does not name T7 or establish its isolate-specific phenotype, locality or growth requirement. Full text and supplements were not inspected; community-level results were not transferred to the isolate.

## Completeness

Exact transformed-table scans found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded T7/T-7 context and marker-accession searches established no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Zero strains agrees with the BacDive subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: no exact BacDive row or descendant contributes an entry. This is not a claim that the original isolate was never cultured. The existing `normalize_culture_identifier` function rejected both T7 and T-7 as unsupported bare deposit identifiers.

The optional FR869808.1 marker link is not a required-representation defect under the current contract. No supported strain entry or eligible SI-DP association was established to receive it. Empty optional biological fields remain appropriate.

The structured iModulonDB adapter ran before browser follow-up and returned 28 datasets without Methylobacterium/Methylorubrum coverage. It is not applicable, not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and inspected evidence scope. Identity and provenance are supported without importing an unrelated assembly on the basis of length statistics or treating the marker as a genome. This pass does not certify full-corpus reproducibility.

## Recommended Edits

None required.

Future marker enrichment belongs in maintained extraction/seeding logic, including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, after explicit identity and a typed non-genome representation are established. Do not edit generated YAML, infer a culture accession from T7, or link GCA_018819405.1 on a numeric match.

Do not promote SEEDED to REVIEWED or append curation history from this report.

## Follow-up Checks

- Repeat exact taxonomy, complete lineage, status, schema and strict checks on source refresh.
- After authorized source/import changes, run full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded comparisons do not replace these gates.
- Require an eligible own-deposit identifier and explicit sequence attribution before a StrainInfo link; keep FR869808.1 outside genome counts.
- Inspect the full text and supplements of PMID 22000032 before T7-specific biological enrichment.
- Match taxonomy by fields rather than arbitrary occurrences in assembly statistics.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial taxid/label/slug search returned five rows, including two unrelated assembly rows. Expanded Methylobacterium/Methylorubrum T7/T-7 context returned the same three target identity/scope rows. All five distinct rows were read fully through structured pinned comparisons and lossless native JSONL decoding. FR869808 / 347300709 returned no rows. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings include ignored and compressed files and remain bounded to these roots.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. The same-turn PubMed response was reread; failed browser output and search snippets were not biological evidence.

Only this new report was written for T7. No YAML/code/generated-page edits, history events, status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota was not reopened.
