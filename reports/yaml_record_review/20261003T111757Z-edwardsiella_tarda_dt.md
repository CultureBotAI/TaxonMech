# YAML Record Review: Edwardsiella tarda DT

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/edwardsiella_tarda_dt.yaml`
- Started UTC: 2026-10-03T11:15:51Z
- Finished UTC: 2026-10-03T11:17:57Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027364`, Edwardsiella tarda DT,
rank STRAIN, domain BACTERIA, parent `NCBITaxon:636`. The entire 84-line
YAML was read. It has EXACT grounding, SEEDED mapping status, one GTDB
mapping, three exact synonyms, one GTDB xref, zero listed BacDive strains,
three source attestations and an embedded seed event.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/edwardsiella_tarda_dt.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/edwardsiella_tarda_dt.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target entry. Strict validation covered the embedded event. |

All ten lineage entries matched the complete pinned taxonomy inventory.
Full subtree traversal found only this target, and a complete BacDive
inventory scan found no strain classified within that subtree. Validation
success does not establish the GTDB mapping's biological scope.

## Identity and Grounding

Raw taxonomy row 218794 supports the ID, label, parent, STRAIN rank,
code 11, two NCBI names and three source labels. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027364&mode=Info)
confirms the identifier, name, parent-species lineage, code and equivalent
DT name forms. Its live rank is no rank rather than the snapshot's STRAIN.
That disagreement remains unresolved: the configured original taxdump
archive was not found under `data/` by an ignored-inclusive filename search.
The review does not infer a rank from the strain-like name.

Native NCBI name shards contain the scientific name and two equivalent
names, exactly the two NCBI synonyms in the YAML. Their EXACT_SYNONYM
classification agrees with `src/taxonmech/ncbi_taxdump.py:90`. The GTDB
species synonym is different: it denotes a larger cluster, not DT alone.
The NCBI Hafniaceae lineage is retained even though native GTDB places
the genomes in Enterobacteriaceae; the repository does not merge trees.

## Evidence

**GTDB cluster.** All native GTDB genome shards were searched with ignored
files included and decompression enabled; structured filtering required
the exact terminal species `s__Edwardsiella tarda`. The 74 members have
five NCBI taxids:

| NCBI taxid | Members | Relevant native scope |
| --- | --- | --- |
| 636 | 68 | Edwardsiella tarda species-classified genomes. |
| 667121 | 3 | ATCC 15947 / NBRC 105688. |
| 1027364 | 1 | DT, RS_GCF_000264825.1. |
| 3318355 | 1 | Edwardsiella sp. A.80236, RS_GCF_044540725.1. |
| 500638 | 1 | ATCC 23685, RS_GCF_000163955.1. |

The representative is RS_GCF_003113495.2, strain ATCC 15947, not DT.
The other two 667121 members are RS_GCF_000264805.1 and
RS_GCF_000341505.1. Raw mapping row 1210 assigns the whole cluster to DT
as closeMatch; other rows map it to those sibling taxa and the parent
species. Seventy-four is the reproduced cluster size, not a strain-DT
genome count. The GTDB web endpoint was inaccessible, so the finding
rests on complete inspected native metadata.

**DT genome context.** Native GTDB RS_GCF_000264825.1 explicitly names DT,
taxid 1027364, GCA_000264825.1, SAMN02469760 and PRJNA224116. The native
current GenBank and RefSeq catalogs independently retain paired
GCA/GCF_000264825.1, contig assembly ASM26482v1, `strain=DT`, that sample,
and projects PRJNA66369/PRJNA224116 respectively. Both record AFJJ00000000.1
and PMID 22590641. The PubMed request returned a browser challenge;
no claims from the uninspected paper are used here.

Native GOLD Go0011937 names DT at this taxid but has an empty culture
collection field. Gp0011937 explicitly connects that organism to
SAMN02469760 and PRJNA66369; Ga0019896 names that project, GCA_000264825.1,
AFJJ00000000 and IMG 2547132402. These are genuine retained source chains,
but bare DT supplies no registered culture-deposit accession. An
ignored-inclusive search of all three raw strain-link inventories found
no target-ID, assembly, sample or Go0011937 assertion. This matches the
documented join boundary rather than proving the biological strain lacks
a genome. The raw GOLD taxon-count table likewise has no target row;
its KGX-derived attestations and native GOLD genome context are separate
inputs.

