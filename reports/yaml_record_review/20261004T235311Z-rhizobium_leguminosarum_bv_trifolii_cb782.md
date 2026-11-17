# YAML Record Review: Rhizobium leguminosarum bv. trifolii CB782

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhizobium_leguminosarum_bv_trifolii_cb782.yaml`
- Started UTC: 2026-10-04T23:50:01Z
- Finished UTC: 2026-10-04T23:53:11Z
- Verdict: needs curation

## Target

Read the complete generated `TaxonRecord`, `NCBITaxon:1033991`, Rhizobium
leguminosarum bv. trifolii CB782. It asserts STRAIN rank, BACTERIA domain,
parent 386, twelve ancestors, EXACT grounding, SEEDED status, a GTDB
species mapping, three exact synonyms, one GTDB xref, code 11, zero
inventoried strains, three source attestations and one seed event.
No record, maintained input, code, status or history was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/rhizobium_leguminosarum_bv_trifolii_cb782.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/rhizobium_leguminosarum_bv_trifolii_cb782.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded backbone, complete lineage, mapped inventories, scope, filename and inline-event checks passed. GTDB and MADIN counts were checked separately below.
- Not run: full-corpus `just verify-corpus`, QC, tests or rendering. `--max-diffs` caps diagnostics, not targets; bounded checks do not prove byte reproduction or semantic correctness.
- Not applicable: `just validate-products`; no curator graph nodes. Authority and native-source identifiers were checked directly.
- Not run: `just validate-history`; ignored-inclusive searches found no target history artifact. Inline seed provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221413`, full native name objects
at `data/catalog/ncbi_names-0005.jsonl.gz:30754`, 30755 and 30756,
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033991&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033991)
agree on the strain identifier, full label, rank, bacterial domain, parent
and code. Both NCBI exact synonyms are source equivalent names with the
same CB782 designation. All twelve ancestor IDs match: root, cellular
organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Hyphomicrobiales, Rhizobiaceae, Rhizobium/Agrobacterium group, Rhizobium,
R. leguminosarum and its trifolii biovar. Expanded ranks and labels agree
where supplied. Complete exact-ID type-material, merged-ID and
dropped-taxon scans found no rows.

NCBI-carried lineage must remain distinct from GTDB classification.
`GTDB:s__Rhizobium_hidalgonense` denotes a species cluster, not CB782
alone. Its promotion to an exact strain synonym is unsupported even if
the assembly's species classification is biologically plausible.

## Evidence

NCBITAXON identity, one NAME and snapshot 2026-09-13 agree with the
backbone. `data/raw/madin_taxa.tsv:640` confirms seven TRAIT_ASSERTION
records; this checks the inventory count, not seven individual phenotype
claims. `data/raw/gtdb_mappings.tsv:1386` reproduces the closeMatch and
ten-genome count; `data/raw/gtdb_species.tsv:153430` has the same count.
Other directly mapped BacDive, LPSN, GOLD, MediaDive and BactoTraits
inventories were empty. A complete backbone child scan was empty, so
zero descendant-inclusive BacDive strains is consistent with the inputs.

A full scan of all 19 GTDB native shards inspected 901341 rows, matching
the RS232 catalog manifest. The exact hidalgonense cluster contains ten
distinct accessions. Eight have NCBI species taxon 1538159, one is CB782
(1033991), and one is WSM2012 (754522). All ten identity/classification
contexts were inspected. The representative is FH14,
RS_GCF_002914525.1; other designations include CH11, CH26, CH16, CH15,
CB763 and JKLM 19E. CB782 is GB_GCA_000520875.1, a nonrepresentative.
The full CB782 native object at
`data/catalog/gtdb_genomes-0003.jsonl.gz:23017` was read. Ten is a valid
source-cluster assembly count, not ten CB782 genomes or ten distinct
physical strains. The live GTDB tree was inaccessible to the web reader;
the finding relies on the complete pinned native snapshot, not a snippet.

