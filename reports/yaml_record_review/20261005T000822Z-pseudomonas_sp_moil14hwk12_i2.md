# YAML Record Review: Pseudomonas sp. MOIL14HWK12:I2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_moil14hwk12_i2.yaml`
- Started UTC: 2026-10-05T00:06:18Z
- Finished UTC: 2026-10-05T00:08:22Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033994`,
Pseudomonas sp. MOIL14HWK12:I2. It asserts SPECIES rank, BACTERIA domain,
parent 196821, ten ancestors, EXACT grounding, SEEDED status, one GTDB
mapping, one exact synonym and xref, code 11, zero BacDive strains,
three source attestations and one seed event. NCBI's species rank must
not be silently replaced with STRAIN because of the isolate-like name.
No record, maintained input, code, status or history was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_moil14hwk12_i2.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_moil14hwk12_i2.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded backbone/complete lineage, seven mapped inventories, children, filename, scope and inline-event checks passed; source counts were checked separately below.
- Not run: full-corpus `just verify-corpus`, QC, tests or rendering. `--max-diffs` limits diagnostics rather than target selection. Bounded checks do not establish byte reproduction or biological correctness.
- Not applicable: `just validate-products`; no curator graph nodes. Source identifiers were verified directly.
- Not run: `just validate-history`; ignored-inclusive filename and compressed-content searches found no target history artifact. Inline seed provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221416`, the full native name at
`data/catalog/ncbi_names-0005.jsonl.gz:30760`,
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033994&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033994)
agree on the exact identifier, label, rank, parent and code. All ten
ancestors match: root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas. Expanded labels/ranks agree
where supplied. NCBI provides no equivalent or synonym name. Complete
exact-ID type-material, merged-ID and dropped-taxon scans found no rows.

The unsuffixed MOIL14HWK12 and :I1 records are separate NCBI taxa,
1033992 and 1033993, with different assembly and sample identifiers.
No source inspected merges these records or establishes their physical
laboratory relationship. Shared cluster membership cannot transfer their
names, trait evidence or source-status warnings to I2.

## Evidence

The NCBITAXON one-NAME attestation and September 13 snapshot agree with
the backbone. `data/raw/madin_taxa.tsv:643` confirms four
TRAIT_ASSERTION entries, not four independently verified phenotypes.
Mapped BacDive, LPSN, GOLD, MediaDive and BactoTraits inventories were
empty; a complete backbone child scan was empty. Zero descendant-inclusive
BacDive strains therefore agrees with the input. Native GOLD presence
does not imply an entry in the separately maintained KGX attestation table.

`data/raw/gtdb_mappings.tsv:1389` carries the closeMatch and count 61;
`data/raw/gtdb_species.tsv:42707` has the same cluster count. The full
native object at `data/catalog/gtdb_genomes-0014.jsonl.gz:28493`
classifies RS_GCF_000510745.1 in Chryseomonas oryzihabitans, identifies
taxon 1033994, strain MOIL14HWK12:I2 and SAMN02597180, and marks it
nonrepresentative. The complete 19-shard scan performed earlier in this
review session inspected 901341 rows, agreeing with the RS232 manifest,
and counted 61 unique accessions in this same exact cluster across 15
NCBI taxon IDs. The representative is RS_GCF_000730625.1, NBRC 102199;
other inspected taxon contexts include L19, AG1002, RIT411, unnamed genome
bins and the two other MOIL taxa. The scan includes I2 explicitly.
It supports a source-cluster assembly count, not 61 I2 genomes or culture
deposits. The live GTDB tree was inaccessible, so the native snapshot,
not a search snippet, supplies the classification evidence.

