# YAML Record Review: Thioalkalivibrio sulfidiphilus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thioalkalivibrio_sulfidiphilus.yaml`
- Started UTC: 2026-10-04T19:43:01Z
- Finished UTC: 2026-10-04T19:49:21Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033854`,
Thioalkalivibrio sulfidiphilus: SPECIES, BACTERIA, genus parent
`NCBITaxon:106633`, `grounding_status: EXACT`, `mapping_status: SEEDED`,
genetic code 11. It has one LPSN name, two GTDB mappings, four NCBI
synonyms, one BacDive strain, six source attestations and one seed event.

This is one species-level review. Its HL-EbGr7 child taxon and the ALJ17,
SGAR and metagenome source objects were inspected only as evidence
context, not counted as additional completed YAML reviews. No record,
source inventory, code or curation-history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/thioalkalivibrio_sulfidiphilus.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/thioalkalivibrio_sulfidiphilus.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`; its standard diagnostic
  is `reports/instance_validation_failures.tsv`.
- Passed bounded structured comparisons of identity, all nine root-first
  ancestors, source inventory rows, filename lock, scope and seed-event
  wording. Complete backbone scans found one child, `396588`, with no
  children beneath it; the complete BacDive inventory contains no strain
  filed under that child, and one directly under the species.
- Read all five matching native GTDB genome objects after scanning all
  901,341 native rows. Cluster membership, distinct-accession counts and
  all matching inventory mappings were checked, not sampled.
- Complete scans of seven strain crosswalk tables found zero rows for
  `kgmicrobe.strain:bacdive_133741`, consistent with the YAML's omitted
  assembly, genome and related-record lists.
- Not run: `just verify-corpus`. It is a full-corpus byte-comparison gate;
  `--max-diffs` limits diagnostic output, not scope. Bounded source
  comparisons above are not a substitute for that gate.
