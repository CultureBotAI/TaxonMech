# YAML Record Review: Staphylococcus aureus M1407

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m1407.yaml`
- Started UTC: 2026-10-03T15:53:50Z
- Finished UTC: 2026-10-03T15:55:14Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord`, identifying `NCBITaxon:1303786`
as strain M1407, domain `BACTERIA`, parent `NCBITaxon:1280`, genetic
code 11. Grounding is `EXACT`; status is `SEEDED`. Ten lineage entries,
one GTDB mapping, one GTDB exact synonym, one equivalence xref, three
attestations and one seed event are present. Strain count is zero. No
strain list, genome links, nomenclature, experimental claims or causal
graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m1407.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m1407.yaml`:
  PASS; one file, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Structured comparison against the complete NCBI backbone reproduces
  rank, parent, genetic code and all ten lineage entries; no target
  children exist there. Complete exact-field inventory scans reproduce
  GTDB and Madin rows; direct BacDive, LPSN, GOLD, MediaDive and
  BactoTraits taxon inventory membership is absent.
- A fresh census across every GTDB genome shard reproduces 19,502
  distinct accessions, 4,209 distinct source taxon IDs and one member
  assigned to taxon 1303786 for the exact terminal species.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute invented. Full QC, global provenance, rendered products,
  exports and genome sequences were not audited.
- No target standalone history entry was found by ignored-inclusive
  search; strict validation checked the embedded event. Standalone
  history validation had no target. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308142` and native name object
`data/catalog/ncbi_names-0007.jsonl.gz:30689` support this exact
strain identity. NCBI synonym fields are empty. The PATHS index has one
row for this identifier/slug.

The NCBI browser page was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303786&retmode=xml)
confirms ID, scientific name, strain rank, Bacteria division, parent 1280,
genetic code 11 and full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303786)
confirms rank and all ten ancestor IDs including root. Read-only public
API requests used network escalation after the established sandbox DNS
failure. NCBI grounding is supported.

Current NCBI order Caryophanales is retained. Older native BV-BRC/GTDB
NCBI fields use Bacillales; GTDB's own taxonomy uses Staphylococcales.
These source hierarchies and ages remain distinct. They do not override
the NCBI lineage or establish species/strain equivalence.

## Evidence

| Assertion | Inspected source | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308142` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_mappings.tsv:17474`; `gtdb_species.tsv:168198` | Correct species-cluster count, not M1407 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11839` | Count reproduced; no named trait claimed |

Scope row `curation/seed_scope.tsv:42164` admits this taxon on
2026-09-12 with three sources. The 2026-09-13T17:54:04Z seed event
preserves that reason and the actual source names without claiming
human review. Counts with different units must not be combined.

The census matches terminal species exactly `s__Staphylococcus aureus`,
excluding aureus_A. Target member RS_GCF_000364125.1 is preserved in
the complete object at `data/catalog/gtdb_genomes-0016.jsonl.gz:42477`,
with M1407, taxon 1303786, SAMN02596941 and GCA_000364125.1.
The representative object at `data/catalog/gtdb_genomes-0006.jsonl.gz:29983`
instead describes RS_GCF_001027105.1, DSM 20231, taxon 1280. The
GTDB taxon-page request during this turn was inaccessible; pinned
primary metadata establish cluster scope and target membership.

Complete native NCBI objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:10018`
and `data/catalog/ncbi_refseq-0000.jsonl.gz:8743` describe the identical
GCA/GCF_000364125.1 pair, assembly Stap_aure_M1407_V1, taxon
1303786, strain M1407, sample SAMN02596941, 11 contigs, three
scaffolds and 2,835,415 bp including gaps. Preserve GenBank project
PRJNA192847 separately from RefSeq umbrella PRJNA224116. Complete
BV-BRC object `data/bvbrc/bvbrc-0001.jsonl.gz:23832` supports genome
1303786.3, GCA_000364125.1, PRJNA192847 and the same strain/sample.

Complete GOLD objects at `data/gold/organisms.jsonl.gz:31295`,
`data/gold/projects.jsonl.gz:25170` and
`data/gold/analyses.jsonl.gz:11541` retain
Go0037001 -> Gp0037001 -> Ga0018166, IMG 2545824670,
GCA_000364125.1, PRJNA192847 and SAMN02596941. The organism
has no culture-collection value, only bare designation M1407. Native
GOLD identity evidence is not a KGX-derived GOLD taxon count; the
different derivations remain separate.

