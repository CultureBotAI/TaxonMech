# YAML Record Review: Bremerella cremea

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bremerella_cremea.yaml`
- Started UTC: 2026-10-03T20:27:18Z
- Finished UTC: 2026-10-03T20:30:55Z
- Verdict: pass with minor issues

## Target

Reviewed all 516 lines of this generated `TaxonRecord`: `NCBITaxon:1031537`,
Bremerella cremea, rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`,
mapping status `SEEDED`. It contains one BacDive strain, nine assembly
assertions, five genome-record assertions and twenty related-record
assertions. These are source assertions, not distinct biological genome counts.

Future fixes belong in maintained source transforms and inventories,
including `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not in this
generated YAML. This review writes only its new report and the standard
validator diagnostic.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bremerella_cremea.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bremerella_cremea.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured inventory comparisons | Exact backbone and ten-entry lineage match; source attestations and seed reason checked; full-field multiset equality for all 9/5/20 strain assertions against raw and StrainInfo inventories. |
| Embedded history | Strict validation passed; seed event agrees with the source inventories and scope reason. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored/hidden files found no target history under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the complete record has no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full test suite, generated-page freshness, exports and FASTA replay. Focused
comparisons do not replace those gates. No generator, history writer or
curation-status promotion was run.

## Identity and Grounding

The identifier, current name, rank, parent `NCBITaxon:2714594`, genetic code
11 and complete lineage match `data/raw/ncbitaxon_taxa.tsv:220742`. Live
taxonomy EFetch and [NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031537)
confirm them. The complete backbone scan finds no child taxa. An
ignored-inclusive anchored identifier search across `data/taxa/` resolves
exactly this record. `data/taxa/PATHS.tsv:13068` and
`curation/seed_scope.tsv:10788` agree with its identifier and slug.

Native NCBI name rows at `data/catalog/ncbi_names-0005.jsonl.gz:29901` and
the next four rows support the two exact synonyms and two related names.
The historical includes-name Blastopirellula sp. LHWP2 is not promoted to
an exact synonym.

The inspected [LPSN current-name page](https://lpsn.dsmz.de/species/bremerella-cremea)
supports identifier 19001, species rank, authority, ICNP publication status,
correct-name status and marker accession JF748733. The inspected
[basionym page](https://lpsn.dsmz.de/species/blastopirellula-cremea) confirms
identifier 790849 and its synonym relationship. The inventory at
`data/raw/lpsn_names.tsv:3610` and basionym row 27760 preserves that
relationship. The YAML's LPSN synonym is conservative rather than an
unsupported equivalence. Its type-deposit list is incomplete; see N1.

The principal GTDB identity is supported by the LPSN link and native
type-genome placement, not by treating every `broadMatch` as identity.
The other three clusters remain explicitly pooled mappings and are absent
from identity xrefs and exact synonyms. One explanatory note overstates
the mapping cardinality; see N2.

## Evidence

- **BacDive strain:** `data/raw/bacdive_strains.tsv:56197`, native
  `data/bacdive/records.jsonl.gz:56196` and the inspected
  [BacDive record](https://bacdive.dsmz.de/strain/133887) support LHWP2,
  JCM 17758, KACC 15559 and type-strain status. Native reference 124043
  explicitly supplies unversioned GCA_039541315 and its contig-level
  assembly description. The two-medium count matches the raw strain row;
  it is not added as a species-level MediaDive attestation.
- **Genome evidence:** Raw assembly rows 32891-32899, genome-record rows
  25846-25850 and related-record rows 88512-88531 match every assertion.
  Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3065` supplies genome
  1031537.8, GCA_039541315.1, SAMD00645723 and PRJDB10510 through both
  explicit JCM strain and culture-collection fields.
- **GOLD chain:** `data/gold/organisms.jsonl.gz:525070`,
  `data/gold/projects.jsonl.gz:609085` and
  `data/gold/analyses.jsonl.gz:451486` support Go0704365 -> Gp0829683 ->
  Ga0675299, the JCM deposit match, IMG 8127939770, assembly, sample and
  project. The two eligible organism fields remain separately attributed.
- **NCBI assembly pair:** Native
  `data/catalog/ncbi_genbank-0036.jsonl.gz:5285` and
  `data/catalog/ncbi_refseq-0006.jsonl.gz:3231`, corroborated by live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039541315.1/dataset_report),
  confirm current GCA/GCF_039541315.1, JCM 17758, type material, contig level,
  ASM3954131v1 and SAMD00645723. RefSeq/GTDB PRJNA224116 remains distinct
  from GenBank/BV-BRC/GOLD PRJDB10510. Source-unversioned BacDive evidence
  is not silently upgraded.