Full native GenBank and RefSeq rows at
`data/catalog/ncbi_genbank-0000.jsonl.gz:16674` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:13841` agree with
[live assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000510745.1/dataset_report).
Exact-taxonomy Assembly search returned one assembly. GCF_000510745.1
and GCA_000510745.1 are both current and explicitly sequence-identical,
with no reported RefSeq exclusion. The scaffold assembly has 5037935
total bases, 5037683 ungapped bases and 19 scaffolds. The metadata
separately report 24 contigs and 22 component sequences; these fields
are not interchangeable. It links to SAMN02597180 and PRJNA79069;
PRJNA224116 is the RefSeq umbrella, not another isolate project.

The complete returned BioSample metadata name MOIL14HWK12:I2 and the
rhizosphere/soil environment. Location, collection date, reference
biomaterial and growth conditions are missing. The ANI taxonomy check
is OK at genus level, without a submitted type assembly, and the best
ANI match is P. oryzihabitans at 98.39%. This source classification
does not establish formal synonymy or authorize replacing the carried
NCBI lineage. Source biological annotations are not automatically
curator-verified phenotype assertions.

All 45 exact-taxonomy nuccore summaries were inspected: one GenBank WGS
master, 22 components, two scaffold records and 20 RefSeq records
comprising a master and 19 scaffolds. These are not 45 genomes. Complete
metadata, source feature, references and comments for
[AZOA00000000.1](https://www.ncbi.nlm.nih.gov/nuccore/AZOA00000000.1)
confirm the exact strain, taxon, sample, project and JGI project 404624.
The master represents a direct JGI submission and identifies components
AZOA01000001 through AZOA01000022. Its displayed length 22 is a
component inventory, not a 22-base genome. Raw bases and all component
gene features were not inspected.

Full BV-BRC object `data/bvbrc/bvbrc-0000.jsonl.gz:3261` connects
PATRIC 1033994.3 to the same assembly, sample and sequencing project;
its culture-collection value is blank. Its terminal lineage display name
drops the suffix, while the genome name, strain and terminal taxon ID
retain I2, so the display label cannot justify a source-record merge.
Full GOLD objects at `data/gold/organisms.jsonl.gz:11321`,
`data/gold/projects.jsonl.gz:11184` and `data/gold/analyses.jsonl.gz:16293`
give Go0012841 -> Gp0012841 -> Ga0025438 -> IMG 2510065055 /
GCA_000510745.1. The direct analysis organism field is empty but the
project bridge is explicit. The organism culture-collection field is
empty. These are genome-provenance relationships, not deposit identity;
Go/Gp/Ga records are not themselves genome identifiers.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. ID, slug and I2 separator variants returned
25 contexts, all inspected. Longer IMG/assembly identifiers were false
substring matches, and SAMEA1033994 is an unrelated Streptococcus sample.

A secondary assembly/sample/project/WGS/IMG search returned 75 contexts,
all inspected. PRJNA790696 is a different, longer BioProject accession;
longer WGS prefixes containing AZOA likewise do not match this WGS project.
The exact target sample occurs at
`data/catalog/allthebacteria.tsv.xz:1033175`, with run SRR3944179,
META_FAIL and SYLPH_RESULTS_FAIL, and no ENA analysis. The full TSV
row was read. Its supplied FASTA URL does not override the metadata
exclusion. No eligible BacDive/StrainInfo culture-deposit bridge was
found in these searches. Do not fabricate one from the strain label.

Bounded web search returned genomic, supplementary-table and computational
literature leads. They were not treated as inspected experiment-level
evidence for I2; no specific primary paper was used in this verdict.
The YAML requires no publication, gene, mechanism or phenotype claim.
Empty optional nomenclature and graph slots are not consequential gaps.
The missing exact-scope support for the synonym is consequential.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. Major: an unresolved, isolate-specific NCBI species placeholder is
   given an exact GTDB species synonym without equivalent concept-scope
   evidence. Lines 43 and 64 carry closeMatch; line 46 creates the
   EXACT_SYNONYM and line 51 supplies the identity xref. Native data
   support classification of I2's assembly in a multi-NCBI-taxon cluster,
   not identity of this entire placeholder concept with the named species.
   NCBI itself supplies no such synonym. The mapping is owned upstream by
   kg-microbe and imported at `src/taxonmech/extract.py:501`.
   `src/taxonmech/seed.py:451` treats every closeMatch as identity and
   line 466 promotes it without a scope check. Correct these maintained
   owners, not generated YAML. A STRAIN-only guard would miss this record.

## Recommended Edits

1. Require positive support for equivalent concept scope before promoting
   species mappings into exact synonyms/xrefs, including species-ranked
   isolate placeholders. Preserve membership/classification separately.
   Correct the source/seeder semantics, then regenerate away the unsupported
   identity assertions. Do not mechanically replace closeMatch with
   broadMatch without checking relation direction and the source contract.
2. Add a `tests/test_seed.py` regression for SPECIES placeholders as well
   as strain-ranked taxa, while retaining valid same-concept mappings.
   Preserve the cluster count 61, four MADIN assertions, source units,
   NCBI lineage, exact target designation and SEEDED status.

## Follow-up Checks

After authorized curation of maintained inputs, rerun scope-sensitive
mapping tests, exact GTDB cluster comparison, regeneration, focused schema
and strict validation, full `just verify-corpus` and relevant QC gates.
Future strain-genome enrichment must require an eligible whole deposit
identifier and honor ATB exclusion. Claims about I1 or the unsuffixed
record require their own explicit bridges before use here. No blocker
prevents further independent record reviews.

## Additional Notes

`data/taxa/PATHS.tsv:13871` fixes the slug;
`curation/seed_scope.tsv:36157` records September 12, 2026 addition.
The September 13 seed event, sources and three-source reason agree.
Ignored-inclusive report/history searches found no prior target artifact.
iModulonDB is not applicable: no gene, regulator or expression module is
asserted. No paid research, outside contact, GitHub mutation, generator
run, human REVIEWED promotion or curation-history write occurred.
