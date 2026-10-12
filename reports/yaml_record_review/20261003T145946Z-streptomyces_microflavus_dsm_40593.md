# YAML Record Review: Streptomyces microflavus DSM 40593

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_microflavus_dsm_40593.yaml`
- Started UTC: 2026-10-03T14:56:17Z
- Finished UTC: 2026-10-03T14:59:46Z
- Verdict: needs curation

## Target

- `TaxonRecord`, `NCBITaxon:1303692`, rank `STRAIN`, domain `BACTERIA`,
  parent species `NCBITaxon:1919`, genetic code 11.
- Read all 1,663 YAML lines in four untruncated portions before judging.
  Grounding is `EXACT` and mapping status `SEEDED`.
- One BacDive strain, 15206, designation A26, retains 24 culture IDs,
  nine assembly assertions, six other-genome assertions, and 87 related
  assertions. These are source assertions, not distinct genome counts.
- One GTDB mapping, two exact synonyms, one equivalence xref, six source
  attestations, and one embedded seed event are present. There is no
  nomenclature block or causal graph.
- Generated YAML remains unchanged. The sole manual write is this report;
  strict validation also produced its standard diagnostic TSV.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_microflavus_dsm_40593.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_microflavus_dsm_40593.yaml`:
  PASS; one file scanned, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Structured identity, parent, genetic code, all 12 lineage entries,
  singleton subtree, and directly classified BacDive membership: PASS.
- Exact multiset comparisons reproduce eight raw plus one StrainInfo
  assembly assertions, six raw other-genome assertions, and 38 raw plus
  49 StrainInfo related assertions, including nested evidence.
- Full own-deposit scan and in-memory StrainInfo replay reproduce
  21 deposit links, one assembly, and 49 related assertions with no
  exclusions. All actual matched-deposit fields pass the culture matcher.
- Native GTDB census confirms 132 distinct species-cluster genomes,
  not 132 genomes of this strain. Semantic finding M1 remains despite
  schema and source-reproduction success.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  replacement was invented. Global source provenance, generated pages,
  exports, and downloaded genome sequences were not audited.
- Ignored-inclusive ID, label, and slug searches of `history/` found no
  target entry. Standalone history validation had no target; strict
  validation checked the embedded event. No audit/status mutation occurred.
