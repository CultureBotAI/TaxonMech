# YAML Record Review: Lactobacillus johnsonii 16

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillus_johnsonii_16.yaml`
- Started UTC: 2026-10-04T23:22:04Z
- Finished UTC: 2026-10-04T23:25:23Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033983`, Lactobacillus
johnsonii 16. It asserts STRAIN rank, BACTERIA domain, parent 33959,
ten ancestors, code 11, EXACT grounding, SEEDED status, a GTDB species
mapping, three synonyms, one xref, zero BacDive strains, three source
attestations and one seed event. No record, source, code, status or history
was changed. The finding concerns scope, not the NCBI identity.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/lactobacillus_johnsonii_16.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/lactobacillus_johnsonii_16.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded backbone, complete lineage, directly mapped inventories, scope, filename and inline-event comparisons passed. A full structured GTDB cluster census matched the manifest file set and row total.
- Not run: full-corpus `just verify-corpus`, QC, tests or rendering. `--max-diffs` limits diagnostics, not scope; bounded comparisons do not prove byte reproduction.
- Not applicable: `just validate-products`; no curator graph nodes. NCBI identity was checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target history artifact. Inline provenance was checked.
- Live GTDB taxon/genome pages were inaccessible through the web tool; its API schema request returned HTTP 403. The GTDB finding uses the inspected pinned RS232 metadata, not unverified current web content.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221405`, the three full native
name objects at `data/catalog/ncbi_names-0005.jsonl.gz:30744`,
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033983&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033983)
agree on strain identity, rank, bacterial domain, parent, code and both
NCBI equivalent names. All ten ancestor IDs match: root, cellular
organisms, Bacteria, Bacillati, Bacillota, Bacilli, Lactobacillales,
Lactobacillaceae, Lactobacillus and Lactobacillus johnsonii. Expanded
labels and ranks agree where supplied. No lineage reconciliation is needed.

Complete exact-ID type-material, merged-ID and dropped-taxon scans found
no rows; a complete backbone scan found no children. The two NCBI exact
synonyms are supported. The GTDB exact synonym is not equivalent in scope
to this strain; see the major finding below.

## Evidence

`data/raw/gtdb_mappings.tsv:1385` reproduces the record's closeMatch
to `GTDB:s__Lactobacillus_sp910589675` and count 683.
`data/raw/gtdb_species.tsv:109378` independently carries that cluster total.
The full scan of all 19 native GTDB shards covered 901341 rows, matching
`data/catalog/MANIFEST.json` and its complete RS232 file set. Exactly
683 distinct accessions belong to this species cluster. Their NCBI taxon
distribution is 33959:673, 153152:3, 1596:3, and one each for 1033983,
1591, 1408186 and 257314. Thus only one member is classified as strain 16.
Other members explicitly include N6.2 and NCC 533. This is positive
evidence that species-cluster identity is broader than this strain.

The full target GTDB object, `data/catalog/gtdb_genomes-0002.jsonl.gz:2341`,
identifies `RS_GCF_001270785.1`, strain 16, taxon 1033983 and the
asserted cluster. It supports cluster membership, not identity of the
entire cluster with the strain. The schema defines genome_count as the
number of assemblies under the source taxon; 683 is correct under that
definition and must not be relabeled as 683 genomes of strain 16.

Full GenBank and RefSeq objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:47391` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:39997` agree with live
[NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_001270785.1/dataset_report).
Exact-taxonomy Assembly search returns one current contig assembly,
GCF_001270785.1, paired with GCA_001270785.1. The source explicitly
marks the pair identical. It has 156 contigs and 1787772 bases, with
BioSample SAMN03995694, sequencing project PRJNA67007, RefSeq project
PRJNA224116 and WGS master LIGY00000000.1. BioSample attributes name
strain 16, mouse feces, Israel and collection date 2007-12-12.

The full [genome announcement](https://pmc.ncbi.nlm.nih.gov/articles/PMC4599083/),
PMID 26450724, DOI `10.1128/genomeA.01141-15`, was inspected via
PubMed XML and Europe PMC full-text XML. It independently identifies
strain 16 and LIGY00000000.1, and distinguishes it from the NCC 533
reference strain. It describes an initial 210-contig assembly and removal
of short contigs before deposition of 156 segments. No registered culture
deposit is supplied in the inspected article. No phenotype was imported.

Full BV-BRC object `data/bvbrc/bvbrc-0000.jsonl.gz:3254` identifies
genome 1033983.3 and the same assembly/sample. Full GOLD objects
`data/gold/organisms.jsonl.gz:10659`, `projects.jsonl.gz:10517` and
`analyses.jsonl.gz:52058` retain Go0012107, Gp0012107 and Ga0081980.
The project links to that organism and sample; the analysis links to the
project, GCA_001270785.1 and IMG 2648501494, but has an empty direct
organism field. These are source-native associations, not eligible culture
deposit joins. The organism's culture-collection field is empty.

The NCBI NAME attestation and GTDB cluster count match their inventories.
`data/raw/madin_taxa.tsv:639` supports one MADIN TRAIT_ASSERTION.
The count is not a phenotype claim; the original Madin edge and its
underlying experimental evidence were not independently re-evaluated.
`data/raw/MANIFEST.yaml` pins the supporting transform. Complete directly
mapped BacDive, LPSN, GOLD, MediaDive and BactoTraits scans found no rows.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. ID, full name, equivalent names and slug
returned 20 contexts; assembly, sample, project, WGS and GOLD/IMG
identifiers returned 51. All returned contexts were inspected.

The searches retained the genuine assembly associations above and rejected
16S descriptions for another Lactobacillus johnsonii deposit, unrelated
WGS accessions containing LIGY, longer BioProject identifiers and
SAMEA1033983, a Streptococcus pneumoniae sample. No registered deposit
supporting a BacDive or StrainInfo join was found within this scope.
Bare designation 16 must not be used as a culture-collection identifier.

`strain_count: 0` counts BacDive records, not known isolates or genomes.
Under the current schema, absence of a BacDive StrainEntry is not proof
that this sequenced isolate does not exist and does not license inventing
one. The native genome catalogs preserve its evidence. Any future direct
taxon-genome presentation would require an explicit model extension,
not a fabricated deposit join.

Exact-taxonomy nuccore search returned 314 records. The detail limit of
20 was exceeded; individual sequence records were not paginated or
exhaustively inspected. Assembly and BioSample metadata and the complete
genome paper supplied the bounded identity check. No exhaustive claim
about all sequence qualifiers is made. Optional phenotype, definition and
causal graph slots need not be populated for this record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. Major: species-cluster membership is promoted to strain identity.
   `data/taxa/bacteria/lactobacillus_johnsonii_16.yaml:43` carries a
   species-to-strain closeMatch; line 52 turns the species label into an
   EXACT_SYNONYM, and line 57 makes it an equivalent xref. The attestation
   repeats the predicate at line 70. The complete RS232 cluster census
   demonstrates the different scopes. The strongest error is the derived
   exact synonym/xref, not the correctly scoped 683 cluster count.
   Maintained owners: kg-microbe's GTDB mapping transform, consumed by
   `src/taxonmech/extract.py:501`, and the unconditional closeMatch
   identity promotion in `src/taxonmech/seed.py:451` and line 466.
   Reproducing the upstream predicate does not justify exact synonymy.

## Recommended Edits

1. In a separately authorized curation change, make the seeder's synonym
   and xref promotion rank- and scope-aware. A strain's single genome
   membership in a species cluster must not produce a species-level exact
   alias. Preserve NCBI identity, lineage and both genuine equivalent names.
2. Correct the mapping semantics in the maintained upstream GTDB transform,
   then refresh through `src/taxonmech/extract.py`. Preserve original source
   provenance and distinguish membership from identity. Do not blindly
   replace closeMatch with broadMatch: this schema defines the predicate
   from the source taxon's side, and the species is broader than the strain.
3. Keep 683 explicitly scoped to the GTDB species. Add regressions in
   `tests/test_seed.py` for a strain inside a multi-strain cluster and for
   preservation of legitimate species-level mappings. Regenerate through
   the supported pipeline, never hand-edit this generated YAML.

## Follow-up Checks

Confirm that regenerated output no longer identifies strain 16 with the
whole species cluster, while preserving its evidenced classification,
source count and NCBI synonyms. Test mapping direction separately from
name generation. Run focused schema/strict validation, the new unit tests
and full `just verify-corpus`; refresh the live GTDB authority check when
available. No blocker prevents further reviews; the major issue remains
unfixed because this task is read-only review.

## Additional Notes

`data/taxa/PATHS.tsv:13860` pins the slug;
`curation/seed_scope.tsv:36154` supplies the September 12, 2026 date
and three-source reason. The event at `2026-09-13T17:54:04Z` agrees.
Ignored-inclusive filename and history-content searches found no prior
target report or history artifact. No identity changes were inferred from
other strains or a genome classifier. iModulonDB is not applicable: no
gene, regulator or expression-module claim is asserted. No paid research,
outside contact, GitHub mutation, generator run or status promotion occurred.
