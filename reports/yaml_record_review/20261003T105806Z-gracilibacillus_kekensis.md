# YAML Record Review: Gracilibacillus kekensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gracilibacillus_kekensis.yaml`
- Started UTC: 2026-10-03T10:52:25Z
- Finished UTC: 2026-10-03T10:58:06Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1027249`, Gracilibacillus kekensis,
rank SPECIES, domain BACTERIA, parent `NCBITaxon:74385`. The complete
613-line YAML was read before judgment and reread after the interrupted
review resumed. Grounding is EXACT and mapping status is SEEDED.

The record carries one LPSN name, one GTDB species mapping, one BacDive
strain, eight source attestations and one embedded seed event. The strain
has eight assembly assertions, seven genome-record assertions including
AllTheBacteria, and 22 related-record assertions. These are source-bearing
assertion counts, not counts of distinct biological genomes.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/gracilibacillus_kekensis.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/gracilibacillus_kekensis.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check with no focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug search of `history/` found no target entry. Strict validation covered the embedded event. |

Additional read-only diagnostics passed:

- Nine ancestor labels/ranks and the parent chain agree with the complete
  pinned taxonomy table. Subtree traversal finds only the target taxon.
- The complete BacDive inventory contains exactly the retained strain for
  that subtree.
- Exact assertion-multiset comparisons reproduce all eight assemblies,
  six non-ATB genome assertions and 22 related assertions from the raw and
  StrainInfo inventories.
- All 33 assertions carrying a matched culture ID reference an existing
  deposit and pass the repository's whole-accession CAFI recognition.
- The ATB link has exactly the six sample chains in its overlay, and every
  chain is an existing BIOSAMPLE assertion in this strain record.

An ad hoc `uv run python` diagnostic encountered a local cache permission
error. The same diagnostic completed with the existing `.venv/bin/python`;
the two documented validators above completed successfully. These checks
do not prove full-corpus reproducibility or genome sequence equivalence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv` row 218774 supports the ID, species label,
parent, code 11, related names and 2026-09-13 snapshot. The native NCBI
names catalog distinguishes the authority string from the includes-name
Gracilibacillus sp. K170; neither is promoted to an exact synonym.