- Graph/product evidence gates are not applicable to this graph-free record.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308116` supports the identity, parent,
code, and strain-specific synonym Streptomyces fulvissimus DSM 40593.
The complete native name objects at
`data/catalog/ncbi_names-0007.jsonl.gz:30668` and 30669 distinguish
the synonym from the current scientific name. The complete pinned
backbone has no descendants of strain 1303692.

Inspected [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303692&retmode=xml)
confirms the name, synonym, strain rank, parent 1919, code 11, and
lineage, including the griseus species group and microflavus subgroup.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303692)
also supplies all 12 ancestor IDs, including root. This NCBI grounding
is supported; the extra GTDB species-level exact synonym is not.

[JCM 4754](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=4754)
corroborates the deposit history through IFO 13482, ISP 5593 and NRRL
B-1453, the DSM 40593 equivalence, BacDive 15206, and the genome family.
It specifically identifies type material of S. fulvissimus, not the
nomenclatural type of S. microflavus. Its legacy NCBI link is 68202;
the inspected current NCBI strain authority independently establishes
the record's identifier and classification.

[LPSN S. fulvissimus](https://lpsn.dsmz.de/species/streptomyces-fulvissimus)
lists DSM 40593 among that name's type cultures and identifies
S. microflavus as the correct name. The
[S. microflavus page](https://lpsn.dsmz.de/species/streptomyces-microflavus)
has different type material, including DSM 40331 and JCM 4496.
The corresponding raw rows are `data/raw/lpsn_names.tsv:20350` and 20493.
Only the latter maps to species 1919; neither maps to strain 1303692.
Absent nomenclature and `is_type_strain` follow the same-taxon LPSN
derivation and must not be read as a negative type-material assertion.

## Evidence

**Attestations and history.** Exact-field scans reproduce:

| Source | Inventory location | Count and unit |
| --- | --- | --- |
| NCBI | `data/raw/ncbitaxon_taxa.tsv:308116` | 1 NAME |
| GTDB | `data/raw/gtdb_species.tsv:169950`; `gtdb_mappings.tsv:17463` | 132 GENOME for the species cluster |
| BacDive | `data/raw/bacdive_strains.tsv:15031` | 1 STRAIN |
| MediaDive | `data/raw/mediadive_taxa.tsv:2818` | 5 MEDIUM: 65, 84, J42, J50, J58 |
| Madin | `data/raw/madin_taxa.tsv:11828` | 4 TRAIT_ASSERTION |
| BactoTraits | `data/raw/bactotraits_taxa.tsv:2282` | 5 TRAIT_ASSERTION |

`curation/seed_scope.tsv:12072` supplies the six-source admission reason.
The 2026-09-13T17:54:04Z embedded seed event preserves it and does not
claim human review. Full exact-field inventory scans found no direct
target LPSN or GOLD taxon row. Primary GOLD culture/genome evidence
does not manufacture a taxon-level KGX GOLD count. Different units
cannot be summed into a biological measurement.

**BacDive and culture identifiers.** The full native object at
`data/bacdive/records.jsonl.gz:15030` supports designation A26, all
24 retained identifiers, source taxon 1303692, and its genome object.
The inspected [BacDive page](https://bacdive.dsmz.de/strain/15206)
corroborates the identity, designation, and species/strain taxon IDs.
Native genome reference 66792 supplies unversioned GCA_000385945,
IMG 2554235391, BV-BRC 1303692.3, and level complete.
The raw medium count is zero, unlike the separate MediaDive count;
omitting a strain medium-count field is consistent with that inventory.

Twenty-three retained culture IDs are matcher-eligible. ISP 5593 is
retained as `kgmicrobe.strain:ISP%205593` but its authority is absent
from the pinned CAFI registry in an ignored-inclusive search. It is
not rewritten to NRRL ISP-5593. NCIB 9609 and NCIMB 9609 remain separate
exact source keys. A26 is a designation, not a culture accession.

**Assembly family.** The complete objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:11019` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:9596` support GCA_000385945.1
and GCF_000385945.1 as an identical GenBank/RefSeq pair, one complete
7,905,758-bp chromosome from DSM 40593, BioSample SAMN02603305.
The GenBank project is PRJNA192408 and the snapshot RefSeq umbrella
project is PRJNA224116. The source type-material qualifier concerns
the heterotypic synonym, consistent with the distinct LPSN type cultures.

Live Datasets reports for
[GCA_000385945.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000385945.1/dataset_report)
and [GCF_000385945.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000385945.1/dataset_report)
confirm current complete status, the pair, culture, sample, chromosome
count, and size. They associate both accessions with PRJNA192408;
the pinned RefSeq umbrella remains source-qualified rather than being
silently replaced. Unversioned BacDive and StrainInfo accessions remain
unversioned in the record.

`data/bvbrc/bvbrc-0001.jsonl.gz:23821` supports 1303692.3 via the
explicit DSM 40593 strain field, assembly, sample, project, chromosome
CP005080.1 and RefSeq chromosome NC_021177.1. Its older S. fulvissimus
label is preserved. `data/catalog/gtdb_genomes-0010.jsonl.gz:30498`
supports RS_GCF_000385945.1, the GenBank accession, sample and umbrella
project through the same explicit culture key. NCBI Kitasatosporales
and GTDB Streptomycetales are distinct source placements, not grounds
for changing the NCBI lineage.

**GOLD chains.** The full native organism at
`data/gold/organisms.jsonl.gz:31632`, Go0037488, supplies DSM 40593
through both culture-collection and strain fields. Its source label
S. griseus disagrees with current NCBI/LPSN naming, but its taxon ID
1919 and exact culture key are preserved. The source name is not
promoted to a taxon synonym.

| Project | Native location | Sample | BioProject | Analysis |
| --- | --- | --- | --- | --- |
| Gp0037488 | `data/gold/projects.jsonl.gz:25631` | SAMN02603305 | PRJNA192408 | Ga0021774 |
| Gp0304920 | `data/gold/projects.jsonl.gz:204525` | SAMN12812662 | PRJNA571619 | No matching analysis in the pinned native search |

`data/gold/analyses.jsonl.gz:13750` explicitly links Ga0021774 to
Gp0037488, GCA_000385945.1, CP005080, and IMG 2554235391. Its empty
direct organism field is resolved through the explicit project chain.
Gp0304920 contributes only sample/project context. Live
[BioSample SAMN12812662](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN12812662&retmode=xml)
confirms DSM 40593, the GOLD project, PRJNA571619, and current species
1919. That sample is not substituted for the genome's SAMN02603305.

Seven further native organisms, Go0603744, Go0603745, Go0603746,
Go0603748, Go0603749, Go0603750, and Go0603751, retain ATCC 27431,
CBS 783.72, IFO 13482, NBRC 13482, NCIB 9609, NRRL B-1453, and RIA 1443
respectively. Their complete objects at organism lines 434752 through
434759 were inspected. The intervening Go0603747 carries unsupported
ISP 5593 and correctly supplies no join. These typed organisms are not
genomes; their doubled field-specific assertions preserve provenance.

**StrainInfo.** The complete native object at
`data/straininfo/records.jsonl.gz:14103` has 26 own deposits and eight
sequence objects. Twenty-one deposits match retained eligible culture
keys. All are available, with nondeprecated collections, nonerroneous
relations, and source taxon 1919. Their SI-DPs are:

| Culture | SI-DP | Culture | SI-DP |
| --- | --- | --- | --- |
| ATCC 27431 | 55610 | BCRC 12172 | 506647 |
| CBS 783.72 | 229397 | CCUG 11114 | 55613 |
| CGMCC 4.1302 | 755113 | CGMCC 4.1524 | 756014 |
| CIP 105783 | 155903 | DSM 40593 | 55614 |
| IFO 13482 | 55615 | IFO 3717 | 55616 |
| JCM 4129 | 55618 | JCM 4754 | 55619 |
| KCTC 9779 | 321794 | LMG 19310 | 55609 |
| NBRC 13482 | 334126 | NBRC 3717 | 334127 |
| NCIB 9609 | 105386 | NCIMB 10505 | 55623 |
| NCIMB 9609 | 55624 | NRRL B-1453 | 55625 |
| VKM Ac-994 | 55627 | | |

CCRC 12172, AS 4.1524, ICMP 155, NCIB 10505, and AS4.1302 are
not retained keys and are not substituted for their apparent relatives.
IFO 3717 has a false type flag while NBRC 3717 has true; these source
assertions are not collapsed into an inferred uniform type flag.
The record-version DOI
[10.60712/SI-ID14103.3](https://api.datacite.org/dois/10.60712/si-id14103.3)
resolves in inspected DataCite metadata to a findable DSMZ strain record,
not a deposit or a literature publication.

GCA_000385945 explicitly names DSM 40593 / SI-DP 55614. All seven
nucleotide links likewise name their own matched deposits. Live NCBI
EFetch verifies their accession versions, lengths, source cultures,
and partial 16S annotations:

| Accession | Culture | Length |
| --- | --- | --- |
| [AB184434.1](https://www.ncbi.nlm.nih.gov/nuccore/AB184434.1) | NBRC 13482 | 1,475 |
| [AB184787.1](https://www.ncbi.nlm.nih.gov/nuccore/AB184787.1) | NBRC 3717 | 1,476 |
| [AY999918.1](https://www.ncbi.nlm.nih.gov/nuccore/AY999918.1) | NRRL B-1453 | 1,325 |
| [D44336.1](https://www.ncbi.nlm.nih.gov/nuccore/D44336.1) | JCM 4754 | 120 |
| [KY820718.1](https://www.ncbi.nlm.nih.gov/nuccore/KY820718.1) | DSM 40593 | 1,054 |
| [KY820858.1](https://www.ncbi.nlm.nih.gov/nuccore/KY820858.1) | DSM 40593 | 976 |
| [LM999765.1](https://www.ncbi.nlm.nih.gov/nuccore/LM999765.1) | DSM 40593 | 1,502 |

Current nucleotide taxonomy is species 1919. Historical S. fulvissimus
descriptions remain source text, not contradictory identity assignments.
The YAML correctly retains unversioned accessions and keeps marker
sequences outside genome counts. There is no transfer of sequences
to deposits that merely share the SI strain record.

**GTDB scope.** An ignored-inclusive compressed census of every
`data/catalog/gtdb_genomes-*.jsonl.gz` shard found 133 textual hits,
of which exactly 132 have terminal GTDB taxon S. microflavus. These
are 132 distinct genome accessions; only one has native NCBI taxon
1303692. The representative is JCM 4496 / RS_GCF_014650075.1,
fully inspected at `gtdb_genomes-0005.jsonl.gz:6149`, not DSM 40593.
The typed mapping and its count faithfully reproduce the upstream
crosswalk, but they cannot support an exact strain synonym or equivalence.
The live GTDB taxon URL was inaccessible through the web tool; the
complete pinned native metadata, not that failed page, supports the census.

## Completeness

- The directly filed BacDive strain, all 24 source identifiers, and all
  implemented source-qualified assertions are retained without capping.
- Ignored-inclusive compressed searches covered all 149 selected native
  NCBI, GTDB and BV-BRC shards for the full retained culture-key spellings,
  ISP 5593, and strain taxon ID. Complete relevant native objects were read.
- All three native GOLD catalogs were searched by culture keys and exact
  connected organism/project/analysis IDs, including Gp0304920.
- Ignored-inclusive compressed searches of `data/atb/` and the complete
  `data/catalog/allthebacteria.tsv.xz` found no target ID, label, slug,
  BacDive key, SAMN02603305, or SAMN12812662. This is a bounded pinned
  source miss, not evidence that the culture lacks sequence data elsewhere.
- The structured iModulonDB dataset adapter was attempted through
  `uv run --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`
  and failed on sandbox DNS. Read-only fallback to the official
  [dataset API](https://imodulondb.org/api/datasets) found 20 organism entries
  and no microflavus, fulvissimus, or DSM 40593 dataset. S. albidoflavus
  and S. coelicolor are not substitutes. iModulonDB is not applicable,
  not negative biological evidence; no component summary was warranted.
- Optional nomenclature, record-level evidence and causal graph need not
  be invented. The consequential defect is the over-scoped synonym/xref,
  not a missing phenotype, medium recipe, or inferred type flag.

## Findings

**M1 - Major: a species-cluster close match becomes exact strain identity.**

At record lines 62-68, the GTDB label Streptomyces microflavus is an
`EXACT_SYNONYM`, and the species identifier appears in `xrefs`.
`src/taxonmech/schema/taxonmech.yaml:180` reserves that field for true
equivalence. The record denotes DSM 40593, while the inspected native
cluster includes 132 genomes and has a different representative/type
culture, JCM 4496. Neither cluster membership nor the source
`skos:closeMatch` establishes exact strain identity.

Maintained owner: `src/taxonmech/seed.py:451` treats every close match
as identity, and lines 466-469 unconditionally promote it into the
equivalence xref and exact synonym without checking taxonomic rank.
The upstream crosswalk at `data/raw/gtdb_mappings.tsv:17463` also needs
scope-aware interpretation; any correction to its source predicate
belongs in the kg-microbe GTDB mapping transform, not hand-edited raw data.

Blocker: None found. Minor: None found. The NCBI strain-specific
S. fulvissimus DSM 40593 synonym and the explicit genome/deposit links
remain supported and must not be removed with the overbroad GTDB entry.

## Recommended Edits

1. In `src/taxonmech/seed.py`, make GTDB synonym/xref promotion
   rank-aware and require defensible same-scope identity. Do not emit
   this species name as an exact synonym or equivalence xref of DSM 40593.
2. Preserve the typed source mapping and its species-level count as
   provenance unless an authorized upstream correction changes them.
   Do not recast 132 as this strain's genome count or change the NCBI lineage.
3. Add a regression in `tests/test_seed.py` for a strain-level close match
   to a broader species cluster, preserving genuine NCBI strain synonyms
   and valid species-level behavior. Then regenerate through the documented
   seed/canary workflow; never patch this YAML or generated pages directly.

## Follow-up Checks

- After an authorized fix, run the focused seed tests and both target
  validators listed above. Confirm that only the unsupported exact GTDB
  synonym/xref disappears and the nine assembly, six other-genome and
  87 related source assertions remain intact.
- Review the upstream mapping's orientation and rank scope before
  changing its predicate; a simple label match is insufficient.
- Run `just verify-corpus` and the normal full quality gates in the
  regeneration workflow. No mutation or hypothetical test pass is claimed here.

## Additional Notes

- Every absence claim above uses direct complete structured reads or
  `rg --no-ignore --hidden`, with `-z` for compressed inputs. Native
  records were reread in untruncated output after an initial broad
  SI-ID search also matched longer identifiers and truncated.
- Source-preserved GOLD naming and SI type-flag differences do not
  justify changing the NCBI record or merging culture identifiers.
- No source refresh, generator, paid research, GitHub action, history
  append, status promotion, or tracked-file edit was performed.
- Eukaryota was not re-reviewed. This report adds one individually
  source-backed non-Eukaryota review, not a bulk pass declaration.
