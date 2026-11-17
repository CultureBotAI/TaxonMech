# YAML Record Review: Enterococcus faecalis OG1X

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_faecalis_og1x.yaml`
- Started UTC: 2026-10-03T11:24:22Z
- Finished UTC: 2026-10-03T11:25:33Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027372`, Enterococcus faecalis
OG1X, rank STRAIN, domain BACTERIA, parent `NCBITaxon:1351`. The entire
84-line YAML was read. It has EXACT grounding, SEEDED mapping status,
one GTDB mapping, three exact synonyms, one GTDB xref, zero listed
BacDive strains, three source attestations and an embedded seed event.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/enterococcus_faecalis_og1x.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/enterococcus_faecalis_og1x.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive target identifier, label and slug searches found no target entry in `history/`. Strict validation covered the embedded event. |

All ten lineage entries matched the complete pinned taxonomy table.
Full subtree traversal found only the target; complete BacDive inventory
inspection found no strain classified within that subtree. These checks
support the zero strain count, not the GTDB equivalence claim.

## Identity and Grounding

Raw taxonomy row 218796 supplies the target identifier, label, parent,
STRAIN rank, code 11 and two NCBI equivalent names. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027372)
confirms the identifier, label, code, equivalent name forms and lineage
through Enterococcaceae and Enterococcus faecalis. The web tool returned
an older cached page whose rank is no rank, unlike the committed snapshot's
STRAIN. This is not sufficient to prove a current projection defect.
Original-source replay is unavailable because an ignored-inclusive
filename search under `data/` found neither the pinned taxdump archive
nor `nodes.dmp`.

Native NCBI name shards contain the scientific name and the two expanded
OG1X forms as equivalent names. Their exact-synonym placement follows
the native categories and importer contract. The GTDB species name is a
different scope: it denotes thousands of genomes, not OG1X alone.

## Evidence

**Full GTDB cluster.** Ignored-inclusive decompressed search across all
native GTDB genome shards, followed by exact terminal-species filtering,
found 5,041 members of `s__Enterococcus faecalis` across 615 NCBI taxids.
Of those, 4,384 bear species taxid 1351, one bears target taxid 1027372,
and 656 bear other taxids. The representative is
RS_GCF_029024925.1, DSM 20478 at taxid 1351, not OG1X.

The sole target-taxid member, RS_GCF_000320305.1, explicitly names OG1X,
GCA_000320305.1, SAMN02471974 and PRJNA224116. Raw mapping row 1212
supplies the closeMatch and 5,041 count used in this record. The count
reproduces the native species cluster; it cannot establish thousands of
OG1X genomes or species/strain identity. The GTDB web endpoint was
inaccessible, but the complete native census supports this conclusion.

**Genome context without a deposit join.** Current native GenBank and
RefSeq objects retain paired GCA/GCF_000320305.1, contig assembly
ASM32030v1, `strain=OG1X`, taxid 1027372, species taxid 1351 and sample
SAMN02471974. Their projects are PRJNA66377 and PRJNA224116 respectively;
both retain AFHH00000000.1. They cite PMID 23104812, but the PubMed
request returned a browser challenge. No uninspected publication text
is used for the verdict.

Native GOLD Go0011940 names OG1X at this taxid with an empty culture
collection field. Gp0011940 explicitly names that organism and supplies
PRJNA66377 and SAMN02471974. Ga0015268 names the project and supplies
GCA_000320305.1, AFHH00000000 and IMG 2534681818. Its empty organism
field does not contradict the explicit project relationship.

These native objects retain source-specific genome context. Bare OG1X
is not a registered culture-deposit accession, however, and the target
has no listed BacDive strain. Ignored-inclusive searches of all three
raw strain-link inventories found no target-ID, OG1X, assembly, sample
or Go0011940 assertion. That is consistent with the maintained join
boundary, not evidence that the strain lacks a genome. The raw GOLD
taxon-count inventory also has no target row; that KGX-derived count is
separate from the native GOLD organism/project chain.

