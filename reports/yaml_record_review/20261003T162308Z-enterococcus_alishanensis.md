# YAML Record Review: Enterococcus alishanensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_alishanensis.yaml`
- Started UTC: 2026-10-03T16:17:29Z
- Finished UTC: 2026-10-03T16:23:08Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` before judgement. The target is
`NCBITaxon:1303817`, label `Enterococcus alishanensis`, rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:1350`, genetic code 11, grounding
`EXACT`, mapping status `SEEDED`. It has nine lineage entries, one LPSN
name, one GTDB mapping, three synonyms, two xrefs, one BacDive strain,
five source attestations and one embedded seed event. It asserts no
strain-genome links, experimental phenotypes or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_alishanensis.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_alishanensis.yaml`:
  PASS; one file, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison supports identity, parent, rank,
  genetic code and all nine lineage objects; no target children occur.
  PATHS and scope each contain exactly one target row. Full exact-field
  inventory checks support the source counts and singleton strain list.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated-site
  drift, exports and nucleotide content were not audited.
- Ignored-inclusive history searches found no target standalone event.
  Standalone history validation therefore had no target; strict validation
  checked the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308150` supports the taxon, code and two
NCBI related names. Complete native name objects at
`data/catalog/ncbi_names-0007.jsonl.gz:30699` through line 30701 retain
the authority, scientific name and historical ALS3 inclusion. The
root-first lineage matches the pinned backbone, without reconciliation
to another source's hierarchy.

The NCBI browser did not provide a consistently accessible view.
Inspected [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303817&retmode=xml)
confirms the ID, species name, rank, Bacteria division, parent 1350,
code 11, all eight non-root ancestors, the two related names and type
material ALS3, NBRC 109593 and BCRC 80605. Root is verified against the
pinned backbone. No identity or NCBI grounding conflict was found.

