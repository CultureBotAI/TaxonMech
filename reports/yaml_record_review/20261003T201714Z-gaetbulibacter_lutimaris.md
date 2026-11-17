# YAML Record Review: Gaetbulibacter lutimaris

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gaetbulibacter_lutimaris.yaml`
- Started UTC: 2026-10-03T20:14:27Z
- Finished UTC: 2026-10-03T20:17:14Z
- Verdict: pass

## Target

Read all 178 lines of this generated `TaxonRecord` for `NCBITaxon:1031273`,
Gaetbulibacter lutimaris: rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. One BacDive type strain has two culture
identifiers and four related-record assertions. It has no assembly or
genome-record assertion. The maintained source inventories and transforms
own future changes; no generated YAML was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/gaetbulibacter_lutimaris.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/gaetbulibacter_lutimaris.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured inventory comparisons | Identity, complete lineage, source counts, index and seed-history checks passed. All four related assertions match the raw/StrainInfo inventories field for field; assembly and genome inventories have no target rows. |
| StrainInfo evidence | Both nested evidence objects match the native own deposit, culture identifier, status, nonerroneous relation, taxon, BacDive reference and version DOI. |
| Embedded history | Checked by strict validation and comparison with the seed-scope reason and attesting sources. |
| Standalone history | Not applicable: ignored-inclusive identifier, name, slug and designation searches under `history/` found no target entry. |
| Graph and ontology-product gates | Not applicable: the fully read YAML contains no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, full test suite,
global provenance, rendered products, exports and upstream KGX regeneration.
The focused comparisons are not a replacement for corpus reproduction.
The live BacDive page was unavailable through the browser tool; its pinned
native record, LPSN, NCBI and live StrainInfo supplied independent identity
checks. No validator or source-check blocker remains for this bounded review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220635` agrees with the label, species rank,
genetic code 11, parent `NCBITaxon:311207` and all eleven root-first lineage
entries. A complete backbone scan found no child taxa. Live
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031273)
and taxonomy EFetch independently confirm this identity and lineage.

The two related synonyms correspond to NCBI's authority and included-name
classes, also preserved in native name rows
`data/catalog/ncbi_names-0005.jsonl.gz:29785` through 29787. Neither the
authority string nor Gaetbulibacter sp. D1-y4 is overstated as exact identity.
The indexed identifier and slug match `data/taxa/PATHS.tsv:12937` and
`curation/seed_scope.tsv:14827`.

