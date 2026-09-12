# Strain identifiers and genome identifiers

A primary TaxonMech use case is answering **which genome identifiers a source
associates with a strain identifier**, and following a genome link back to the
strain's BacDive record and culture-collection deposits. This enables links
between experimental observations made on a strain and genomic data.

**NCBI GenBank/RefSeq assemblies are the priority**, with all available genome
identifier systems in scope when their strain links have evidence. GTDB,
BV-BRC / PATRIC, IMG and AllTheBacteria genome records retain their own
identifier types.
BioSample, BioProject and GOLD organism/project references provide related
context without being counted as genomes. Expanding database coverage does
not replace an NCBI assembly ID or establish that identifiers from different
resources denote the same genome.

## Relationship model

| Entity or relationship | Representation | Meaning |
|---|---|---|
| Taxon | `TaxonRecord.identifier`, an NCBITaxon CURIE | Classification context for a species or lower taxon |
| Strain | `strains[].strain_id`, with `source_id` and `designation` | A source's strain record |
| Source deposit or alias identifier | `strains[].culture_collection_ids[]` | Values carried from kg-microbe's BacDive transform; registered authority and authority-specific accession format are checked separately before a genome join |
| NCBI genome assembly (primary) | `strains[].genome_assemblies[].assembly_id` | A GenBank or RefSeq assembly accession, with its version when supplied |
| Strain-to-assembly assertion | `GenomeAssemblyLink` | A source explicitly associates this assembly with this strain record |
| Other database genome record | `strains[].genome_records[].genome_id` | A typed GTDB, BV-BRC / PATRIC, IMG or AllTheBacteria genome identifier |
| Strain-to-genome-record assertion | `GenomeRecordLink` | An association to this database record, supported by direct source evidence or a retained sample chain |
| Related sample, project or organism | `strains[].related_records[].record_id` | A BioSample, BioProject or GOLD organism/project identifier, classified by `record_type` |
| Strain-to-related-record assertion | `GenomeRelatedRecordLink` | Source context attached to a strain, excluded from genome counts |

The relationship is many-to-many: one strain can have multiple genome links,
and multiple source strain records can point to the same genome identifier.
Preserve each assertion and its provenance. A link is not `sameAs` between a
strain and a genome record, nor proof that every culture deposit or substrain
has an identical sequence. BacDive can group assemblies of substrains under
one strain record. Source descriptions remain visible so those distinctions
can be reviewed.

## Fields and provenance