**BacDive and nomenclature boundaries.** Raw BacDive row 4250 and native
object 4355 classify the type strain under sibling taxid 667121, with
species taxid 636 also listed. The inspected
[BacDive page](https://bacdive.dsmz.de/strain/4355) identifies K 349,
K349, 4-78, 1483-59 and deposits including ATCC 15947 and NBRC 105688.
Neither its native classification nor its genome assertions establish a
DT deposit relationship. Its contents cannot be transferred merely
because a taxonomy search result offers a type-strain linkout.

Raw LPSN row 16880 and the inspected
[LPSN species page](https://lpsn.dsmz.de/species/edwardsiella-tarda)
concern parent species 636, name 775882, and identify ATCC 15947 and its
equivalents as the type strain. This is not a separate nomenclatural
name for DT. Omitting parent nomenclature and type-deposit assertions
from this strain record is appropriate. The target itself cites no DOI,
PMID, gene accession, curator snippet or experimental claim.

**Attestations and audit.** Madin row 509 supplies five trait assertions;
the NCBI attestation counts one NAME. The GTDB attestation reproduces
the 74-GENOME species count discussed above. These counts cannot be summed
or treated as direct phenotype evidence. Scope row 36095 and the seed
event consistently name GTDB, MADIN and NCBITAXON.

## Completeness

Zero strains is supported by full inventory/subtree inspection. The native
genome catalogs preserve DT context, but the present strain-link model
does not authorize new links based on a shared name or taxon alone.
No unsupported transfer of type-strain, StrainInfo or ATB associations is
recommended. The target has no source-backed sample assertion on a
listed strain from which an ATB join could be derived.

Ignored-inclusive searches covered identifiers, label and slug in
`data/raw/`, `curation/` and `history/`; there was no history entry.
Ignored-inclusive report filename enumeration found no prior review for
this stem. A separate filename search throughout `data/` found neither
a taxdump archive nor `nodes.dmp`; `conf/ncbi_taxdump.yaml` pins the
2026-09-13 archive and its SHA-256. Snapshot replay remains unavailable.

Optional definition, discussion, curator evidence and graph slots can
remain empty. iModulonDB was not applicable: this record makes no gene,
regulator, pathway or expression-module assertion.

## Findings

**Major M1: GTDB species identity is promoted onto strain DT.** The
74-member, five-taxid cluster becomes an EXACT_SYNONYM and an equivalence
xref on this narrower strain record. Only one native member has the
target taxid. The unqualified species-sized GENOME attestation must not
be interpreted as strain-specific coverage either.

Maintained owners: the upstream kg-microbe GTDB mapping transform feeding
`data/raw/gtdb_mappings.tsv` and the rank-agnostic identity-promotion block
in `src/taxonmech/seed.py:438`. Its condition at line 451 accepts every
closeMatch as identity; xref and exact-synonym emission follow from line
467. A generated YAML patch would not address those owners.

Finding counts: 0 blocker, 1 major, 0 minor. The native/live rank
disagreement and inaccessible paper remain bounded uncertainties, not
additional demonstrated import defects.

## Recommended Edits

1. Make GTDB identity promotion rank- and scope-aware in
   `src/taxonmech/seed.py`. Preserve species-cluster context without
   claiming that a single strain is equivalent to the species.
2. Correct upstream mapping semantics and keep cluster counts explicitly
   species-scoped. Add DT and the 74-member cluster as a regression
   fixture, alongside a valid species-level identity mapping.
3. Resolve the rank discrepancy against the hash-verified pinned taxdump
   before proposing any independent NCBI inventory correction. Do not
   infer culture deposits or import sibling-type associations.

## Follow-up Checks

1. Verify that DT keeps its valid NCBI identity, names and lineage but no
   longer receives an exact species synonym or species-identity xref.
2. After maintained fixes, run the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Confirm that native
   genome context is retained and no unsupported deposit join appears.
3. Inspect pinned `nodes.dmp` if made available. Retry PMID 22590641 only
   if literature-backed characterization is needed; its metadata citation
   was not used as evidence for the current verdict.

## Additional Notes

Only this new report was manually written. No YAML, source inventory,
scope, status or history event changed. Strict validation emitted its
normal diagnostic TSV. No paid research or GitHub mutation was performed.
The type-strain and parent-species context is not a separate record review.
Eukaryota was outside this target.
