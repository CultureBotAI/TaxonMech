# YAML Record Review: Frankia sp. ACN1ag

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/frankia_sp_acn1ag.yaml`
- Started UTC: 2026-10-03T19:31:24Z
- Finished UTC: 2026-10-03T19:36:57Z
- Verdict: pass

## Target

Read the complete 78-line generated `TaxonRecord` for
`NCBITaxon:102891`, Frankia sp. ACN1ag. It carries rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:2632575`, genetic code 11,
grounding `EXACT`, mapping status `SEEDED` and zero listed strains.
There are ten lineage entries, one GTDB mapping, one source-attributed
synonym, one xref, three source attestations and one embedded seed event.
No nomenclature, strain-genome assertions or causal graph are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/frankia_sp_acn1ag.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/frankia_sp_acn1ag.yaml`:
  PASS; one file, zero errors. Diagnostic:
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirmed identity, parent,
  rank, code and all ten lineage objects. No child taxon was found in
  the complete backbone scan. Complete source-inventory scans matched
  the mapping, counts and source units; scope, slug and embedded
  seed-reason comparisons also passed.
- `just verify-corpus`: Not checked; this is a full-corpus-only gate.
  The bounded comparisons above are not a substitute. Full QC,
  global provenance/hash replay, rendered products and exports were
  not audited. Primary archives and genome FASTAs were not downloaded.
- Ignored-inclusive ID, label and slug searches found no standalone
  target history event. Strict validation checked the embedded event;
  standalone history validation had no target. Graph/product gates
  are not applicable because the record has no graph.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18158` and the complete native name object
at `data/catalog/ncbi_names-0000.jsonl.gz:38164` support the exact
identifier and scientific name. The root-first lineage is root,
cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes,
Frankiales, Frankiaceae, Frankia and unclassified Frankia. The raw
NCBI exact, related and broad synonym fields are empty; the YAML's
Frankia torreyi synonym comes from GTDB, not NCBI.

Inspected live
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102891&retmode=xml)
and
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/102891)
confirm the identity, species rank, parent, code and ancestor chain.
Datasets includes all ten ancestor IDs; EFetch supplies the nonroot
lineage labels and ranks. No alternate name was supplied. An
isolate-like label does not authorize changing NCBI's species rank.

Frankia sp. ACN1ag(2009), `NCBITaxon:631139`, remains a distinct
active taxon under the same parent. Its complete local name object at
`data/catalog/ncbi_names-0003.jsonl.gz:43541` and inspected live
[EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=631139&retmode=xml)
and
[Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/631139)
do not establish equivalence with 102891. Its record was not re-reviewed.

## Evidence

**GTDB classification.** `data/raw/gtdb_mappings.tsv:1246` supplies
`GTDB:s__Frankia_torreyi`, label `s__Frankia_torreyi`, predicate
`skos:closeMatch` and count 4; `gtdb_species.tsv:64978` agrees.
The four complete native cluster objects were read:

| Native catalog location | GTDB genome | Source organism / taxon |
|---|---|---|
| `gtdb_genomes-0013.jsonl.gz:23618` | RS_GCF_001414035.1 | Frankia sp. ACN1ag / 102891 |
| `gtdb_genomes-0010.jsonl.gz:13447` | RS_GCF_000948395.1 | Frankia torreyi / 1856; representative |
| `gtdb_genomes-0014.jsonl.gz:2908` | RS_GCF_001421075.1 | Frankia sp. CpI1-P / 1502734 |
| `gtdb_genomes-0016.jsonl.gz:14578` | RS_GCF_019581175.1 | Frankia sp. ArI3 / 1858 |

All paths in this table are under `data/catalog/`. The target genome
explicitly names ACN1ag, taxon 102891, GCA_001414035.1,
SAMN03353435 and the GTDB Frankia torreyi classification. The count
is four members of the GTDB cluster, not four ACN1ag isolates or four
culture deposits. The live NCBI target assembly count of one is not
a contradiction: it measures a different set.

The sole source close mapping yields the GTDB-attributed synonym and
xref under `src/taxonmech/seed.py:437`. This retains the source
classification alongside, rather than replacing, NCBI's identity and
lineage. It is not evidence that the other NCBI IDs or their genomes
are interchangeable. The mapping predicate is the supplied KGX
predicate, not a newly inferred taxonomy reconciliation.

**Native assembly context.** The complete GenBank and RefSeq objects
at `data/catalog/ncbi_genbank-0001.jsonl.gz:4027` and
`ncbi_refseq-0000.jsonl.gz:45194` explicitly associate ACN1ag and
taxon 102891 with GCA_001414035.1 and GCF_001414035.1,
respectively. NCBI supplies their explicit pairing, scaffold level,
SAMN03353435 and source-specific projects PRJNA275977 and
PRJNA224116. These facts were not inferred by replacing accession
prefixes. Assembly name ACN1AG does not rename the taxon.

The complete BV-BRC object at
`data/bvbrc/bvbrc-0000.jsonl.gz:3001` names genome 102891.4,
ACN1ag, GCF_001414035.1, PRJNA275977, SAMN03353435 and
LJPA00000000. This is genome metadata, not a registered culture
deposit. PMID 26679592 appears in native assembly metadata, but is
not cited by the target YAML and was not used for literature claims.

