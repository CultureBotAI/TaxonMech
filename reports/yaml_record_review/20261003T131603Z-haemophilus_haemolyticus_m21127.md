# YAML Record Review: Haemophilus haemolyticus M21127

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/haemophilus_haemolyticus_m21127.yaml`
- Started UTC: 2026-10-03T13:14:12Z
- Finished UTC: 2026-10-03T13:16:03Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1028804`, Haemophilus haemolyticus
M21127, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:726`.
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 84-line YAML. It contains ten lineage entries, one GTDB
mapping, three synonyms, one xref, zero BacDive strain entries, three
source attestations and the embedded seed event. No publication, genome
accession or causal graph is directly asserted. The finding concerns a
species label promoted to strain identity, not the NCBI grounding itself.

This is a read-only review. Only this report was manually written; no
source, generated record, history, status or page was changed. Eukaryota
was outside the review.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/haemophilus_haemolyticus_m21127.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/haemophilus_haemolyticus_m21127.yaml` | PASS; one file, zero errors. |
| Complete identity, lineage and NCBI synonyms | PASS; label, rank, parent, code, both NCBI synonyms and all ten ancestor objects agree with the raw inventory. |
| Complete BacDive subtree check | PASS; target is its only subtree member, with zero classified BacDive entries. |
| Full native GTDB species census | PASS for source count: five distinct accessions, two NCBI taxids, only one M21127 genome. All five source objects were read. |
| All raw GTDB mapping targets | PASS for inventory fidelity: closeMatch to 1028804 and broadMatch to 726, both with count five. Does not validate exact strain identity. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused validator. |
| `just validate-history` | Not run: ignored-inclusive identifier/name/slug search found no standalone target history. Strict validation checked the embedded seed event. |
| Graph and generated products | No graph asserted; graph grounding not applicable. Generated pages and exports were not audited. |

Initial direct NCBI requests failed, but following the parent species and
record links recovered Taxonomy, BioSample and BioProject evidence. The
live GTDB page remained unavailable. PMC returned a browser challenge for
the genome publication; the article body was not treated as inspected
evidence. No sequence payload was reassessed.

## Identity and Grounding

The [current NCBI summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028804)
identifies M21127 as a strain. The inspected
[legacy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1028804&lvl=3&mode=node)
confirms identifier, name, both equivalent strain names, parent lineage
and code 11, but still displays `no rank`. The current summary and pinned
taxonomy support `STRAIN`; retain that source-version distinction rather
than overwriting the YAML from the legacy surface.

The full raw identity at `data/raw/ncbitaxon_taxa.tsv:219209` agrees with
the YAML. All native name objects at
`data/catalog/ncbi_names-0005.jsonl.gz:28267` onward were read: one scientific
name and two equivalent names explicitly containing M21127. These two
NCBI exact synonyms are supported.

The GTDB species is a classification of multiple genomes, not a strain
alias. Its native order is Enterobacterales, whereas the preserved NCBI
lineage uses Pasteurellales. Those are separate source hierarchies; neither
the broader species nor GTDB's order should replace the NCBI identity.

## Evidence

**Raw provenance.** `data/raw/gtdb_species.tsv:72333` and
`data/raw/gtdb_mappings.tsv:1242` support the source species, count five
and imported closeMatch. `data/raw/madin_taxa.tsv:536` supplies one trait
assertion. `curation/seed_scope.tsv:36103` agrees with the three-source
selection and embedded seed event. The NCBI count is one scientific-name
attestation, not a count of synonyms. No particular phenotype is asserted
by the Madin count.

**Complete GTDB cluster membership.** Read all five native objects, then
independently streamed every native GTDB genome shard to verify exact
species membership and unique-accession count:

| Genome | Native strain/isolate value | NCBI taxid | Native object |
| --- | --- | --- | --- |
| RS_GCF_000222045.1 | M21127 | 1028804 | `data/catalog/gtdb_genomes-0006.jsonl.gz:26604` |
| RS_GCF_003351405.1 | M19345 | 726 | `data/catalog/gtdb_genomes-0009.jsonl.gz:1913` |
| RS_GCF_003490655.1 | M26156 | 726 | `data/catalog/gtdb_genomes-0015.jsonl.gz:45186` |
| RS_GCF_004368395.1 | HI2028 | 726 | `data/catalog/gtdb_genomes-0007.jsonl.gz:8622` |
| GB_GCA_963522805.1 | ERR9968989_bin.11_MetaWRAP_v1.3_MAG | 726 | `data/catalog/gtdb_genomes-0010.jsonl.gz:27454` |

M19345, not M21127, is the representative. The last member is explicitly
metagenome-derived; do not interpret five source genomes as five pure
cultures. Only one member carries the target taxid. The other raw mapping
at `data/raw/gtdb_mappings.tsv:305316` relates the same species to NCBI
species 726 with broadMatch. The count five is correct for the source
cluster, not a claim of five M21127 genomes.

**Native target genome context.** Complete relevant source objects read:

