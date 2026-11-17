# YAML Record Review: Candidatus Parabeggiatoa communis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_parabeggiatoa_communis.yaml`
- Started UTC: 2026-10-06T02:29:41Z
- Finished UTC: 2026-10-06T02:36:57Z
- Verdict: pass

## Target

The entire 76-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034942`, `Candidatus Parabeggiatoa communis`, rank `SPECIES`,
domain `BACTERIA`, with parent `NCBITaxon:1034941` and nine root-first
ancestors. It carries genetic code 11, `grounding_status: EXACT`,
`mapping_status: SEEDED`, and `strain_count: 0`.

One GTDB species mapping, `GTDB:s__Parabeggiatoa_communis`, is represented as
`skos:closeMatch` with `genome_count: 2`. There are three source-qualified
synonyms and one GTDB xref. Attestations are one NCBITAXON `NAME` from the
2026-09-13 snapshot and two GTDB `GENOME` assertions. The inline seed event
is dated 2026-09-13T17:54:04Z. No individual strain, nomenclature, phenotype,
mechanism, or causal-graph objects are asserted.

## Validation

Both documented focused validators completed successfully with
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

| Command | Result |
| --- | --- |
| `just validate data/taxa/bacteria/candidatus_parabeggiatoa_communis.yaml` | Exit 0; no schema issues. |
| `just validate-strict data/taxa/bacteria/candidatus_parabeggiatoa_communis.yaml --out /private/tmp/communis-validation.tsv` | Exit 0; one file scanned, zero ERROR rows. The full TSV is header-only. |

Additional checks completed:

- Compared the complete owning backbone row and all nine ancestors with the
  YAML; identity, ranks, parent chain, genetic code, and NCBI synonyms agree.
- Read the complete exact-ID rows in all seven supplementary inventories,
  the unique index/scope entries, and the native objects behind the GTDB
  cluster. The scope reason and inline seed event agree with the two sources.
- Checked exact-ID type-material, merged-ID, and dropped-record inventories;
  none contains this ID. No immediate child of the target occurs in the
  pinned backbone.
- Reconciled 87 unique local candidate addresses with complete native-object
  reads. For repeated fields, lossless common-fields-plus-row-delta output
  was checked by reconstructing each original object, not by projecting away
  potentially relevant fields.
- Verified SHA-256 for `data/catalog/gtdb_genomes-0003.jsonl.gz` and
  `data/catalog/gtdb_genomes-0005.jsonl.gz` against `data/catalog/MANIFEST.json`.
  They match `27952cd83f56e084919e6bc31778365b9e7495d80a9fe6bbc97055a586ce8344`
  and `43bdf17b0d30e3faa3ca880d89b5204fd9e79939bd82f32e5c1109b9d8674dfc`.
- Inspected live NCBI taxonomy, both exact-taxid assembly summaries, four
  filtered 16S-marker records, three relevant WGS masters, the public SeqCode
  name object, primary publication metadata/abstracts, and selected complete
  sections of the genome-assignment paper.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, full
strict/history gates, complete provenance/hash reproduction, render drift,
README statistics, publication-size gates, and vendored synchronization.
The two shard checksums do not constitute a full provenance audit. The
manifest's original GTDB metadata inputs were unavailable at the declared
`data/raw/gtdb/` paths; a filesystem search under `data/raw`, including ignored
files, found neither metadata filename. No re-extraction was attempted.

No undocumented focused ontology/history validator was substituted for a
corpus gate. Source references, lineage terms, and the inline event were
checked through the bounded comparisons above. No sequence alignment, ANI
calculation, or genome-quality recomputation was performed.

## Identity and Grounding

The owning row at `data/raw/ncbitaxon_taxa.tsv:221760` agrees with the complete
record. Its index entry is `data/taxa/PATHS.tsv:14229`; its scope entry is
`curation/seed_scope.tsv:66006`. NCBI Taxonomy EFetch and Datasets agree on the
active ID, species name, parent, bacterial domain, code 11, and ancestor
chain; Datasets includes root in its nine ancestor IDs. See the
[NCBI Taxonomy record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034942).

The native NCBI name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31177`
through 31179 distinguish the authority, scientific name, and equivalent
name. The authority is correctly carried as `RELATED_SYNONYM`, while
`Parabeggiatoa communis` is an `EXACT_SYNONYM`. This agrees with the importer
name-class policy. The second exact synonym with the same text has GTDB
provenance and is not an accidental duplicate of the NCBI assertion.

