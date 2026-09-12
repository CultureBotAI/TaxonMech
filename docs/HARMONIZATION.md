# Harmonization

How a TaxonRecord is identified, what each source contributes, and how the
corpus is seeded and kept reproducible.

## Identity

**The identifier is the NCBI Taxonomy CURIE.** Every source kg-microbe
transforms already maps its taxa onto NCBI: BacDive strains are
`subclass_of` an NCBI taxon, GOLD organisms likewise, LPSN names and GTDB
species carry `close_match` / `broad_match` edges to NCBI taxa, and MediaDive,
Madin and BactoTraits assert about NCBI taxa directly. Choosing NCBI as the
backbone therefore adds no mapping of this repository's own; it only decides
which side of the existing mappings is the record.

A taxon that no NCBI id covers — a GTDB placeholder species with only
`broad_match` edges, say — is not a record today. The schema allows a minted
`taxonmech:` identifier with `grounding_status: UNGROUNDED` for that case, but
the seeder does not mint: doing so would need a rule for when two sources'
unmapped taxa are the same taxon, and that rule should be argued for on real
examples first.

## Scope and lineage

Records are species-level and below; see [CURATION.md](CURATION.md). The
consequence for harmonization is that TaxonMech never has to place a taxon:
every record's `lineage` is NCBI's parent chain as the inventory carries it,
root first. GTDB's tree and LPSN's parent names are not merged into it,
conflicts between the three are not resolved, and no placement is inferred
for a taxon a source leaves unplaced. Where the trees disagree, the record
shows NCBI's lineage and the other sources' mappings side by side and leaves
the disagreement visible.

## What each source contributes

| Source | Input | Contribution to the record |
|---|---|---|
| NCBI Taxonomy | `ontologies/ncbitaxon_{nodes,edges}.tsv`; ranks and typed synonyms from `data/raw/ncbitaxon.db` | `label`, `rank`, `parent_taxon`, `lineage`, `synonyms`, `genetic_code`, the `NCBITAXON` attestation |
| LPSN | `lpsn/{nodes,edges}.tsv`, `lpsn_api/{nodes,edges}.tsv` | `nomenclature` (authority, status, type strain designations, publications, 16S accessions), `synonyms` from `same_as`, an `xref` to the correct name, the `LPSN` attestation |
| GTDB | `gtdb/{nodes,edges}.tsv`; `data/raw/gtdb/{bac120,ar53}_metadata.tsv.gz` | Species `taxonomy_mappings`, synonyms and attestations from KGX; strain-level NCBI assembly and GTDB genome links from explicit culture identifiers in metadata |
| BacDive | `bacdive/{nodes,edges}.tsv`; `data/raw/bacdive_strains.json` | `strains` (designation, deposits, `is_type_strain`, explicit NCBI `genome_assemblies` and BV-BRC / PATRIC and IMG `genome_records`), `strain_count`, the `BACDIVE` attestation |
| MediaDive | `mediadive/edges.tsv` | `medium_count` per strain and the `MEDIADIVE` attestation counting media |
| GOLD | kg-microbe `gold/edges.tsv`; primary `data/source_snapshots/goldData.xlsx` | Taxon-level `GOLD` attestation from KGX; strain-linked NCBI/IMG identifiers and typed related records through the workbook's organism, sequencing-project and analysis-project IDs |
| AllTheBacteria | Committed `data/atb/` overlap from the 2025-05 assembly metadata snapshot | Snapshot-scoped assembly links through existing BioSample evidence; genome crosslinks retain matching source chains |
| StrainInfo | Committed `data/straininfo/` API snapshot and deposit crosswalk | Explicit own-deposit NCBI assertions, SI-ID/SI-DP related records, strain-record DOIs and nucleotide references |
| Madin et al., BactoTraits | `madin_etal/edges.tsv`, `bactotraits/edges.tsv` | attestations counting trait assertions |

Raw inputs restore information absent from the KGX transforms: NCBI's
semantic-sql build supplies rank and typed synonyms, BacDive's JSON supplies
direct strain-to-genome assertions, and GTDB metadata supplies genome IDs
with culture-deposit identifiers. GOLD's primary workbook supplies explicit
organism and project relationships. The manifest hashes every input snapshot.
NCBI assemblies are the primary genome identifiers; GTDB, BV-BRC / PATRIC,
IMG and AllTheBacteria genome-record identifiers retain their own types and
provenance.

