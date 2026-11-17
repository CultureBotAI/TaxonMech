# YAML Record Review: Isoptericola rhizophila

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/isoptericola_rhizophila.yaml`
- Started UTC: 2026-10-03T15:58:48Z
- Finished UTC: 2026-10-03T16:02:09Z
- Verdict: pass with minor issues

## Target

Read the complete generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303811`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:254250`, genetic code 11, grounding `EXACT`, status `SEEDED`.
There are nine lineage entries, two related synonyms, one BacDive strain
with two culture deposits and medium count 1, two source attestations,
and one seed event. No nomenclature, GTDB mapping, equivalence xref,
type flag, genome link, experiment or causal graph is asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/isoptericola_rhizophila.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/isoptericola_rhizophila.yaml`:
  PASS; one file, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured NCBI backbone comparison reproduces identity,
  rank, parent, code and all nine lineage entries; no children occur under
  the target. Full exact-field inventory scans reproduce the one BacDive
  row and find no direct LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
  taxon membership. Full raw strain-link table scans find no assembly,
  genome-record or related-record row for `kgmicrobe.strain:bacdive_162447`.
- `just verify-corpus`: Not checked; full-corpus-only, with no focused
  substitute invented. Full QC, global provenance, rendered products,
  exports and nucleotide sequence content were not audited.
- No target standalone history entry was found by ignored-inclusive
  searches; standalone history validation had no target. Strict validation
  checked the embedded event. Graph/product gates are not applicable.