- Not applicable: `just validate-products`, because this record has no
  curator-added causal-graph nodes. NCBI terms were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was inspected.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221320` and the inspected live
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033854&retmode=xml)
agree on the identifier, species name, rank, genus parent and genetic code.
The complete lineage agrees with the pinned backbone. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033854)
confirms the HL-EbGr7 child `396588`; the species and its type-strain taxon
are not interchangeable identities.

The four source names and synonym categories agree with the NCBI
inventory. In particular, the ALJ17 name is RELATED_SYNONYM, not a claim
that ALJ17 is the type strain. Exact-ID merged/dropped table scans found
an incoming merge from old taxon `748653` at
`data/raw/ncbi_merged_ids.tsv:94390`, not retirement of `1033854`.

The [LPSN page](https://lpsn.dsmz.de/species/thioalkalivibrio-sulfidiphilus)
confirms name record 790102, Sorokin et al. 2012, species rank and a
validly published correct name. The complete inventory row
`data/raw/lpsn_names.tsv:27090` supplies the legitimate flag, exact status
text and cited identifiers. Its type-strain field is empty despite the
page's explicit HL-EbGr7, NCCB 100376 and UNIQEM U246 designations.
That consequential omission is finding M1 below.

## Evidence

The record reproduces these inspected source inventory assertions:

| Source | Inventory row and assertion |
| --- | --- |
| NCBITAXON | `ncbitaxon_taxa.tsv:221320`: one NAME, snapshot `2026-09-13`. |
| LPSN | `lpsn_names.tsv:27090`: one name, source closeMatch. |
| GTDB | `gtdb_mappings.tsv:1381` and `:1382`: broadMatch cluster counts four and one. |
| BACDIVE | `bacdive_strains.tsv:56051`: one directly classified strain. |
| GOLD | `gold_organisms.tsv:459`: five directly classified ORGANISM assertions. |
| MADIN | `madin_taxa.tsv:638`: seven TRAIT_ASSERTIONs. |

The table paths are under `data/raw/`. Different assertion units are not
summed. GOLD and MADIN counts were verified against their maintained
inventory, not promoted into new biological observations. The separate
native GOLD workbook contains two species-direct organism rows and one
HL-EbGr7 child row for this search. It is not the same counting input as
the KGX-derived GOLD inventory. The original configured KGX transforms
were unavailable here, so five was not independently rederived from
their original edges; this limitation is not evidence that the count
should be replaced by a count from a different source snapshot.

The full native GTDB scan found these two clusters, without duplicate
accessions:

| Cluster | Genomes | Native NCBI taxon distribution |
| --- | ---: | --- |
| `s__Thioalkalivibrio_A sulfidiphilus` | 4 | Three species-direct `1033854`; one type-strain child `396588`. |
| `s__Thioalkalivibrio_A sulfidiphilus_A` | 1 | One species-direct `1033854`, ALJ17. |

The first cluster contains `RS_GCF_000021985.1` as its type-material
representative, SGAR-7 `RS_GCF_049262555.1`, SGAR-13
`RS_GCF_048594305.1` and metagenome `GB_GCA_050485945.1`. The second
contains only representative `RS_GCF_000377945.1`. All five complete
objects were inspected at catalog shard/line positions
`0007:40458`, `0000:10971`, `0006:40803`, `0011:24862` and `0016:5902`,
respectively, in `data/catalog/gtdb_genomes-*.jsonl.gz`.

The complete mapping table adds a first-cluster mapping to child taxon
`396588` at row 286090, but no second taxon mapping for the singleton
`sulfidiphilus_A` cluster. The species is split across two GTDB clusters;
this supports retaining pooling predicates without asserting equivalence.
There is no LPSN GTDB correspondence in this record's inventory, and no
GTDB xref or exact synonym was invented. The singleton's generic note
nevertheless makes an unsupported additional-taxa claim, finding m1.
The live GTDB page was inaccessible; this check concerns the pinned
native release, not a newly retrieved web census.

The nomenclatural references were inspected at their authorities:

- [PMID 21984678](https://pubmed.ncbi.nlm.nih.gov/21984678/) identifies the
  species description, DOI `10.1099/ijs.0.034504-0`, printed in August
  2012, volume 62, pages 1884-1889, after online publication in October
  2011. Its abstract explicitly identifies HL-EbGr7, NCCB 100376 and
  UNIQEM U246 as the type, and treats ALJ17 separately. PubMed metadata
  and abstract were read; the full article body was not inspected.
- [Crossref metadata for DOI 10.1099/ijs.0.047837-0](https://api.crossref.org/works/10.1099/ijs.0.047837-0)
  confirms the IJSEM notification list concerning volume 62, part 8,
  published in part 11 on November 1, 2012, pages 2555-2556. This is
  nomenclatural notification, not a second species experiment. The web
  tool could not open the API URL; a direct public API read succeeded.
- The [NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=EU709878&rettype=gb&retmode=xml)
  resolves the source's unversioned marker to `EU709878.1`, a 1,389-base
  partial 16S rRNA sequence of HL-EbGr7, taxon `396588`, with a type
  annotation. This is a marker, not a genome assembly or deposit ID.

The full BacDive object at `data/bacdive/records.jsonl.gz:56050` and the
[BacDive strain page](https://bacdive.dsmz.de/strain/133741) confirm
strain 133741, HL-EbGr7, species-direct classification and type status.
They provide NCCB 100376 and the spelling `UNIQUEM U246`; the latter
differs from `UNIQEM U246` in LPSN, NCBI and the original description.
The YAML faithfully preserves BacDive's spelling rather than silently
resolving the conflict. BacDive supplies the marker but no genome entry.

The existing CAFI-backed normalizer accepts `NCCB 100376` as
`NCCB-100376`. It rejects both U246 spellings and the bare HL-EbGr7
designation. Decoding the YAML's percent-escaped UNIQUEM identifier does
not produce an eligible deposit key. Consequently spelling correction
alone would not establish a new supported genome join.

The inspected [live NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000021985.1/dataset_report)
and full native GenBank/RefSeq objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:722` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:683` establish current paired
`GCA_000021985.1` / `GCF_000021985.1`, ASM2198v1, Complete Genome,
type material, HL-EbGR7 taxon `396588`, BioSample `SAMN00001443` and one
3,464,554-base chromosome. The exact child-taxonomy Assembly query
returns one paired entry. These inspected assembly/sample metadata
provide the laboratory name but not an eligible culture deposit.

GOLD's complete native chain likewise supplies bare HL-EbGR7, not a
deposit-backed join: `Go0002121` at organisms line 1894, its explicitly
linked project `Gp0002121` at projects line 1916, and analysis
`Ga0031212` at analyses line 21191 support `PRJNA29177`,
`SAMN00001443`, `GCA_000021985.1`, chromosome `CP001339` and
`img.taxon:643348585`. BV-BRC's complete object at
`data/bvbrc/bvbrc-0020.jsonl.gz:2228` supplies `patric:396588.4` and
the same assembly/sample context, again with only the bare strain name.

Separate GOLD organism `Go0043992` at organisms line 36874 carries
UNIQEM U246, but no project or analysis joined to that organism was found
in the complete ignored-inclusive search. It must not be combined with
Go0002121's genome solely because the designations describe the type.
The inspected ALJ17 chain, `Go0022579` -> `Gp0022579` -> `Ga0000103`,
belongs to ALJ17 and `GCA_000377945.1`, not the type. All GOLD native
file paths above are `data/gold/{organisms,projects,analyses}.jsonl.gz`.

## Completeness

The omitted type designations and type flag are consequential despite
being schema-optional. In contrast, omitted genome and related-record
lists agree with the repository's explicit deposit-evidence rules:
known genomes exist, but the inspected sources do not establish an
eligible asserted deposit-to-genome link for this BacDive strain.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The first search used the taxon,
both species spellings, slug, laboratory name, NCCB/UNIQUEM designations
and marker, and completed with 61 matching lines. The follow-up used
UNIQEM U246, SI number 138421 and Go0043992, and completed with 18.
Matching contexts were inspected, followed by full relevant objects.
Unrelated numeric, BacDive-ID and StrainInfo-deposit-ID matches were
excluded rather than confused with the target's SI strain identifier.

No SI strain object 138421 was found in those local searches. The
structured StrainInfo manifest reports an all-record snapshot of
314,470 records captured `2026-09-13T17:29:00Z`, with no request for
138421. The public rich API request
`https://api.straininfo.dsmz.de/v2/data/strain/max/138421` returned HTTP
404, and its web page was inaccessible. BacDive's SI link therefore
remains an unresolved external lead, not a proven missing eligible
association. No same-number object from another namespace was imported.