## Completeness

Ignored-inclusive searches of all compressed JSONL files under
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/` used ID, designation and slug.
Matching complete objects were read. Excluded near matches include:

- StrainInfo SI-ID328606, `data/straininfo/records.jsonl.gz:255315`,
  Neurospora crassa taxon 5141, FGSC 4155, deposit SI-DP775299,
  alias M1407 A.
- StrainInfo SI-ID356558, `data/straininfo/records.jsonl.gz:279057`,
  Symbiodinium taxon 2949, CCAC 0047, deposit SI-DP828431, alias M1407.
- GOLD Gp0613715 at `data/gold/projects.jsonl.gz:457097`, describing
  Panicum virgatum J005.B gene-expression analysis M1407.21GWRNA,
  organism Go0597144, PRJNA1384029 and SAMN54148375.
- NCBI `data/catalog/ncbi_genbank-0017.jsonl.gz:3694` and GTDB
  `data/catalog/gtdb_genomes-0017.jsonl.gz:14210`, GCA_018646865.1,
  Cryomorphaceae bacterium taxon 1898111, isolate SI034_bin14,
  SAMN14913802. Here 1303786 is genome length, not a taxon match.

No target BacDive or StrainInfo native object was found in that bounded
search. The full BacDive membership scan and singleton subtree support
strain count zero, not absence of genomes. Genome metadata exist, but
the documented model attaches them to supported BacDive strain rows via
explicit source assertions or eligible culture-deposit joins. A bare
designation or taxon ID is not a culture-deposit key. Do not copy unrelated
deposits or fabricate a strain row to expose catalog-only genome leads.

Ignored-inclusive searches of raw strain assembly/genome/related tables,
StrainInfo link/assembly/exclusion tables and history found no target ID,
M1407 designation or slug. Compressed searches of `data/atb/` and the
complete `data/catalog/allthebacteria.tsv.xz`, also using SAMN02596941,
found no target/sample result. These are pinned-source boundaries, not
biological absence claims.

No same-taxon LPSN inventory row supports nomenclature or type flags.
Do not inherit those claims from the parent species. No DOI, PMID, gene,
regulator, pathway, named phenotype or transcriptomics dataset is asserted;
iModulonDB is not applicable. Unspecified Madin counts are not evidence
for an experimental phenotype or causal graph.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. GTDB's exact synonym and
  equivalence xref identify strain M1407 with the broader
  `GTDB:s__Staphylococcus_aureus` species cluster. The 19,502-member
  cluster spans many strains; only one member has target taxon 1303786.
  Classification membership does not establish identity. The maintained
  rule at `src/taxonmech/seed.py:451` promotes `skos:closeMatch`
  without rank/scope checks; lines 466-469 add the synonym/xref, contrary
  to `src/taxonmech/schema/taxonmech.yaml:180`. Fix owners:
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate
  upstream kg-microbe predicate review. Count 19,502 is correct only at
  species-cluster scope, not as an M1407 genome count.
- Minor: None found.

## Recommended Edits

1. Make seeder equivalence rank/scope-aware. Preserve GTDB classification
   and source provenance while suppressing unsupported species exact
   synonym/xref for this strain. Explicitly scope the species-cluster
   count; do not replace 19,502 with 1 while retaining cluster semantics.
2. Add a strain/species regression in `tests/test_seed.py` and preserve
   supported same-scope mappings. Review the source predicate upstream,
   without guessing relation direction or hand-patching extracted TSVs.
3. Follow authorized dry-run/canary/regeneration steps after fixing the
   maintained rule. Do not hand-edit YAML, invent culture joins or
   promote human review status.

## Follow-up Checks

Run the regression with
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
retained classification, explicit count scope, suppressed unsupported
synonym/xref and unchanged NCBI identity. Repeat the exact-terminal GTDB
census/member check; run `just verify-corpus` and full QC. M1 remains
unresolved; this report does not implement the correction.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, or `rg --no-ignore --hidden`, adding `-z` for compressed sources.
The only manual write is this new report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. Eukaryota records were not re-reviewed;
unrelated native objects were inspected only to exclude false matches.