The complete mapping at `data/raw/gtdb_mappings.tsv:1403` and species row at
`data/raw/gtdb_species.tsv:136346` support the GTDB ID, label, parent,
`skos:closeMatch`, and count of two. The seeder's inspected mapping policy
retains this predicate and permits the corresponding xref and exact name
synonym. This is a source-qualified species-concept match, not a claim that
every GTDB member has the same NCBI assignment or is the same physical strain.

The inspected [LPSN species page](https://lpsn.dsmz.de/species/parabeggiatoa-communis)
identifies the Salman et al. 2011 name, nomenclatural type `Limfjorden D4`,
and marker `AF532770`. It distinguishes not-validly-published status from
pro-validly-published/pro-correct status. The YAML makes no conflicting
publication-status claim. The type designation is not, by itself, a registered
culture-collection accession.

Source hierarchy differences remain explicit: NCBI carries Thiotrichales /
Thiotrichaceae, whereas the GTDB native rows carry Beggiatoales /
Beggiatoaceae. The naming paper also argues for retaining Beggiatoaceae.
TaxonMech's documented rule is to carry NCBI lineage and retain other source
classifications separately, not silently reconcile them.

## Evidence

The 13 inspected GTDB genome objects returned by the genus search belong to
five distinct species clusters. Exactly two belong to the target cluster:

| GTDB member | Native row and identity | Interpretation |
| --- | --- | --- |
| `GB_GCA_035871815.2` | `data/catalog/gtdb_genomes-0003.jsonl.gz:35320`; representative; isolate `WS_Bin1`; `SAMN38990891`; `PRJNA1054368`; NCBI taxon 1034942 | Supports the target species concept and one member of the GTDB count. |
| `GB_GCA_032082465.1` | `data/catalog/gtdb_genomes-0005.jsonl.gz:38235`; non-representative; isolate `CTOTU50709`; `SAMN29163922`; `PRJNA850115`; NCBI taxon 2030882, Thiotrichaceae bacterium | A member of this GTDB cluster with a broader NCBI assignment, not a direct NCBI assertion for taxon 1034942. |

The latter source difference is also visible in the separate
`skos:broadMatch` row to `NCBITaxon:2030882` at
`data/raw/gtdb_mappings.tsv:143290`. It is not silently converted to an exact
match or used to rewrite the target lineage. The GTDB attestation of two
`GENOME` assertions matches the cluster count, not the count of genomes
directly assigned to this NCBI taxon. The NCBI count of one `NAME` remains a
different unit and must not be added to it as a biological total.

Live exact `txid1034942[Organism:noexp]` Assembly search returned two records,
whose full summaries were read: `GCA_035871815.2` and `GCA_982596375.1`.
The second is isolate `ANDE17-1_SAMEA4470836_MAG_00000031`, BioSample
`SAMEA122210866`, BioProject `PRJEB72912`, with sequence release 2026-04-30.
It is not the second member of the pinned GTDB pair. GTDB's inspected home
page dates RS232 to 2026-04-15; these two source-specific counts therefore
must not be treated as interchangeable inventories. See
[GTDB release information](https://gtdb.ecogenomic.org/).

Complete current WGS master metadata were read for
[JAYQWI000000000.2](https://www.ncbi.nlm.nih.gov/nuccore/JAYQWI000000000.2),
[DAMDPU000000000.1](https://www.ncbi.nlm.nih.gov/nuccore/DAMDPU000000000.1),
and [CEWYVP000000000.1](https://www.ncbi.nlm.nih.gov/nuccore/CEWYVP000000000.1).
They corroborate the isolates, taxon assignments, samples, projects, and MAG
status. WS_Bin1 is a microbial-mat MAG; CTOTU50709 is an urban-metagenome MAG;
the additional assembly is a hydrothermal-vent MAG. None supplies an eligible
culture-collection deposit. Those environmental observations do not establish
species-wide habitat or metabolic claims.

Version and source differences were retained. The native historical row for
`GCA_035871815.1` is marked replaced, while `.2` is current. Two BV-BRC rows
for the `.2` assembly retain an older taxon 3100794/generic Parabeggiatoa
classification. The inspected current NCBI WGS/Assembly responses and GTDB
representative use taxon 1034942. These are source/version differences, not
grounds to overwrite the faithful target identity or merge physical strains.

The filtered Nuccore query was exactly
`txid1034942[Organism:noexp] AND (biomol_rrna[Properties] OR 16S[Title])`.
It returned four records, all inspected in full for metadata, references,
source features, and rRNA features:

| Marker | Isolate | Length and scope |
| --- | --- | --- |
| [AF532770.1](https://www.ncbi.nlm.nih.gov/nuccore/AF532770.1) | Limfjorden D4 | 1,496 bp; partial 16S; matches LPSN's type marker. |
| [AF532772.1](https://www.ncbi.nlm.nih.gov/nuccore/AF532772.1) | Limfjorden L22 | 1,497 bp; partial 16S. |
| [AF532773.1](https://www.ncbi.nlm.nih.gov/nuccore/AF532773.1) | Limfjorden L6 | 1,497 bp; partial 16S. |
| [AF532774.1](https://www.ncbi.nlm.nih.gov/nuccore/AF532774.1) | Limfjorden L8 | 1,496 bp; partial 16S. |

All four assert taxon 1034942 and marine sediment, without collection-deposit,
BioSample, BioProject, or assembly links in those marker records. A shared
species assignment does not equate their isolate designations. The filtered
four-record result is not claimed to be the entire Nuccore record set or a
review of all constituent genome contigs; sequence bases were not inspected.

Primary bibliographic records and full author abstracts were inspected for
[Salman et al. 2011, PMID 21498017](https://pubmed.ncbi.nlm.nih.gov/21498017/),
DOI `10.1016/j.syapm.2011.02.001`, and
[Mussmann et al. 2003, PMID 12755720](https://pubmed.ncbi.nlm.nih.gov/12755720/),
DOI `10.1046/j.1462-2920.2003.00440.x`, both cited by the markers.
The studies' mixed populations and sampled filaments are not automatically
evidence for universal species traits.
[Oren et al. 2020, PMID 32603289](https://pubmed.ncbi.nlm.nih.gov/32603289/),
DOI `10.1099/ijsem.0.003789`, was also verified as LPSN's Candidatus-list
reference; its abstract is not blanket evidence of valid publication.

[Ravin et al. 2024, PMID 38892213](https://pubmed.ncbi.nlm.nih.gov/38892213/),
DOI `10.3390/ijms25116028`, provides the WS_Bin1 assignment evidence. Its
abstract was read through PubMed. Complete sections 2.3, 2.4, 2.6, 2.8.3,
and 3.5 were read through the public
[Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11172852/fullTextXML)
after browser fetches failed. Section 2.4
assigns WS_Bin1 to this species using reported 99.87% 16S similarity, while
distinguishing three other species groups within the genus. The paper's
table uses assembly `.1`; current `.2` metadata were checked separately.
Genomic pathway predictions and genus-wide discussion were not transferred
into an unqualified phenotype or culture claim for this YAML. This was not
an independent reanalysis of the paper's alignments or functional annotations.

## Completeness

The represented identity, source mapping, synonyms, source-unit counts, and
seed provenance are supported. Zero imported strains is compatible with the
presence of MAGs and environmental isolate markers; it is not a claim that
the organism has never been observed or sequenced. The repository's own-
deposit rules do not allow constructing strain/genome links from species
names, MAG labels, or sample/project co-occurrence.

The initial gitignore-independent, compressed-file-aware search used
`rg --no-ignore --hidden -n -z -i` with
`\b1034942\b|Parabeggiatoa|candidatus_parabeggiatoa_communis` across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`.
It found 85 rows: 56 native JSON objects and 29 full TSV rows, all read.
An additional accession/BioSample/marker/isolate search returned nine rows,
two not previously seen, bringing the distinct inspected total to 87. The
extra rows were the CTOTU50709 BV-BRC and GenBank objects. No eligible
own-deposit link emerged. Source-manifest `SOURCE.json` files were excluded
from these biological-candidate searches; no global absence claim is made.

Exact-ID scans of the complete seven supplementary inventories found only
the GTDB mapping. They found no target row in `bacdive_strains.tsv`,
`lpsn_names.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`,
or `bactotraits_taxa.tsv` under `data/raw`. The LPSN name page is an optional
enrichment opportunity, not proof that the pinned transform failed its
documented coverage. Local LPSN coverage is explicitly a pinned transform,
not an assertion that the current website is completely mirrored.

The native SeqCode discovery objects are genus 36807 and species 50590.
The complete public [species API object](https://api.seqco.de/v1/names/50590.json)
confirms rank species, automated-discovery status, no priority date, and an
unknown nomenclatural type. Its QC warnings concern missing registry
description/type/publication metadata. It is not evidence of SeqCode valid
publication or a missing type-genome link, and those registry warnings are
not defects in this TaxonMech record.

Ignored-inclusive ID/name/slug searches of reports/history and an independent
report-filename search found no previous target review before this report was
created. The inline seed event remains present. iModulonDB is not applicable:
the YAML asserts no gene, regulator, expression module, or transcriptomics
claim. No optional causal graph or unsupported phenotype was added.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the represented claims. The hierarchy differences, broader
NCBI assignment for one GTDB member, differing genome sets, and older
BV-BRC/assembly classifications are preserved rather than conflated. The
verdict is limited to this target, its pinned inputs, and the checks completed.

## Recommended Edits

None required for the supported current record. Do not change the GTDB count
to the size of a differently scoped NCBI set, sum NAME and GENOME units, add
strains from MAG names, infer culture equivalence, or promote `SEEDED` to
`REVIEWED` through this read-only audit.

Future authorized source refreshes belong in the inputs and extraction
pipeline owned by `scripts/extract_source_inventory.py`, with NCBI pins in
`conf/ncbi_taxdump.yaml`. Any changed GTDB predicate or mapping count must be
supported upstream, carried into `data/raw/gtdb_mappings.tsv` through that
pipeline, and handled by `src/taxonmech/seed.py`; do not patch generated YAML.
Optional LPSN enrichment must preserve qualified nomenclatural status and
type-marker evidence. No scope change is indicated in
`curation/seed_scope.tsv`.

## Follow-up Checks

No blocking follow-up is required for this pass. Before future enrichment or
refresh, inspect the exact source-release membership and predicate again,
reconcile assembly versions and source taxon differences, and require a
registered own-deposit chain before adding strain/genome relationships.
Regenerate through `scripts/seed_from_sources.py` and the validated writer,
rerun the same focused schema/strict validators, then run documented full
reproduction, history, provenance, and publication gates for the changed corpus.

## Additional Notes

GTDB species-tree and genome-detail web fetches were unavailable through the
web reader. The inspected official home page confirmed the release, and the
complete retained native rows plus two matching shard hashes supported this
record's mapping/count audit. No live detail-page result was invented.
SeqCode browser fetches also failed, but its public API succeeded. The
publisher full-text fetch returned 429 and PMC's browser page presented a
browser check; Europe PMC's public XML API supplied the sections actually
inspected. Full texts of the older naming/marker papers were not re-read.

Guidance, field checklist, schema and relevant importer/seeder rules were
used with their generated-file boundaries. Only this new report was written.
No record, source inventory, scope, history, prior report, generated page,
or shared index was modified, and no curation event or status promotion was
made. Eukaryota and its completed reports remain untouched. The full-corpus
review goal remains active beyond this one completed target.
