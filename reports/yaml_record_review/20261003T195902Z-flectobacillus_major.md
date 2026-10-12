# YAML Record Review: Flectobacillus major

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flectobacillus_major.yaml`
- Started UTC: 2026-10-03T19:53:05Z
- Finished UTC: 2026-10-03T19:59:02Z
- Verdict: pass with minor issues

## Target

Read all 823 lines of the generated `TaxonRecord` for
`NCBITaxon:103`, Flectobacillus major. Rank is `SPECIES`, domain
`BACTERIA`, parent `NCBITaxon:101`, genetic code 11, grounding
`EXACT` and mapping status `SEEDED`. The record has eleven lineage
entries, one LPSN nomenclature entry, three NCBI synonyms, two
xrefs, five source attestations and one embedded seed event.

One BacDive type-strain record, 3784, is gathered from the child
`NCBITaxon:929703`, Flectobacillus major DSM 103. It has six
culture/alias values, 9 assembly assertions, 7 other genome-record
assertions and 33 related-record assertions. These are separately
sourced relationships, not counts of distinct biological genomes.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/flectobacillus_major.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/flectobacillus_major.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison matched identity, rank,
  code, parent, eleven lineage entries and source synonyms. A full
  descendant traversal found only DSM 103, taxon 929703.
- Complete field-by-field multiset comparison matched all 9 assembly,
  all 6 non-ATB genome-record and all 33 related-record assertions
  to raw/StrainInfo tables, parsing nested JSON evidence. All 12
  StrainInfo assertions were independently checked against native
  deposits, classifications, DOI, statuses and same-deposit sequences.
- ATB metadata matched the full native catalog exactly. All six
  sample assertions matched the YAML related records and overlay;
  all five genome crosslinks had matching source evidence, not a
  Cartesian product of co-occurring genomes and samples.
- `just verify-corpus`: Not checked; full-corpus-only. The bounded
  comparisons do not substitute for corpus reproduction. Full QC,
  global provenance/hash replay, rendered products and exports were
  not audited. Primary archives and genome FASTAs were not downloaded.
- Ignored-inclusive ID, label, slug and culture searches found no
  standalone target history event. Strict validation checked the
  embedded event; standalone history validation had no target.
  Graph/product gates are not applicable because there is no graph.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:77` supports the species identity,
synonym Microcyclus major and two related authority strings.
The eleven-entry chain is root, cellular organisms, Bacteria,
Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group,
Bacteroidota, Cytophagia, Cytophagales, Flectobacillaceae and
Flectobacillus. The source clade ranks are preserved.

