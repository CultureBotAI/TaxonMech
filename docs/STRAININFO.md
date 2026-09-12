# StrainInfo strain records, deposits and sequences

TaxonMech imports the evidence-backed overlap with
[StrainInfo](https://straininfo.dsmz.de/), DSMZ's resource for microbial strain
identifiers and culture deposits. The
[StrainInfo browser](https://culturebotai.github.io/TaxonMech/pages/straininfo.html)
covers matched inventoried strains, including those omitted from taxon-page
listings. NCBI assembly identifiers remain the primary genome links.

## Keep the identities separate

| Identifier | Meaning | TaxonMech representation |
|---|---|---|
| SI-ID14277 | Source strain record | `straininfo.strain:14277`, related type `STRAININFO_STRAIN` |
| SI-DP847459 | Source culture deposit, DSM 30083 | `straininfo.deposit:847459`, related type `STRAININFO_DEPOSIT` |
| 10.60712/SI-ID14277.3 | Version 3 of the source strain record | `straininfo_evidence.strain_doi: DOI:10.60712/SI-ID14277.3` |
| GCA_000690815 | NCBI assembly, version unspecified in the source | `genome_assemblies[].assembly_id: ncbi.assembly:GCA_000690815` |
| Gene, rRNA operon or patent sequence accession | Nucleotide sequence reference | `related_records`, type `NUCLEOTIDE_SEQUENCE`, `INSDC:` ID |

The strain record DOI is distinct from a deposit identifier and a publication
citation. Strain, deposit, DOI and nucleotide-reference identifiers never
increase genome counts. StrainInfo is an asserting source; its NCBI
assertions enter the existing NCBI count.

The native [SI-ID14277 record](https://straininfo.dsmz.de/strain/14277) has a
contextual [SI-DP847459 deposit view](https://straininfo.dsmz.de/strain/14277?SI-DP847459).
The prefix-compatible `straininfo.deposit:` resolver uses
`https://straininfo.dsmz.de/pass?pass=`.

## Import boundary and evidence

The complete search table supplies candidates. Imported links require a
candidate's own rich API deposit record and a whole culture identifier
matching the BacDive deposit inventory. The pinned CAFI authority and
case-sensitive accession templates used for GTDB/GOLD also apply here.
Normalize only the recognized authority prefix's case and initial separator;
preserve accession suffix case, punctuation and leading zeros. Search-result
membership, species names, source BacDive cross-references and SI-ID group
membership do not establish a match.

A source strain must have a supported published status. Erroneous deposits,
erroneous relations and deposits in deprecated source collections do not
supply links. Other source deposit statuses remain visible without implying
that a culture is currently available for purchase.

Every genome or nucleotide reference must explicitly name the **same matched
SI-DP** in `strain.sequence[].deposit`. A sequence under another deposit in
the SI-ID group cannot transfer to this deposit. Source groups can contain
conflicting organism assignments; their grouping remains a source assertion
without declaring biological equivalence.

Every assertion retains `source: STRAININFO`, the source SI-ID,
`matched_strain_id`, original deposit designation and field names. Nested
`straininfo_evidence` records the SI-ID, SI-DP, source statuses,
`match_method: culture_identifier`, optional record DOI and source BacDive
reference. Sequence assertions retain `sequence_type` and
`sequence_deposit_id`. A source BacDive reference that disagrees with the
culture-matched local strain remains visible with its conflict flag; the
reference never supplies or overrides the match.

NCBI accessions preserve the supplied version, including an absent suffix.
TaxonMech never appends `.1`, selects today's latest version or equates an
unversioned identifier with a versioned one from another source. Types
`gene`, `rrnaop` and `patent` remain nucleotide references. Unsupported
accession/type combinations are recorded as exclusions.

## Snapshot, inventories and queries

The component is a dated, hash-pinned capture of the public API. The full
ID/search census selects rich records whose culture designations overlap
inventoried deposits. Source request URLs and response byte hashes remain in
`SOURCE.json`. The compressed projection preserves original identity,
relation, sequence, alternative and archive fields and relevant deposit
metadata, omitting unrelated phenotype fields.

| File | Content |
|---|---|
| `conf/straininfo.yaml` | Snapshot/API pin, source location, license and resource citation |
| `data/straininfo/SOURCE.json` | Capture timestamp, catalog/candidate counts, request provenance, projection and selection-input hashes |
| `data/straininfo/records.jsonl.gz` | Original-shaped rich source projection for candidate records |
| `data/straininfo/strain_links.tsv` | Uncapped local-strain, SI-ID, SI-DP, matched culture and record DOI associations |
| `data/straininfo/assemblies.tsv` | Explicit deposit-to-NCBI assertions with serialized nested evidence |
| `data/straininfo/related_records.tsv.gz` | Compressed SI strain/deposit and nucleotide assertions with the same evidence |
| `data/straininfo/exclusions.tsv` | Source IDs, accessions, exclusion reasons and original values, including unused conflicting cross-references |
| `data/straininfo/MANIFEST.yaml` | Source pin, input/output hashes, coverage and exclusion counts |
| `pages/straininfo-index.json` | Search identifiers and pointers to detail batches |
| `pages/straininfo-index.json.gz` | Deterministic compressed copy used by browsers with native stream decompression; plain JSON remains the fallback |
| `pages/straininfo-details/*.json` | Lazy-loaded source assertions, native links and separately labeled existing TaxonMech genome associations |

The component joins existing strains by `strain_id`; it does not create
BacDive strains or change taxonomic classification. Its inventories are
uncapped. Taxon YAML embeds the subset for listed strains.

Query the committed overlap without a separate database or network request:

```bash
just straininfo-query --info
just straininfo-query --strain SI-ID14277 --limit 20
just straininfo-query --deposit SI-DP847459 --evidence
just straininfo-query --strain kgmicrobe.strain:DSM-30083
just straininfo-query --culture 'DSM 30083'
just straininfo-query --bacdive 4907
just straininfo-query --doi 10.60712/SI-ID14277.3
just straininfo-query --genome GCA_000690815 --evidence
just straininfo-query --deposit 847459 --genome GCA_000690815 --format tsv
just straininfo-query --existing-genome atb.assembly:202505.SAMN00718807
```

Selectors are exact and combined on **one matched deposit path**.
`--strain` accepts an SI-ID, local BacDive strain CURIE or matched culture
CURIE. `--culture` accepts an exact source designation or matched culture
CURIE without inferring aliases. `--genome` searches explicit StrainInfo
NCBI assertions; `--sequence` searches nucleotide references.
`--existing-genome` searches separately labeled existing TaxonMech strain
associations without making them StrainInfo assertions.

Results retain the matched deposit and separate source assembly IDs from
existing TaxonMech genome IDs. `--evidence` includes complete assertions;
`--offset` and `--limit` page deposit paths; `--format tsv` exports them.
Startup validates current StrainInfo source configuration and input/output
hashes. Existing ATB context also requires its current source pin, inventory
dependencies and output hashes.
Validation replays the full source evidence before returning results and can
take tens of seconds per invocation. `--limit` reduces the returned paths,
without reducing that validation work.

The browser uses case-insensitive substring search across indexed IDs and
deposit designations. Results are SI-ID groups; details show the exact
deposit associated with each sequence. Existing ATB, GTDB, PATRIC and IMG
links remain **existing TaxonMech strain associations** with their original
provenance. ATB strain cards link to StrainInfo context through the local
strain ID; their `shares_biosample` evidence is unchanged by StrainInfo.

## Example: DSM 30083 and NCTC 9001

DSM 30083 is SI-DP847459 in SI-ID14277 and carries the unversioned NCBI
assertion `GCA_000690815`. ATCC 11775, SI-DP11317, also explicitly supplies
that accession. The source record DOI is `10.60712/SI-ID14277.3`.

The same local BacDive strain, `kgmicrobe.strain:bacdive_4907`, also carries
NCTC 9001, SI-DP747505. StrainInfo supplies `GCA_900706755` through that NCTC
deposit. Querying DSM 30083 together with that accession must return no match.

Existing TaxonMech evidence separately links this local strain to
`ncbi.assembly:GCA_000690815.1`, GTDB, IMG and ATB
`atb.assembly:202505.SAMN00718807`. The browser exposes these paths without
attributing ATB to StrainInfo or equating versioned and unversioned assemblies.

## Attribution and refresh

StrainInfo metadata retain **CC-BY-4.0** attribution. Cite
[StrainInfo—the central database for linked microbial strain identifiers](https://doi.org/10.1093/database/baaf059).
TaxonMech's CC0 license does not relicense upstream metadata.

`just straininfo-fetch --help` describes capturing primary API evidence.
`just straininfo-index` checks the configured snapshot in a dry run;
`just straininfo-index --apply` publishes the component. After changing the
BacDive deposit inventory or pinned CAFI registry, capture and pin a
corresponding source snapshot before rebuilding. Then follow the seed dry
run, canary, bulk seed, render and statistics workflow. Seeding and normal
queries use committed evidence without fetching live records or genome FASTAs.
