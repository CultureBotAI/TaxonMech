# YAML Record Review: Leptospira borgpetersenii serovar Hardjo-bovis str. Sponselee

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_borgpetersenii_serovar_hardjo_bovis_str_sponselee.yaml`
- Started UTC: 2026-10-03T15:15:39Z
- Finished UTC: 2026-10-03T15:17:55Z
- Verdict: needs curation

## Target

Read all 86 lines of the generated `TaxonRecord` before judgement.
The target is `NCBITaxon:1303729`, rank `STRAIN`, domain `BACTERIA`,
parent `NCBITaxon:338217`, genetic code 11. Grounding is `EXACT` and
mapping status `SEEDED`. There is one GTDB mapping, one GTDB exact
synonym, one equivalence xref, four source attestations and one seed
event. Strain count is zero, with no strain list, nomenclature block,
genome links, experimental claims or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_borgpetersenii_serovar_hardjo_bovis_str_sponselee.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_borgpetersenii_serovar_hardjo_bovis_str_sponselee.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison confirms identity, rank, parent,
  genetic code and all eleven root-first lineage entries. No target
  children occur in the pinned backbone.
- Complete exact-field inventory scans reproduce the single GTDB mapping,
  GOLD count 1, Madin count 1 and zero BacDive membership. No direct
  LPSN, MediaDive or BactoTraits rows were found.
- Full exact-terminal-species census of the native GTDB genome catalogs
  confirms 190 distinct accessions, only two with target taxon 1303729.
  Source reproduction does not establish species/strain equivalence.
- `just verify-corpus`: Not checked; full-corpus-only, with no focused
  substitute invented. Global provenance, rendered products, exports,
  source refreshes and genome sequences were not audited.
- Ignored-inclusive ID, full-label and slug searches found no target
  standalone history entry; history validation had no target. Strict
  validation covered the embedded event. Graph/product gates do not apply.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308128` and the complete native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30676` support the exact strain
identity. The PATHS index resolves it to this single slug.

The retrieved [NCBI browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1303729)
has older no-rank/Spirochaetia values. These were not silently substituted
for the pinned record. Directly inspected current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303729&retmode=xml)
reports strain rank, class Leptospiria (3118682), parent 338217, code 11
and the complete non-root lineage matching the YAML.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303729)
also confirms strain rank and all eleven ancestor IDs including root.
The NCBI identity is supported; the GTDB equivalence is not.

The similarly named Sponselee CDC taxon is not interchangeable with this
target: [NCBI EFetch for 1218567](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1218567&retmode=xml)
still returns that separate strain identifier under the same parent.
Native genome metadata sometimes classify CDC-designated assemblies as
1303729; preserve that source classification without merging the taxa.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308128` | Exact ID and label; snapshot 2026-09-13 |
| GTDB 190 GENOME | `data/raw/gtdb_species.tsv:110758`; `gtdb_mappings.tsv:17464` | Species-cluster count reproduced, not strain-specific |
| GOLD 1 ORGANISM | `data/raw/gold_organisms.tsv:7435` | Direct target count reproduced |
| MADIN 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11829` | Count reproduced; no particular phenotype is asserted |

The scope row at `curation/seed_scope.tsv:28042` admits the target on
2026-09-12 with four sources. The embedded 2026-09-13T17:54:04Z event
preserves that reason and the actual four source names. It does not claim
human review. Counts with different units must not be added together.

The native GTDB census was parsed across all `gtdb_genomes-*.jsonl.gz`
files, selecting terminal taxonomy exactly `s__Leptospira borgpetersenii`.
All 190 rows have distinct accessions. Only RS_GCF_000355135.1 and
RS_GCF_000346975.1 have `ncbi_taxid: 1303729`; their complete objects are
at `gtdb_genomes-0002.jsonl.gz:29676` and
`gtdb_genomes-0008.jsonl.gz:10057`. Their strain fields are respectively
Sponselee and Sponselee CDC, not registered culture-deposit identifiers.
The representative is RS_GCF_003046425.1, strain DSM 21538, taxon 280504,
serovar Javanica. Other rows include Ballum and unrelated strain
designations. This establishes the broader species-cluster scope.
GTDB taxon/genome pages were inaccessible through the web tool; the
inspected pinned primary metadata supply the evidence, not search snippets.

Native GOLD objects retain the explicit chain Go0036328 -> Gp0036328 ->
Ga0039054, with GCA_000355135.1 and IMG 2600255131, project PRJNA191805,
and sample SAMN01994529. Source locations are
`data/gold/organisms.jsonl.gz:30824`, `projects.jsonl.gz:24624` and
`analyses.jsonl.gz:24840`. The organism has no culture-collection value;
Sponselee is a bare strain name. The analogous CDC chain Go0033550 ->
Gp0033550 -> Ga0017014 belongs to source taxon 1218567 and must remain
distinct. GOLD's live organism page was inaccessible; pinned objects
were inspected directly.

Current pinned NCBI GenBank/RefSeq objects preserve both assembly
families: GCA/GCF_000355135.1 with Sponselee/SAMN01994529 and
GCA/GCF_000346975.1 with Sponselee CDC/SAMN01801594. Their current catalog
taxon is 1303729. BV-BRC objects 1303729.3 and 1218567.3 likewise
preserve their own opaque IDs and strain designations. Their historical
Spirochaetia classification does not override the NCBI lineage in the YAML.

## Completeness

The complete source search included ignored files and compressed native
catalogs under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/`, using target ID, Sponselee and slug.
Related hits were inspected, not treated as interchangeable identities.

