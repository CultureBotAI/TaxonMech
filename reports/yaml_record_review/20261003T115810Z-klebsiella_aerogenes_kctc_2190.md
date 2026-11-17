# YAML Record Review: Klebsiella aerogenes KCTC 2190

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/klebsiella_aerogenes_kctc_2190.yaml`
- Started UTC: 2026-10-03T11:51:43Z
- Finished UTC: 2026-10-03T11:58:10Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1028307`, Klebsiella aerogenes
KCTC 2190, rank STRAIN, domain BACTERIA, parent `NCBITaxon:548`.
The complete parsed content of the 4,072-line YAML was inspected:
top-level fields and strain metadata, then every assembly, genome and
related-record row in lossless constant/column tables. Each table row
was checked for exact reconstruction; no evidence row or nested field
was sampled away. The initial plain-text read was truncated and was
not used as a substitute for this complete inspection.

The record has EXACT grounding, SEEDED mapping status, one GTDB mapping,
four synonyms, one xref, one BacDive strain with 27 source designations,
five source attestations and one embedded seed event. Its 33 assembly,
24 genome-record and 198 related-record assertions are evidence rows,
not that many distinct genomes.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/klebsiella_aerogenes_kctc_2190.yaml` | PASS; no issues, exit 0. |
| `just validate-strict data/taxa/bacteria/klebsiella_aerogenes_kctc_2190.yaml` | PASS; one file, zero errors, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive target searches found no separate history entry; strict validation covered the embedded event. |

Both commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.
All ten lineage entries matched the full pinned taxonomy inventory.
Complete subtree traversal found only this taxon, and full BacDive
inventory inspection found exactly strain 4358 filed here. All 27
designations matched the raw strain row and native BacDive literature
field. Structured comparisons proved exact reproduction of 30 raw
assembly, 23 raw genome and 83 raw related-record assertions, plus
three StrainInfo assembly and 115 StrainInfo related-record assertions.
The remaining genome record is the independently checked ATB overlay.

## Identity and Grounding

Raw taxonomy row 219119 and the inspected
[NCBI taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028307)
agree on the identifier, strain label, parent species, code 11 and
lineage. The browser reports no rank, whereas the pinned inventory
reports STRAIN; the underlying archive is unavailable locally, so this
source-version difference could not be resolved directly. It does not
justify changing the established strain identity into a species.

Native NCBI names contain the older Enterobacter aerogenes KCTC 2190
synonym and the two str./strain equivalent-name variants. Those three
exact aliases preserve the strain designation. In contrast, the GTDB
exact synonym Klebsiella aerogenes drops it and denotes the broader
species; see the major finding.

Native BacDive 4358 explicitly distinguishes species taxid 548 from
strain taxid 1028307. Its type status, 27-designation literature field
and StrainInfo 2190 link agree with inspected identity sections of the
[BacDive page](https://bacdive.dsmz.de/strain/4358). Source-classified
species-level assemblies attached through the same deposit are not
automatically wrong strain links. The native source and join evidence,
not a shared species name, establish those attachments.

## Evidence

**GTDB cluster versus strain.** Ignored-inclusive decompressed searches
of every native GTDB genome shard found exactly 794 members of
`s__Klebsiella aerogenes`. Only two have taxid 1028307:
`RS_GCF_000215745.1` and `RS_GCF_050435165.1`, both explicitly KCTC 2190.
The first is the species representative. Another 751 members have
taxid 548, and 41 have other taxids. Thus the raw GTDB row 1223 count
is a cluster count, not a count of genomes assigned to this strain.
The inspected native metadata also confirms the ATCC 13048 member
`GB_GCA_003417445.1`. The GTDB web endpoint was inaccessible; the
complete native RS232 membership supplied this check.

**Primary assemblies and culture joins.** Native current and historical
GenBank/RefSeq objects support the following source-specific chains:

| Assembly stem | Explicit designation | BioSample | Primary project |
| --- | --- | --- | --- |
| 000215745.1 | KCTC 2190 | SAMN02603581 | PRJNA66537 |
| 050435165.1 | KCTC 2190 | SAMN34299913 | PRJNA958341 |
| 003417445.1 | ATCC 13048 | SAMN09843510 | PRJNA486324 |
| 019048125.1 | FDAARGOS 1442; DSM 30053 supplied by BV-BRC/GOLD | SAMN16357584 | PRJNA231221 |
| 059429655.1 | DSM 30053 | SAMN60994193 | PRJNA1479782 |
| 900635435.1 | NCTC10006; registered NCTC 10006 supplied by BV-BRC/GOLD | SAMEA2548136 | PRJEB6403 |

All are GenBank `GCA_` accessions; the YAML includes the explicitly
joined current `GCF_` counterparts for 000215745, 050435165 and
059429655. RefSeq uses `PRJNA224116`, retained separately from primary
projects. Historical `GCF_003417445.1` and `GCF_900635435.1` are
suppressed and are not added as current evidence. The FDAARGOS NCBI
strain name alone supplies no DSM join; explicit collection fields in
other sources do. Native BV-BRC 1028307.3, 548.355, 548.405 and 548.864
were individually inspected, including all sample/project and culture
fields. BacDive's five genome objects independently supply the
unversioned assemblies, eight IMG/BV-BRC assertions and their reference
IDs 66792, 67770 and 124043.

**GOLD.** All 21 referenced native objects were resolved: thirteen
organisms, four sequencing projects and four analyses. Structured
comparison verified all 67 YAML GOLD assertions against their named
fields, verbatim deposit identifiers and project/organism chains.
The principal chains are Go0011266/Gp0011266/Ga0028581,
Go0482699/Gp0366392/Ga0340892, Go0594508/Gp0608453/Ga0520146 and
Go0669476/Gp0746803/Ga0609673. They support IMG 650716035, 8051016830,
8121873782 and 8113086437 respectively. Empty analysis-level organism
fields do not break these unambiguous project chains. Additional
organisms Go0601172 and Go0601174 through Go0601181 retain their own
collection fields; they are not extra inferred genome assemblies.

**StrainInfo.** Native SI-ID 2190, DOI `10.60712/SI-ID2190.3`, is
published online, references BacDive 4358 and classifies the grouped
strain under species taxid 548. Every one of the 118 YAML assertions
was checked against its native deposit and, where relevant, sequence
object. All 21 matched deposits are available and satisfy the full
collection/accession matcher. The 73 nucleotide assertions represent
72 distinct accessions: AJ300554 has two explicitly named matched
deposits. All sequence descriptions, types, SI-DP identities, DOI,
statuses and deposit designations match the native source.

The three genome assertions are explicitly assigned to KCTC 2190,
ATCC 13048 and NCTC 10006, not propagated from mere group membership.
DQ859778 and DQ859844 explicitly name both ATCC 13048 and ICMP 15660
in the source deposit arrays, explaining why the ATCC join remains
valid despite ICMP wording in their descriptions. The E08572 metadata
inconsistency is retained as a separate minor finding below.

**ATB.** The full native 2025-05 catalog contains processed sample
SAMN16357584, run SRR15076202, analysis ERZ25919795, dataset r0.2,
PASS assembly/HQ filters, the recorded sequence checksum and matching
archive/download identifiers. Both YAML sample links exactly match
the committed overlay and the independent BV-BRC/GOLD sample evidence.
SAMEA2548136 is NOT_PROCESSED in the full catalog and explicitly
excluded as assembly_unavailable. Whole-file, ignored-inclusive
decompressed searches found no occurrences of the other four named
samples. No additional eligible ATB assembly is supported by those
snapshot checks; this is not a claim about live-database absence.

**Attestations and functional scope.** Raw MediaDive row 86 supplies
five media IDs, and Madin row 519 supplies two trait assertions. These
are inventory counts, not five independently reviewed growth results
or two asserted phenotypes. The nomenclature block is empty because
no direct strain-level LPSN name is mapped; a species name should not
be copied down as a separate strain name. The absent optional type
flag does not assert false, despite native type-strain evidence.

The sequence titles include mar genes, soxR, porin and salt-tolerance
terms, triggering the structured iModulonDB check. The installed
`culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets`
runner failed with DNS resolution for the datasets endpoint. Web access
to the API failed, the homepage returned no content, and targeted
searches supplied no usable matching dataset. Coverage is unresolved,
not negative evidence. Source titles are not promoted into mechanism,
resistance, stress-response or transcriptomic conclusions.

## Completeness

The strain listing is uncapped and complete against the current local
BacDive subtree inventory. Registered deposit joins are independently
supported; CDC, NCDC and WDCM source aliases are retained but rejected
as join keys by the collection matcher. SI-ID membership does not
authorize importing every additional deposit into the BacDive list.

Ignored-inclusive identifier/label/slug searches covered `data/raw/`,
`curation/` and `history/`; source tables were additionally parsed in
full for exact strain comparisons. No separate history entry was
found. The configured taxonomy archive was not at its specified path,
and a repository-wide ignored-inclusive filename search found only
taxdump configuration, code, tests and bytecode, not the archive.
The history and archive misses therefore include ignored files.

The live StrainInfo and GTDB pages were inaccessible. E08572 could not
be independently resolved through NCBI or ENA browser/API endpoints.
Other nucleotide accessions were verified against the authoritative
native StrainInfo sequence/deposit objects, not individually re-fetched
from INSDC. These limits remain distinct from the proven GTDB error.

## Findings

Blocker: 0. Major: 1. Minor: 1.

**Major - species-cluster identity and count are inflated onto a strain.**
At YAML lines 44, 55 and 4049, the 794-genome GTDB species becomes an
unqualified strain mapping/count, exact synonym and xref. Native
membership confirms only two entries with taxid 1028307. Being a
representative strain does not make KCTC 2190 equivalent to all members
of Klebsiella aerogenes. This is a scope error, not an invalid strain
identifier or a failure of the explicitly evidenced assembly joins.

Maintained owners: the kg-microbe GTDB mapping transform feeding
`data/raw/gtdb_mappings.tsv:1223`, its extraction in
`src/taxonmech/extract.py:755`, and rank-unaware identity promotion in
`src/taxonmech/seed.py:451` and count projection at line 585. The seeder
currently treats any closeMatch as identity before emitting an exact
alias. Schema validation does not test this biological scope invariant.

**Minor - E08572 sequence type conflicts with its description.**
YAML line 2120 describes an enzyme-encoding DNA accession, but its
evidence at line 2136 categorizes it as `rrnaop`. The complete native
StrainInfo sequence object contains the same combination; the importer
has not invented it. This is an unresolved source-metadata discrepancy,
not proof that the deposit link or accession is wrong. Independent
NCBI/ENA access failed, so the correct replacement category is not
asserted here.

Maintained owner: the StrainInfo source record captured under
`conf/straininfo.yaml`, with faithful projection in
`src/taxonmech/straininfo_links.py:250`. Resolve the source annotation
before any authorized snapshot/overlay regeneration; do not silently
rewrite the generated nested provenance.

## Recommended Edits

1. Make GTDB identity promotion rank/scope-aware in the maintained
   transform and seeder. Remove the species-level exact alias/xref from
   this strain unless an actual same-scope identity claim can be shown.
   Preserve the mapping as a documented broader/cluster-membership
   relationship with direction made explicit. Keep 794 only as a
   clearly qualified cluster count; do not silently redefine it as two.
2. Add a regression using this strain and the parent species as a
   positive control. Prove that explicitly supported strain assemblies
   survive, while cluster membership cannot produce species-as-strain
   equivalence or an unqualified strain genome count. Re-extract and
   canary-reseed only during a separately authorized curation change.
3. Resolve E08572 at its sequence authority and the StrainInfo source.
   Refresh the pinned source only after a supported annotation decision;
   preserve the exact own-deposit link and source DOI/history context.

## Follow-up Checks

Run focused mapping/count regression tests, both record validators and
the full-corpus reproduction check after authorized regeneration.
Recount all 794 GTDB members separately from the two target-taxid
members. Retain exact comparisons for all raw and overlay evidence,
including suppressed RefSeq handling and the two ATB sample chains.

Restore or reacquire the configured taxonomy archive under its pinned
hash before resolving the STRAIN/no-rank source-version difference.
Retry StrainInfo, E08572 and iModulonDB authority access when available;
do not turn an access failure into a negative biological assertion.

## Additional Notes

Only this new review report was manually written. YAML, source code,
inventories, pages, review status and both history surfaces remain
unchanged. The embedded seed event stays SEEDED_FROM_SOURCES and makes
no human-review claim. No paid research, GitHub mutation, bulk
regeneration or source-index rebuild was performed. Validator success
establishes structural validity, not correction of the major scope error.
