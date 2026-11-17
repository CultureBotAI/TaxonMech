# YAML Record Review: Paenibacillus marinum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_marinum.yaml`
- Started UTC: 2026-10-04T05:55:33Z
- Finished UTC: 2026-10-04T05:59:45Z
- Verdict: needs curation

## Target

Generated `TaxonRecord` for `NCBITaxon:1033264`, Paenibacillus marinum,
rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`, status `SEEDED`.
The entire YAML was read. It contains nine lineage entries, two related
synonyms, one BacDive strain, two StrainInfo related records, two source
attestations and one seed event. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_marinum.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_marinum.yaml`: passed, one file, zero ERROR rows. This refreshed `reports/instance_validation_failures.tsv`.
- Read-only structured comparisons: complete backbone parent chain, synonyms,
  scope, attestations, and all strain assembly/genome/related-record inventory
  fields matched. Both StrainInfo evidence objects matched their own eligible
  native deposit, including DOI, status, culture identifier and BacDive ID.
- Not checked: full-corpus `just verify-corpus`, `just qc`, test suite,
  provenance/history/product gates, global term/reference checks and rendered
  site drift. No invented focused substitute was used for those gates; the
  source comparisons above do not prove full corpus reproducibility.

## Identity and Grounding

The taxon identity itself is supported. NCBI Taxonomy EFetch and Datasets
resolve 1033264 to Paenibacillus marinum, species, parent 44249, genetic code
11, with the same complete root-first lineage. Authority and THE22 names are
appropriately related rather than exact synonyms. Pinned backbone row 220941
and native name rows 30249-30251 in `data/catalog/ncbi_names-0005.jsonl.gz`
agree. Exact merged/dropped scans found no target entry.