Full native GenBank and historical RefSeq objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:17109` and
`data/catalog/ncbi_refseq_historical-0000.jsonl.gz:5383` agree with
[current NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000520875.1/dataset_report).
GCA_000520875.1 is current; its explicitly paired, sequence-identical
GCF_000520875.1 is suppressed for unverified source organism. The genome
has four replicons totaling 6703653 bases. BioSample SAMN02769652 names
CB782, plant root and Kenya; the sequencing project is PRJNA67103.
NCBI reports failed submitted-species verification and a best ANI match
to R. hidalgonense. These source warnings must be preserved, not silently
used to rewrite TaxonMech's NCBI-carried lineage.

Exact-taxonomy nuccore search returned four records. After initial output
truncation, a structured reread recovered all four identity records, source
qualifiers, references and comments: CP007067.1 is the 4378440-base
chromosome; CP007068.1, CP007069.1 and CP007070.1 are plasmids of
1563772, 509829 and 251612 bases. Their sum agrees with the assembly.
Non-source gene features and raw bases were not reviewed. The entries
are direct JGI submissions, not four independent complete genomes.

The full BV-BRC objects at `data/bvbrc/bvbrc-0000.jsonl.gz:3255` through
3258 explicitly link 1033991.3 to the complete assembly and 1033991.40,
1033991.41 and 1033991.42 to its individual plasmids. The latter are not
three additional whole-genome assemblies. Culture-collection provenance
is blank or absent; the strain name alone does not create an eligible
deposit identifier.

Full GOLD organism/project/analysis rows at `data/gold/organisms.jsonl.gz:6621`,
`data/gold/projects.jsonl.gz:6583` and `data/gold/analyses.jsonl.gz:15935`
give Go0007437 -> Gp0007437 -> Ga0025077 -> IMG 2510065076 and
GCA_000520875.1. The analysis's direct organism field is empty, but its
project bridge is explicit; the organism's culture-collection field is
empty. The [primary JGI portal](https://genome.jgi.doe.gov/portal/RhilegtrifoCB782/RhilegtrifoCB782.info.html)
independently corroborates CB782, project 403027, Gp0007437, BioProject
67103, taxon 1033991 and IMG 2510065076. Its older draft label does not
supersede the current GenBank assembly status. GOLD project and organism
IDs remain related records, not genome identifiers.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. Exact ID, slug and CB782 separator variants
returned 19 contexts, all inspected; SAMEA1033991 is an unrelated
Streptococcus pneumoniae sample. A separate assembly/sample/project/
replicon/JGI-identifier search returned ten contexts, all inspected.

The second search found exact sample SAMN02769652 in
`data/catalog/allthebacteria.tsv.xz:1047118`, with run SRR3927482 but
status META_FAIL and no ENA analysis. This full TSV row was inspected.
It is ineligible for an ATB strain/genome link under the documented
filter, despite the presence of a provided FASTA URL. No eligible
BacDive/StrainInfo deposit bridge was found within these searches.
Native taxon/genome evidence exists; zero BacDive strains must not be
misread as genome absence or fixed by inventing a strain identifier.

The consequential defect is species-to-strain identity promotion, not
an obligation to populate optional nomenclature, phenotype or graph slots.
The record does not currently assert a live RefSeq genome link or an ATB
link, so their source-status caveats are not separate YAML defects.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. Major: a multi-strain GTDB species is promoted to exact strain identity.
   YAML line 49 carries a species-to-strain closeMatch, line 52 introduces
   Rhizobium hidalgonense as an EXACT_SYNONYM, line 63 promotes its xref,
   and line 76 repeats the predicate. The ten-member native cluster
   contains CB782 alongside other strains, including FH14 and WSM2012.
   Species classification does not make the species name an exact name
   for CB782. The source mapping is owned upstream by kg-microbe's GTDB
   transform and ingested by `src/taxonmech/extract.py:501`. TaxonMech's
   `src/taxonmech/seed.py:451` treats every closeMatch as identity and
   line 466 promotes it to synonym/xref without a rank/scope guard.
   These maintained owners, not generated YAML, must receive the fix.

## Recommended Edits

1. Correct the maintained mapping semantics and add a rank/scope guard to
   GTDB identity promotion. Preserve CB782's membership/classification
   evidence, but do not present the entire species cluster as the strain.
   Remove the generated exact species synonym and identity xref through
   regeneration after the source/seeder correction. Do not blindly replace
   closeMatch with broadMatch: verify relation direction and the existing
   upstream predicate contract first.
2. Add a regression in `tests/test_seed.py` covering a strain in a
   multi-strain species cluster. Retain both valid NCBI equivalent names,
   the ten-genome source-cluster count, seven MADIN assertions and separate
   source units. Preserve the NCBI lineage and SEEDED status.

## Follow-up Checks

Rerun the complete exact GTDB cluster comparison and regression tests.
Verify no species-level identity assertion is promoted onto the strain
and that valid same-scope species mappings still work. After an authorized
maintained-input change, regenerate and run focused validators plus full
`just verify-corpus` and the relevant QC gates. Before any future genome
enrichment, retain the RefSeq suppression and ATB META_FAIL exclusions and
require an explicit eligible deposit bridge. No blocker prevents reviewing
other records while this curation issue remains open.

## Additional Notes

`data/taxa/PATHS.tsv:13868` pins the slug;
`curation/seed_scope.tsv:36155` records addition on September 12, 2026
with the three-source reason. The September 13 seed event agrees with
that reason and need not share the scope-addition date. Ignored-inclusive
filename and compressed history-content searches found no prior target
report or history artifact before this report. No human REVIEWED status
was inferred. iModulonDB is not applicable: the YAML asserts no gene,
regulator or expression module. No paid research, outside contact, GitHub
mutation, generator run or status promotion occurred.