LPSN `790618`, authority Yoon et al. 2013, name, rank, status, type deposits,
citations and marker accession match `data/raw/lpsn_names.tsv:27558` and
the inspected [LPSN species page](https://lpsn.dsmz.de/species/gaetbulibacter-lutimaris).
The current-name identity and type designations are supported. LPSN notes
a possible future generic reassignment from a phylogenetic study, but still
lists this name as correct; that note does not authorize replacing the
NCBI genus or inventing another accepted name.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:56139` and the complete native
  record `data/bacdive/records.jsonl.gz:56138` agree on BacDive 133829,
  D1-y4, CCUG 61504, KCTC 23716, species taxon 1031273 and type-strain
  status. Both registered culture identifiers pass the local CAFI-backed
  normalizer and have matching taxon assignments in
  `data/raw/culture_collection_strains.tsv:34123` and row 117590. The
  native sequence section contains JF739861, not a genome assembly.
- **Type material:** Local NCBI type-material rows 1511-1516, live NCBI,
  LPSN and the species publication agree on CCUG 61504, KCTC 23716 and
  D1-y4. D1-y4 remains the strain designation, not an invented collection
  accession.
- **GOLD:** Native `data/gold/organisms.jsonl.gz:36496` explicitly links
  Go0043553 to CCUG 61504 in both the culture-collection and strain fields.
  The two YAML assertions preserve those separate source fields and match
  `data/raw/strain_related_records.tsv:87497` and the next row. An organism
  record alone does not imply a genome, sequencing project or BioSample.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:306641` and the
  fully inspected live [SI-ID 408754 record](https://api.straininfo.dsmz.de/v2/data/strain/max/408754)
  agree on DOI `10.60712/SI-ID408754.3`, published status, BacDive 133829,
  taxon 1031273 and available CCUG deposit SI-DP 916269. Its culture
  collection is not deprecated and its own deposit relation is not
  erroneous. The join is supported by the whole CCUG 61504 designation,
  not just group membership or the BacDive pointer. Overlay strain-link
  row 15330 and related rows 38148-38149 exactly match both assertions.
- **Own-deposit boundary:** StrainInfo retains KCTC 23716 and D1-y4 only
  as designations. Its complete native and live records contain one own
  deposit and no sequence entries. Not inventing a KCTC SI-DP, a
  StrainInfo sequence assertion or a genome association is correct.
- **Publication identifiers:** Crossref metadata resolves
  [10.1099/ijs.0.040352-0](https://api.crossref.org/works/10.1099/ijs.0.040352-0)
  to the species description, volume 63, pages 995-1000, and
  [10.1099/ijs.0.053207-0](https://api.crossref.org/works/10.1099/ijs.0.053207-0)
  to the notification list, volume 63, pages 1939-1941. The fully inspected
  [PubMed abstract and metadata, PMID 22685106](https://pubmed.ncbi.nlm.nih.gov/22685106/)
  corroborate the species, type-deposit equivalences, DOI and marker
  accession. Publication was electronic in 2012 and in print in 2013,
  explaining the live StrainInfo bibliography's 2012 date without changing
  the supported nomenclatural authority. Full article texts were not read.
- **Marker sequence:** NCBI nuccore metadata for
  [JF739861.1](https://www.ncbi.nlm.nih.gov/nuccore/JF739861.1) identifies a
  1440-base partial 16S sequence from D1-y4, taxon 1031273, annotated as
  type material and linked to the cited species article. The YAML
  correctly preserves LPSN's unversioned accession; no sequence alignment
  or gene-function inference was performed.
- **Attestations:** Complete raw-inventory scans confirm NCBI NAME 1,
  LPSN NAME 1, BacDive STRAIN 1, GOLD ORGANISM 1 and MADIN
  TRAIT_ASSERTION 7. There is no direct GTDB, MediaDive or BactoTraits row
  in the corresponding inventories. Counts are evidence-record counts,
  not validated physiological properties or quantities to sum together.

## Completeness

Ignored-inclusive compressed searches covered the native catalog, BacDive,
BV-BRC, GOLD, SeqCode, StrainInfo and history with the full name, slug,
taxon identifier, D1-y4 and whole culture identifiers. Exact typed taxon
fields in native NCBI/GTDB and BV-BRC catalogs were also screened. SeqCode
name 8131 corroborates the name without adding a type-genome claim.
No eligible genome candidate or additional BacDive strain was found within
those source boundaries. Complete raw assembly/genome scans and the
StrainInfo overlay comparison likewise yield no target genome assertion.

The live NCBI misspelling Gaetbulibacter aquimaris was additionally searched
in native sources and the complete ignored AllTheBacteria catalog. It does
not identify a missing genome candidate and must not be promoted to an
accepted or exact alternate name. It is not present in the pinned name
projection; this nonessential misspelling does not alter record identity.

The complete `data/catalog/allthebacteria.tsv.xz` and `data/atb/` searches
find no matching name, alias, culture designation or target strain link.
There is no BioSample assertion through which an ATB crosslink could be
grounded. No genome FASTA, archive or checksum replay applies to an absent
association. Full structured retired-ID and dropped-row scans found no
target entry. These are bounded local findings, not a claim that no
sequence or strain exists anywhere else.

The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb
datasets` adapter returned 28 dataset keys and no Gaetbulibacter coverage.
No organism-matched expression query applies; this absence is not negative
evidence about the marker sequence. The YAML does not assert a molecular
mechanism, and an optional causal graph is not required.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and stated source boundaries.
The unavailable live BacDive page is a verification limitation, not
evidence that its supported stable identifier or strain assertion is wrong.

## Recommended Edits

None required. Preserve the supported NCBI identity, type deposits and
source-scoped GOLD and StrainInfo assertions. Do not add a genome or
StrainInfo deposit by transferring evidence through an alias or species name.

## Follow-up Checks

- Recheck the live BacDive authority page when accessible; compare its
  identity with the pinned record and live SI-ID 408754 evidence.
- On a later authorized source refresh, recheck any new own-deposit or
  assembly evidence before adding associations. A possible future genus
  reassignment requires authority evidence, not the speculative LPSN note
  alone.
- Any future curation should rerun both target validators and appropriate
  corpus, provenance and rendered-product gates. No curation change is
  proposed by this review.

## Additional Notes

This is an individual read-only review, not a sampled or bulk pass. All
absence statements use ignored-inclusive searches or complete structured
reads of the named source surfaces. The native snapshots were not refreshed.
Only this new report was written; prior reports, source code, YAML,
curation history, review status and Eukaryota records were untouched.
