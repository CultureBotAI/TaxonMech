# Strain identifiers and genome identifiers

A primary TaxonMech use case is answering **which genome identifiers a source
associates with a strain identifier**, and following a genome link back to the
strain's BacDive record and culture-collection deposits. This enables links
between experimental observations made on a strain and genomic data.

**NCBI GenBank/RefSeq assemblies are the priority**, with BV-BRC / PATRIC and
IMG genome records included as separately typed identifiers. Expanding
database coverage does not replace an NCBI assembly ID or establish that
identifiers from different resources denote the same genome.

## Relationship model

| Entity or relationship | Representation | Meaning |
|---|---|---|
| Taxon | `TaxonRecord.identifier`, an NCBITaxon CURIE | Classification context for a species or lower taxon |
| Strain | `strains[].strain_id`, with `source_id` and `designation` | A source's strain record |
| Culture deposit | `strains[].culture_collection_ids[]` | Deposit identifiers associated with that strain by kg-microbe's BacDive transform |
| NCBI genome assembly (primary) | `strains[].genome_assemblies[].assembly_id` | A GenBank or RefSeq assembly accession, with its version when supplied |
| Strain-to-assembly assertion | `GenomeAssemblyLink` | A source explicitly associates this assembly with this strain record |
| Other database genome record | `strains[].genome_records[].genome_id` | A typed BV-BRC / PATRIC or IMG genome identifier |
| Strain-to-genome-record assertion | `GenomeRecordLink` | A source explicitly associates this database record with this strain record |

The relationship is many-to-many: one strain can have multiple genome links,
and multiple source strain records can point to the same genome identifier.
Preserve each assertion and its provenance. A link is not `sameAs` between a
strain and a genome record, nor proof that every culture deposit or substrain
has an identical sequence. BacDive can group assemblies of substrains under
one strain record. Source descriptions remain visible so those distinctions
can be reviewed.

## First source: BacDive

The extractor reads `Sequence information / Genome sequences` from
kg-microbe's `data/raw/bacdive_strains.json`, which is recorded and hashed in
`data/raw/MANIFEST.yaml`. The transformed BacDive graph supplies the strain
IDs and deposits; the raw snapshot supplies the missing genome links.

For each assertion, `GenomeAssemblyLink` requires `assembly_id`, `source` and
`source_id`. It retains `source_reference_id` (BacDive's `@ref`),
`assembly_name`, `assembly_level` and `taxon_id` when present. That taxon is
the source's classification of the assembly and may disagree with the
strain's classification; it never changes the record's lineage.

`GenomeRecordLink` requires `genome_id`, `source_database` (`patric` or `img`
as supplied by BacDive), `source` and the asserting `source_id`. The current
import uses `source: BACDIVE` and `source_id: bacdive:<digits>`. It retains
`source_reference_id`, `genome_name`, `assembly_level` and `taxon_id` when
present. The accepted identifier types are:

| Database | TaxonMech identifier | Source relationship |
|---|---|---|
| GenBank/RefSeq | `ncbi.assembly:GCA_…` or `ncbi.assembly:GCF_…` | NCBI assembly assertion in `genome_assemblies` |
| BV-BRC / PATRIC | `patric:<digits>.<digits>` | PATRIC genome ID from BacDive in `genome_records`, linked to BV-BRC |
| IMG | `img.taxon:<digits>` | IMG genome-record ID from BacDive in `genome_records` |

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

The extractor deduplicates byte-equivalent field values within an assertion;
different references, descriptions, accession versions and strain IDs remain
separate. Malformed identifiers and links to strains excluded from the taxon
inventory are recorded in `data/raw/dropped.tsv`.

## Accessions and evidence rules

- Preserve a supplied NCBI accession version. If the source omits the suffix,
  retain the accession with unspecified version; do not silently append
  `.1` or resolve it to today's latest version.
- Preserve a PATRIC genome ID as an opaque identifier, including its numeric
  suffix. Do not interpret that suffix as an NCBI assembly version.
- Never obtain a RefSeq ID by replacing `GCA` with `GCF`. NCBI versions the
  GenBank and RefSeq records separately, and a pair can have different
  versions. Pairing needs explicit NCBI metadata. See [NCBI assembly versioning](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/version-status/).
- A shared NCBITaxon ID, GTDB species, strain name or type-strain label is
  insufficient evidence for a strain-to-genome link. GTDB species genome
  counts stay in `taxonomy_mappings` and never propagate to every strain.
- Co-occurrence on one BacDive record does not pair GenBank with RefSeq or
  establish equivalence between NCBI, BV-BRC / PATRIC and IMG identifiers.
  A cross-database identity assertion needs its own source evidence.
- Keep chromosome accessions, 16S marker accessions, BioSample accessions
  and project identifiers distinct from genome identifiers. LPSN's
  `sequence_accessions` remain sequence identifiers; GOLD organism and GTDB
  species identifiers remain their own entities.
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
and IMG assertions. Both include all imported links for the inventoried
strains, including taxa outside the current corpus scope and strains omitted
by the 200-entry listing cap. Join either inventory's `strain_id` to
`data/raw/bacdive_strains.tsv` to obtain the BacDive ID, strain designation,
NCBI classifications and culture-collection identifiers. To start with a
culture identifier, match an exact element of the pipe-delimited
`culture_collection_ids` column, then join the resulting strain IDs.

For example, this prints the complete genome crosswalk for a culture deposit,
with NCBI assemblies first, using the committed inventories alone:

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
    ("strain_assemblies.tsv", "assembly_id"),
    ("strain_genome_records.tsv", "genome_id"),
):
    with (raw / inventory).open() as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["strain_id"] in strain_ids:
                print(row["strain_id"], row[identifier_field], row["source_id"])
```

Each generated taxon record embeds links only for its listed strains. The
corpus report labels this as **listed** coverage and deduplicates linked
identifiers and strain-identifier pairs across records, with counts per
database. These are identifier counts, not a count of unique biological
genomes across resources. They do not equate GTDB's species genome totals
with the number of strains that have direct genome links.

## Further sources

Next priorities are explicit NCBI assembly-to-BioSample and isolate metadata,
evidenced GenBank/RefSeq pairing, and authoritative cross-references between
the imported database genome records. NCBI remains the first priority while
other genome databases can be added when explicit strain relationships and
identifier semantics are established. Each requires source-specific
provenance and matching rules; name matching alone does not establish genome
identity.