**Type-strain linkout boundary.** The NCBI page offers a linkout to
BacDive 5292, but raw row 5183 and the inspected native BacDive identity
object classify Tissier under sibling strain taxid 1169286 and parent
species 1351. Its deposits include ATCC 19433 and DSM 20478, not OG1X.
The linkout does not authorize importing that strain's deposits or genomes
onto this target.

Raw LPSN row 16930 and the inspected
[LPSN species page](https://lpsn.dsmz.de/species/enterococcus-faecalis)
concern parent species 1351, name 775964, and identify ATCC 19433,
DSM 20478 and their equivalents as type material. The species name and
its type strain must not be copied onto OG1X as strain-specific
nomenclature or identity. The target itself cites no publication, gene
accession, curator evidence snippet or causal mechanism.

**Attestations and audit.** Raw Madin row 511 supplies three trait
assertions; NCBI contributes one NAME. GTDB contributes the species-sized
GENOME count discussed above. Scope row 36096 and the embedded seed
event name the same three sources, GTDB, MADIN and NCBITAXON. These
units are not summed or promoted to experimental phenotype claims.

## Completeness

The zero-strain listing is supported by complete inventory and subtree
inspection. The native catalogs retain the known genome; the present
record model does not permit assigning arbitrary source genomes through
shared taxonomy or a bare strain name. The target has no supported
listed-strain BioSample assertion from which an ATB link could be
derived. No transfer of species-type or StrainInfo associations is
recommended based on web linkouts alone.

Ignored-inclusive searches covered identifier, label and slug in
`data/raw/`, `curation/` and `history/`. No history entry or earlier
report for this stem was found. A separate ignored-inclusive filename
search throughout `data/` found no original taxdump archive or `nodes.dmp`;
the configured 2026-09-13 snapshot cannot be replayed locally as inspected.

Empty optional definition, discussion, curator evidence and graph slots
are appropriate. iModulonDB was not applicable: the target record names
no gene, regulator, pathway or expression-module assertion. Publication
metadata in external genome context do not add such a claim to the YAML.

## Findings

**Major M1: a GTDB species is presented as exact identity for strain OG1X.**
The species-level closeMatch becomes an EXACT_SYNONYM and an equivalence
xref despite the 5,041-member, 615-taxid cluster. Only one member has
the target taxid. The unqualified GENOME attestation must not be read
as strain-specific coverage either.

Maintained owners: the upstream kg-microbe GTDB mapping transform feeding
`data/raw/gtdb_mappings.tsv`, and `src/taxonmech/seed.py:438`. Its identity
condition at line 451 accepts every closeMatch without a rank/scope
guard; xref and exact-synonym emission follow from line 467. Editing the
generated YAML alone would not correct those owners.

Finding counts: 0 blocker, 1 major, 0 minor. Cached-page rank disagreement
and inaccessible publication text remain bounded uncertainties, not
additional demonstrated defects.

## Recommended Edits

1. Make GTDB identity promotion rank- and scope-aware in the maintained
   seeder, so species-cluster membership does not become exact identity
   on this narrower strain record.
2. Correct upstream mapping semantics and retain the cluster count with
   explicit species scope. Add OG1X and this large cluster as a regression
   fixture, with a valid species-level mapping as a positive control.
3. Resolve the rank difference through hash-verified pinned-taxdump replay
   before proposing a separate taxonomy inventory correction. Do not infer
   a culture accession or copy the type-strain linkout into this record.

## Follow-up Checks

1. Verify that OG1X retains its supported NCBI identity, equivalent names
   and lineage while losing unsupported exact species equivalence.
2. After maintained fixes, use the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Confirm native genome
   metadata remain available without an unsupported deposit join.
3. Retry PMID 23104812 only if literature-backed characterization is
   needed. Its uninspected text was not required for the scope finding.

## Additional Notes

Only this new report was manually written. No YAML, source inventory,
scope, status or history event changed. Strict validation emitted its
normal diagnostic TSV. No paid research or GitHub mutation was performed.
The species/type-strain context is not a separate record review.
Eukaryota was untouched.