[LPSN 789861](https://lpsn.dsmz.de/species/gracilibacillus-kekensis)
supports the species name, Gao et al. 2012 authority, valid publication,
correct-name standing, type-strain designations and HQ439902. The raw
LPSN row also supplies the legitimate flag. Live NCBI Taxonomy requests
failed, so current browser rank and lineage were not independently read;
the pinned taxonomy and native source identities provide the bounded
support used here.

The GTDB mapping denotes the same species, not a species cluster equated
to an individual strain. The complete native GTDB catalog search finds
one member, `RS_GCF_900143085.1`, classified to this species with both
NCBI taxon and species IDs 1027249 and culture CGMCC 1.10681. This supports
the closeMatch predicate and count one. GTDB's Bacillales/Amphibacillaceae
placement differs from the pinned NCBI Caryophanales/Bacillaceae lineage;
the YAML correctly carries the latter rather than reconciling sources.

## Evidence

**Type strain and bibliography.** The inspected
[species description](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.030858-0)
identifies K170, CGMCC 1.10681 and DSM 23178 as the type strain. The
[PubMed entry](https://pubmed.ncbi.nlm.nih.gov/21685255/) ultimately resolved
after an earlier challenge and confirms PMID 21685255, the same DOI and
HQ439902 as associated sequence data. The second
[publisher DOI](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.045435-0)
resolves to the notification for names in volume 62, part 5. It is a
nomenclatural reference, not independent strain phenotype evidence.

**BacDive.** Raw row 1464, the native object in
`data/bacdive/records.jsonl.gz`, and the inspected
[BacDive 1468 page](https://bacdive.dsmz.de/strain/1468) agree on K170,
the two culture deposits, type status and taxon 1027249. Native reference
66792 supplies the unversioned `GCA_900143085`, `patric:1027249.3` and
`img.taxon:2667528169` assertions. Native reference 16552 supplies
HQ439902. No version suffix has been invented for the BacDive assembly.

**Primary genome metadata.** Native NCBI GenBank and RefSeq entries support
`GCA_900143085.1` and `GCF_900143085.1`, respectively, with scaffold level,
type-material status, culture CGMCC 1.10681 and sample SAMN05216179. The
native GTDB row preserves those accessions and its exact culture field.
The native BV-BRC object 1027249.3 independently supplies the RefSeq
assembly, culture, sample and WGS accession FRCZ00000000. Its assembly is
not misrepresented as a GenBank identifier.

**GOLD provenance.** Native objects in `data/gold/` support the chain
Go0043673 to Gp0120000 to Ga0079828, culture CGMCC 1.10681,
`GCA_900143085.1` and IMG 2667528169. The analysis lacks its own organism
field, but its explicit project link resolves to that organism. Separate
source culture and strain fields account for repeated assertions.

The complete native organism scan finds three target-taxid objects:
Go0043673, Go0612428 and Go0612429. Go0612429 explicitly supplies DSM
23178; Go0612428 supplies bare K170 without a culture collection ID.
Counting the latter as a GOLD organism while not joining its bare alias
to the BacDive strain respects the matching boundary.

The three BioProject accessions remain source-scoped: PRJEB18418 comes
from GenBank/BV-BRC, PRJNA224116 from RefSeq/GTDB, and PRJNA323106 from
GOLD project Gp0120000. The YAML does not claim they are interchangeable.

**StrainInfo.** Native SI-ID 402134.3 has one own deposit, available DSM
23178 at SI-DP 909113, published-online status, taxon 1027249, LPSN
789861 and BacDive 1468. Its version DOI is
`10.60712/SI-ID402134.3`. The two retained typed related records preserve
that evidence. CGMCC 1.10681 and K170 are relation designations, not
additional deposit objects. There are no sequence objects in this native
record, so absence of StrainInfo genome links is appropriate.

**AllTheBacteria.** The full compressed native metadata search returned
SAMN05216179 at line 1160321. It agrees with the overlay and YAML on run
SRR4216916, analysis ERZ4270412, SeqKit sum, species, PASS filters, the
661k dataset and supplied download/archive locations. Available FASTA
status supports retention. No archive or genome FASTA was downloaded.

The six sample chains are BV-BRC, two GOLD source-field matches, GTDB,
GenBank and RefSeq. The separately inspected genome crosslinks preserve
the explicit source chains for GTDB, IMG, GCA, GCF and PATRIC rather than
forming a Cartesian product. Shared sample is not asserted as assembly
or sequence identity.

**Attestations.** Raw inventories support NCBI and LPSN counts of one NAME,
GTDB one GENOME, BacDive one STRAIN, MediaDive one MEDIUM, GOLD three
ORGANISM records, Madin 16 TRAIT_ASSERTION records and BactoTraits 30
TRAIT_ASSERTION records. Scope row 4036 names eight sources, consistent
with the seed event. These counts do not import strain-level phenotypes
or imply that all sources have the same unit.

## Completeness

No consequential gap was established. The raw LPSN type list contains DSM
23178 only, whereas its live page lists CGMCC 1.10681 and K170 as well.
Both recognized deposits and the K170 designation are already represented
on the correctly flagged type strain, so this narrower source projection
does not lose the strain identity or its supported genome links.

The BacDive inventory's medium count of zero and the species MediaDive
count of one are different source projections. They are not contradictory
genome or strain counts. The live BacDive page's medium recipe does not
authorize a new species-wide growth assertion.

Ignored-inclusive searches covered the target identifier, label and slug
in raw inventories, scope and history; compressed catalog searches also
covered native identity and linked accession evidence. No target history
entry was found. A separate ignored-inclusive filename search confirmed
no earlier report for this exact stem before creation.

Optional definition, causal graph, curator evidence and discussion fields
can remain empty for this seeded record. iModulonDB was not applicable:
the YAML asserts no gene, regulator, pathway or expression module.

## Findings

None found: 0 blocker, 0 major and 0 minor findings. Live endpoint limits
below remain limits of this review, not proof of broken identifiers.

## Recommended Edits

None required by the inspected evidence. Do not hand-edit this generated
YAML, merge source-scoped projects, append guessed accession versions, or
transfer sequences from StrainInfo relation aliases.

If a future refresh expands the LPSN type-designation inventory, its
maintained owner is the upstream LPSN transform feeding
`data/raw/lpsn_names.tsv`; the seeder consumes that projection. It is not
a justification for an isolated YAML patch.

## Follow-up Checks

1. Retry the NCBI Taxonomy browser, the GTDB species page and HQ439902's
   nucleotide authority endpoint when accessible. The current review used
   native catalogs and inspected LPSN, BacDive and publication evidence;
   it did not verify the nucleotide sequence itself.
2. Run `just verify-corpus` before asserting full-corpus reproducibility.
   Focused inventory comparisons above do not replace that gate.
3. Any later maintained-input change should be followed by the documented
   dry-run/canary workflow and both focused validators before wider seeding.

## Additional Notes

This is one read-only record review. No taxon YAML, maintained inventory,
scope, template, curation event or history record was edited. No status was
promoted and no GitHub or paid-provider action was taken. The strict
validator emitted its normal diagnostic TSV. Eukaryota was not reviewed.
