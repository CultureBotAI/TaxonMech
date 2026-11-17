# YAML Record Review: Edwardsiella ictaluri ATCC 33202

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/edwardsiella_ictaluri_atcc_33202.yaml`
- Started UTC: 2026-10-03T11:06:50Z
- Finished UTC: 2026-10-03T11:13:36Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027360`, Edwardsiella ictaluri
ATCC 33202, rank STRAIN, domain BACTERIA, parent `NCBITaxon:67780`.
The entire 1,405-line YAML was read in untruncated chunks. It has EXACT
grounding, SEEDED mapping status, one GTDB mapping, five exact synonyms,
one BacDive strain, 14 culture identifiers, 13 assembly assertions,
10 genome-record assertions, 66 related-record assertions, five source
attestations and an embedded seed event. It has no nomenclature object.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/edwardsiella_ictaluri_atcc_33202.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/edwardsiella_ictaluri_atcc_33202.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target entry. Strict validation covered the embedded event. |

Read-only structured checks passed for all ten lineage entries, the full
target subtree and complete BacDive inventory membership. The subtree is
the target alone; BacDive 4356 is its sole inventoried strain. Exact
assertion-multiset comparisons passed for all 13 assemblies, 10 genome
records and 66 related records. All 83 whole-culture-accession provenance
checks and all 36 StrainInfo native assertion checks passed. These checks
establish reproduction and source scope, not GTDB species/strain identity.

## Identity and Grounding

Raw taxonomy row 218793 supplies the target label, parent, STRAIN rank,
code 11 and four NCBI names. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027360)
confirms the identifier, label, code and species lineage. Its live rank
is no rank rather than the snapshot's STRAIN. The native names catalog
classifies CECT 885 and JCM 1680 as generic synonyms and the two expanded
ATCC forms as equivalent names; the live page instead labels the first
two heterotypic synonyms. Exact synonym projection follows the inspected
native categories. Resolving those snapshot/live differences requires
replay of the pinned original taxonomy, not inference from the label.

The NCBI lineage passes through Hafniaceae. Native GTDB metadata use
Enterobacteriaceae. The record correctly retains the NCBI hierarchy
rather than silently reconciling the two source classifications.

ATCC 33202 is the type strain of the parent species, but neither type
status nor representative-genome status makes that strain identical to
the whole species cluster. The GTDB exact species synonym and xref are
the consequential scope defect below.

## Evidence

**GTDB.** An ignored-inclusive decompressed search of all native GTDB
genome shards found 88 members with terminal species
`s__Edwardsiella ictaluri`: 85 have NCBI taxid 67780, two have taxid
634503 and only one has target taxid 1027360. The target member,
RS_GCF_000264785.1, is the representative and names strain ATCC 33202,
GCA_000264785.1, SAMN02469763 and PRJNA224116. The two 634503 members,
RS_GCF_000022885.2 and RS_GCF_041890255.1, both name strain 93-146.
Thus the 88-member cluster demonstrably exceeds this target strain.
Raw GTDB mapping row 1209 supplies the closeMatch and count used in the
YAML. The GTDB web endpoint was inaccessible; the finding rests on the
inspected full native cluster, not a search snippet.