The child row at `data/raw/ncbitaxon_taxa.tsv:195805` and complete
native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:1794`
through line 1797 identify DSM 103 as a strain directly below this
species. The species name/authority objects at
`data/catalog/ncbi_names-0000.jsonl.gz:320` through line 323 agree.

Inspected live
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103,929703&retmode=xml)
confirms both identities, ranks, genetic codes, lineage and names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103,929703)
confirms all ancestor IDs, including root, and the sole child.
Exact grounding and bacterial placement are supported. Type-material
designations are not species synonyms.

The inspected
[LPSN name page](https://lpsn.dsmz.de/species/flectobacillus-major)
supports record 776283, the accepted validly published name,
authorship, 2016 emendation and M62787. The local authority retains
the emendation in its string. The current type list has one additional
deposit, discussed under Findings.

NCBI's Flectobacillaceae placement differs from LPSN/BacDive's
Spirosomataceae and GTDB's Spirosomataceae/Bacteroidia placement.
The YAML deliberately uses NCBI's lineage rather than blending
source classifications, consistent with `docs/HARMONIZATION.md`.

## Evidence

**Nomenclature and bibliographic references.**
`data/raw/lpsn_names.tsv:17114` reproduces all generated nomenclature
fields, including three type-deposit IDs, the status flags, two DOIs,
M62787 and the LPSN/GTDB xrefs. Inspected Crossref metadata for
[10.1099/00207713-27-2-147](https://api.crossref.org/works/10.1099/00207713-27-2-147)
identifies the 1977 Larkin/Williams/Taylor taxonomic paper, volume
27, issue 2, pages 147-156. Metadata for
[10.1099/00207713-30-1-225](https://api.crossref.org/works/10.1099/00207713-30-1-225)
identifies the 1980 Approved Lists, volume 30, issue 1, pages
225-420. Their bibliographic roles agree with the nomenclature
source. Full article texts were not read; no experimental or quoted
paper claim was inferred from metadata.

**BacDive strain and source scope.** The complete native object at
`data/bacdive/records.jsonl.gz:3680` and inspected
[BacDive 3784 page](https://bacdive.dsmz.de/strain/3784)
confirm the strain identity, type status, species/child taxon IDs
and six carried culture/alias values. The raw strain row is
`data/raw/bacdive_strains.tsv:3681`. This is one source strain,
not six strains. ATCC 29496 and DSM 103 already intersect the
LPSN type-deposit list, independently supporting `is_type_strain`.

The native genome assertion retains reference 66792 and explicitly
supplies unversioned GCA_000427405, BV-BRC 929703.3 and
IMG 2509601041. Their source co-occurrence does not independently
prove sequence equivalence. The encoded BKM B-859 alias remains
preserved but fails the pinned CAFI matcher; VKM B-859 passes.
The matcher does not rewrite BKM into VKM.

**NCBI and GTDB assemblies.** Complete primary objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:12913` and
`ncbi_refseq-0000.jsonl.gz:11082` supply GCA_000427405.1 and
GCF_000427405.1, their explicit pairing, DSM 103, taxon 929703,
species 103, scaffold level, SAMN00262208 and source-specific
projects PRJNA63323 and PRJNA224116. The manifest at
`data/raw/MANIFEST.yaml:79` and line 86 identifies the named
GenBank/RefSeq input snapshots. Source-unversioned accessions from
BacDive and StrainInfo were not silently assigned a version.

Inspected live
[NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000427405.1/dataset_report)
confirms the current GenBank accession, current explicit RefSeq
partner, assembly level, culture designation, BioSample, GenBank
project and type-material status. The live RefSeq annotation date
is newer than the pinned native annotation; the assembly accession
and checked relationships are unchanged. No biological conclusion
was drawn from a nearest ANI match or differing annotation counts.

The complete GTDB object at
`data/catalog/gtdb_genomes-0006.jsonl.gz:601` supplies representative
RS_GCF_000427405.1, DSM 103, both explicitly supplied NCBI
accessions and its project/sample IDs. `gtdb_species.tsv:64516`
has count 1. The GTDB mapping at `gtdb_mappings.tsv:320631`
belongs to child 929703, not species 103. Consequently the absence
of a species GTDB attestation/mapping is correct; the species xref
comes from LPSN's explicit GTDB association, not promotion of a
child attestation.

**BV-BRC and GOLD.** The complete BV-BRC object at
`data/bvbrc/bvbrc-0028.jsonl.gz:13723` explicitly connects DSM 103,
genome 929703.3, GCA_000427405.1, SAMN00262208 and PRJNA63323.
GOLD's complete Go0001169 object at
`data/gold/organisms.jsonl.gz:1042` supplies DSM 103 in its culture
field and the source strain text VKMB-859, DSM 103. Project
Gp0001169 at `projects.jsonl.gz:1071` supplies the same sample
and project. Analysis Ga0025035 at `analyses.jsonl.gz:15893`
explicitly references Gp0001169 and supplies GCA_000427405.1 and
IMG 2509601041. Its empty direct organism field is not a conflict:
the sole project resolves the chain. Separate culture and strain
fields legitimately yield separate provenance assertions.

Go0625612 and Go0625614 at organism lines 456212 and 456214
supply VKM B-859 and ATCC 29496 related records, without invented
projects or genomes. The other direct species organisms were read:
Go0191687 is bare 0614N1; Go0191688 is NCIMB 13237; Go0625613
uses unsupported BKM B-859. They contribute census context, not
eligible links to this BacDive strain.