Complete crosswalk scans returned zero matching rows in
`data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`,
`data/raw/strain_related_records.tsv`, `data/straininfo/assemblies.tsv`,
`data/straininfo/related_records.tsv.gz`, `data/atb/strain_links.tsv`
and `data/atb/genome_links.tsv`. Native ATB hits for other species
isolates do not establish a type-strain join. Direct MediaDive and
BactoTraits inventory scans found no target rows. Empty optional media,
phenotype and causal-graph fields were not treated as defects.

## Findings

Counts: 0 blocker, 1 major, 1 minor.

1. **M1, major: the explicitly established type is not represented.**
   The record lacks `nomenclature[].type_strain_designations` and
   `strains[].is_type_strain` for its only strain. LPSN and the inspected
   species-description abstract explicitly support NCCB 100376 and
   HL-EbGr7; five NCBI type-material rows beginning at
   `data/raw/ncbi_type_material.tsv:1687` independently agree. BacDive
   also declares this strain a type. The loss is visible in the empty
   `type_strain_ids` cell of `data/raw/lpsn_names.tsv:27090`.
   `src/taxonmech/extract.py:420` imports type IDs from LPSN KGX
   close-match edges; `src/taxonmech/seed.py:405` copies the IDs and
   `:514` derives the type flag by exact deposit intersection. An
   explicit LPSN NCCB-100376 assertion would match the existing deposit.
   The maintained owner is the LPSN transform/extraction path configured
   in `conf/sources.yaml`, with `src/taxonmech/extract.py` as its local
   consumer. The original KGX files were unavailable, so this review
   cannot assign the original loss specifically to upstream production
   versus local extraction. Do not hand-patch the generated YAML.