**GOLD context and import boundary.** Complete native objects at
`data/gold/organisms.jsonl.gz:62948`,
`projects.jsonl.gz:66274` and `analyses.jsonl.gz:46988` preserve
the explicit Go0112912 -> Gp0115738 -> Ga0074159 chain.
The organism names ACN1ag and taxon 102891, the project supplies
PRJNA275977 and SAMN03353435, and the analysis supplies
GCA_001414035.1, LJPA00000000 and IMG 2619618881.
The analysis's direct organism field is empty; its explicit project
resolves the chain. The organism's culture-collection field is empty.

There is no local BacDive strain for the target and bare ACN1ag fails
the pinned CAFI culture-identifier matcher. Consequently these native
objects do not license adding strain-linked genome assertions. GOLD's
taxon attestation uses the KGX inventory, while the workbook supplies
strain-linked relationships (`docs/HARMONIZATION.md:44`). The native
organism's presence does not by itself make the absent KGX-derived
GOLD attestation a target-record defect.

**AllTheBacteria context.** The complete full-catalog row at
`data/catalog/allthebacteria.tsv.xz:1075632` supplies SAMN03353435,
SRR7456386, ERZ4102450, available FASTA, PASS filters, dataset
661k and a source-provided SeqKit sum. It names Frankia sp. ACN1ag
and a Frankia torreyi classification, retaining archive and direct
download metadata. No existing eligible strain BIOSAMPLE assertion
connects this sample to a local BacDive strain. Thus a known ATB
assembly is not a missing eligible strain import. Its FASTA, archive
contents and checksum were not fetched or replayed.

**Attestations and audit.** Complete inventories support NCBITAXON
1 NAME, GTDB 4 GENOME and MADIN 5 TRAIT_ASSERTION; Madin's row
is `data/raw/madin_taxa.tsv:542`. These units are not summed.
Madin's count is source coverage metadata, not five asserted
phenotypes requiring organism-wide biological interpretation.
The NCBI snapshot note is 2026-09-13.

`data/taxa/PATHS.tsv:11470` pins the slug;
`curation/seed_scope.tsv:31673` admits the taxon on 2026-09-12.
The embedded event at 2026-09-13T17:54:04Z correctly retains
seed_from_sources, SEEDED_FROM_SOURCES, the three source names
and the exact scope reason. This read-only review does not promote
the record's `SEEDED` status.

## Completeness

Absence checks included ignored files. ID, label, slug and ACN1ag
searches covered `data/raw/`, `curation/` and `history/`; complete
structured reads covered the backbone, seven source inventories,
scope and path indexes. No target BacDive, LPSN, GOLD KGX,
MediaDive or BactoTraits inventory row was found. GTDB and Madin
have the rows described above. No standalone history event was found.

Full-source candidate searches covered catalog, BacDive, BV-BRC,
GOLD, SeqCode and StrainInfo native projections, plus ATB and
StrainInfo TSV/compressed metadata. Twelve relevant native objects
were read in full. Twenty-nine remaining native candidates were
parsed and screened by complete identity fields and matching key
paths; this is not a review verdict on those foreign records.

Numeric matches included Vibrio orientalis deposit CIP 102891,
an unrelated BacDive record numbered 102891, a BV-BRC genome with
that suffix, other collections' accession 102891, and genome
statistics equal to 102891. None establishes taxon identity. The
seven matching StrainInfo overlay rows were read fully and belong
to Vibrio, not Frankia. Further ignored-inclusive TSV/compressed
searches for SAMN03353435, Go0112912, Gp0115738, Ga0074159,
GCA_001414035.1 and GCF_001414035.1 found no eligible target
raw/ATB/StrainInfo overlay row.

LPSN 801302, Frankia torreyi, maps to NCBITaxon:1856 in
`data/raw/lpsn_names.tsv:34260`, not to 102891. The shared GTDB
cluster does not authorize importing its nomenclatural authority,
DSM 44263 type designation, sequence or publications into ACN1ag.
Optional nomenclature and strains are correctly empty under the
current contracts. No biological claim requires a causal graph.
iModulonDB is not applicable: the record names no gene, regulator,
pathway, stress response or expression dataset; a trait-assertion
coverage count alone supplies no specific query or phenotype claim.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the NCBI identity, distinct ACN1ag(2009)
taxon, source-attributed GTDB classification and cluster count,
typed identifiers, and empty culture-linked slots.

Future enrichment requires an authorized maintained source path:
eligible BacDive culture evidence and the documented source/overlay
pipelines before `src/taxonmech/seed.py` may emit strain links.
GOLD attestation changes belong in its KGX inventory pipeline, not
an ad hoc native-organism count or a hand edit to generated YAML.

## Follow-up Checks

No corrective check is required. An authorized refresh should recheck
the exact NCBI identity, four GTDB cluster members, whole eligible
culture identifiers and explicit assembly/sample/project chains;
then rerun both focused validators. Corpus-wide reproducibility
and publication assurance also require `just verify-corpus` and
full QC, neither performed here.

## Additional Notes

Browser retrieval of the NCBI page and GTDB search page failed;
the inspected NCBI public APIs and pinned primary projections
provided the evidence stated above. Live status of the GTDB page
and every native genome record was not independently established.
No primary-archive, global provenance or genome-content audit is
claimed. The complete source objects were reread after an earlier
combined output was truncated; the foreign candidate screen remains
explicitly narrower than a record-level review.

The only manual write is this new report. Strict validation wrote
its standard diagnostic. No YAML, source, prior report, history or
review status was changed. No generator, refresh, paid research,
GitHub mutation or cross-repository edit occurred. Eukaryota was
not re-reviewed.
