# Species, strain and genome source coverage

TaxonMech inventories the complete pinned NCBI bacterial and archaeal
backbone and generates every eligible species-or-below record. It also
retains source-native catalogs independently of NCBI mapping. An unmapped
GTDB cluster, SeqCode name or StrainInfo deposit remains discoverable without
minting an identity or guessing an equivalence from its name.

The machine-readable [source manifest](../data/catalog/MANIFEST.json) gives
the measured record counts, source files, byte hashes, dates and scope of each
catalog. The [coverage register](../conf/source_coverage.yaml) distinguishes
complete snapshots, complete pinned transforms, source crosslinks, supporting
evidence and external resources. The generated [Sources page](../pages/sources.html)
provides the same coverage and downloads. Counts from overlapping resources
must not be added together as numbers of biological species, strains or genomes.

## Included catalogs

| Resource | Retained coverage |
|---|---|
| NCBI Taxonomy | All bacterial/archaeal taxa, scientific names and other original name classes; type and excluded-from-type material; merged identifiers |
| NCBI Assembly | GenBank and RefSeq current and historical summaries, preserving all columns for prokaryotes and records with unresolved taxonomy |
| GTDB RS232 | Every bacterial/archaeal genome, every species cluster and every supplied NCBI mapping, including unmapped clusters |
| BacDive v2 | Complete public ID census and identity/deposit/genome/16S projection; one wholly empty export row reported separately |
| StrainInfo | Complete public strain census and every captured strain's own deposits and sequence assertions, independent of local matches |
| SeqCode | Complete public name discovery census and type-genome endpoint; rank, status and source classification retained where supplied |
| GOLD / IMG | Every public workbook organism, sequencing project and analysis; identity, culture, NCBI and IMG columns retained |
| BV-BRC / PATRIC | Complete public bacterial and archaeal genome metadata capture, checked against identical before/after identifier censuses |
| AllTheBacteria | Entire pinned metadata export, including unavailable samples and all source status flags, runs, analyses, SeqKit sums and download locations |
| LPSN | Every name in the pinned kg-microbe transform, including names without an NCBI mapping; available API annotations retained |

These are complete **named snapshots**, not an assertion that every organism
has been discovered or that every database is fully mirrored. TYGS, WDCM GCM /
gcType / reference strains, SILVA / Living Tree Project, EnteroBase and PubMLST
are included in the resource directory with explicit boundaries. Collection
accessions from ATCC, DSMZ, JCM, NBRC, CIP, CECT, CCUG, LMG, KCTC and other
collections come from their captured source assertions; this does not assert
independent complete crawls of each collection. Private and access-restricted
records are outside the public captures.

## Identifier lookup and relationship queries

```bash
just source-query                            # counts, files and coverage boundaries
just source-query --source straininfo --identifier straininfo.strain:14277
just source-query --source gtdb_genomes --identifier ncbi.assembly:GCA_000005845.2
just source-query --source ncbi_genbank --identifier biosample:SAMN02604091
just source-query --source seqcode_names --identifier seqcode:45
just source-query --source bvbrc --identifier patric:1001994.6
just atb-query --help                         # full ATB assembly index and supported crosslinks
just straininfo-query --help                  # deposit-specific supported genome relationships
```

`source-query` builds a disposable, source-specific SQLite identifier index
under ignored `data/indexes/`. Input bytes are verified before reuse, and the
cache filename is bound to the source manifest. A query reports its full hit
count independently of `--limit`. **A discovery hit is an occurrence in a
source record**, not an inferred strain identity or genome equivalence.

Taxon records and the ATB/StrainInfo relationship queries use stricter
evidence. NCBI assembly links require an explicit `strain=` value in
`infraspecific_name` matching a whole registered culture accession. BV-BRC
uses whole culture identifiers in `culture_collection` or `strain`. Historical
NCBI assemblies remain cataloged without being presented as current direct
strain links. Sample/project identifiers and GOLD Go/Gp/Ga records stay
outside genome counts. ATB genome crosslinks require that the same source
record or explicit GOLD chain connects the sample and genome to the deposit.
See [strain–genome evidence](STRAIN_GENOMES.md).