[LPSN](https://lpsn.dsmz.de/species/paenibacillus-marinum) treats the name as
not validly published and a preferred, not correct, name. It lists THE-22,
DSM 18499 and LMG 23758 as type designations. These name-level assertions do
not establish that the record's VP-31 strain is THE22. NCBI exact grounding
does not imply valid publication or settle the conflicting strain identity.

## Evidence

- `data/raw/bacdive_strains.tsv:23052` supplies BacDive 23248, VP-31,
  DSM-18499 and **both** NCBITaxon:1033264 and NCBITaxon:2930037. Native
  `data/bacdive/records.jsonl.gz:23051` identifies its main organism as
  Phaeospirillum sp., non-type VP-31, while an embedded LPSN section identifies
  Paenibacillus marinum. The conflict is already in the source, not introduced
  by a spelling normalization. The live [BacDive page](https://bacdive.dsmz.de/strain/23248)
  also mixes a Phaeospirillum page title with a Paenibacillus display name,
  VP-31, DSM 18499 and the two taxonomy IDs.
- The [DSMZ deposit catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-18499)
  identifies DSM 18499 as Phaeospirillum sp. VP-31 from drinking water in
  Seville, Spain. Its main entry does not identify THE22. A conflicting
  Zoogloea caeni label on a secondary BacDive link was not used to override
  the catalogue's main entry.
- `data/straininfo/records.jsonl.gz:294773` contains SI-ID 396884 and its own
  available, non-deprecated DSM 18499 deposit, SI-DP 903472. Both strain and
  deposit taxonomy are Phaeospirillum, NCBITaxon:85265, with VP-31 as the
  designation and `typeStrain: false`. There are no native sequence entries.
  The YAML faithfully preserves these distinct typed related records and
  their taxon conflicts. Overlay rows 194134-194135 and strain-link row 80800
  match. The [versioned DOI](https://doi.org/10.60712/SI-ID396884.2) resolves to
  SI-ID 396884; inspected DataCite metadata describes a Phaeospirillum strain.
- Live NCBI EFetch independently resolves 2930037 to Phaeospirillum sp.
  (species) and 85265 to Phaeospirillum (genus), distinct from Paenibacillus.
- [Bouraoui et al., PMID 23456638](https://pubmed.ncbi.nlm.nih.gov/23456638/)
  describes THE22 from a Tunisian hot spring and equates it with DSM 18499
  and LMG 23758. Crossref verifies DOI `10.1002/jobm.201200275`, authors,
  journal, volume 53 and pages 877-883. The abstract and metadata, not the
  full article, were inspected. This supports the published designation
  claim but conflicts with the current DSMZ deposit entry; it does not
  demonstrate that THE22 and VP-31 are the same strain.
- Exact NCBI Assembly search returned zero with a phrase-not-found warning.
  Exact Nuccore search returned four records, all inspected: THE22 16S
  `FR865169.1` and `NR_178385.1` (1536 bases each), T172_AH2 `MF193684.1`
  (841 bases), and T169_AH2 `MF193681.1` (848 bases). These are locus
  sequences, not genome assemblies, and cannot be transferred to VP-31
  through the disputed DSM number.

## Completeness

The strain count of one and both source-attestation counts reproduce the
inventories; this is not an independently confirmed census of this species.
The uncapped list has all inventoried strains. No assembly/genome links are
missing from the exact strain's maintained overlays.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched target ID, label,
stem, DSM 18499, LMG 23758, THE22, VP-31 and the StrainInfo identifier in
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
It completed with 46 matching lines. Separate recursive structured
`SOURCE.json` scans found no matches. These are bounded local-source results,
not a claim that no additional evidence exists anywhere.

Complete structured culture-token scans found no eligible DSM-18499 genome
matches in 4,111,794 NCBI GenBank/RefSeq rows, 1,419,549 BV-BRC rows, 901,341
GTDB rows or 531,961 GOLD organism rows. All 314,470 native StrainInfo rows
yielded just the own-deposit record discussed above. Substring hits for
XVP-31x and MAVP-31 belong to other organisms; `GCA_010332645.1` and
`SAMEA1033264` are unrelated accession-number coincidences, not taxon matches.

Exact maintained LPSN, GTDB mapping, GOLD, MediaDive, Madin and BactoTraits
taxon scans returned no rows. Empty optional fields therefore reproduce the
current inputs. SeqCode native row 34912 resolves to record 36799; its live
API marks this name as automated discovery with an unknown type, not a
validated nomenclatural substitute. Do not invent a type-strain flag or
populate THE22 sequences on VP-31 to fill these gaps.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: unresolved cross-genus strain identity in the sole strain entry.**
   YAML lines 46-51 associate VP-31/DSM-18499 with Paenibacillus marinum,
   while native BacDive classification, the DSMZ catalogue and own-deposit
   StrainInfo evidence support Phaeospirillum. The publication, NCBI type
   material and LPSN repeat the conflicting DSM designation for THE22.
   The record preserves some conflicting evidence but does not resolve or
   qualify the primary strain association. Source-faithful generation and
   green validators do not establish biological identity. This affects the
   only strain and the BacDive attestation, but does not invalidate the
   NCBI taxon ID or authorize changing its carried lineage. Future owners:
   BacDive/collection source identity reconciliation, the pinned source
   refresh through `src/taxonmech/bacdive_v2.py:57` and
   `src/taxonmech/extract.py`, and `src/taxonmech/seed.py:485` for any explicit
   representation of unresolved associations. Do not hand-edit the YAML.

## Recommended Edits

Resolve DSM 18499 against collection-authoritative evidence for VP-31 and
THE22 before treating this association as curated. Preserve the conflicting
source statements and versioned identifiers. Do not silently rename VP-31,
guess an alternative DSM accession, mark it type, or erase the StrainInfo
taxon to conceal disagreement. A source correction should flow through the
maintained snapshot/extraction path and regenerate the raw inventories.
If unresolved associations need a distinct representation, implement a
tested extractor/seeder policy rather than an ad hoc generated-file patch.

Reassess the BacDive attestation and `curation/seed_scope.tsv:63829` after
identity resolution; loss of a source must not silently leave an inaccurate
two-source scope reason. A later evidence-backed LPSN refresh should retain
the non-valid-publication status and the unresolved deposit discrepancy.

## Follow-up Checks

Inspect authoritative THE22/LMG 23758 deposit documentation and any corrected
publication or source record. No collection was contacted in this review.
Add focused regression coverage for incompatible explicit species mappings
without treating a source conflict as permission to infer taxonomy. After an
authorized source/policy change, run extraction dry-run, inspect the target
inventory deltas, then `just seed-canary NCBITaxon:1033264 --force`, both
focused validators, `just verify-corpus` and the remaining authoritative QC
gates. No canary or regeneration was run during this review.

## Additional Notes

NCBI Taxonomy Browser and the initial web-tool BacDive/StrainInfo requests
were inaccessible; direct public EFetch, Datasets and HTTP/DOI reads
succeeded. StrainInfo's landing page required JavaScript, so native pinned
deposit evidence and DataCite DOI metadata were used without claiming a live
deposit-API refresh. iModulonDB was not applicable: the YAML makes no gene,
regulator or expression-module claim. No phenotype was added from the paper.

`data/taxa/PATHS.tsv:13382` resolves this unique target. The seed event and
NCBI snapshot remain 2026-09-13. No YAML, maintained input, scope, status,
history, tracked code or GitHub state was changed. This review created only
this new report, apart from the documented strict-validation TSV refresh.