| Source | Checked evidence |
| --- | --- |
| `data/catalog/ncbi_genbank-0000.jsonl.gz:3843` | GCA_000222045.2, latest, contig level with 38 contigs, M21127, target taxid/species 726, SAMN02952885 and PRJNA66575. |
| `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1159` | GCA_000222045.1 is suppressed; source not-live date 2012-01-29. Preserve the version distinction. |
| `data/catalog/ncbi_refseq-0000.jsonl.gz:3307` | GCF_000222045.1, latest in this snapshot, identical paired GenBank assembly GCA_000222045.2, same strain/sample, project PRJNA224116. |
| `data/bvbrc/bvbrc-0000.jsonl.gz:2993` | Genome 1028804.3, WGS, M21127, GCA_000222045.2, PRJNA66575, SAMN02952885 and AFQP00000000. |
| `data/gold/organisms.jsonl.gz:10575` | Go0012008, taxid 1028804, M21127; no culture-collection identifier. |
| `data/gold/projects.jsonl.gz:10433` | Gp0012008 explicitly joins Go0012008, PRJNA66575 and SAMN02952885. |
| `data/gold/analyses.jsonl.gz:8817` | Ga0015257 joins Gp0012008, IMG 2534681807 and unversioned GCA_000222045. Do not invent an accession version. |

The [BioSample record](https://www.ncbi.nlm.nih.gov/biosample/SAMN02952885)
confirms strain M21127, AFQP00000000.1 and PRJNA66575. The
[BioProject record](https://www.ncbi.nlm.nih.gov/bioproject/66575)
explicitly connects GCA_000222045.2 at contig level to that sample and
taxid. Its generic project background was not promoted into a clinical
or phenotype claim on the target.

The project names the genome study identified by PMID 21952546 in native
assembly metadata. Its article body was not inspected; search excerpts
were not used to add traits or adjudicate genome-analysis claims.

**Native GOLD presence differs from taxon-attestation coverage.** No
target count row is present in `data/raw/gold_organisms.tsv`. The native
organism/project/analysis chain nevertheless exists.
`docs/HARMONIZATION.md` and `conf/sources.yaml` distinguish KGX-derived
taxon counts from workbook-derived genome evidence. An empty collection
field and bare M21127 designation do not establish an eligible BacDive
deposit join. The missing GOLD attestation matches the maintained input;
no replacement count or strain association was inferred.

## Completeness

Identity, lineage, code, NCBI aliases and seed provenance are complete for
the asserted record. Zero BacDive strains agrees with the full subtree
check and is not a claim that M21127 lacks a sequenced genome. The native
genomes above cannot be attached to a fabricated BacDive row merely by
sharing a strain label or taxonomy.

Ignored-inclusive identifier, full-name, slug, strain-token, exact sample
and assembly-stem searches covered `history/`, `data/raw/`,
`data/bacdive/`, `data/straininfo/` and `data/atb/`, including compressed
data where needed. No target standalone history, native BacDive entry,
StrainInfo match or ATB match was found within those locations. No target
LPSN row was found in the raw nomenclature inventory. These are bounded
local-source checks, not worldwide absence claims.

No phenotype, gene, regulator, transcriptomic dataset or causal graph is
asserted. iModulonDB and graph checks are not applicable; their omission
from this review supplies no negative biological evidence.

## Findings

Blocker: 0. Major: 1. Minor: 0.

**M1 (major): GTDB species membership is promoted to exact strain
identity.** Target lines 46-49 declare Haemophilus haemolyticus N an exact
synonym of M21127; lines 56-57 promote the species to an equivalent xref.
The complete native cluster has five genomes, including four not assigned
to this strain taxid. The source closeMatch and representative-based
classification do not support that identity assertion.

Maintained owner: `src/taxonmech/seed.py:451` treats any closeMatch as
identity without a rank/scope guard; lines 467-469 emit the xref and exact
synonym. `src/taxonmech/extract.py` preserves upstream mapping predicates.
The schema restricts identity xrefs to true equivalences, and
`docs/HARMONIZATION.md` describes the current promotion policy. Generated
YAML and raw inventory files are not manual-fix owners.

## Recommended Edits

1. In a separately authorized change, add rank/scope-aware GTDB identity
   handling to `src/taxonmech/seed.py`. Regenerate without the broader
   species exact synonym or identity xref, preserving both NCBI strain
   aliases and source classification context.
2. Preserve five as the source-cluster count. Review the upstream predicate
   semantics before choosing a replacement relation, and update the
   maintained harmonization guidance. Do not silently relabel the count
   as one or guess a mapping direction in generated YAML.
3. Add `tests/test_seed.py` cases for strain-level closeMatch targets with
   multiple cluster members, singleton clusters and valid same-scope
   species identities. Ensure metadata for metagenome-derived members is
   not converted into cultured-strain identity.

## Follow-up Checks

After the maintained fix, run focused seed tests, both target validators,
dry `just seed` and `just seed-canary NCBITaxon:1028804`. Inspect the actual
result for retained NCBI aliases, unchanged source count/provenance and
removal of the broader exact synonym/xref. Run full `just verify-corpus`
before accepting corpus-wide regeneration.

Retry the live GTDB page when accessible. Any future addition of native
genome links without a BacDive anchor requires an explicit supported
schema/join design; taxon co-membership and a matching bare label are
insufficient to create a deposit association.

## Additional Notes

The finding is biological scope inflation despite successful schema
validation. No human-review promotion, seed status change or curation
history was written. Review-report filename coverage remains separate
from full-corpus completion and from the quality of other reports.
