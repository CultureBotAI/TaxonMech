# YAML Record Review: Sporosarcina newyorkensis 2681

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sporosarcina_newyorkensis_2681.yaml`
- Started UTC: 2026-10-03T11:04:19Z
- Finished UTC: 2026-10-03T11:05:49Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1027292`, Sporosarcina newyorkensis
2681, rank STRAIN, domain BACTERIA, parent species `NCBITaxon:759851`.
The entire 87-line YAML was read before judgment. It has EXACT grounding,
SEEDED mapping status, one GTDB mapping, four exact synonyms, a GTDB xref,
zero listed BacDive strains, three source attestations and a seed event.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/sporosarcina_newyorkensis_2681.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/sporosarcina_newyorkensis_2681.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target entry. Strict validation covered the embedded event. |

Read-only structured checks verified all ten lineage entries against the
complete pinned taxonomy table. Full subtree traversal found no descendant
taxon, and the complete BacDive inventory contained no strain classified
within this target subtree. Schema success does not resolve the semantic
scope error below.

## Identity and Grounding

Raw taxonomy row 218792 supplies the target label, parent, STRAIN rank,
code 11 and three NCBI synonyms. The inspected
[NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027292)
confirms the ID, label, parent-species lineage, code and the two equivalent
2681 name variants. However, the live browser says no rank, while the
committed snapshot says STRAIN. The configured original archive was not
available under `data/`, so this review cannot distinguish temporal change
from an inventory discrepancy. No rank is inferred from the strain name.

The native names catalog marks the two expanded 2681 forms as equivalent
names and Sporosarcina sp. 2681 as a generic synonym. Their exact placement
reproduces `src/taxonmech/ncbi_taxdump.py:90`. The live browser instead
labels the last name a heterotypic synonym. This difference is preserved
as a snapshot-versus-live uncertainty, not silently overwritten or counted
as a proven importer defect.

The GTDB species-level name does not denote strain 2681 alone. Promoting
it to the same exact-synonym category loses that essential distinction.

## Evidence

**GTDB cluster membership.** An ignored-inclusive decompressed search of
all native `data/catalog/gtdb_genomes-*.jsonl.gz` shards found seven rows
with the exact terminal species `s__Sporosarcina newyorkensis`:

| Genome accession | NCBI taxid | Native strain identifiers |
| --- | --- | --- |
| RS_GCF_000220335.1 | 1027292 | 2681 |
| GB_GCA_040689655.1 | 1296 | SG_MMG_SSB-3 |
| RS_GCF_038003105.1 | 2921560 | FSL W7-1283 |
| RS_GCF_038615825.1 | 2921557 | FSL K6-3508 |
| RS_GCF_019748715.1 | 114975 | S;N-308-OC-B4 |
| RS_GCF_900167515.1 | 759851 | DSM 23966 |
| RS_GCF_050277375.1 | 759851 | NPDC101421 |

Only the first row has target taxid 1027292. The representative is
RS_GCF_019748715.1, whose NCBI name is Sporosarcina aquimarina. The
GB_GCA_040689655.1 row has the NCBI name Mammaliicoccus sciuri. These
source classification differences are retained, not reconciled here.
They independently disprove an exact identity between the entire GTDB
species cluster and this single strain taxon.

Raw GTDB mapping row 1208 nevertheless assigns this target a closeMatch
and seven genomes. Row 306319 separately maps the same GTDB species to
the actual NCBI parent species. Seven is a reproducible cluster size, not
evidence for seven genomes belonging to strain 2681. The attempted GTDB
web page was inaccessible; native metadata support this finding.

