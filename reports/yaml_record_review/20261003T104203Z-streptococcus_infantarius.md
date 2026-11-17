# YAML Record Review: Streptococcus infantarius

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_infantarius.yaml`
- Started UTC: 2026-10-03T10:34:34Z
- Finished UTC: 2026-10-03T10:42:03Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:102684`, Streptococcus infantarius,
rank `SPECIES`, domain `BACTERIA`. The complete 4,508-line YAML was read before
judgment. It has `grounding_status: EXACT`, `mapping_status: SEEDED`, 21
strain entries and an embedded seed event, not a human review event.

Scope is this record only. Neither its species identity nor its strain-level
source assertions were edited. Findings distinguish faithful source imports
from unresolved biological classification.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/streptococcus_infantarius.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/streptococcus_infantarius.yaml` | PASS; one file, zero files with ERROR, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: documented full-corpus regeneration comparison, not a focused record validator. Inventory comparisons below are not a substitute for this gate. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs in this record. |
| `just validate-history` | Not run: ignored-inclusive search of `history/` for identifier, label and slug found no target history entry. The embedded event was covered by strict validation. |

Additional read-only diagnostics:

- Full pinned taxonomy table: identity, parent, genetic code, nine ancestor
  labels/ranks and parent chain agree. The six-taxon subtree was enumerated;
  its BacDive membership is exactly the 21 retained strain IDs.
- Per-strain assertion multisets agree exactly with the raw/overlay tables:
  24 raw plus two StrainInfo assembly assertions, 24 raw non-ATB genome
  assertions, and 122 raw plus 116 StrainInfo related-record assertions.
- All 118 StrainInfo assertions resolve in 20 native strain objects. Deposit
  designation/status/taxon, strain version DOI/status and BacDive reference
  match. Each sequence assertion has the accession on that same deposit.
- All 276 assertions with `matched_strain_id` point to an existing deposit
  of their own strain and pass the repository CAFI culture-key recognition.
  StrainInfo deposit normalization agrees with each matched identifier.
- GTDB native cluster recounts reproduce 67, 119 and 21 genomes.
- Tracked-file diff was empty at report creation. No source, YAML, history,
  mapping status or GitHub state was changed.

These diagnostics check structured provenance; they do not validate sequence
content, experimentally establish deposit equivalence, or resolve taxonomy.

## Identity and Grounding

The species, parent `NCBITaxon:1301`, Bacteria lineage and genetic code 11
agree with `data/raw/ncbitaxon_taxa.tsv`. The lineage includes Bacillati,
Bacillota, Bacilli, Lactobacillales and Streptococcaceae. The accessible
[NCBI taxonomy tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=102684)
supports species placement; alternate detailed-browser fetches failed.
The pinned inventory remains the basis for the exact rank/code comparison.

[LPSN species 784982](https://lpsn.dsmz.de/species/streptococcus-infantarius)
supports the current name, Schlegel et al. 2000 authority and the four
structured type designations ATCC BAA-102, CCUG 43820, CIP 103233 and DSM
22960. Additional textual designations on the authority page are represented
among the BacDive culture identifiers; this is not a missing-type finding.

LPSN 784984 is a subspecies, not a second species-level exact identity.
The YAML retains it only as a sourced `RELATED_SYNONYM` and does not add it
as a species xref. The current
[subspecies page](https://lpsn.dsmz.de/subspecies/streptococcus-infantarius-infantarius)
identifies the parent/basonym relationship. The generic related-name
representation loses detail but does not assert rank equivalence.

The primary GTDB name and LPSN species xrefs are supported. All three GTDB
mappings remain `skos:broadMatch`; the two pooled clusters are explicitly
described as pooled and are not promoted into species synonyms or xrefs.
`EXACT` describes the NCBI grounding, not consensus across every strain's
source classification.

## Evidence

**Taxonomy and nomenclature.** The raw NCBI, LPSN and GTDB rows were inspected.
The six-taxon subtree comprises this species, subspecies 150054 and strains
471872, 1069533, 1255580 and 1255600. BacDive 14832 is the one strain filed
under a descendant, 471872; its `classified_as` is therefore appropriate.
The remaining source identities are filed directly under 102684.

The publisher's
[2000 description](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-50-4-1425)
supports the original species proposal and HDP 90056/NCDO 599 type linkage.
The [notification-list page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-50-5-1701)
resolves the second DOI. Direct DOI resolver requests failed, but these
publisher pages were inspected. PMID 10939646 returned a browser challenge,
so its current PubMed bibliographic record was not independently verified.
No claim is made to have inspected the full article PDF.

[NCBI AF429762.1](https://www.ncbi.nlm.nih.gov/nuccore/AF429762) identifies the
partial 16S sequence for the type-strain lineage. The YAML preserves the
source's unversioned accession rather than inventing a version.

**GTDB.** All compressed native GTDB shards were searched and exact terminal
species names counted, rather than counting text matches:

| Cluster | Total genomes | With NCBI species taxid 102684 |
| --- | ---: | ---: |
| Streptococcus infantarius | 67 | 54 |
| Streptococcus lutetiensis | 119 | 2 |
| Streptococcus ruminicola | 21 | 1 |

The YAML uses cluster totals, not the last column. Native representative
`RS_GCF_000154985.1` matches ATCC BAA-102 and the infantarius cluster.
`GB_GCA_040543605.1` matches DSM 22957, carries NCBI species 102684, but is
classified in the lutetiensis cluster. The live GTDB taxon page could not
be retrieved; native snapshot metadata supports these bounded checks.

**BacDive and genome provenance.** All 21 exact native BacDive objects were
inspected, including their taxonomy, culture identifiers and sequence fields.
No culture list was inferred from a shared species name. The three strains
with assemblies are:

| BacDive ID | Assembly assertions | Genome assertions | Related assertions |
| --- | ---: | ---: | ---: |
| 14832 | 14 | 14 | 71 |
| 14833 | 9 | 10 | 64 |
| 137714 | 3 | 2 | 23 |
| Remaining 18 entries combined | 0 | 0 | 80 |
| Total | 26 | 26 | 238 |

These are assertion counts, not unique-genome counts. Distinct source fields
and versioned/unversioned accessions are deliberately retained.

The seven referenced BV-BRC objects and three referenced NCBI assembly
objects were found in native compressed catalogs. Their assembly, culture,
BioSample, BioProject and taxon fields support the retained joins. In
particular, BV-BRC 102684.84 has no assembly accession, so its genome record
is not an invented assembly. NCBI GCA_040543605.1 also records exclusion from
RefSeq for an unverified source organism; retaining its supplied accession
does not establish the species assignment.

All referenced GOLD entity objects were inspected: 35 organisms, four
projects and four analyses. Analysis-to-project-to-organism chains resolve;
the ten additional IMG/BioSample/BioProject identifiers in those assertions
are supported fields, not missing GOLD entity objects. Native GOLD has 92
organism objects directly assigned to 102684, whereas the transformed
attestation inventory contains 106; see finding M2.

**Classification conflicts.** These are present in the source data and
must not be silently resolved by deleting supported links:

- BacDive 14833 names the coli subspecies and files it under 102684.
  Its DSM 22957/FDAARGOS_1018 assembly and multiple StrainInfo deposits carry
  150055, S. lutetiensis. Its other assembly GCA_040543605.1 carries NCBI
  102684 while GTDB assigns the lutetiensis cluster.
- The current [LPSN coli page](https://lpsn.dsmz.de/subspecies/streptococcus-infantarius-coli)
  and [LPSN lutetiensis page](https://lpsn.dsmz.de/species/streptococcus-lutetiensis)
  preserve historical nomenclatural complications. The latter explicitly
  discusses HDP 90246/CCUG 47831/NCIMB 700964. These observations do not make
  BacDive 14833 the type of the parent species reviewed here.
- [BacDive 137714](https://bacdive.dsmz.de/strain/137714) groups CIP 106106,
  CCUG 4214 and NCTC 8133 under infantarius, but its genome section names
  S. equinus and taxid 1335 for GCA_901543475. Native BV-BRC 53354.15 names
  S. gallolyticus subsp. gallolyticus. StrainInfo likewise preserves different
  deposit taxa. The YAML retains these source taxa rather than rewriting them.
- Several other coli-associated CCUG deposits have StrainInfo taxid 150055;
  some older collection deposits have taxid 1335. The species container is
  therefore a source-based grouping, not proof that all deposits have a
  harmonized contemporary classification.

**StrainInfo.** Native groups 8005, 8012, 8013, 9430, 57524, 57527, 57531,
57538, 57543, 57546, 61185, 70326, 94689, 94690, 108688, 108884, 110566,
111080, 411274 and 411722 support the retained assertions. The two assemblies
are specifically attached to ATCC deposit 118958 and NCTC deposit 145276.
The nucleotide references remain typed related records, not genomes.

Group 8005 refers to BacDive 136477 but also contains deposits used by
BacDive 151351. The four assertions under 151351 correctly preserve
`bacdive_reference_conflict: true`. No extra LMG or other deposit was imported
merely because it appears in the same StrainInfo group.

**AllTheBacteria.** Local assembly, strain-link and genome-link inventories
support two eligible sample-derived genome records:

- SAMN16357188, SRR12825932, ERZ25831315, linked through DSM 22960 evidence
  in BV-BRC 102684.41 and GOLD Gp0550453.
- SAMN16357187, SRR12825931, ERZ25831308, linked through DSM 22957 evidence
  in BV-BRC 150055.112 and GOLD Gp0550452.

Both retain PASS metadata/assembly filters, native SeqKit and download
metadata, and exact sample evidence. Their genome crosslinks follow matching
sample/genome provenance, not a Cartesian product of identifiers on a strain.
SAMN00000017 and SAMEA3632067 are explicitly `assembly_unavailable` in the
local exclusions and NOT_PROCESSED in the assembly inventory, so they are
correctly absent from ATB genome records. The full catalog XZ was not replayed.

**Other attestations.** Raw inventories reproduce MediaDive 3 media, Madin 5
trait assertions and BactoTraits 1 trait assertion. They are direct-taxon
source counts, not phenotypes or totals to sum across sources. The BacDive
count is 21 strains including one descendant-classified strain. The seed
event names the same eight attesting sources.

## Completeness

All 21 strain identities are retained; there is no capped-list discrepancy.
All raw/overlay assembly, non-ATB genome and related-record assertion sets
match, with the two ATB records separately supported as above.

Definition, causal graph and record-level evidence are optional for this
seeded record. Their absence is not a finding. Marker-gene accessions are
identity/provenance references, not transcriptomic or mechanism claims;
iModulonDB was not applicable and no expression evidence was inferred.

Ignored files were included in searches of report filenames, `history/`,
the native compressed catalogs and relevant raw/overlay inventories. No
previous exact-stem report or target history entry was found in those
locations. This is not a claim about unseen external curation systems.

Current authority verification is incomplete for PubMed, live GTDB and
individual collection/sequence pages beyond the inspected examples. Local
source-backed provenance is verified more broadly than current web identity.

## Findings

Counts: 0 blocker, 0 major, 2 minor.

1. **M1 - Minor: classification disagreements need an explicit summary.**
   The raw source identities are preserved, but the YAML has no discussion
   explaining the infantarius/coli/lutetiensis and NCTC 8133 disagreements.
   The evidence above is sufficient to flag uncertainty, not to choose a
   replacement species. This is a non-blocking contextual gap because the
   source IDs, conflicting taxon fields and broad mapping predicates remain
   available. Ownership: `src/taxonmech/seed.py` for a tested, source-scoped
   representation; any actual mapping correction belongs upstream in
   KG-Microbe or the source authority. `docs/CURATION.md` forbids direct
   generated-YAML edits and describes curator overlays as future work.

2. **M2 - Minor: GOLD attestation scope is underspecified.**
   The 106 count faithfully matches `data/raw/gold_organisms.tsv`; it is not
   the 92 directly classified organisms in the native GOLD catalog inspected
   here. `src/taxonmech/extract.py` obtains the former from KG-Microbe GOLD
   subclass edges, independently of the native workbook-derived link catalog.
   The attestation note says direct taxon records without identifying that
   inventory boundary. Ownership: `src/taxonmech/seed.py` attestation notes
   and the `src/taxonmech/extract.py` provenance contract. Do not replace 106
   with 92 without an explicitly authorized source/snapshot migration.

## Recommended Edits

1. Add a tested, source-scoped conflict summary through maintained generation
   logic or a separately implemented persistent curator overlay. Preserve
   each accession, deposit, source taxon and disagreement. Do not relabel
   the species, discard supported links, promote broad mappings to exact
   identity, or set the parent-species type flag on BacDive 14833.
2. Clarify GOLD count provenance as the transformed direct-taxon inventory
   used for seeding, distinct from the native catalog used for genome links.
   Keep the current count until a deliberate inventory update is validated.

These are future actions only. No generated record or prior report was edited.

## Follow-up Checks

- After an authorized generator change, run focused regression tests for
  source-conflict retention and attestation wording, then both validators
  listed above on the regenerated record.
- Run `just verify-corpus` after authorized regeneration to check the whole
  committed corpus; the per-record diagnostics here cannot establish that.
- Reinspect current collection and nomenclature authorities before resolving
  any deposit classification. Recheck the NCBI RefSeq exclusion for DSM 22957.
- Reconcile transformed GOLD edge provenance against its pinned snapshot
  before changing the attestation inventory; preserve native organism,
  project and analysis chains independently.
- Retry PubMed and live GTDB authority pages when accessible. Do not treat
  retrieval failure as evidence against the cited records.

## Additional Notes

The review-report filename was checked independently of gitignore before
creation. Report existence measures coverage only, not the quality of every
prior review. Eukaryota was not reopened. The other Codex session is closed;
no worktree or branch change was made for this read-only review.

The strict validator writes its normal validation TSV under `reports/`.
The only manually authored artifact from this review is this new report.
The existing SEEDED status and embedded seed history remain unchanged.