**BacDive and collections.** Raw BacDive row 4251 and the native object
for BacDive 4356 agree on this most-specific taxon, designation GA 77-52,
1976-78, LPSN 775881 and 14 culture identifiers. The native object lists
both strain taxid 1027360 and species taxid 67780. The inspected
[BacDive page](https://bacdive.dsmz.de/strain/4356) confirms the strain,
type status and deposit context. Native record provenance includes DOI
10.13145/bacdive4356.20260601.11; this was inspected as source metadata,
not independently resolved through the DOI service.

Native BacDive reference 67770 links GCA_000264785, IMG 2547132403 and
PATRIC 1027360.4 at taxid 1027360, and GCA_900447225, IMG 2850123092
and PATRIC 67780.22 at taxid 67780. Their unversioned assembly identifiers
are retained as supplied. Sequence references include AY706738 and
AB050826 at the target taxid, plus AB682288 for NBRC 105724 at the species
taxid. The last sequence is not a StrainInfo-owned sequence in the
inspected object and is not evidence of an omitted StrainInfo assertion.

**Assembly and genome chains.** Assertion counts by source are:

| Assertion kind | Source counts |
| --- | --- |
| Assemblies, 13 | GOLD 4; BACDIVE 2; GTDB 2; NCBI 2; STRAININFO 2; BV-BRC 1. |
| Genome records, 10 | BACDIVE 4; GOLD 4; GTDB 1; BV-BRC 1. |
| Related records, 66 | STRAININFO 34; GOLD 24; NCBI 4; GTDB 2; BV-BRC 2. |

The native NCBI assembly catalog verifies the paired GCA/GCF_000264785.1
contig assembly, strain ATCC 33202, SAMN02469763 and the appropriate
GenBank/RefSeq projects PRJNA66365/PRJNA224116. BV-BRC 1027360.4 supplies
the same GenBank assembly/sample/project chain and AFJI00000000.

The NCTC 12122 genome is independently supported by BacDive, GOLD and
StrainInfo. Native NCBI and BV-BRC metadata for GCA_900447225.1 instead
spell the strain `NCTC12122`, with SAMEA4504062, PRJEB6403 and BV-BRC
67780.22. Native GTDB RS_GCF_900447225.1 likewise uses that compact token.
The inspected culture parser recognizes `NCTC 12122` but not `NCTC12122`.
Those catalogs therefore do not supply an additional accepted deposit
join; no fuzzy matching or species-wide link transfer is justified.

Four GOLD organism objects and their available project/analysis objects
were inspected. Go0011936 -> Gp0011936 -> Ga0019897 supports ATCC 33202,
SAMN02469763, PRJNA66365, GCA_000264785.1 and IMG 2547132403.
Go0500230 -> Gp0384430 -> Ga0352930 supports the explicitly spaced NCTC
12122 deposit, SAMEA4504062, PRJEB6403, GCA_900447225.1 and IMG
2850123092. Go0625630 and Go0625632 support JCM 16934 and DSM 13697.
Blank analysis-level organism fields do not sever explicit project
chains. Repeated source-field assertions retain distinct provenance;
they are not counts of distinct biological genomes.

**StrainInfo.** Native object 389450.3, DOI 10.60712/SI-ID389450.3,
was read and all 36 generated assertions matched its own available
deposits and sequences. Its 12 owned deposits are LMG 7860, ATCC 33202,
NCTC 12122, DSM 13697, CCUG 18764, CECT 885, JCM 1680, NCIMB 13272,
KCTC 12264, CGMCC 1.1873, JCM 16934 and CIP 81.96. NBRC 105724 is not
an owned deposit object here; aliases do not create sequence ownership.

The 12 native sequences comprise two assemblies and ten nucleotide
records. ATCC deposit DP42414 owns GCA_000264785, JX185392, AY706738,
EU427506, JX185358 and HQ697334; NCTC DP42417 owns GCA_900447225;
CECT DP133216 owns DQ314205; JCM DP172591 owns AB454422, AB026681,
AB469968 and AB050826. The nucleotide records are correctly outside
genome-record counts. AB026681's native description mentions several
strains; retaining its own-deposit link is not a claim of exclusive
isolate identity or an inferred gene function. All ten direct NCBI
nucleotide-page attempts failed, so current endpoint resolution and
sequence-level identity were not independently confirmed.

**Type status and nomenclature.** The inspected
[LPSN species page](https://lpsn.dsmz.de/species/edwardsiella-ictaluri)
and raw LPSN row 16879 concern parent taxid 67780, not a separately named
strain taxon. They identify ATCC 33202 and its equivalents as type
material and cite the species description, DOI
10.1099/00207713-31-4-396; the original article was not used to support
additional claims. The inspected
[JCM 1680 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1680)
and [JCM 16934 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=16934)
confirm type status, equivalence, collection histories and sequence links.
StrainInfo's JCM 1680 and KCTC 12264 type flags are false, unlike its
other ten deposits; the JCM 1680 disagreement is explicit and is not
propagated into this YAML as a negative type assertion.

**Attestations.** Raw MediaDive row 82 contributes five medium identifiers
(693, 92, J12, J22, J27); Madin row 508 contributes four trait assertions.
The NCBI NAME, BacDive STRAIN, GTDB GENOME, MediaDive MEDIUM and Madin
TRAIT_ASSERTION units remain distinct. Scope row 14823 and the seed event
name those same five sources. GOLD genome links derive from native
objects, whereas the taxon-level GOLD count inventory has a parent-only
row; absence of a child GOLD attestation reproduces that separate input.

## Completeness

The omitted `is_type_strain` slot is not a false assertion. The documented
contract in `docs/HARMONIZATION.md:176`, the schema slot and `seed.py`
derive it from a matching LPSN designation for the same taxon. This child
has no own LPSN nomenclature object; the parent owns the species name.
Expanding ancestral or direct-source type evidence would require an
explicit maintained-model change, not an ad hoc generated-record patch.

Ignored-inclusive searches covered identifiers, label and slug in raw
inventories, curation inputs and history; no target history entry or
earlier report was found. The ATB overlay and complete decompressed
native catalog contain SAMEA4504062 as NOT_PROCESSED, with zero available
FASTA files, and the overlay records `assembly_unavailable`. SAMN02469763
is absent from both searched ATB sources. Neither supports an omitted
eligible ATB assembly. Native BacDive rRNA is not generally imported by
the current link projection; AB682288 is outside the StrainInfo check.

Optional definition, discussion, curator evidence and graph fields are
correctly left empty for this seeded identity/link record. The installed
iModulonDB adapter was unavailable; ignored-inclusive runner discovery
within the inspected Mechs subtree did not locate a usable claw checkout.
The fallback site yielded no inspectable dataset content and a targeted
search yielded no matching result. This is not proof of dataset absence
and supplies no expression-module or phenotype evidence.

## Findings

**Major M1: an 88-genome GTDB species is promoted to exact strain identity.**
The mapping starting at YAML line 40 emits the species name as an
EXACT_SYNONYM and the GTDB species as an identity xref. The full native
cluster includes strain 93-146 and many species-classified genomes;
only one member bears the target strain taxid. Representative/type
status does not justify equating the species and strain. The unqualified
88-GENOME attestation also must not be read as strain-specific coverage.

Maintained owners are the upstream kg-microbe GTDB mapping transform
feeding `data/raw/gtdb_mappings.tsv` and `src/taxonmech/seed.py:438`.
The condition at line 451 treats every closeMatch as identity; xref and
exact-synonym emission follow from line 467. Editing generated YAML alone
would leave the source of the defect intact.

Finding counts: 0 blocker, 1 major, 0 minor. Native/live taxonomy
differences, the documented type-flag boundary and unavailable sequence
endpoints remain explicit limitations, not additional proven defects.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank- and
   scope-aware. Preserve the supported RS_GCF_000264785.1 genome link,
   while preventing a species cluster from becoming an exact synonym or
   identity xref on this narrower strain merely because of closeMatch.
2. Correct the maintained upstream GTDB mapping semantics and retain
   species-cluster counts with explicit scope. Add this target and its
   88-member cluster as a regression fixture, with a valid species-level
   mapping as a positive control.
3. Resolve taxonomy rank/name-class differences against the hash-verified
   pinned NCBI source before proposing separate inventory corrections.

## Follow-up Checks

1. Confirm the strain loses the unsupported exact species identity while
   its valid genome/deposit chains and NCBI names remain unchanged.
2. Run the documented dry-run/canary generation workflow after maintained
   fixes, both focused validators and then `just verify-corpus`. Schema
   success alone cannot establish the semantic correction.
3. Retry the ten nucleotide endpoints if current accession resolution or
   sequence identity is needed; native source provenance alone does not
   replace sequence-level validation. Preserve the JCM/StrainInfo type
   disagreement if a future model imports those boolean assertions.

## Additional Notes

Only this new report was manually written. No record, source inventory,
scope, review status or history event was changed. Strict validation
emitted its normal diagnostic TSV. No paid research or GitHub mutation
was used. Parent-species projections and catalog context do not constitute
a separate review of the entire parent record. Eukaryota was untouched.