2. **m1, minor: the singleton GTDB mapping has an inaccurate note.**
   Its note says the cluster also maps to other NCBI taxa. The complete
   native cluster contains only ALJ17 under `1033854`, and the complete
   mapping inventory has only that taxon for this cluster. The actual
   complexity is one NCBI species mapping to multiple GTDB clusters.
   The predicate and count are supported; the generic explanatory
   sentence at `src/taxonmech/seed.py:462` is the maintained fix owner.

## Recommended Edits

1. Restore source-grounded LPSN type-designation ingestion through the
   configured upstream LPSN transform and `src/taxonmech/extract.py`.
   First inspect the actual KGX edges in an available source checkout:
   repair upstream if the NCCB assertion is absent there, or the local
   extractor if a supported explicit edge is dropped. Regenerate the
   inventory and seeded record through the documented pipeline. Preserve
   LPSN provenance and require the existing NCCB deposit intersection to
   derive `is_type_strain: true`; do not use an unconditional flag or
   infer identity from bare strain-name similarity.
2. In `src/taxonmech/seed.py`, make broadMatch explanatory wording
   accurate for a taxon split across clusters without asserting reverse
   multiplicity. Preserve source predicates, cluster IDs and counts, and
   keep the secondary cluster out of exact synonyms and xrefs.
3. Keep the UNIQEM/UNIQUEM conflict explicit in future source work.
   Recheck an authoritative collection assertion before any alias change;
   do not broaden the global deposit normalizer or combine GOLD chains
   merely to attach the known genome. This is follow-up context, not a
   third finding against the faithful BacDive representation.

## Follow-up Checks

- Add focused extraction/seeding regression coverage for a species with
  an explicit LPSN NCCB type deposit and a matching BacDive strain.
  Confirm both the nomenclatural designation and derived type flag, and
  ensure nonmatching deposits do not acquire the flag.
- Add a mapping-note regression for one NCBI taxon split over two GTDB
  species where a cluster has no second NCBI taxon. Recount native
  cluster membership and preserve the present four/one counts.
- Rerun the two focused validators after any authorized curation change,
  then run the documented full `just verify-corpus` gate for regeneration.
  Do not present a bounded source comparison as byte-level reproduction.
- Resolve the original LPSN KGX availability and SI-ID 138421 lead when
  those source artifacts are accessible. Any proposed genome link still
  needs an explicit eligible deposit assertion in the owning source.

## Additional Notes

The filename lock at `data/taxa/PATHS.tsv:13776`, scope row at
`curation/seed_scope.tsv:14830` and seed timestamp
`2026-09-13T17:54:04Z` agree. The event's historical five-source scope
reason is copied from the scope inventory; it is not a contradictory
recount of today's six listed attestations. This review does not promote
the record from SEEDED or append a curation event.

Ignored-inclusive filename searches found no earlier target report or
target-specific history artifact before this report was created.
The configured kg-microbe LPSN main/API node and edge files were
unavailable, and an ignored-inclusive LPSN filename search of that
configured checkout found none. This limits attribution of the upstream
loss, not the independent source support for the missing type.

iModulonDB is not applicable to this taxonomic/nomenclatural record;
no gene, regulator, expression module or mechanism claim is being made.
No paid research, outside contact, GitHub mutation, record edit,
generator run or curation-history mutation occurred.
