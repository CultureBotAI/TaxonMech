# Strain identifiers and genome identifiers

A primary TaxonMech use case is answering **which genome identifiers a source
associates with a strain identifier**, and following an assembly back to the
strain's BacDive record and culture-collection deposits. This enables links
between experimental observations made on a strain and genomic data.

## Relationship model

| Entity or relationship | Representation | Meaning |
|---|---|---|
| Taxon | `TaxonRecord.identifier`, an NCBITaxon CURIE | Classification context for a species or lower taxon |
| Strain | `strains[].strain_id`, with `source_id` and `designation` | A source's strain record |
| Culture deposit | `strains[].culture_collection_ids[]` | Deposit identifiers associated with that strain by kg-microbe's BacDive transform |
| Genome assembly | `strains[].genome_assemblies[].assembly_id` | An NCBI assembly accession, with its version when supplied |
| Strain-to-assembly assertion | `GenomeAssemblyLink` | A source explicitly associates this assembly with this strain record |

The relationship is many-to-many: one strain can have multiple assemblies,
and multiple source strain records can point to the same assembly. Preserve
each assertion and its provenance. A link is not `sameAs` between a strain
and an assembly, nor proof that every culture deposit or substrain has an
identical sequence. BacDive can group assemblies of substrains under one
strain record. Source descriptions remain visible so those distinctions can
be reviewed.

## First source: BacDive

The extractor reads `Sequence information / Genome sequences` from
kg-microbe's `data/raw/bacdive_strains.json`, which is recorded and hashed in
`data/raw/MANIFEST.yaml`. The transformed BacDive graph supplies the strain
IDs and deposits; the raw snapshot supplies the missing assembly links.

For each assertion, `GenomeAssemblyLink` requires `assembly_id`, `source` and
`source_id`. It retains `source_reference_id` (BacDive's `@ref`),
`assembly_name`, `assembly_level` and `taxon_id` when present. That taxon is
the source's classification of the assembly and may disagree with the
strain's classification; it never changes the record's lineage.

Only GenBank/RefSeq assembly accessions enter this first inventory. BacDive
distinguishes assembly accessions from 16S sequences and other database
identifiers in its [field documentation](https://api.bacdive.dsmz.de/strain_fields_information).
The raw snapshot also contains PATRIC and IMG genome IDs and some chromosome
or WGS sequence accessions. Those require separate identifier types and are
not imported as NCBI assemblies.

The extractor deduplicates byte-equivalent field values within an assertion;
different references, descriptions, accession versions and strain IDs remain
separate. Malformed assembly accessions and links to strains excluded from
the taxon inventory are recorded in `data/raw/dropped.tsv`.

## Accessions and evidence rules

- Preserve a supplied accession version. If the source omits the suffix,
  retain the accession with unspecified version; do not silently append
  `.1` or resolve it to today's latest version.
- Never obtain a RefSeq ID by replacing `GCA` with `GCF`. NCBI versions the
  GenBank and RefSeq records separately, and a pair can have different
  versions. Pairing needs explicit NCBI metadata. See [NCBI assembly versioning](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/policies-annotation/genome-processing/version-status/).
- A shared NCBITaxon ID, GTDB species, strain name or type-strain label is
  insufficient evidence for a strain-to-assembly link. GTDB species genome
  counts stay in `taxonomy_mappings` and never propagate to every strain.
- Keep chromosome accessions, 16S marker accessions, BioSample accessions
  and genome assembly accessions distinct. LPSN's `sequence_accessions`
  remain sequence identifiers and do not become genome assembly links.
- An absent entry means no NCBI assembly link was imported for this strain.
  The source may supply genome IDs in another database, which this first
  inventory does not import. It does not establish that the source lacks
  genome links or that the strain has no sequenced genome.
- Imported assertions remain `SEEDED`, pending review. Their accession
  syntax is validated, but current NCBI availability, suppression and
  assembly-to-isolate agreement have not been independently verified.

## Complete crosswalk and record listings

`data/raw/strain_assemblies.tsv` contains all imported assertions for the
inventoried strains, including taxa outside the current corpus scope and
strains omitted by the 200-entry listing cap. Join its `strain_id` to
`data/raw/bacdive_strains.tsv` to obtain the BacDive ID, strain designation,
NCBI classifications and culture-collection identifiers. To start with a
culture identifier, match an exact element of the pipe-delimited
`culture_collection_ids` column, then join the resulting strain IDs.

For example, this prints the complete assembly crosswalk for a culture
deposit using the committed inventories alone:

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
with (raw / "strain_assemblies.tsv").open() as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        if row["strain_id"] in strain_ids:
            print(row["strain_id"], row["assembly_id"], row["source_id"])
```

Each generated taxon record embeds links only for its listed strains. The
corpus report labels this as **listed** coverage and deduplicates strain and
assembly identifiers across records. It does not equate GTDB's species
genome totals with the number of strains that have direct assembly links.

## Further sources

Next priorities are explicit NCBI assembly-to-BioSample and isolate metadata,
evidenced GenBank/RefSeq pairing, and typed IMG/BV-BRC genome links. Each
requires source-specific provenance and matching rules. GOLD organism IDs
and GTDB species IDs remain their own entities. None is promoted to a strain
or assembly identity through name matching alone.