BacDive 171179 and 171214 have designations LEP1181, Sponselee and
LEP1444, Sponselee, but both are classified at species taxon 174.
Their complete native records at `data/bacdive/records.jsonl.gz:93409`
and 93444 contain CRBIP6.1181 and CRBIP6.1444 and empty sequence objects.
Corresponding StrainInfo objects SI-ID373063/SI-DP859376 and
SI-ID372767/SI-DP859080 also name species 174 and contain no sequences.
A shared bare designation does not justify pulling these parent-species
records into this strain taxon's singleton subtree. Count zero is a
BacDive classification count, not a claim that no cultures or genomes exist.

Ignored-inclusive compressed searches of `data/atb/` and the complete
ATB catalog also used both discovered sample IDs. The native rows are:

- `data/catalog/allthebacteria.tsv.xz:1014763`: SAMN01994529,
  SRR799785, ERZ4062788, available FASTA and PASS filters.
- `data/catalog/allthebacteria.tsv.xz:1011735`: SAMN01801594,
  SRR611245, ERZ3637941, META_FAIL; excluded from strain crosslinks.

No corresponding hit appeared in the committed ATB overlap. An available
FASTA is not sufficient: there is no existing target BacDive strain with
a supported deposit-to-BioSample assertion. These native genome leads
must not become fabricated culture joins or genome-equivalence claims.
The missing strain-genome links are therefore not a required-field defect
under the current model. Broader native taxon-genome representation would
be a separate modeling task, not a generated-YAML patch.

No LPSN name directly maps to this strain taxon in the complete inventory.
Omitted nomenclature and type flags must not be read as negative claims.
No DOI/PMID, gene, locus, regulator, pathway or transcriptomic dataset is
asserted. iModulonDB is not applicable to an unspecified trait-count
attestation; no phenotype or causal graph is inferred.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. YAML lines 49-54 promote
  `GTDB:s__Leptospira_borgpetersenii` into an `EXACT_SYNONYM` and an
  equivalence xref for the Sponselee strain. The 190-member native cluster
  includes other serovars and strains, and only two rows carry this taxon
  ID. Its membership supports classification context, not identity.
  `src/taxonmech/seed.py:451` accepts `skos:closeMatch` as identity without
  rank/scope checking; lines 466-469 emit the exact synonym and xref.
  This conflicts with the true-equivalence contract at
  `src/taxonmech/schema/taxonmech.yaml:180`. Maintained owners are
  `src/taxonmech/seed.py` and regression tests in `tests/test_seed.py`;
  the source predicate in kg-microbe also warrants review. The 190-genome
  count is numerically correct for the species cluster, not this strain.
- Minor: None found.

## Recommended Edits

1. Make the maintained seeder's equivalence decision rank/scope-aware.
   Preserve the GTDB classification relationship and its provenance, but
   do not generate a species exact synonym or equivalence xref on this
   strain record without genuine identity evidence. Label the cluster
   count's scope explicitly. Do not replace 190 with 2 while retaining
   species-cluster count semantics.
2. Add a regression in `tests/test_seed.py` for this strain/species pattern,
   retaining valid same-scope species mappings. Review kg-microbe's mapping
   predicate at its maintained source; do not hand-patch the extracted
   TSV or guess a replacement predicate direction.
3. After an authorized implementation, follow the dry-run/canary workflow
   and regenerate affected records. Do not merge Sponselee CDC, infer a
   culture join, edit generated YAML manually, or promote human review status.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the actual YAML: GTDB classification retained, unsupported exact synonym
and xref absent, cluster count clearly scoped, NCBI identity unchanged.
Repeat the exact-terminal GTDB census and ensure the two target-classified
genomes remain distinct from species-cluster membership and culture identity.
Run `just verify-corpus` and the full QC workflow for the resulting
regeneration. M1 remains unresolved; this review made no corrective edit.

## Additional Notes

Absence claims are bounded to inspected pinned inputs and use full
structured reads or `rg --no-ignore --hidden`, including `-z` for
compressed sources. Prior-report absence was checked with `find`.
Current NCBI API reads required network escalation after sandbox DNS had
failed earlier in this review session. Web-rendered and snapshot sources
were not assumed to be equally current.

The only manual write is this new report; strict validation wrote its
standard diagnostic. No target YAML, prior report, source, history or
status was changed. No generator, refresh, paid research, GitHub mutation
or cross-repository write occurred. Eukaryota was not re-reviewed.