[LPSN record 26456](https://lpsn.dsmz.de/species/enterococcus-alishanensis)
supports the species name, Chung et al. 2022 authority, ICNP publication
status, correct-name status, cited publications and AB807774 marker.
The inventory's legitimate flag is supported by its retained status;
the inspected current page supplies no contradictory status. Its
medical-use wording concerns nomenclature, not a clinical or safety
claim about the organism.

GTDB's distinct genus label `Enterococcus_A` is retained as an external
classification, not used to rewrite the NCBI lineage. The species-level
closeMatch is defensible here: its representative is the ALS3 type
assembly. The generated exact synonym's spelling needs the minor
correction below; this is not a wrong-species identity finding.

## Evidence

### Nomenclature, Literature and Strain

`data/raw/lpsn_names.tsv:4606` exactly reproduces the YAML nomenclature,
including its single retained type designation, three publication
identifiers and marker accession. No LPSN-to-GTDB ID occurs in that row;
the GTDB mapping has separate inventory provenance.

[PMID 35180047](https://pubmed.ncbi.nlm.nih.gov/35180047/) and the
[publisher's original article](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005255)
agree on DOI `10.1099/ijsem.0.005255`, authorship and publication in
2022. Their inspected abstracts identify ALS3 as the type strain and
equate it to NBRC 109593 and BCRC 80605. Full article text was not
retrieved; no uninspected experimental result is used as a finding.

The second DOI resolves to the
[IJSEM notification article](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005343),
with matching Oren/Garrity authorship, volume 72, article 005343 and
2022 publication metadata. [PMID 35647790](https://pubmed.ncbi.nlm.nih.gov/35647790/)
corroborates that citation but is not an asserted YAML identifier.
LPSN explicitly associates the notice with this name. The notice's
full-text endpoint was inaccessible; its name-specific table was not
independently inspected.

[NCBI sequence metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB807774&rettype=gb&retmode=text)
resolves AB807774 to AB807774.1, a 1,513-base partial 16S rRNA record
for ALS3, taxon 1303817, with type-material annotation. Its old
definition uses Enterococcus sp. ALS3 while its organism field uses the
current species. This is a marker, not a genome. Preserve the source's
unversioned YAML accession; sequence bases were not inspected.

`data/raw/bacdive_strains.tsv:90499` and the complete native object at
`data/bacdive/records.jsonl.gz:90498` support BacDive 168266, its taxon,
NBRC-109593 and BCRC-80605 deposits, and type status. The native object
retains DOI `10.13145/bacdive168266.20251217.10`, an empty sequence
section and legacy StrainInfo reference 393358. The
[BacDive page](https://bacdive.dsmz.de/strain/168266) agrees on identity
and deposits, but the fetched page is older than the pinned native
version and is not evidence of a new snapshot.

The inspected [NBRC catalogue entry](https://www.nite.go.jp/nbrc/catalogue/NBRCCatalogueDetailServlet?CAT=00109593&ID=NBRC)
independently confirms NBRC 109593, the species name, BCRC 80605,
ALS3 and type status. Raw culture-deposit rows at lines 10423 and
133886 and NCBI type-material rows 21091-21096 agree. The seeder's
same-taxon LPSN/deposit intersection correctly yields `is_type_strain`.
An empty designation and omitted zero medium count reproduce the
BacDive inventory; they do not imply no known strain alias or medium.

### GTDB and Genome Context

`data/raw/gtdb_mappings.tsv:17476` and
`data/raw/gtdb_species.tsv:58256` support the mapping and count two.
A complete exact-terminal census of the native GTDB catalog found
exactly two distinct accessions for `s__Enterococcus_A alishanensis`:

| Native object | Accession | Strain | NCBI taxon | Representative |
| --- | --- | --- | --- | --- |
| `data/catalog/gtdb_genomes-0006.jsonl.gz:24452` | RS_GCF_019218635.1 | ALS3 | 1303817 | yes |
| `data/catalog/gtdb_genomes-0008.jsonl.gz:31530` | RS_GCF_051714685.1 | AZ103 | 2774628 | no |

The GTDB web taxon page was inaccessible. These full native objects
support the pinned count, not current release coverage. AZ103 remains
a separate NCBI placeholder; two GTDB members do not mean two NCBI
alishanensis genome records or two culture deposits.

ALS3's full GenBank/RefSeq objects at `ncbi_genbank-0017.jsonl.gz:31459`
and `ncbi_refseq-0003.jsonl.gz:34672` under `data/catalog/` identify
the identical GCA/GCF_019218635.1 pair, SAMN19878291, 50 contigs and
3,731,072 bases. BV-BRC 1303817.3 at
`data/bvbrc/bvbrc-0001.jsonl.gz:23834` agrees. GOLD's full chain is
Go0649548 -> Gp0685650 -> Ga0587648 -> IMG 3005782173, with the same
GenBank accession and sample, in `data/gold/organisms.jsonl.gz:479236`,
`projects.jsonl.gz:516828` and `analyses.jsonl.gz:385152`.

These objects carry bare ALS3 identifiers, not an eligible whole NBRC
or BCRC deposit token establishing the required genome join. GOLD's
culture field is empty. Literature corroborates the alias but does not
authorize bypassing the repository's source-chain rules. No genome link
was fabricated from shared taxonomy or type status.

The native catalogs also contain JNUCC77, taxon 1303817, the identical
GCA/GCF_053653825.1 pair and SAMN52655648, at GenBank 0049:28617 and
RefSeq 0008:9742. This separate strain is not a listed BacDive deposit
or one of the two pinned GTDB members. AZ103's GenBank 0047:37118 and
RefSeq 0007:39657 objects support its separate taxon 2774628 and
GCA/GCF_051714685.1 pair, SAMN16255356. Neither licenses transferring
genomes onto BacDive 168266.

### Attestations and Audit

All five source attestations agree with exact inventory membership:
NCBI 1 NAME, LPSN 1 NAME, GTDB 2 GENOME, BacDive 1 STRAIN, GOLD
1 ORGANISM. GOLD's count also agrees with
`data/raw/gold_organisms.tsv:7437`. These units must not be summed.
`curation/seed_scope.tsv:15422` admits the taxon with the five-source
reason carried by the 2026-09-13T17:54:04Z embedded seed event.
The curator, action and `SEEDED` status are consistent; no human
review status is asserted or granted by this report.

## Completeness

Ignored-inclusive searches covered target ID, label, slug, BacDive ID,
ALS3 and culture deposits in raw inventories, curation, history and
compressed native catalogs. Complete exact-field raw membership and
strain-link scans found no additional direct MediaDive, Madin or
BactoTraits membership, and no assembly/genome/related rows for the
listed BacDive strain. There are no descendants to contribute strains.

Additional complete ATB catalog and overlay searches used the target,
deposits and ALS3/JNUCC77 sample accessions; no matching ATB evidence
was found. That sample search does not claim coverage of AZ103's
sample. StrainInfo link, assembly, exclusion, related-record and native
searches found no eligible target deposit association. Its legacy
393358 web entry was inaccessible. A thin SeqCode 26389 name object
at `data/seqcode/names.jsonl.gz:25690` is only a name lead; the live
page was inaccessible and no additional claim was inferred.

Near matches were inspected and excluded: ALS3 labels for Pseudomonas
putida and Streptomyces; SI-ID 168266 for Tolypocladium geodes;
SI-DP 393358 for an E. coli deposit; E. coli strain 168266; and 168266
as an unrelated assembly statistic. Source-specific ID namespaces,
strain identity and taxonomy were not conflated. The fungal match was
not a re-review of any Eukaryota YAML record.

The missing optional genome links are justified at the current join
boundary, not proof that no genomes exist. No causal graph is required.
iModulonDB is not applicable: the record asserts nomenclature and a
marker accession, not a functional gene, regulator, pathway, trait or
transcriptomics claim.

## Findings

- Blocker: None found.
- Major: None found.
- Minor 1: GTDB synonym spelling loses source structure. The YAML exact
  synonym `Enterococcus A alishanensis` is not the native spelling
  `Enterococcus_A alishanensis`. `src/taxonmech/seed.py:468` replaces
  every underscore in the encoded label with a space, erasing the
  genus suffix delimiter as well as the species separator. The typed
  source ID remains intact, so this is a non-blocking source-label
  fidelity issue. Owner: seeder synonym construction and
  `tests/test_seed.py`, with a source-native label retained upstream
  where needed to avoid ambiguous decoding.
- Minor 2: LPSN type-designation coverage is incomplete. The YAML and
  raw LPSN row retain only NBRC-109593, while LPSN, the original paper
  and NBRC also identify BCRC 80605 and ALS3. BCRC is already present
  among the strain deposits and the type flag is correct, so identity
  is not lost. The narrower nomenclature list nevertheless omits
  supported type context. Owner: the maintained kg-microbe LPSN
  transform/input consumed by `src/taxonmech/extract.py:448`, then
  `data/raw/lpsn_names.tsv`; the seeder at line 405 faithfully copies
  the limited inventory. Inspect upstream edges before deciding
  whether extraction or the upstream transform needs correction.

## Recommended Edits

1. Preserve the GTDB genus suffix in synonym rendering. Prefer a
   source-native name or structured genus/epithet fields, not a blanket
   underscore replacement. Add a regression for this suffixed genus
   alongside an ordinary binomial. Do not change the mapping ID,
   count, source taxonomy or NCBI lineage as part of that fix.
2. Trace the LPSN input for record 26456 and retain the additional
   source-supported type designations with their proper identity kinds.
   BCRC-80605 is a collection deposit; ALS3 is a bare strain alias,
   not a new collection accession or an unrestricted genome-join key.
   Regenerate the inventory and record only through the authorized
   extraction/seeding workflow. Do not manually patch YAML.

## Follow-up Checks

Run focused extraction/seeder regressions, inspect an authorized
canary for taxon 1303817, then run both focused validators above.
Confirm source-faithful GTDB spelling, preserved NCBI lineage and
two-member GTDB count, complete supported type context, and unchanged
deposit-restricted genome joins. Any generated corpus change also
requires `just verify-corpus` and full QC. Those gates remain unrun.
Retry unavailable authority pages if current-release confirmation is
needed; this verdict is bounded to inspected metadata and snapshots.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, and `rg --no-ignore --hidden`, with compressed-source searches.
Read-only NCBI requests used network escalation after established
sandbox DNS failures. All cited literature claims are limited to
inspected abstracts, metadata and the explicit LPSN association.

The only manual write is this new report; strict validation wrote its
standard diagnostic. No YAML, source, earlier report, history or review
status was changed. No generator, refresh, paid research, GitHub action
or cross-repository write occurred. Eukaryota coverage was left intact.
