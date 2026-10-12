# YAML Record Review: Senegalimassilia anaerobia JC110

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/senegalimassilia_anaerobia_jc110.yaml`
- Started UTC: 2026-10-05T08:06:17Z
- Finished UTC: 2026-10-05T08:12:57Z
- Verdict: needs curation

## Target

Read the entire 84-line generated `TaxonRecord` for `NCBITaxon:1034345`, Senegalimassilia anaerobia JC110. It is a `STRAIN` in `BACTERIA`, parent `NCBITaxon:1473216`, with code 11, `EXACT` grounding, `SEEDED` mapping status, a GTDB species mapping, three exact synonyms, and zero inventoried strains. Its attestations count one NCBITAXON name, 50 GTDB genomes, and four MADIN trait assertions.

The target is distinct from the parent species and from the unrelated nitrogen-fixing bacterium JC110, `NCBITaxon:119294`. Shared bare strain designation is not an identity join.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/madin_taxa.tsv`, `curation/seed_scope.tsv`, and their extractor/seeder paths. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/senegalimassilia_anaerobia_jc110.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/senegalimassilia_anaerobia_jc110.yaml --out /private/tmp/jc110-strict-20261005.tsv`: exit 0; one file scanned, zero error files or rows.
- Structured comparisons passed identity, full lineage, NCBI attestation, unique path, scope, and inline-event checks. Additional assertions verified both NCBI synonyms and every represented GTDB/MADIN ID, label, predicate, count, and unit against the inventories. Reproducing an input does not establish correct biological scope.
- `just verify-corpus`: not run; full-corpus-only. Its inspected `--max-diffs` option limits diagnostics, not target scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive target history searches found no separate artifact. The inline seed event was inspected.
- Live GTDB tree and representative-genome pages were inaccessible through the web tool. The complete pinned RS232 species membership was checked locally instead.
- Original kg-microbe GTDB and Madin KGX files were not available at the configured checkout paths. An ignored-inclusive filename search of that checkout found no corresponding transformed files. Consequently the four Madin edges were not independently recounted; their committed inventory row was verified.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221578` supports the target's identity, rank, parent, code, and two NCBI synonyms. Three complete native name objects at `data/catalog/ncbi_names-0005.jsonl.gz` lines 30941-30943 retain both synonyms and the scientific name, with empty unique-name fields.

Complete live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034345&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034345) responses agree with `STRAIN` and parent 1473216. The inspected [browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034345&mode=Info) instead displays no rank. This source-surface discrepancy is preserved; the pinned primary inventory and both structured services support the YAML rank. None makes JC110 the entire species.

The ten root-first ancestors match the pinned backbone in identifier, label, and rank: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 201174 Actinomycetota, 84998 Coriobacteriia, 84999 Coriobacteriales, 84107 Coriobacteriaceae, 1473205 Senegalimassilia, and 1473216 Senegalimassilia anaerobia. NCBI lineage is retained rather than reconciled with the Eggerthellaceae placement in GTDB/LPSN-derived metadata.

No target children, merged-ID rows, dropped rows, or exact target type-material rows were found in complete corresponding inventory scans. Type-material assertions for JC110, DSM 25959, and CSUR P147 occur under the parent species; their absence under the strain ID is not biological absence of type status.

## Evidence

`data/taxa/PATHS.tsv:14042` uniquely maps the target slug. `curation/seed_scope.tsv:36158`, added 2026-09-12, agrees with the reason in the seed event dated 2026-09-13T17:54:04Z. `data/raw/madin_taxa.tsv:646` supports four trait assertions, not four strains or a specific phenotype. The other five mapped-source tables have no entry directly under this child taxon.

`data/raw/gtdb_mappings.tsv:1391` maps `GTDB:s__Senegalimassilia_anaerobia` to this strain by `skos:closeMatch` with 50 genomes. `data/raw/gtdb_species.tsv:164526` independently stores that species count. The same GTDB species has five further mapping rows: the parent species at line 31830 and NCBI taxa 1714350, 1883427, 1898203, and 1922200 at lines 50191, 76302, 83667, and 97065. Those rows use `skos:broadMatch`; their existence is not an instruction to copy that predicate onto this child.

An ignored-inclusive scan of every `data/catalog/gtdb_genomes-*.jsonl.gz` shard parsed all exact terminal species matches and found **50 RS232 genome rows**. Their `ncbi_taxid` distribution is 41 under 1473216, one under 1034345, three each under 1714350 and 1922200, and one each under 1883427 and 1898203. Thus the count is correct for the source species cluster, not a count of JC110 genomes.