- Direct upstream LPSN and MediaDive transform inspection was unavailable:
  the requested paths under the kg-microbe root configured in
  `conf/sources.yaml` returned file/directory-not-found errors. This is a
  limit at that configured location, not proof that no other checkout exists.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308144` reproduces the ID, name, rank,
parent, code and related synonyms. Native objects at
`data/catalog/ncbi_names-0007.jsonl.gz:30691` through line 30693
identify the authority spelling, scientific name and includes-name
separately. The PATHS index contains one target row.

The NCBI browser page was inaccessible through the web tool. Inspected
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303811&retmode=xml)
confirms species identity, parent 254250, Bacteria division, code 11 and
the full non-root lineage. It classifies the authority and BKS 3-46
includes-name as non-exact names, consistent with `RELATED_SYNONYM`.
It also lists type-material designations and the misspelling BKS3-46;
the misspelling need not be added as an exact synonym.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303811)
confirms all nine ancestor IDs including root. API reads used network
escalation after established sandbox DNS failures. Grounding is supported.

NCBI's species identity does not imply nomenclatural validity. Inspected
[LPSN](https://lpsn.dsmz.de/species/isoptericola-rhizophila), record
number 2147, identifies this name as not validly published and preferred
rather than correct. The YAML asserts neither status. Their omission is
the bounded completeness issue m1, not an incorrect NCBI identity.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME, snapshot 2026-09-13 | `data/raw/ncbitaxon_taxa.tsv:308144` | Exact identity and snapshot supported |
| BACDIVE 1 STRAIN; strain count 1 | `data/raw/bacdive_strains.tsv:84683` | One direct strain, no descendants or duplicate listing |
| BacDive ID, deposits, medium count 1 | Same complete BacDive row | All emitted values reproduced |
| JCM-19252 and MTCC-11080 classification | `data/raw/culture_collection_strains.tsv:104168`; line 131465 | Both map to target taxon |

The BacDive row has empty designation and LPSN fields. Complete native
object `data/bacdive/records.jsonl.gz:84682` supplies BacDive 162447,
taxon 1303811, JCM 19252, MTCC 11080, type-strain status and marker
KC608148; it does not contain a genome-sequence section. The live
[BacDive strain page](https://bacdive.dsmz.de/strain/162447) agrees on
identity, deposits and the 16S marker, and links StrainInfo 394394.

[JCM 19252](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=19252)
independently equates the deposit with MTCC 11080 and BKS3-46, calls it
a proposed type strain, links BacDive 162447 and taxon 1303811, and
lists medium 28. That JCM medium is corroborating culture context, not
proof of the exact MediaDive edge underlying `medium_count: 1`.
The emitted count is verified against the committed inventory only; no
specific medium recipe or growth phenotype is asserted by the YAML.

Pinned NCBI type-material rows `data/raw/ncbi_type_material.tsv:21085`
through line 21090 independently retain JCM 19252, MTCC 11080 and
BKS 3-46 variants. The current seeder derives `is_type_strain` from
same-taxon LPSN deposit matches (`src/taxonmech/seed.py:514`), not
directly from these NCBI rows or BacDive's flag. Its absence is not false.

The inspected [original-publication abstract](https://pubmed.ncbi.nlm.nih.gov/24858573/)
resolves PMID 24858573 to DOI 10.1007/s10482-014-0197-1, Kaur and
colleagues, 2014, and explicitly associates BKS 3-46 with both deposits.
The publisher full-text endpoint was inaccessible; no unseen full-text
claims were used. This is a source-discovered reference, not a citation
already in the YAML.

[NCBI GenBank metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=KC608148&rettype=gb&retmode=text)
confirms KC608148.1, 1,410 bp, partial 16S rRNA, strain BKS 3-46,
taxon 1303811, type-material qualifier and PMID 24858573. Metadata
were read through the feature table; nucleotide content was not audited.
Preserve the source's unversioned KC608148 where that is what it supplied.
This marker is not an assembly or a genome-count contribution.

Scope row `curation/seed_scope.tsv:51422` admits the taxon on
2026-09-12 with two sources. The 2026-09-13T17:54:04Z seed event
matches the reason and actual source names without claiming human review.

## Completeness

Ignored-inclusive searches covered `data/raw/`, `curation/`, `history/`
and all compressed JSONL catalogs under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
Queries used target ID, full label, slug, BacDive ID, collection-qualified
deposit forms and BKS 3-46/BKS3-46. Full inventory field scans established
membership separately from incidental text matches.

No target NCBI assembly, GTDB genome, BV-BRC genome or GOLD organism
was found in those pinned catalogs. Whole-deposit searches and a separate
compressed scan of `data/atb/` and `data/catalog/allthebacteria.tsv.xz`
found no target assembly lead. Empty genome links are supported within
this search boundary, not a universal statement that no genome exists.
Only the partial 16S marker was established.

No matching current StrainInfo native object, deposit link, assembly or
related-record row was found by target/deposit/legacy-link searches.
The live StrainInfo 394394 page exposed only a JavaScript application
shell, so its current deposit assertions were not verified. BacDive's
legacy link cannot by itself authorize a StrainInfo deposit or sequence
join. The pinned SI-ID162447 object at
`data/straininfo/records.jsonl.gz:115212` instead concerns CBS 394.67,
SI-DP430303; matching BacDive's numeric ID does not identify the strain.
Its exclusion at `data/straininfo/exclusions.tsv:43627` is unrelated.

Other numeric native hits were read and excluded: 162447 occurs as a
contig N50 in unrelated GTDB assemblies GCF_002531455.1,
GCF_016919745.1, GCA_041397325.1 and GCA_047529225.1. Number
394394 occurs as an N50 in GCF_900173495.1 and GCF_018913465.1.
Raw hits for DSM 11080, ATCC 19252, or LPSN 11080 are different
identifiers, not these JCM/MTCC deposits.

`data/seqcode/names.jsonl.gz:35238` retains name record 37129.
Its public page/API were inaccessible through the web tool; the thin
name object alone supplies no validated nomenclatural status, genome
type or cross-database equivalence. None was inferred.

Full exact-ID membership and ignored-inclusive label/URL searches of
`data/raw/lpsn_names.tsv` found no target row, despite the inspected
LPSN page. This inventory gap limits nomenclature and derived type
context. Record number 2147 is not a license to invent a CURIE mapping.
No typed phenotype, regulator, pathway or transcriptomics dataset is
asserted; iModulonDB is not applicable. Source-discovered marker evidence
does not require a causal graph or phenotype enrichment.

## Findings

- Blocker: None found.
- Major: None found.
- Minor m1: Incomplete nomenclatural provenance. The record omits the
  available LPSN status and proposed-type context, leaving readers without
  that qualification. Present identity and deposit claims remain correct;
  an absent type flag is not an explicit negative assertion. The pinned
  LPSN row is absent, so the fix belongs first to the maintained upstream
  LPSN ingestion/mapping feeding `src/taxonmech/extract.py:420`, then
  the seeder's existing nomenclature/type derivation and regression tests.
  The upstream cause is unresolved because configured transforms were
  unavailable. Do not add a hand-curated generated YAML fragment.

## Recommended Edits

1. Investigate upstream LPSN source coverage for the inspected name and
   establish its supported NCBI/deposit relationships. Retain source status
   and proposed-type qualifications. Do not infer publication validity
   from NCBI's rank or BacDive's type flag.
2. In a separately authorized extraction change, test that negative and
   qualified status phrases are not interpreted as positive booleans.
   `src/taxonmech/extract.py:479` and line 481 currently use substring
   checks; any newly ingested status must be tested before regeneration.
   This is a follow-up risk for adding the missing row, not a false field
   currently present in this YAML.
3. Regenerate inventories and run dry-run/canary steps only after the
   maintained source fix. Retain KC608148 as a marker reference, never
   a genome. Do not fabricate StrainInfo joins, add inferred phenotypes
   or promote human review status.

## Follow-up Checks

Add focused extraction/status tests alongside existing source tests and
same-taxon deposit/type regression coverage in `tests/test_seed.py`.
Run those tests and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, run both focused validators, inspect
negative status handling and qualified type context, and ensure the strain
count and NCBI identity remain unchanged. Run `just verify-corpus` and
full QC for regenerated outputs. Resolve upstream transform availability
before claiming the exact LPSN omission mechanism or MediaDive edge.

## Additional Notes

The only manual write is this report; strict validation wrote its standard
diagnostic. No record, source, prior report, history or status was edited.
Ignored files were included via full structured reads, `find`, and
`rg --no-ignore --hidden`, using `-z` for compressed sources. No source
refresh, generator, paid research, GitHub mutation or cross-repository
write occurred. No Eukaryota record was re-reviewed. Optional enrichment
gaps are distinguished from incorrect asserted identity or genome links.