## Taxon scope and publication

`curation/seed_scope.tsv` is the explicit species-or-below record set. The
NCBI primary snapshot replaces the former pruned KGX taxonomy selection.
GTDB now attests taxonomy candidates as well. Higher taxa remain lineage
entries, and all prior scoped identifiers remain addressable. Retired NCBI
identifiers use the hash-pinned preceding taxonomy projection, are marked
`DEPRECATED`, and their successors name them in `replaces`; other sources'
taxon assertions are not silently rewritten.

Taxon YAML retains every classified BacDive strain. There is no 200-strain
record cap. The site uses a shared taxon viewer with lossless compressed
record shards and strain tables paged in groups of 200. Every pre-expansion
taxon remains reachable at its published URL. `pages/index.json.gz` holds
the complete search array; `pages/index.json` is now its download manifest
with count, size and checksum. The site uses native or vendored gzip
decoding, and static browse pages remain available if search cannot load.
`curation/legacy_page_paths.tsv` preserves every prior taxon URL, including
incoming strain fragments. Static browse pages retain the complete record listing.
Native catalog downloads are kept in repository data, outside the Pages
artifact; publication must remain below its enforced size budget.

Large-corpus validation uses bounded-memory record loading and batched
validation workers. `just qc` runs each full-corpus validation, reproduction,
render and report gate once; the corresponding smoke tests still run under
standalone `just test`.

## Reproduction and refresh

Seeding, tests, corpus verification, source queries and rendering work from
committed inventories and projections without network access. Re-extraction
uses the pinned primary NCBI files plus the configured kg-microbe checkout,
current BacDive/BV-BRC projections and GOLD workbook/projection. Each input
and output is recorded in the raw manifest. Original HTTP responses are
retained in ignored `data/source_snapshots/`; committed source metadata keep
request URLs, hashes, ranges/pages and capture boundaries.

```bash
just straininfo-fetch --out data/source_snapshots/straininfo-NEW --all
# Pin newly captured primary inputs before rebuilding dependent inventories.
just source-catalog --project
just extract-inventory-dry
just extract-inventory
just atb-index --apply
just straininfo-index --apply
just source-catalog
just source-query --check
just propose-scope --rule attested --rank '' --all --append > /tmp/taxonmech-scope-additions.tsv
# Review and append the explicit scope additions.
just seed
just seed-canary NCBITaxon:562 --force
# Inspect the written canary, then regenerate through the validated writer.
just seed-apply --force
just render
just docs-stats
just qc
```

The BacDive, SeqCode and BV-BRC capture scripts are `scripts/fetch_bacdive.py`,
`scripts/fetch_seqcode.py` and `scripts/fetch_bvbrc.py`; each requires an output
snapshot directory. GOLD's projection uses `taxonmech.gold_snapshot.project`.
New snapshots must preserve before/after census checks, all identifiers,
source statuses and attribution. The original full ATB SQLite catalog is
rebuildable from the pinned metadata and must not be replaced by its smaller
strain-overlap table.

## Source terms and primary documentation

Project content remains CC0; imported data retain their source terms and
citations. BacDive, StrainInfo, SeqCode and AllTheBacteria attribution accompanies
their source metadata. SeqCode's public data are [CC BY 4.0](https://registry.seqco.de/help/open_data).
NCBI/ENA/DDBJ identifiers follow [INSDC data-sharing policy](https://www.ebi.ac.uk/ena/browser/about/policies).
[BV-BRC metadata documentation](https://www.bv-brc.org/docs/system_documentation/data.html)
describes its strain, culture and genome fields.
[TYGS's API](https://tygs.dsmz.de/application_programming_interface/show)
documents analysis-result retrieval; directory inclusion does not claim a
direct complete TYGS bulk capture. [SILVA taxonomy](https://www.arb-silva.de/documentation/silva-taxonomy)
is a ribosomal sequence classification resource, not an assembly identifier system.