The complete representative row at `data/catalog/gtdb_genomes-0005.jsonl.gz:20707` is `RS_GCF_000236865.1`, with JC110, `ncbi_taxid: 1034345`, and `ncbi_species_taxid: 1473216`. Full counterexample rows were also inspected: `RS_GCF_048250375.1` at shard 0009 line 16151 is MAG2756, and `RS_GCF_902374535.1` at shard 0000 line 49019 is MGYG-HGUT-01387. Neither is asserted to be JC110 in these source records. Matching assembly statistics do not establish equivalence. `data/catalog/MANIFEST.json` identifies this catalog as RS232; no live GTDB count is claimed.

The inspected [LPSN species page](https://lpsn.dsmz.de/species/senegalimassilia-anaerobia), record 791410, gives the validly published correct name, the corrected genus spelling, and type designations JC110, DSM 25959, and CSUR P147. It links marker JF824809. The complete mapped LPSN row at `data/raw/lpsn_names.tsv:28261` attaches the species name and GTDB species identifier to **1473216**, not 1034345.

The complete [BacDive 22980 record](https://bacdive.dsmz.de/strain/22980) identity/sequence sections and its native projection at `data/bacdive/records.jsonl.gz:22785` support JC110 and the two culture deposits. BacDive's taxon assignment is explicitly species-level, 1473216. `data/raw/bacdive_strains.tsv:22786` preserves that assignment. This explains the target's zero BacDive-derived strain count.

The parent `data/taxa/bacteria/senegalimassilia_anaerobia.yaml` was fully read as supporting context, not independently assigned a review verdict. It already contains BacDive 22980, its type flag, both deposits, two source-specific GenBank assembly assertions, IMG and BV-BRC assertions, and related identifiers. The JC110 genome associations are therefore not missing corpus-wide.

Exact BacDive-ID scans of all seven strain/genome/related crosswalks found two assembly rows, three other-genome rows, five ordinary related rows, two StrainInfo related rows, and no StrainInfo assembly or ATB link rows. BacDive preserves unversioned `GCA_000236865`, while GOLD explicitly supplies `GCA_000236865.1`; these must not be rewritten into one source assertion. IMG `2547132148` and BV-BRC `1034345.3` are independently typed genome references.

Complete native GOLD organism, project, and analysis objects were inspected at `data/gold/organisms.jsonl.gz:15253`, `projects.jsonl.gz:14752`, and `analyses.jsonl.gz:11795`. They preserve the chain DSM 25959 -> Go0017854 -> Gp0017854 -> Ga0019646, with explicit GenBank/IMG fields and sample SAMEA2272806. The separate CSUR P147 organism Go0615115 was inspected but not given another organism's analysis links. The native StrainInfo record at `data/straininfo/records.jsonl.gz:301177` identifies SI-ID 403288, its own available DSM 25959 deposit SI-DP 910354, and record-version DOI 10.60712/SI-ID403288.2; it supplies no sequence objects. No genome is inferred from strain-group membership.

Live [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000236865.1/dataset_report), exact-taxid Assembly search, and ESummary confirm one assembly result with current paired GCF_000236865.1/GCA_000236865.1, scaffold level, JC110, and SAMEA2272806. ESummary explicitly reports identical GenBank/RefSeq pairing. PRJEA70543 is the GenBank project; PRJNA224116 is also reported on the RefSeq side but occurs across unrelated genomes and is not an isolate-identity key. Complete local GenBank, RefSeq, and BV-BRC objects corroborate these identifiers.

Full [JF824809.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF824809.1) identifies a 1341-base partial 16S sequence from JC110, taxon 1034345, with type-material qualification. Full [CAEM00000000.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/CAEM00000000.1) identifies the WGS project and its contig range; its master-record length is not an 84-base genome. These two explicitly cited sequence records were inspected, not every nucleotide component in NCBI.

Primary PubMed metadata/abstract for [PMID 24019984](https://pubmed.ncbi.nlm.nih.gov/24019984/) and the publisher's [2013 original description](https://link.springer.com/article/10.4056/sigs.3246665) were inspected. The introduction, classification text, genome-history/assembly sections, and species description explicitly connect JC110 to CSUR P147 and DSMZ 25959 and identify JF824809 and CAEM00000000. The paper's historical assembly statistics differ from current NCBI metadata; no historical statistic was used to overwrite current source fields. Tables and figures were not separately inspected. None of the paper's growth, biochemical, or susceptibility observations was generalized into a new taxon claim.

## Completeness

The represented NCBI identity, lineage, code, NCBI synonyms, source counts, and inline provenance are supported. Optional phenotype and causal-graph sections are correctly absent; iModulonDB is not applicable to the claims represented.

Zero inventoried strains is reproducible under the current source-classification rule: `seed.py:483` gathers BacDive entries under the target or its descendants, not its ancestors. BacDive files JC110 at the parent. Changing that assignment or exposing an evidence-backed association on both surfaces requires an explicit maintained policy, not a name-based inheritance rule or direct YAML patch.

Ignored-inclusive searches covered hidden and compressed contents under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding generic `SOURCE.json` descriptors. A narrowed target-ID/JC110 search returned 33 contexts in total, including the legacy-path context returned in its initial output; unrelated nitrogen-fixing JC110 entries were rejected. Refined accession/sample/deposit/project/publication searches returned 30 contexts, which were inspected. Exact source-table and strain-crosswalk checks, rather than broad substring misses, support the stated absences.

The initial species-wide search output was truncated. A later exploratory search including shared RefSeq project PRJNA224116 produced many unrelated matches and was deliberately terminated; its output is not exhaustive evidence and was not used for absence or identity conclusions. The completed refined search excluded that non-discriminating project. SeqCode name-only records were inspected as discovery context, not as strain mappings.

## Findings

**Major M1: A GTDB species concept is promoted to an exact synonym of one strain.** Target lines 52-55 assert Senegalimassilia anaerobia as an `EXACT_SYNONYM` of JC110. Lines 40-44 and 67-72 carry the corresponding species-to-strain `closeMatch`. The schema's mapping semantics describe closeMatch as denoting the same species, but this record is explicitly a child strain. Native GTDB membership shows 50 source-cluster genomes and only one exact JC110 taxon assignment. Being the representative/type strain does not make the strain identical to the species.

The value 50 itself is supported as the species cluster's volume; it is not a separate count error. The defect is the cross-rank identity interpretation. `src/taxonmech/extract.py:501` preserves upstream GTDB mapping rows, and `src/taxonmech/seed.py:451` treats closeMatch as identity without a rank guard before emitting the exact synonym at line 468. The maintained owners are the upstream kg-microbe GTDB mapping transform, the extracted `data/raw/gtdb_mappings.tsv`, and TaxonMech's seeder interpretation. This is one linked scope finding, not separate duplicate findings for each emitted field.

Counts: 0 blocker, 1 major, 0 minor.

## Recommended Edits

1. Correct or explicitly qualify the upstream species-to-strain mapping. Keep JC110's NCBI identity unchanged. The existing parent-species mapping and LPSN association provide the species-level context, but do not silently rewrite all predicates or infer a new reconciled taxonomy.
2. Add a rank-aware guard and regression test around `src/taxonmech/seed.py` GTDB synonym/xref promotion. A species-cluster match to a strain must not yield a bare species `EXACT_SYNONYM`. Preserve source provenance separately when retaining a non-equivalence classification association. Re-extract and regenerate through the validated writer only in an authorized curation change.
3. Optional usability follow-up: expose an explicitly evidenced route from this strain taxon to the already-present parent-record BacDive entry. Preserve BacDive's reported species classification, whole deposit identifiers, source chains, and supplied accession versions. Do not copy all parent strains or genomes down to every child.

## Follow-up Checks

Test a species-level GTDB cluster mapped to this `STRAIN` and verify that exact-synonym promotion is rejected or correctly scoped while supported species-level mappings still work. Check the resulting mapping predicate in its declared source-to-target direction, and verify that source-cluster counts remain distinguished from exact-strain assembly counts.

After authorized upstream/seeder changes, rerun extraction, validated seeding, focused schema/strict validators, and full corpus reproduction. Recheck both this record and the parent for preserved source provenance and no accidental strain/genome duplication. Resolve the original Madin-edge and live-GTDB access limits before claiming those independent checks completed.

## Additional Notes

The review adds only this report. No record, source, earlier report, generated page, history, or status was changed. All invoked sessions reached a terminal state, including the deliberately stopped broad search.

The NCBI browser/structured rank difference, NCBI versus GTDB/LPSN lineage differences, source-level placement of BacDive 22980, and historical/current assembly-statistic differences remain explicit. None justifies guessing identifiers, replacing NCBI lineage, or treating shared taxonomy, projects, names, or sequence statistics as genome equivalence.