**BacDive classification and genome context.** Raw BacDive row 11846 and
the exact native object for BacDive 12002 classify designation 2681 at
species taxid 759851, not at this child taxid. The inspected
[BacDive page](https://bacdive.dsmz.de/strain/12002) supports deposits DSM
23540, CCUG 59651 and LMG 26024. Native reference 66792 explicitly links
GCA_000220335, IMG 2512047070 and PATRIC 759851.3 to a genome bearing
taxid 1027292. Reference 17268 supplies the strain's GU994081 sequence.

A structured projection of the parent record confirms that BacDive 12002
and those three genome identifiers are already retained there with the
child genome taxid and original source provenance. This is parent-record
context, not an independent review of that entire record. A sequence's
taxon ID does not change the source strain object's classification, and
bare 2681 is not a culture-deposit join key.

**Species nomenclature.** Raw LPSN row 26717 and the inspected
[LPSN species page](https://lpsn.dsmz.de/species/sporosarcina-newyorkensis)
concern taxid 759851 and identify type strain 6062, DSM 23544, CCUG 59649
and LMG 26022. Those are not 2681's deposits. The native BacDive 12002
object explicitly has type strain set to no. No parent nomenclature or
type-strain designation should be copied onto this child solely because
the species names match. The target YAML itself cites no DOI or PMID.

**Attestations and history.** Raw Madin row 507 supplies one trait
assertion. NCBI contributes one NAME, and the GTDB row contributes the
seven-genome cluster count discussed above. These units remain distinct.
Scope row 36094 and the seed event consistently name GTDB, MADIN and
NCBITAXON. The Madin count alone is not a phenotype assertion.

## Completeness

The zero strain count is supported by full inventory/subtree inspection;
it is not proof that this biological strain has no known genome. The
parent record preserves the source-classified BacDive entry and its links.
No additional ATB or StrainInfo object is asserted by the target YAML,
and no unsupported transfer of parent associations is recommended.

Ignored-inclusive searches covered target identifier, label and slug in
raw inventories, curation inputs and history. There was no target history
entry. An ignored-inclusive filename search found no earlier report for
this stem. A separate ignored-inclusive filename search throughout `data/`
found neither a taxdump archive nor `nodes.dmp`; configuration pins
`data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`.

Empty optional definition, discussion, curator evidence and graph fields
are appropriate. iModulonDB was not applicable: the record has no gene,
regulator, pathway or expression-module claim.

## Findings

**Major M1: GTDB species identity is promoted onto an individual strain.**
The mapping at YAML line 43 is used to emit an EXACT_SYNONYM at line 46
and an identity xref at line 60, despite the seven-member, six-taxid native
cluster above. That representation conflates the species with strain
2681. The scope problem also makes the unqualified cluster-sized GENOME
attestation unsafe to interpret as strain-specific coverage.

Maintained owners: the upstream kg-microbe GTDB mapping transform feeding
`data/raw/gtdb_mappings.tsv`, and the rank-agnostic identity-promotion block
in `src/taxonmech/seed.py:438`. Its condition at line 451 treats every
closeMatch as identity, then emits the xref and exact synonym from line 467.
A generated YAML edit would not fix either owner.

Finding counts: 0 blocker, 1 major, 0 minor. The live rank/name-class
differences remain bounded follow-up questions, separate from M1.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank- and
   scope-aware. A species cluster must not become an exact name or identity
   xref on a narrower strain taxon merely because its raw predicate is
   closeMatch. Preserve supported cluster membership as non-equivalent
   context under the repository's mapping contract.
2. Correct the upstream mapping semantics feeding the raw GTDB inventory;
   retain the native cluster count as explicitly cluster-scoped evidence,
   not an invented strain-specific genome total. Add a regression fixture
   using this target and its wider seven-member cluster.
3. Resolve the rank/name-class snapshot questions from the hash-verified
   pinned taxdump before considering any separate NCBI inventory change.

## Follow-up Checks

1. Test that strain 2681 retains its supported NCBI names and lineage but
   receives no exact species synonym or species-identity xref. Verify that
   valid species-level mappings still retain their intended behavior.
2. Use the documented dry-run/canary workflow after maintained fixes, then
   rerun both focused validators and `just verify-corpus`. Green schema
   validation alone cannot prove the scope correction.
3. Compare the pinned `nodes.dmp` and `names.dmp` assertions to the current
   browser. The importer uppercases native ranks rather than inferring
   STRAIN; report a projection defect only if replay establishes one.

## Additional Notes

Only this new report was manually written. No YAML, source inventory,
scope, status or history event was changed. The strict validator emitted
its normal diagnostic TSV. No GitHub mutation or paid research was used.
Eukaryota was outside the review target.