For each assertion, `GenomeAssemblyLink` requires `assembly_id`, `source` and
`source_id`. It retains `source_reference_id` (BacDive's `@ref`),
`assembly_name`, `assembly_level` and `taxon_id` when present. That taxon is
the source's classification of the assembly and may disagree with the
strain's classification; it never changes the record's lineage.

`GenomeRecordLink` requires `genome_id`, `source_database`, `source` and the
asserting `source_id`. It retains `source_reference_id`, `genome_name`,
`assembly_level` and `taxon_id` when present. `GenomeRelatedRecordLink` carries
`record_id` and `record_type` with source provenance and optional
`record_name` and `taxon_id`.

All three link classes share `StrainLinkEvidence`. When a source row is
matched through a culture-deposit identifier, `matched_strain_id` records
the existing deposit CURIE, `source_strain_identifiers` keeps the source
value verbatim, `source_strain_field` names that strain column and
`source_field` identifies the field supplying the linked identifier. GOLD
chains also retain `source_organism_id` and `source_project_id` when present.
The inventory manifest records the exact input file and byte hash; the link
points to the source record within that snapshot.

| Database | TaxonMech identifier | Source relationship |
|---|---|---|
| GenBank/RefSeq | `ncbi.assembly:GCA_…` or `ncbi.assembly:GCF_…` | NCBI assembly assertion in `genome_assemblies` |
| BV-BRC / PATRIC | `patric:<digits>.<digits>` | PATRIC genome ID from BacDive in `genome_records`, linked to BV-BRC |
| IMG | `img.taxon:<digits>` | IMG genome-record ID from BacDive or a primary GOLD analysis in `genome_records` |
| GTDB genome | `gtdb.genome:RS_GCF_…` or `gtdb.genome:GB_GCA_…` | Original GTDB metadata accession and version in `genome_records`; separate from `GTDB:s__…` species mappings |
| AllTheBacteria assembly | `atb.assembly:202505.SAM…` | Local snapshot-scoped assembly identifier in `genome_records`, associated through retained BioSample evidence |
| BioSample | `biosample:SAM…` | `related_records` entry of type `BIOSAMPLE` |
| BioProject | `bioproject:PRJ…` | `related_records` entry of type `BIOPROJECT` |
| GOLD organism | `gold:Go…` | `related_records` entry of type `GOLD_ORGANISM` |
| GOLD sequencing project | `gold:Gp…` | `related_records` entry of type `GOLD_PROJECT` |
| GOLD analysis project | `gold:Ga…` | `related_records` entry of type `GOLD_ANALYSIS` |
| StrainInfo strain | `straininfo.strain:…` | Source strain record, related type `STRAININFO_STRAIN`; distinct from its deposits and record-version DOI |
| StrainInfo deposit | `straininfo.deposit:…` | Culture deposit, related type `STRAININFO_DEPOSIT`; sequence links require this exact deposit's assertion |
| Source nucleotide sequence | `INSDC:…` | Related type `NUCLEOTIDE_SEQUENCE` for StrainInfo gene, rRNA operon or patent references; excluded from genome counts |

## BacDive assertions

The extractor reads `Sequence information / Genome sequences` from
kg-microbe's `data/raw/bacdive_strains.json`, which is recorded and hashed in
`data/raw/MANIFEST.yaml`. The transformed BacDive graph supplies the strain
IDs and deposits; the raw snapshot supplies the missing genome links.
BacDive assertions use `source: BACDIVE` and `source_id: bacdive:<digits>`;
`source_database` retains `patric` or `img` for those genome-record links.

BacDive distinguishes assembly accessions, other database genome IDs and
16S sequences in its [field documentation](https://api.bacdive.dsmz.de/strain_fields_information).
The BV-BRC genome identifier is distinct from its contig and feature IDs;
see the [BV-BRC data model](https://www.bv-brc.org/docs/cli_tutorial/cli_getting_started.html).
IMG similarly distinguishes genome, scaffold and gene identifiers in its
[import documentation](https://img.jgi.doe.gov/docs/faq/).

These links preserve the source's `assembly_level` value, including labels
such as `plasmid` and `wgs`. They are database-record assertions and must not
all be described as complete genome assemblies. Chromosome and WGS sequence
accessions in the snapshot do not become NCBI assembly or other database
genome-record IDs.

The extractor deduplicates identical assertions;
different references, descriptions, accession versions and strain IDs remain
separate. Malformed identifiers and links to strains excluded from the taxon
inventory are recorded in `data/raw/dropped.tsv`.

## Culture-collection authorities

An entry in `culture_collection_ids` is not automatically a globally scoped
deposit identifier. The BacDive transform also carries bare strain aliases
such as `BR-17` and `Mu-3`; joining those across sources can associate genomes
with unrelated organisms. The reproduced failures are recorded in
[issue #27](https://github.com/CultureBotAI/TaxonMech/issues/27).

GTDB and GOLD matching therefore requires both a collection authority
recognized by DSMZ's CAFI registry and an accession that fully matches that
authority's `regex_id.full` template. Prefix recognition alone is unsafe:
`AS` is a registered historical collection acronym, but its accession format
requires digits followed by a dot and more digits. Lab aliases such as
`AS-8`, `AS-7` and `AS_2` fail that format and do not establish a join;
`AS 1.2` has the supported form.
TaxonMech packages a byte-identical copy of
[the upstream register at `effeca350ac72faeb01d19c2c14830a905c5d116`](https://github.com/LeibnizDSMZ/cafi/blob/effeca350ac72faeb01d19c2c14830a905c5d116/src/cafi/data/acr_db.json)
as `src/taxonmech/data/cafi_acronyms.json`. The source URL, hash, authors and
CC-BY-4.0 attribution are recorded in
[`cafi_acronyms.metadata.json`](../src/taxonmech/data/cafi_acronyms.metadata.json).

CAFI's `acr` and `acr_synonym` fields recognize authority prefixes; the
corresponding `regex_id.full` validates the complete accession, with case
preserved. An explicit separator must divide the authority from its
accession. Matching normalizes only the prefix's case and that separator.
A valid accession retains its case, punctuation and leading zeros:
`CCUG 123a` and `CCUG 123A` remain different keys. Historical collection
aliases are recognized without being rewritten to another prefix; `IFO`
does not become `NBRC`. Compound prefixes can use CAFI's colon spelling or
the literal hyphen form, but those spellings also remain distinct keys.

Unknown authorities and unsupported accession formats remain in the BacDive
inventory and record listings but do not create cross-source genome joins.
This deliberately limits coverage: a legitimate deposit spelling that the
pinned templates do not support remains unjoined until its authority or
format has evidence. It does not establish that an unmatched strain lacks a
genome. Direct BacDive genome assertions do not depend on this cross-source
matcher.

## GTDB genome metadata

The extractor reads kg-microbe's `data/raw/gtdb/bac120_metadata.tsv.gz` and
`data/raw/gtdb/ar53_metadata.tsv.gz`. These are genome-level metadata inputs,
separate from the transformed GTDB species mappings. GTDB describes its
NCBI-based genome collection and metadata in its
[FAQ](https://gtdb.ecogenomic.org/faq).

Each semicolon-delimited token in `ncbi_strain_identifiers` is matched as a
whole culture-deposit identifier against existing `culture_collection_ids`,
subject to the [authority and accession-format rule](#culture-collection-authorities).
Matching normalizes only recognized authority-prefix case and the initial
separator, while preserving suffix case, leading zeros and internal
punctuation. A bare designation, isolate name, species name,
NCBITaxon ID or substring never establishes the join. If a row names several
matching deposits, the matching evidence remains visible for each link.

The resulting assertions use `source: GTDB` and retain the original metadata
key as `source_id: gtdb.genome:RS_GCF_…` or `gtdb.genome:GB_GCA_…`, including
its version. Removing the `RS_` or `GB_` wrapper yields the NCBI assembly
accession carried by that key. An explicit
`ncbi_genbank_assembly_accession` supplies an additional GenBank link when
present; its version may differ and is preserved as reported. This does not
infer RefSeq pairing by replacing an accession prefix.

`ncbi_biosample` and `ncbi_bioproject` values are retained in
`related_records`, with the same strain-match evidence. A sample or project
link supplies context for the matched genome row; it is not another genome.
The full metadata values and input hashes remain the evidence even if a
newer GTDB release changes an accession or classification.

## Primary GOLD organism and project metadata

GOLD distinguishes an organism, the project that sequences it and the
analysis that assembles or annotates the data. Those entities can supply
genome links without becoming genome identifiers themselves. See
[GOLD's terminology](https://gold.jgi.doe.gov/help).

The extractor reads the primary
[public workbook](https://gold.jgi.doe.gov/download?mode=site_excel), stored
by default at `data/source_snapshots/goldData.xlsx`. `--gold-workbook` or
`GOLD_WORKBOOK` can select another copy. The workbook is not committed;
`data/raw/MANIFEST.yaml` records its URL and byte hash, and the derived
inventories reproduce the corpus without requiring the workbook.

The `Organism` sheet's `ORGANISM CULTURE COLLECTION ID` and `ORGANISM STRAIN`
fields supply whole culture identifiers. Semicolon, comma and pipe separate
tokens in these GOLD fields; the same authority and accession-format checks
and prefix-only normalization used for GTDB apply. Matching never uses the organism name
or taxonomy. The `Sequencing Project` sheet joins by `ORGANISM GOLD ID` and
retains its `PROJECT GOLD ID`, NCBI BioSample and BioProject accessions.

The `Analysis Project` sheet resolves `AP PROJECT GOLD IDS` through those
sequencing projects. Every referenced project must resolve to the same known
organism, and `AP ORGANISM GOLD ID`, when supplied, must agree. An analysis
with a direct organism link can also be retained when no project IDs are
supplied. Conflicting or unknown chains are recorded in `dropped.tsv` and do
not supply strain-genome links.

Supported genome analyses contribute `AP IMG TAXON ID` as an IMG genome
identifier and exact `assemblyAccession` values from the `AP GENBANK` JSON
as NCBI assembly links. Chromosome accessions elsewhere in that JSON are not
assemblies. Other analysis types can supply a typed GOLD analysis reference
without adding genome identifiers. Each assertion uses `source: GOLD` and
retains its organism/project chain, matched deposit, source columns and
verbatim strain-identifier field.

GOLD's `Go`, `Gp` and `Ga` identifiers remain in `related_records` as
`GOLD_ORGANISM`, `GOLD_PROJECT` and `GOLD_ANALYSIS`. NCBI and IMG identifiers
from their explicit fields enter the corresponding genome inventories.
They are counted by identifier database, independently of GOLD as the source
asserting the link. GOLD metadata retain their
[source usage policy](https://gold.jgi.doe.gov/usagepolicy); the requested
resource citation is [GOLD v.10](https://doi.org/10.1093/nar/gkae1000).

## AllTheBacteria assembly metadata

AllTheBacteria contributes assemblies through exact BioSample identifiers
already supported by the strain's GTDB or GOLD evidence. Each link uses
`source: ALLTHEBACTERIA`, `source_database: allthebacteria` and a local
snapshot ID such as `atb.assembly:202505.SAMN…`. Its `atb_evidence` retains
the sample, original BIOSAMPLE assertions, ENA analysis when available,
source run accessions, filters, SeqKit sum and native FASTA/archive links.
This adds an assembly identifier without counting the sample as a genome.

The uncapped `data/atb/strain_links.tsv` covers eligible available assemblies,
including strains omitted from taxon pages. `data/atb/genome_links.tsv`
records `shares_biosample` crosslinks only where an existing genome assertion
and sample assertion have matching source provenance. It never joins every
genome listed under one strain. Neither shared sample nor matching species
means the assemblies are identical. The full source catalog keeps all
statuses; the browser uses only the committed linked overlap. See the
[ATB catalog, flags and query guide](ALLTHEBACTERIA.md).

## StrainInfo deposit-specific assertions

StrainInfo adds a separate, uncapped component in `data/straininfo/`. Match a
rich source record's own eligible deposit designation through the pinned
CAFI authority and full accession template. Preserve the matched culture,
SI-ID strain record, SI-DP deposit, source statuses and strain record-version
DOI. A genome or nucleotide accession must explicitly name that matched
SI-DP in its source sequence record. Membership in the same SI-ID group,
species names and source BacDive cross-references cannot transfer sequences
between deposits.

Explicit NCBI GCA/GCF accessions enter `genome_assemblies`, preserving supplied
versions and leaving unversioned accessions unversioned. SI strain/deposit
IDs and gene/rRNA/patent sequence accessions enter typed `related_records`,
outside genome counts. StrainInfo is the asserting source; NCBI is the genome
identifier database. The [StrainInfo browser and query guide](STRAININFO.md)
exposes source deposit paths and separately labeled existing TaxonMech
associations, including ATB, GTDB and IMG, with their original provenance.

## Secondary crosswalk exclusions

MicrobeDecoder's combined CSV contains GOLD and NCBI associations that
conflict with primary organism records. For example:

| MicrobeDecoder strain row | GOLD ID assigned in that row | Primary GOLD organism |
|---|---|---|
| `bacdive:159652`, *Abditibacterium utsteinense* | `gold:Go0006270` | *Cutibacterium acnes* HL103PA1 |

The snapshot hashes, source rows and additional contradictions are recorded
in [issue #25](https://github.com/CultureBotAI/TaxonMech/issues/25). These
secondary associations are excluded. Primary GTDB culture-deposit matches
and primary GOLD organism/project chains supply the import evidence;
otherwise uncorroborated secondary IMG links remain unimported. Inclusion of
an identifier system does not require accepting contradictory relationships.

## Accessions and evidence rules

- Preserve a supplied NCBI accession version. If the source omits the suffix,
  retain the accession with unspecified version; do not silently append
  `.1` or resolve it to today's latest version.
- Preserve a PATRIC genome ID as an opaque identifier, including its numeric
  suffix. Do not interpret that suffix as an NCBI assembly version.
- Preserve the GTDB genome accession wrapper and version in `gtdb.genome:`.
  A GTDB species identifier, including a placeholder name derived from an
  accession, never substitutes for that genome identifier.
- Never obtain a RefSeq ID by replacing `GCA` with `GCF`. NCBI versions the
  GenBank and RefSeq records separately, and a pair can have different
  versions. Pairing needs explicit NCBI metadata. See [NCBI assembly versioning](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/version-status/).
- A shared NCBITaxon ID, GTDB species, strain name or type-strain label is
  insufficient evidence for a strain-to-genome link. GTDB species genome
  counts stay in `taxonomy_mappings` and never propagate to every strain.
- Co-occurrence on one BacDive record does not pair GenBank with RefSeq or
  establish equivalence between NCBI, GTDB, BV-BRC / PATRIC and IMG identifiers.
  A cross-database identity assertion needs its own source evidence.
- Keep chromosome accessions, 16S marker accessions, BioSample accessions
  and project identifiers distinct from genome identifiers. LPSN's
  `sequence_accessions` remain sequence identifiers; GOLD organisms,
  sequencing projects and GTDB species remain their own entities.
- An absent `genome_assemblies` entry means no NCBI assembly link was imported
  for this strain; an absent `genome_records` entry means no supported
  non-NCBI genome-record link was imported. Either kind can occur without the
  other. Absence does not establish that the source lacks genome links or
  that the strain has no sequenced genome.
- Imported assertions remain `SEEDED`, pending review. Their accession
  syntax is validated, but current database availability, suppression,
  cross-database equivalence and agreement with the strain's identity have
  not been independently verified.

## Complete crosswalk and record listings

The primary `data/raw/strain_assemblies.tsv` contains NCBI assembly assertions;
`data/raw/strain_genome_records.tsv` contains the additional BV-BRC / PATRIC
and IMG assertions plus GTDB genome links. Both include all imported links
for the inventoried strains, including taxa outside the current corpus scope
and strains omitted by the 200-entry listing cap. Join either inventory's
`strain_id` to `data/raw/bacdive_strains.tsv` to obtain the BacDive ID, strain designation,
NCBI classifications and culture-collection identifiers. To start with a
culture identifier, match an exact element of the pipe-delimited
`culture_collection_ids` column, then join the resulting strain IDs.

`data/raw/strain_related_records.tsv` uses the same join for sample, project
and GOLD organism/project references. Its `record_type` identifies the entity
kind; these rows are never added to the genome crosswalk or genome counts.

`data/straininfo/assemblies.tsv` adds explicit source deposit-to-NCBI links;
`data/straininfo/related_records.tsv.gz` adds its typed related references.
The StrainInfo component is joined to the same local strain IDs, independently
of the taxon listing cap.

This prints genome associations for local BacDive strains carrying a culture
deposit, with NCBI first and each additional source's matched deposit visible.
StrainInfo assertions are restricted to the selected deposit:

```python
import csv
from pathlib import Path

raw = Path("data/raw")
deposit = "kgmicrobe.strain:DSM-30083"
with (raw / "bacdive_strains.tsv").open() as handle:
    strain_ids = {
        row["strain_id"] for row in csv.DictReader(handle, delimiter="\t")
        if deposit in row["culture_collection_ids"].split("|")
    }
for inventory, identifier_field in (
    (raw / "strain_assemblies.tsv", "assembly_id"),
    (Path("data/straininfo/assemblies.tsv"), "assembly_id"),
    (raw / "strain_genome_records.tsv", "genome_id"),
):
    with inventory.open() as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["source"] == "STRAININFO" and row["matched_strain_id"] != deposit:
                continue
            if row["strain_id"] in strain_ids:
                print(row["strain_id"], row[identifier_field], row["source_id"],
                      row.get("matched_strain_id", ""))
with Path("data/atb/strain_links.tsv").open() as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        if row["strain_id"] in strain_ids:
            print(row["strain_id"], row["atb_id"], row["sample_id"])
```

Each generated taxon record embeds links only for its listed strains. The
corpus report labels this as **listed** coverage and deduplicates linked
identifiers and strain-identifier pairs across records, with counts per
database. These are identifier counts, not a count of unique biological
genomes across resources. They do not equate GTDB's species genome totals
with the number of strains that have direct genome links.

## Further sources

Next priorities are direct NCBI assembly/isolate metadata, additional
evidenced GenBank/RefSeq relationships and authoritative cross-references
between the imported database genome records. NCBI remains the first
priority while additional identifier systems can be added when explicit
strain relationships and identifier semantics are established. Each requires
source-specific provenance and matching rules; name matching alone does not
establish genome identity.