- **GTDB clusters:** Raw mapping rows 1303-1306 match the four predicates
  and counts. A complete exact-cluster native scan finds two cremea members
  (JCM 17758 and LHWP2), two marina_A members, two marina_B members and
  one cremea_A member. JCM 17758 is the representative type genome at
  `data/catalog/gtdb_genomes-0005.jsonl.gz:43355`; LHWP2 is a second
  type-material assembly at `gtdb_genomes-0006.jsonl.gz:15880`. The primary
  attestation correctly counts two, not the sum of all pooled clusters.
- **Publications:** [PubMed 31894496](https://pubmed.ncbi.nlm.nih.gov/31894496/)
  and [Crossref metadata](https://api.crossref.org/works/10.1007/s10482-019-01378-1)
  verify the reclassification paper and DOI. Its inspected abstract
  explicitly proposes the new combination; physiology of Pan97 belongs
  to Bremerella volcania and is not transferred to this record.
  [Crossref validation-list metadata](https://api.crossref.org/works/10.1099/ijsem.0.004688)
  and DOI-resolved [PubMed 33787483](https://pubmed.ncbi.nlm.nih.gov/33787483/)
  verify the second cited DOI and list identity. Their date metadata
  disagree with LPSN's 2021 validation chronology; see Additional Notes.
  Full articles were not read, and the journal DOI page was inaccessible.
- **Marker and original type:** Inspected
  [JF748733.1](https://www.ncbi.nlm.nih.gov/nuccore/JF748733.1) metadata
  identify a 1,430-base partial 16S sequence from LHWP2, taxon 1031537,
  with explicit type-material annotation. The full abstract of the original
  description, [PubMed 23159757](https://pubmed.ncbi.nlm.nih.gov/23159757/),
  independently corroborates LHWP2 = KACC 15559 = JCM 17758. The source
  accession stays unversioned in the YAML; no alignment was performed.
- **Source counts:** Complete target-ID inventory scans corroborate NCBI
  NAME 1, LPSN NAME 1, primary GTDB GENOME 2, BacDive STRAIN 1, GOLD
  ORGANISM 5 and MADIN TRAIT_ASSERTION 18. No direct MediaDive or
  BactoTraits row was found in those complete inventories. These counts
  are not phenotype assertions.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 keys, none covering Bremerella
  or Blastopirellula. No applicable organism-matched query exists; this
  is not negative evidence about the organism or its marker.

## Completeness

The strain list is complete for the local species subtree, not capped.
Ignored-inclusive compressed searches covered native catalog, BacDive,
BV-BRC, GOLD, SeqCode and StrainInfo snapshots using current/historical
names, whole culture identifiers and typed taxon identity. Native GOLD's
five organism records agree with the inventory count, but only JCM 17758
has an eligible culture-deposit join to the BacDive strain.

The separate GCA/GCF_041699455.1 LHWP2 assembly is real and type-derived;
native GenBank row `ncbi_genbank-0038.jsonl.gz:8080`, RefSeq row 25950 in
`ncbi_refseq-0006.jsonl.gz`, BV-BRC row 3061 and the GOLD Go0711862 chain
all support it. Those source strain fields supply only the bare laboratory
designation LHWP2, not an eligible JCM/KACC deposit. Its exclusion follows
`docs/STRAIN_GENOMES.md` and is not evidence of genome absence. Likewise,
HEX-1 MGV, HEX-2 MGV and HEX PRIS-MGV candidates are not this culture
deposit. Name, taxonomy and ANI similarity are not substitute join keys.

The full ignored ATB catalog contains four available assemblies for the
species-name candidates: SAMN09637267, SAMN09637346, SAMN09637541 and
SAMN43181681 at rows 1443349, 1443386, 1443394 and 3029892. None is the
record's own deposit-backed SAMD00645723. Whole sample/name/deposit
searches over `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz` found no eligible JCM-linked overlap.
No crosslink is inferred from the shared species name, and no FASTA replay
is needed for the absent eligible association.

BacDive links to SI-ID 27972, but its public StrainInfo API returned HTTP
404. Ignored-inclusive searches of native and overlay StrainInfo files
using names, deposits, LHWP2 and the exact SI-ID found no target evidence.
An initial unbounded DOI-prefix search matched unrelated SI-IDs 279720-279729;
the corrected whole-ID search excluded those numeric-prefix collisions.
No StrainInfo assertions should be invented from the BacDive link alone.
SeqCode name hits corroborate the two names, not extra strains or genomes.

## Findings

Counts: 0 blocker, 0 major, 2 minor.

**N1 - Minor: the nomenclatural type-deposit list omits KACC 15559.** YAML
line 51 lists only JCM 17758. Both inspected LPSN pages and the original
description identify KACC 15559 as another deposit of LHWP2. Native NCBI
type-material rows 1519-1520 and live taxonomy independently agree.
KACC 15559 is already correctly present in the BacDive strain at YAML
line 116, so identity, type status and existing genome joins remain sound.

Maintained owner: the LPSN source transform feeding
`data/raw/lpsn_names.tsv:3610` and row 27760. Both raw rows omit KACC;
`src/taxonmech/extract.py:420` collects type-deposit edges and
`src/taxonmech/seed.py:405` faithfully copies the resulting list. Repair
the maintained upstream LPSN evidence/transform, then re-extract and seed.
Do not invent a culture CURIE for the bare LHWP2 designation or hand-edit
the YAML. Upstream KGX edge contents were not inspected in this review,
so the exact earlier loss point remains to be located.

**N2 - Minor: a pooled-mapping note claims an unsupported extra NCBI mapping.**
YAML lines 85-86 say the cremea_A species also maps to other NCBI taxa.
An ignored-inclusive exact-ID scan of the complete raw mapping table finds
only row 1304, mapped to this taxon. The complete native cluster has only
RS_GCF_003335505.1, HEX PRIS-MGV, taxon 1031537, at
`data/catalog/gtdb_genomes-0000.jsonl.gz:26240`. Thus the phrase does not
describe this cluster. It confuses several GTDB species mapping to one
NCBI taxon with one GTDB species mapping to several NCBI taxa.

Maintained owner: the unconditional `skos:broadMatch` note in
`src/taxonmech/seed.py:463`. This is a wording/cardinality defect, not an
unsupported identity xref: the predicate, count, pooled status and exclusion
from exact synonyms are appropriate and should remain unchanged.

## Recommended Edits

1. Correct the maintained LPSN type-deposit source/transform to retain the
   evidenced KACC 15559 entry. Trace the actual transformed edges before
   deciding whether the fix belongs in kg-microbe or TaxonMech extraction.
   Add a focused extraction regression for multiple registered type deposits.
2. Replace the seeder's unconditional extra-NCBI-taxa wording with a neutral
   statement of observed pooling, or emit cardinality-specific wording only
   when verified from the complete mapping inventory. Add a
   `tests/test_seed.py` case for the singleton cremea_A cluster and a case
   that really has multiple NCBI mappings. Preserve source predicates,
   counts, supported identity links and genome/deposit provenance.
3. After an authorized implementation, use the documented extraction and
   seed workflow. No source edits, regeneration or status changes occurred
   during this review.

## Follow-up Checks

- Run focused extraction and seeding tests for N1/N2, then inspect
  `just seed --only NCBITaxon:1031537` before an authorized
  `just seed-canary NCBITaxon:1031537`.
- Rerun both target validators and exact source comparisons. Confirm both
  registered type deposits appear in nomenclature, while the original
  strain designation, all 9/5/20 assertions and source accession versions
  remain intact. Confirm no extra-NCBI mapping is asserted for cremea_A.
- Shared transform changes require the full tests, corpus reproduction,
  provenance and generated-product checks in a separate curation workflow.
- Recheck all four GTDB authority pages when accessible; their browser
  requests failed. The mapping assessment used inspected pinned native
  members, not unread pages. Retry SI-ID 27972 only if later source state
  supplies an eligible own-deposit record.

## Additional Notes

Crossref and PubMed currently give the validation-list DOI a 2019 date,
while LPSN cites validation list 198 in 2021 and the record's authority
uses 2021. Volume 71, issue 3 and the DOI/title resolve consistently.
This source-metadata discrepancy is preserved here; it does not justify
rewriting nomenclatural priority from aggregator dates. The full validation
list was not inspected, and the proposed nomenclatural correction does not
depend on resolving that date discrepancy.

All absence statements are bounded to the named complete structured reads
or ignored-inclusive searches. Source counts, computational pathway text
on BacDive and the reclassification paper's other species do not supply
new phenotype claims. One new report was created; the record, source code,
previous reports, history and curation status were not edited. Eukaryota
was left untouched.