BacDive assertions are joined by BacDive strain ID. GTDB genome rows join
through whole semicolon-delimited culture identifiers in
`ncbi_strain_identifiers`, matched to existing `culture_collection_ids` only
when the collection authority appears in the pinned CAFI registry and the
complete accession satisfies its `regex_id.full` template. Prefix recognition
alone is insufficient. Some existing source entries are bare strain aliases,
so membership in that field alone does not make an identifier suitable for a
genome join. The matcher
normalizes only the recognized authority prefix's case and initial
separator; suffix case, leading zeros and internal punctuation remain
significant. It does not rewrite one collection prefix to another. Unknown
authorities and unsupported accession formats remain unjoined, while their
source values are retained. Each
link records the matched deposit and verbatim source identifiers. Neither
shared species membership nor a matching strain name establishes a link.
Multiple genome identifiers listed by one strain record remain separate
assertions; co-occurrence does not supply a cross-database equivalence
mapping. See [STRAIN_GENOMES.md](STRAIN_GENOMES.md).

The collection-authority register is the attributed CAFI snapshot in
`src/taxonmech/data/cafi_acronyms.json`, with its pinned commit and byte hash
in the accompanying metadata file. Recognized acronym synonyms are not
rewritten to a common prefix. This limits the matching set without deleting
the source's aliases or suppressing its direct BacDive genome assertions;
see [the authority boundary](STRAIN_GENOMES.md#culture-collection-authorities).

GOLD's organism sheet uses the same registered-authority and accession-format
boundary for whole culture identifiers. Sequencing
projects link by `ORGANISM GOLD ID`; analysis projects link through
`AP PROJECT GOLD IDS` and, when supplied, `AP ORGANISM GOLD ID`. Every
stated link must resolve to the same known organism before the analysis
supplies strain-genome identifiers. Supported genome analyses contribute
the explicit `AP IMG TAXON ID` and `AP GENBANK.assemblyAccession` fields.
The organism and project IDs remain typed related records, with the full
join chain preserved in provenance.

AllTheBacteria's whole `sample_accession` joins to existing BIOSAMPLE
assertions in `strain_related_records.tsv`. This preserves the prior GTDB or
GOLD strain evidence without rejoining names, taxa or free-form designations.
Crosslinks to NCBI, GTDB and IMG additionally require matching provenance:
the GTDB metadata row or GOLD organism/project chain must connect that genome
to that sample. They use `relationship: shares_biosample`, never `sameAs`.
The committed `data/atb/strain_links.tsv` and `genome_links.tsv` preserve
these chains as JSON evidence; the full catalog and eligibility boundary are
specified in [ALLTHEBACTERIA.md](ALLTHEBACTERIA.md).

StrainInfo rich source records supply a separate overlay, joined through
whole eligible `deposits.designation` values under the same CAFI authority
and full accession-template rule. SI-ID group membership and the source
BacDive reference never supply the join. Each sequence must explicitly name
the same matched SI-DP; no assembly transfers from another deposit in the
group. The nested evidence retains both identities, source statuses, exact
culture match, sequence deposit and record-version DOI. Alternative/archive
metadata remain source context without asserting that strain groups or
assemblies are equivalent. The browser exposes existing TaxonMech genome
associations separately, preserving their earlier sources and ATB sample
chains. See [STRAININFO.md](STRAININFO.md).

## Mapping predicates

The predicate on a `taxonomy_mappings` entry is the one kg-microbe emits,
and it is worth knowing how kg-microbe assigns it: a GTDB species whose
genomes NCBI labels with exactly one taxon gets `skos:closeMatch` to it; when
several GTDB species carry genomes NCBI labels with the *same* taxon, every
one of them gets `skos:broadMatch` to that taxon. So a `broadMatch` is a
**pooling signal**, not an identity claim. *Escherichia coli* receives
`broadMatch` edges from 51 GTDB species — *Citrobacter freundii* among them —
because GTDB reclassified genomes that NCBI still labels E. coli.

The record therefore ranks its mappings: first the GTDB species LPSN links to
the taxon's name, then any 1:1 `closeMatch`, then the pooled `broadMatch`
species by genome count. Only the first two kinds become `xrefs` and
synonyms; pooled entries are kept, flagged in `notes`, and the `GTDB`
attestation counts the genomes of the primary species alone. Summing the
pooled species' genomes would credit E. coli with *Citrobacter*'s.

LPSN's `close_match` to an NCBI taxon is kg-microbe's name-to-taxon mapping.
The record keeps every LPSN name that maps to it under `nomenclature`; the one
whose status says *correct name* supplies the `LPSN` attestation and the
`xref`. Names LPSN marks deprecated are kept with a note, because a deprecated
name is exactly what a reader searching an old paper will have.

## Which strains belong to a record

BacDive files a strain under the most specific NCBI taxon it has, and for a
type strain that is often a strain-level taxon of its own: the type strain of
*Acinetobacter baumannii* is filed under `NCBITaxon:575584` "Acinetobacter
baumannii ATCC 19606 = CIP 70.34", not under the species. A species record
that looked only at strains filed directly under its own id would miss its
type strain. So a record gathers every BacDive strain filed under its NCBI
subtree, and each gathered strain says where it came from in
`classified_as`. Because every record is species-level or below, that
subtree is small and the count is meaningful. The `BACDIVE` attestation
counts what the record gathered and notes how many strains came from
descendants.

This gathering is deliberately asymmetric: the `GOLD`, `MEDIADIVE`, `MADIN`
and `BACTOTRAITS` counts remain what each source files *directly* under the
record's taxon, and say so in their `notes`. *Escherichia coli* therefore
reports 1,861 strains gathered from nine descendant taxa but only the GOLD
organisms filed under `NCBITaxon:562` itself. Strains are gathered because a
species record without its type strain is wrong; whether the other counts
should be summed over the subtree is a modelling decision tracked in the
issues, not something to do silently.

## Type strains

BacDive itself does not flag type strains in the transform. LPSN does list the
type strain's culture-collection numbers for each name, as `close_match` edges
to `kgmicrobe.strain:DSM-30083`-style ids, and BacDive strains `close_match`
the same ids for their deposits. A strain is `is_type_strain: true` when one of
its deposits is a designation LPSN gives for a name of the same taxon. This is
a derived flag: it is only as complete as LPSN's designations and BacDive's
deposit lists, and a type strain deposited under a number LPSN does not list
will be missed.

## The universe and the scope

Extraction inventories every NCBI taxon that BacDive, LPSN, MediaDive, GOLD,
Madin or BactoTraits attests, plus every ancestor, so a record's lineage is
always resolvable from the committed data. GTDB is deliberately not an
attesting source for the universe: its 199,923 species carry 322,327 mapping
edges to NCBI taxa, most of them strain-level taxa nothing else mentions, and
inventorying those would triple the data for no gain. GTDB mappings are kept where they land inside the
universe.

The **corpus** is the subset of the universe listed in
`curation/seed_scope.tsv`. Every row carries the date and the rule or reason
that put it there. `scripts/propose_scope.py` ranks candidates; a human
decides what to append. This keeps "which taxa are records" an explicit,
reviewable diff rather than an emergent property of upstream refreshes.

## Reproducibility

`data/raw/MANIFEST.yaml` records the kg-microbe commit and the byte hash of
every input read and every inventory written, including the direct GOLD
workbook and its source URL. `scripts/check_provenance.py`
verifies the committed inventories against it. `scripts/verify_corpus.py`
rebuilds every in-scope record through the seeder's own `build_document` and
compares byte-for-byte with what is on disk, so a hand edit, a bad merge, or a
seeder change that was not re-applied all fail `just qc`.

The seed timestamp on every record is the manifest's `extracted_at`, not the
wall clock, and the extractor carries the previous `extracted_at` forward when
every input hashes the same, so neither a re-seed nor a re-extraction of
unchanged data produces a diff.

## Strain listings

A species like *Escherichia coli* has thousands of BacDive strains. A record
lists at most 200 (`STRAIN_LISTING_CAP` in `seed.py`): type strains first,
then the strains with the most culture-collection deposits, then by BacDive
id. `strain_count` always gives the full number, and
`data/raw/bacdive_strains.tsv` holds every strain with its taxon. The cap is a
readability decision; the data is not lost.

`data/raw/strain_assemblies.tsv` keeps every imported NCBI assembly link for
the inventoried strains; `data/raw/strain_genome_records.tsv` adds BV-BRC /
PATRIC, IMG and GTDB genome-record links. `data/atb/strain_links.tsv` adds
eligible AllTheBacteria associations through BioSample evidence. Join these
to `bacdive_strains.tsv` on `strain_id` for the complete mapping to culture-collection identifiers.
Listing caps do not truncate these inventories. Corpus reports count linked
identifiers and strain-identifier pairs per database; their sum is not a
count of unique biological genomes across resources.

`data/raw/strain_related_records.tsv` uses the same strain join for typed
BioSample, BioProject and GOLD organism/project references. These provide
source context and are excluded from genome-identifier counts.
