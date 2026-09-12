# AllTheBacteria assemblies and strain crosslinks

TaxonMech prioritizes NCBI assemblies and adds AllTheBacteria assemblies
through existing BioSample evidence. The [assembly browser](https://culturebotai.github.io/TaxonMech/pages/atb.html)
searches the linked overlap by ATB ID, sample, ENA analysis, strain, culture
deposit, genome identifier or source species label. It includes strains
outside taxon-page listings and links them to their BacDive source records.

## Snapshot and identifiers

The pinned input is AllTheBacteria's assembly metadata TSV snapshot for
2025-05, downloaded from [OSF file 4kjh7](https://osf.io/4kjh7/).
`conf/allthebacteria.yaml` pins the URL, SHA256 and attribution;
`data/atb/MANIFEST.yaml` records these together with input/output hashes and
catalog/crosslink counts. The metadata snapshot date is 2025-05-06; the OSF
file was uploaded later. Source `dataset` values identify the underlying
assembly batches and can predate the metadata snapshot.

TaxonMech defines `atb.assembly:202505.SAM…` as a **local, snapshot-scoped
assembly identifier**. It preserves the whole single sample accession and
the release. It is distinct from `biosample:SAM…`, an NCBI assembly accession,
and the optional `ena.analysis:ERZ…` analysis record. A sample alone is not
an immutable assembly identifier.

The source warns that metadata, run availability and sequence files can
change. The browser uses supplied `aws_url` and `osf_tarball_url` values,
without inventing release-specific download URLs. Preserve the source run
accessions and `assembly_seqkit_sum`; this is a SeqKit sum, not an MD5 file
checksum. See the upstream [metadata](https://allthebacteria.org/docs/metadata_sqlite/)
and [assembly documentation](https://allthebacteria.org/docs/assemblies/).

## Evidence and eligibility

The whole ATB `sample_accession` must equal an existing BIOSAMPLE assertion
for the strain. That prior assertion retains the GTDB culture-deposit match
or GOLD organism/project chain; no species, taxon, bare strain name or
substring match creates a link. `atb_evidence.sample_links` preserves these
original assertions, including source fields and verbatim strain evidence.

A crosslink to an existing NCBI, GTDB or IMG genome additionally requires
matching genome/sample provenance. For GTDB this means the same metadata
genome row and strain-match evidence. For GOLD, the genome analysis and
sample sequencing project must retain the same explicit organism/project
chain and strain evidence. The crosslink carries both assertions. Other
genomes co-listed under a strain do not inherit the sample.

Every crosslink is `shares_biosample`, **not `sameAs`, identical sequence or
GenBank/RefSeq pairing**. NCBI genome crosslinks appear first. Related sample
and project identifiers remain separate from genome counts.

The local full catalog preserves every source row and status. Derived
strain/genome links require an available FASTA and exclude the source flags
`NO_RUNS`, `RUN_REMOVED`, `RMMS`, `META_FAIL` and `RUN_CHANGE`, which signal
missing or changed source identity. Non-HQ status alone does not exclude an
assembly. Unsupported assembly-filter values or missing/invalid runs,
SeqKit sums and native download/archive metadata also prevent a crosslink.
Available FASTAs with an ENA submission failure remain eligible;
the ENA analysis link is optional. Unavailable semicolon-separated sample
keys remain one original catalog row: they are never split into invented
assembly identifiers. Exclusions are recorded in `data/atb/exclusions.tsv`.

## Committed overlap and full local catalog

| File | Scope and content |
|---|---|
| `data/atb/assemblies.tsv` | All source metadata rows whose whole sample key overlaps TaxonMech BIOSAMPLE evidence, including excluded statuses; all 17 source columns retained |
| `data/atb/strain_links.tsv` | Eligible `strain_id`, `atb_id`, `sample_id` associations with complete `sample_evidence_json` |
| `data/atb/genome_links.tsv` | Supported genome associations with `relationship: shares_biosample` and paired genome/sample `source_evidence_json` |
| `data/atb/exclusions.tsv` | Overlapping samples excluded from derived links, with reasons |
| `data/atb/MANIFEST.yaml` | Source pin, full-catalog statistics, crosslink counts and byte provenance |
| `data/indexes/allthebacteria.sqlite` | Ignored local index of the complete metadata snapshot and derived crosslinks |
| `pages/atb-index.json` | Lightweight search index of eligible assembly/sample/strain/genome identifiers and labels |
| `pages/atb-details/*.json` | Deterministic batches of full assembly metadata, listed taxon-page links, uncapped BacDive references and original source evidence; fetched when an assembly is selected |

The website reads only the committed overlap. It does not download or scan
the full source catalog. `data/atb/strain_links.tsv` joins on `strain_id` to
`data/raw/bacdive_strains.tsv`, independently of the 200-strain taxon listing
cap. Existing NCBI, GTDB, PATRIC and IMG inventories remain separate.

Build the full local catalog and regenerate the overlap:

```bash
just atb-fetch                  # download and verify pinned metadata only
just atb-index                  # dry run: report counts without publishing
just atb-index --apply          # publish local SQLite and data/atb crosswalks
```

Query the local index after applying it:

```bash
just atb-query --info
just atb-query --sample SAMN00718807 --evidence
just atb-query --atb-id atb.assembly:202505.SAMN00718807
just atb-query --ena-analysis ERZ9433419
just atb-query --strain kgmicrobe.strain:DSM-30083
just atb-query --genome ncbi.assembly:GCF_000690815.1
just atb-query --species 'Escherichia coli' --limit 20
just atb-query --species 'Escherichia coli' --all-statuses --limit 20
```

The accession examples resolve the DSM-30083 sample in this pinned snapshot.
Species queries search exact source metadata labels; they do not create
taxonomic or strain-identity assertions. Catalog queries return available FASTAs by default, including rows flagged
as unsuitable for crosslinking; those flags never add strain/genome links.
`--all-statuses` additionally exposes unavailable source rows for matching
sample, ENA or species lookups. Strain/genome selectors search the eligible
source-evidenced crosslinks. `--evidence` includes the original source
assertions; `--offset` pages results and `--format tsv` exports them. TaxonMech's
`just atb-*` recipes are separate from the upstream AllTheBacteria CLI.

After an intentional inventory refresh, rebuild the ATB crosswalk before
seeding; provenance checks detect changed input inventories. Seeding,
rendering and normal QC use the committed overlap without requiring the
full local SQLite catalog or downloading genome FASTAs.

## Example: Escherichia coli DSM 30083

The culture deposit `kgmicrobe.strain:DSM-30083` leads to
`kgmicrobe.strain:bacdive_4907` and the existing sample assertion
`biosample:SAMN00718807`. The ATB snapshot reports that whole sample key for
[assembly `atb.assembly:202505.SAMN00718807`](https://culturebotai.github.io/TaxonMech/pages/atb.html#atb.assembly:202505.SAMN00718807),
with ENA analysis `ERZ9433419` and source scientific name
*Escherichia coli DSM 30083 = JCM 1649 = ATCC 11775*.

The supported source chains connect this ATB sample to NCBI
`GCA_000690815.1` and `GCF_000690815.1`, then GTDB
`gtdb.genome:RS_GCF_000690815.1` and IMG `img.taxon:2528311135`.
These are `shares_biosample` associations. Other genomes listed by the same
BacDive strain remain outside this crosslink unless their own sample chain
supports it. The browser exposes each original assertion for inspection.

## Attribution

The AllTheBacteria metadata are supplied under **CC-BY-4.0**. Preserve the
upstream attribution and cite [AllTheBacteria](https://doi.org/10.1101/2024.03.08.584059).
TaxonMech's CC0 license for its own content does not relicense these metadata.
