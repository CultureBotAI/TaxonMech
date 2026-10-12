# YAML Record Review: Enterobacter sp. Ds-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_ds_1.yaml`
- Started UTC: 2026-10-06T18:09:09Z
- Finished UTC: 2026-10-06T18:13:17Z
- Verdict: pass

## Target

The fully read generated TaxonRecord denotes NCBITaxon:1035251, Enterobacter sp. Ds-1, rank SPECIES, domain BACTERIA, parent NCBITaxon:2608935, genetic code 11, grounding EXACT and status SEEDED. It contains ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14457`; scope is `curation/seed_scope.tsv:322241`. HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Eukaryota was not reopened.

## Validation

The review skill, checklist, justfile and curation skill were reread this turn. CLAUDE.md, CURATION, HARMONIZATION, SCHEMA, history guidance, source boundaries and relevant schema/seeder had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/enterobacter_sp_ds_1.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/enterobacter_sp_ds_1.yaml --out /private/tmp/eds-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded manual comparisons confirmed identity, every ancestor, path/scope, attestation and event. These are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction CLI has no target selector. No corpus-wide reproducibility/reference-integrity claim is made.
- `just validate-products` was not run: graph grounding is absent and its inspected configuration skips NCBITaxon. Identifiers were checked against pinned/live taxonomy instead.
- Ignored-inclusive content/path searches found no target external history artifact within the searched history tree. No history or status mutation was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded with read-only network access. All 28 rows were inspected; none covers Enterobacter. Not applicable, not negative biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221966` supports identifier, exact label, rank, parent, code 11, empty synonyms and the 2026-09-13 snapshot. The scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31434`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035251&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035251) agree. Every stored ancestor label/rank matches the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Gammaproteobacteria (1236), Enterobacterales (91347), Enterobacteriaceae (543), Enterobacter (547), unclassified Enterobacter (2608935). XML omits root in LineageEx; Datasets includes it.

SPECIES is NCBI's rank for this strain-labelled taxon, not proof of a formally named species. EXACT identifies the source concept, not nomenclatural validity. Relevant [LPSN Enterobacter genus nomenclature](https://lpsn.dsmz.de/genus/enterobacter) was inspected and a full-page text search found no Ds-1. Its conserved, validly published/correct genus status and type species Enterobacter cloacae do not identify this strain or establish a target type flag. No exact target LPSN mapping occurs in the pinned inventory.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot. The seed event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree. Count 1 measures a source-name assertion, not a genome or biological strain.

No exact target row occurs in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this taxon as parent. Zero inventoried strains agrees with the own/subtree BacDive gathering rule in `src/taxonmech/seed.py:488`; it does not mean the organism has never been cultured.

The exact live query `txid1035251[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 333830297. Full [HQ857788.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/HQ857788.1), excluding bases, was inspected: 816 nt, partial 16S rRNA, strain Ds-1, explicit taxon:1035251 and cultivated-soil isolation source. Submitted 27 December 2010 by R. Sasikala and S. Barathi; created 29 May 2011, updated 28 June 2011. The source feature has no geographic qualifier, culture deposit, BioSample, BioProject or assembly identifier. The Indian institutional submission address is not itself a specimen-location qualifier. Its bibliography is direct submission only, without PMID or DOI. This marker is not a genome assembly.

Bounded exact taxon/accession, strain-name and author-context web searches did not establish an inspected primary publication or culture/genome bridge for this target beyond the sequence metadata. Search snippets concerning other isolates were not used as evidence. Shared submitters or similarly numbered soil strains do not transfer results from Bordetella Ds-4 or other bacteria.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, exact label and slug returned 11 rows: three genuine target rows and eight numeric collisions. All original candidate native JSON/TSV rows, including two compressed ATB rows, were read losslessly.

An expanded delimiter-bounded search for Ds-1, DS1 and Ds 1 returned 155 rows: 66 inventory/name rows, 88 other JSON rows and one ATB row. Every row was parsed for identity and all matching fields; these projections are triage, not complete reviews of those organisms. Its boundaries exclude longer suffix-bearing designations. Only the target backbone/name rows established this exact identity; the initial query independently covered scope. A same-root HQ857788 search returned no hit.

The five SOURCE.json documents and ignored-independent history filename inventory were checked with initial identifiers and a word-bounded strain/accession pattern, without a target/accession hit. An earlier unbounded metadata pattern also matched response filenames such as records-1000.json.gz; those artifact-name collisions were not biological evidence. The bounded rerun completed without such hits. These checks concern the listed input roots, not all original ignored snapshots or remote databases.

All four exact bare-designation BacDive candidates were read in full, together with their transformed rows. They belong to Clostridium disporicum (2744), Methanosarcina (7120), Paenibacillus glycanilyticus (11590) and Parvibaculum lavamentivorans (13867), not this target. For example, the Parvibaculum record links DS-1 with DSM 13023, AY387398 and GCA_000017565, whereas the Paenibacillus record links DS-1 with NBRC 16618 and GCA_004000805. These unversioned source accessions were not assigned invented versions or transferred to Enterobacter.

Eight StrainInfo matching records were identity-triaged. Full follow-up reads confirmed Pseudomonas SI-ID36872 and Parvibaculum SI-ID49388 as distinct source records. The full SI-ID162933 record supplies DS-1, CBS 296.63 and ATCC 12737, but no taxon or sequence. Its exact [ATCC product page](https://www.atcc.org/products/12737) and [product sheet](https://www.atcc.org/api/pdf/product-sheet?id=12737) timed out in the web reader; a direct public-sheet attempt returned HTTP 403. A search-result identity lead was not promoted to inspected authority evidence. This unclassified record remains unconnected, not proof of a missing target deposit.

Other matches identify different taxa or community projects. Generic/unknown bacterial labels are not positive identity bridges. The culture normalizer rejects Ds-1, DS-1 and Ds1 as deposit keys. No supported owning-strain/own-deposit bridge or required missing genome relationship was established. Optional definition, evidence and graph slots need not be filled.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the existing seeded assertions and bounded completeness checks. SI-ID162933 remains an unresolved label collision; the unavailable authority page limits that optional follow-up but does not establish a defect in this YAML. Pass does not certify unrun corpus gates or universal completeness.

## Recommended Edits

None required. Retain the exact NCBI identifier, Ds-1 label, parent chain and SEEDED status. Do not import another organism's DS-1 deposits/type flags, assign an unclassified StrainInfo record by alias, or count a marker as a genome.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests. Scope changes belong in `curation/seed_scope.tsv`; authoritative taxonomy corrections belong upstream in kg-microbe or NCBI. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Resolve SI-ID162933's own primary deposit identity before any attempted join. Require an eligible complete collection accession and source-specific chain before adding strain/genome links. Keep strain, taxon, marker, deposit, sample, project and genome identities separate. StrainInfo must name the same matched SI-DP; GOLD must resolve the same organism/project/analysis chain; ATB requires existing BioSample evidence. Shared sample does not imply genome equivalence.

After any authorized maintained-input change, rerun target schema/strict validation and relevant join tests, followed by `just verify-corpus` and `just qc`. Require target-specific evidence before any phenotype or publication assertion.

## Additional Notes

- Four excluded Ligilactobacillus salivarius rows identify taxid 1624, strain 1001295st1_D6_RTP21277_210401, GCA/GCF_040924775.1, BV-BRC 1624.986 and SAMN41035251: `data/bvbrc/bvbrc-0004.jsonl.gz:27287`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20844`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19990`, `data/catalog/gtdb_genomes-0000.jsonl.gz:49870`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6410` concerns Mycobacterium tuberculosis, taxid 1773, BV-BRC 1773.18590 and ERR1035251. `data/catalog/allthebacteria.tsv.xz:569721` concerns that run, SAMEA3558784 and ERZ3502656. Available FASTA/PASS filters do not supply a target association.
- `data/catalog/ncbi_genbank-0023.jsonl.gz:12327` concerns Salmonella enterica serovar Anatum, taxid 58712, MS160193, GCA_025080275.1 and SAMEA103525168. `data/catalog/allthebacteria.tsv.xz:66149` concerns that sample, ERR1865246 and ERZ3070652. No Enterobacter identity follows from the numeric substring.
- BacDive native rows `data/bacdive/records.jsonl.gz:2644`, `data/bacdive/records.jsonl.gz:6994`, `data/bacdive/records.jsonl.gz:11437` and `data/bacdive/records.jsonl.gz:13701` correspond to transformed `data/raw/bacdive_strains.tsv` lines 2645, 6995, 11438 and 13702. Full StrainInfo reads were `data/straininfo/records.jsonl.gz:25353`, `data/straininfo/records.jsonl.gz:37249` and `data/straininfo/records.jsonl.gz:115685`. Row numbers are not assumed to equal SI-ID.
- Some broad-search source records concern eukaryotes; those were excluded as identity context only. No eukaryotic TaxonRecord was reopened or given a new report.
- The target was reread byte-identical. Only this report was written; no YAML, source inventory, history, status, generated product, Git or GitHub mutation was made.