**StrainInfo and the nucleotide marker.** The complete native
object at `data/straininfo/records.jsonl.gz:7686` agrees on the
asserted fields with the inspected
[live SI-ID7686 response](https://api.straininfo.dsmz.de/v2/data/strain/max/7686).
Its DOI is 10.60712/SI-ID7686.3, its status is published, and all
five matched deposits are available, nondeprecated and have
nonerroneous source relations:

| Deposit | SI-DP | Imported sequence explicitly naming that deposit |
|---|---|---|
| ATCC 29496 | 31295 | M62787, rRNA marker |
| CCM 2921 | 31296 | None; strain/deposit context only |
| DSM 103 | 31297 | GCA_000427405, unversioned genome |
| VKM B-859 | 31299 | None; strain/deposit context only |
| CCUG 14833 | 135074 | None; strain/deposit context only |

All 12 imported assertions match their own deposit evidence.
StrainInfo marks CCUG 14833 itself non-type, while the group and
other deposits carry type status; the YAML does not assert a
separate StrainInfo type flag for every deposit. No sequence is
transferred by group membership.

Inspected
[NCBI M62787 metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=M62787&rettype=gb&retmode=xml)
confirms the 1476-base partial 16S rRNA marker, ATCC 29496,
species 103 and type-material annotation. Live version M62787.2
does not replace the source-unversioned accession. Metadata and
feature annotations were checked; no alignment was performed.

**AllTheBacteria.** The entire native metadata row at
`data/catalog/allthebacteria.tsv.xz:1003717` equals the overlap
row at `data/atb/assemblies.tsv:2151`. It supports release-scoped
atb.assembly:202505.SAMN00262208, dataset 661k, both run IDs,
ERZ9432161, available FASTA, PASS assembly/HQ filters, exact
SeqKit sum and the supplied download/archive metadata.
`data/atb/strain_links.tsv:4210` preserves six matching sample
assertions. `data/atb/genome_links.tsv:18335` through line 18339
preserve five genome crosslinks with explicit same-source evidence
and relationship `shares_biosample`, not sequence equivalence.

Inspected live
[ENA analysis ERZ9432161](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ9432161)
explicitly references SAMN00262208 and both runs. Live run metadata
for [SRR190858](https://www.ebi.ac.uk/ena/browser/api/xml/SRR190858)
and [SRR3924020](https://www.ebi.ac.uk/ena/browser/api/xml/SRR3924020)
confirms public DSM 103 context and the shared SRS190396 sample.
ENA's file MD5 is not the ATB SeqKit sum. No FASTA/archive download
or checksum replay is claimed.

**Attestations and audit.** Counts agree with the inventories:
NCBI 1 NAME, LPSN 1 NAME, BacDive 1 descendant STRAIN,
GOLD 5 direct ORGANISM (`gold_organisms.tsv:385`) and Madin
2 direct TRAIT_ASSERTION (`madin_taxa.tsv:564`). Child counts
of GOLD 1, MediaDive 1, Madin 1 and BactoTraits 6 are correctly
not promoted to the species. The BacDive row has medium_count 0;
the child MediaDive inventory is a separate source surface.

`data/taxa/PATHS.tsv:12424` pins the slug. Scope line 23242
admits the species on 2026-09-12 with the historical four-source
reason. The 2026-09-13T17:54:04Z seed event correctly carries
five current generated source names, including descendant BacDive,
while retaining that exact scope reason. `SEEDED` is appropriate.

## Completeness

Absence checks included ignored files. Typed species/child IDs,
full current/former names, slug and culture searches covered
`data/raw/`, `curation/` and `history/`; no standalone target
history event was found. Complete structured reads covered the
backbone subtree, source inventories, raw relationship tables and
ATB/StrainInfo overlays. Native searches covered catalog, BacDive,
BV-BRC, GOLD, SeqCode and StrainInfo compressed projections.
All returned species/name objects were read in full. A supplemental
whole-deposit/typed-StrainInfo search returned 16 objects and no
additional object beyond that already inspected set.

The SeqCode object at `data/seqcode/names.jsonl.gz:7628` is a
name-index entry, not extra culture/genome evidence. StrainInfo's
additional LMG 13163, NCIMB 11363 and CGMCC 1.2802 deposits
are not in the local BacDive culture inventory and are not imported
solely from SI group membership. The separate native SI-ID60814
object at line 48418 denotes NCIMB 13237 / 0614N1, not this
type-strain culture. Its shared species is not sufficient to join it.

The full ATB genus search returned the target row and a different
Flectobacillus sp. AKPR sample, SAMN13930412. The latter has no
eligible prior target-strain sample assertion and is not imported.
The nomenclature-specific gap below does not mean VKM B-859 is
absent from the record, culture inventory or related-record evidence.

The local `kg-microbe-sources imodulondb datasets` runner succeeded
and returned no Flectobacillus dataset. iModulonDB is therefore not
applicable to the marker cross-check; this is not negative biological
evidence. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: 1 - The LPSN-derived type-deposit list is incomplete against
  the current authority page. `data/taxa/bacteria/flectobacillus_major.yaml:55`
  lists ATCC 29496, DSM 103 and LMG 13163, but the inspected
  [LPSN type list](https://lpsn.dsmz.de/species/flectobacillus-major)
  also includes VKM B-859. NCBI type-material metadata independently
  agrees (`data/raw/ncbi_type_material.tsv:1496`). VKM B-859 passes
  CAFI and already occurs in the BacDive/GOLD/StrainInfo relationships,
  so this is a nonblocking nomenclature provenance gap, not wrong
  taxon identity or a missing culture/genome connection.

The generated list faithfully mirrors `data/raw/lpsn_names.tsv:17114`.
Future repair belongs in the upstream LPSN source/transform feeding
that inventory via `src/taxonmech/extract.py:420`, not a YAML patch.
`src/taxonmech/seed.py:405` already carries supplied type IDs through.
This review does not establish whether source age or an upstream
transform omission caused the missing designation.

## Recommended Edits

1. In an authorized curation/source-refresh task, update the LPSN
   input for lpsn:776283 so its type-deposit relation includes
   `kgmicrobe.strain:VKM-B-859`, preserving the three existing IDs
   and evidence. The configured source paths are kg-microbe's
   `data/transformed/lpsn/{nodes,edges}.tsv`; any transform repair
   must be made in its maintained producer, not directly in generated
   KGX output. Re-extract the inventory and regenerate through the
   documented workflow. Do not append a fabricated manual YAML value.
2. Keep the supported strain relationships, accession versions,
   child classification, source counts and deposit-specific marker
   evidence unchanged. Do not rewrite BKM aliases or import SI-only
   deposits as part of this bounded nomenclature correction.

## Follow-up Checks

After an authorized fix, inspect the source relation, refreshed
`data/raw/lpsn_names.tsv` row and generated nomenclature list for
all four current type-deposit IDs. Recheck the LPSN page and
independent NCBI type-material evidence. Run the same focused
schema and strict validators above. Use `just extract-inventory-dry`
to inspect the configured extraction path before an authorized
refresh; normal extraction/seeding, overlay and provenance steps
must follow the repository workflow. Run `just verify-corpus` and
full QC before claiming corpus reproducibility or publication readiness.

## Additional Notes

GTDB browser retrieval failed; the full pinned native metadata and
live NCBI API supplied the checked genome identity. The configured
upstream KGX edge paths were not readable at their configured
locations during this review; no assertion is made that such files
are absent everywhere. The report identifies the local inventory
gap and owning extraction path without attributing an unproved
upstream parser defect. Full primary archives and global hashes
were not replayed.

Initial ad hoc comparisons required correcting JSON-column decoding
and using the existing CURIE-decoding helper. Corrected comparisons
passed; those diagnostic-script adjustments required no record edit.

Only this new report was manually written. Strict validation wrote
its usual diagnostic. No YAML, source, prior report, history or
status was changed. No generator, refresh, paid research, GitHub
mutation or cross-repository edit occurred. Eukaryota was not re-reviewed.
