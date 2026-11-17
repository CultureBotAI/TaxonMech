# Record review: Archaeoglobus lithotrophicus

- Review: 20261021T075339Z-archaeoglobus_lithotrophicus
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-20T07:30:25Z
- Finished UTC: 2026-10-21T07:53:39Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Archaeoglobus lithotrophicus has supported exact NCBI identity and source-scoped representation. No record-specific import defect was established. Historical aggregate counts remain inventory-verified without an independent original-edge recount.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Original unreviewed path-order position 139; batch-0014 target 9. Excluded 185 actual targets from validated freshmain and thirteen committed isolated branches; full corpus enumeration includes ignored files.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01ca63effdf8c03a644df893ba6129b2d8448ea4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:138903 | data/taxa/archaea/archaeoglobus_lithotrophicus.yaml | generated | Archaeoglobus lithotrophicus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:138903 | NCBITaxon:138903 denotes Archaeoglobus lithotrophicus at SPECIES rank beneath NCBITaxon:2233, genetic code 11. All 9 carried ancestors agree with the pinned inventory and captured official NCBI response; the response omits only the root entry. Source name classes remain distinct from taxon classification. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:138903 | Complete direct reads of twelve source/scope/path tables, including ignored files, support 0 imported BacDive strains over the exact target subtree (0 descendant taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME; MADIN 2 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions are not interchangeable and do not prove phenotype or biological genome equivalence. |
| Imported strain links | not_applicable | False | NCBITaxon:138903 | No imported BacDive strain or strain-level link is asserted; no deposit is inferred from an isolate designation. |
| Original manifest-pinned aggregate recounts | unavailable | True | NCBITaxon:138903 | Pinned projection counts agree: [{"source":"MADIN","count":2,"unit":"TRAIT_ASSERTION","raw_projection_agrees":true,"historical_primary_aggregate_checked":false}]. Original aggregate edges were not independently recounted. |
| Native strict record validation | passed | True | NCBITaxon:138903 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:138903 | Actual terminal exit code 0. All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:138903 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:138903 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:138903 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33) |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:138903.

NCBITaxon:138903 denotes Archaeoglobus lithotrophicus at SPECIES rank beneath NCBITaxon:2233, genetic code 11. All 9 carried ancestors agree with the pinned inventory and captured official NCBI response; the response omits only the root entry. Source name classes remain distinct from taxon classification.

### Name classes and nomenclatural scope

nomenclature: supported. Targets: NCBITaxon:138903.

NCBI 138903 remains species Archaeoglobus lithotrophicus. The quoted 1993 authority and includes-name Archaeoglobus lithotrophicus TF2 remain RELATED_SYNONYM, rather than strain equivalence or a valid-publication assertion. No LPSN nomenclature is asserted in this native record. Current independent nomenclatural status was not fetched; no unsupported claim of validation is inferred from taxonomy presence.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:138903.

Complete direct reads of twelve source/scope/path tables, including ignored files, support 0 imported BacDive strains over the exact target subtree (0 descendant taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME; MADIN 2 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions are not interchangeable and do not prove phenotype or biological genome equivalence.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:138903.

EXACT grounding and SEEDED status agree with NCBI identity. The sole seed event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction time; no native status/history was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### recover-pinned-aggregate-inputs

Recover manifest-hash-matching original aggregate inputs and independently recount the exact target assertions through the maintained extractor; do not edit generated YAML.

- Require exact original input SHA-256 before using it as historical evidence.
- Recount only the exact target with each source's own assertion unit and compare to its pinned inventory row.
- Record any discrepancy in a new review observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeoglobus_lithotrophicus.yaml; entire TaxonRecord; identifier=NCBITaxon:138903 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"}; line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"}; line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"}; line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 28042: {"taxon_id":"NCBITaxon:138903","label":"Archaeoglobus lithotrophicus","rank":"SPECIES","parent_id":"NCBITaxon:2233","genetic_code":"11","exact_synonyms":"","related_synonyms":"\"Archaeoglobus lithotrophicus\" Stetter et al. 1993&#124;Archaeoglobus lithotrophicus TF2","broad_synonyms":"","attested_by":"ncbitaxon&#124;madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"}; line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"}; line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 53995: {"identifier":"NCBITaxon:138903","added":"2026-09-12","reason":"attested rule: Archaeoglobus lithotrophicus, 2 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 141436: {"identifier":"NCBITaxon:138903","slug":"archaeoglobus_lithotrophicus"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2012529,2250530,1935016,2234,224325,1344584,403219,1121009,138903,2798580; TaxaSet/Taxon[TaxId='138903']; ten-target captured response | supports | Inspected the official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact mapped and linked LPSN names; bounded inventory absence does not establish worldwide nomenclatural absence. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected direct mappings and selected clusters' reverse mappings, retaining each source predicate and taxon boundary. |
| gtdb-species | data/raw/gtdb_species.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected source species identifiers, labels, parent clusters and genome counts. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; line 13827: {"taxon_id":"NCBITaxon:138903","assertion_count":"2"} | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; exact target/subtree/source-identifier search has no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits one-to-one species closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation construction | supports | Inspected mapping ranking, qualified predicates, fixed broadMatch wording, synonym/xref construction, primary cluster counts and same-taxon type-strain derivation. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| historical-madin-edge | data/raw/MANIFEST.yaml; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv; expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24 | partial | Retained configured-path source check found bytes differing from the manifest-pinned original; this does not establish global absence. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeoglobus_lithotrophicus.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-09.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-20T07:30:31Z, finished 2026-10-20T07:30:33Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0012/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-09.tsv |
| history-receipt | just validate-history; All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. All 18 standalone history records; the generated seed event was also inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>history links: 18 record(s), 0 invalid<br>No issues found<br>18 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo; started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.<br>All checks passed!<br>1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- The review assesses exact identifiers, nomenclature, source placement and import completeness at the captured versions; it does not establish experimental phenotypes, assembly sequence equivalence or a phylogenetic species boundary.
- The original manifest-pinned aggregate source bytes were unavailable at the configured historical paths in retained hash observations. Inventory counts agree, but original aggregate-edge recounts remain unavailable; primary deposit chains do not replace those historical aggregates.
- No independent current nomenclatural authority was fetched for lithotrophicus; the record asserts only NCBI name classes and carries no valid-publication assertion.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus gate results are represented only by the corresponding terminal receipts; running gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts remain explicitly historical; new review bundles still require individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base recapture preserves target/source-table bytes; five changed guidance/scope/path/seeder inputs were explicitly reassessed. Original captures and exact transition receipts remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native receipts do not claim these later steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075339Z-archaeoglobus_lithotrophicus
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: Archaeoglobus lithotrophicus'
started_at: '2026-10-20T07:30:25Z'
finished_at: '2026-10-21T07:53:39Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author the existing generated target; this
    review changes only new review artifacts in an isolated checkout.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Archaeoglobus lithotrophicus has supported exact NCBI identity and source-scoped
  representation. No record-specific import defect was established. Historical aggregate
  counts remain inventory-verified without an independent original-edge recount.
source:
  git_revision: 01ca63effdf8c03a644df893ba6129b2d8448ea4
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 8e8fd97c64fbff27e023c7a768b4c806c98f56cd6571e7102217a2c833284df6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 4c7090b9d7fd0c6f7f2b4e47b48cbf64835e8d27b44944649e1ccd9038ce462d
    role: context
  - path: AGENTS.md
    sha256: bde64bd1943c4fc64b332cdbc76b89c1460294d9b1042beeedbfa91160a70331
    role: context
  - path: CLAUDE.md
    sha256: 7ffd88ac6de931cabf76781935be14d465472038e3bb654208b837c3e2df8258
    role: context
  - path: conf/id_label_targets.yaml
    sha256: bfd1b248f7b189cd054e15b7ad0171042a30980d2ebdbdd8e7d85cea68dde9c8
    role: context
  - path: conf/ncbi_taxdump.yaml
    sha256: 1d734bbb3ebf9d36e304d8030c5852fa4f0f306fca2849be5dec8f3dff86f887
    role: context
  - path: conf/record_review.yaml
    sha256: 366312506b771fc18fc5bfc30d5ec942b2c96212e1f4f95c463cfa1707fbebaa
    role: context
  - path: curation/seed_scope.tsv
    sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
    role: context
  - path: data/atb/MANIFEST.yaml
    sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
    role: context
  - path: data/raw/bacdive_strains.tsv
    sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
    role: context
  - path: data/raw/bactotraits_taxa.tsv
    sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
    role: context
  - path: data/raw/culture_collection_strains.tsv
    sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
    role: context
  - path: data/raw/gold_organisms.tsv
    sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
    role: context
  - path: data/raw/gtdb_mappings.tsv
    sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
    role: context
  - path: data/raw/gtdb_species.tsv
    sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
    role: context
  - path: data/raw/lpsn_names.tsv
    sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
    role: context
  - path: data/raw/madin_taxa.tsv
    sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
    role: context
  - path: data/raw/mediadive_taxa.tsv
    sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
    role: context
  - path: data/raw/ncbitaxon_taxa.tsv
    sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
    role: context
  - path: data/straininfo/MANIFEST.yaml
    sha256: 25dd601c8cf6d4d84e5cc756d1e642ebef89f565bd31967152bf0026fa072847
    role: context
  - path: data/taxa/PATHS.tsv
    sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
    role: context
  - path: data/taxa/archaea/archaeoglobus_lithotrophicus.yaml
    sha256: 47ba0f6f0c9851f5c5639c2bbac34bd9dee01d3364aaea4b1e39844f69fc1912
    role: target
  - path: docs/ALLTHEBACTERIA.md
    sha256: a1b0c298988782ad4b7dbb80c661c483a67cd0e478366eddbea7d1ba7595e7cd
    role: context
  - path: docs/CURATION.md
    sha256: 9e09c97bcd617f2b3d0090f775b80565fccc9d00e4c398ed58d3a31192a8fa8e
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
    role: context
  - path: docs/SCHEMA.md
    sha256: 9e767cebb2506f8372c65ceb5f75e5ef2df2b23c2be3727cfd198f447a6a0e30
    role: context
  - path: docs/SOURCE_COVERAGE.md
    sha256: 43f17c3c80815d395136aab53f310be3190a8d614a45fc2f4a3942faeb0bc9e9
    role: context
  - path: docs/STRAININFO.md
    sha256: 65d274e7126fcf7810da746366b0e60c1957f05df9016fb0900600932b278241
    role: context
  - path: docs/STRAIN_GENOMES.md
    sha256: 7cfdbc8a600173d6569f885b409b1543098bb6022e8764324d91879eaed2b597
    role: context
  - path: docs/record-review-profile.md
    sha256: bc2074242edcf09f510aae8d9cf40961ea0c1155ca497808765bdabfb35ee721
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: c46d88186cad450fbd47ce5176bf2afc8289252e287324245ad30090753c750e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: d3a8e398b0484fef1ce4ae13e639a03dd41467c1d597d753132e4dba04df9da3
    role: context
  - path: scripts/validate_history.py
    sha256: aa8fd8528a28cf56a92768c05d57aea7ff48745510796126f144856b8fd7ae8b
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_strict.py
    sha256: d0d75cc805cc746053076b5f75f5e6c817ab15c75a9362f8ce3be53bd4ec7382
    role: context
  - path: scripts/verify_corpus.py
    sha256: 48c4ef707543d1b836052013e8991d530d14559f9b58aa3ff9faf02c4e1ffc2e
    role: context
  - path: src/taxonmech/extract.py
    sha256: 7c5b5bf385e0c060f1cb3dbac304d05ddb941e4c83c900017a04133efd6d1822
    role: context
  - path: src/taxonmech/ncbi_taxdump.py
    sha256: 83e3bfd53721a1f85291022511de6504d84caa58e899c0fd8d1797e9f00f67cf
    role: context
  - path: src/taxonmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/taxonmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/taxonmech/schema/taxonmech.yaml
    sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
    role: context
  - path: src/taxonmech/seed.py
    sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
    role: context
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Original unreviewed path-order position 139; batch-0014 target 9. Excluded
    185 actual targets from validated freshmain and thirteen committed isolated branches;
    full corpus enumeration includes ignored files.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:138903
targets:
- target_id: NCBITaxon:138903
  path: data/taxa/archaea/archaeoglobus_lithotrophicus.yaml
  label: Archaeoglobus lithotrophicus
  record_class: TaxonRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/seed.py
    role: Maintained generated-record builder
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Maintained source inventory extractor
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/ncbi_taxdump.py
    role: Maintained NCBI primary-taxonomy projection
  - repository: CultureBotAI/TaxonMech
    path: data/raw/ncbitaxon_taxa.tsv
    role: Pinned taxon identity, name classes and carried ancestry
  - repository: CultureBotAI/TaxonMech
    path: curation/seed_scope.tsv
    role: Explicit species-or-below scope
checks:
- check_id: identity-authority
  name: Exact NCBI taxon, rank and lineage
  status: passed
  required: true
  summary: NCBITaxon:138903 denotes Archaeoglobus lithotrophicus at SPECIES rank beneath
    NCBITaxon:2233, genetic code 11. All 9 carried ancestors agree with the pinned
    inventory and captured official NCBI response; the response omits only the root
    entry. Source name classes remain distinct from taxon classification.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
- check_id: optional-inventories
  name: Complete exact identifier and name inventory search
  status: passed
  required: true
  summary: 'Complete direct reads of twelve source/scope/path tables, including ignored
    files, support 0 imported BacDive strains over the exact target subtree (0 descendant
    taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME;
    MADIN 2 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions
    are not interchangeable and do not prove phenotype or biological genome equivalence.'
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - bacdive-inventory
  - culture-inventory
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - scope-row
  - path-row
  - gtdb-species
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: No imported BacDive strain or strain-level link is asserted; no deposit
    is inferred from an isolate designation.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: historical-source-counts
  name: Original manifest-pinned aggregate recounts
  status: unavailable
  required: true
  summary: 'Pinned projection counts agree: [{"source":"MADIN","count":2,"unit":"TRAIT_ASSERTION","raw_projection_agrees":true,"historical_primary_aggregate_checked":false}].
    Original aggregate edges were not independently recounted.'
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - manifest
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - historical-madin-edge
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only; its captured
    bytes remain unchanged. Actual earlier per-target invocation; the receipt retains
    its original cwd and times.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - strict-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-strict data/taxa/archaea/archaeoglobus_lithotrophicus.yaml --out
    /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-09.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only; its captured bytes remain unchanged.
    Actual earlier per-target invocation; the receipt retains its original cwd and
    times.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 18 standalone history records; the generated
    seed event was also inspected in this target. Actual native gate execution at
    base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes
    and terminal exit codes identify these runs. Expanded-corpus gate results are
    represented only by the corresponding terminal receipts; running gates remain
    unavailable in unsaved previews. Earlier unchanged-target strict receipts remain
    explicitly historical; new review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - history-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 18 standalone history records; the generated seed event was also
    inspected in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused
    approximation. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - corpus-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph. Actual native gate execution
    at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes
    and terminal exit codes identify these runs. Expanded-corpus gate results are
    represented only by the corresponding terminal receipts; running gates remain
    unavailable in unsaved previews. Earlier unchanged-target strict receipts remain
    explicitly historical; new review bundles still require individual validation/save/check.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - products-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc, including native
    corpus-wide checks. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check. 1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - qc-receipt
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/uv-cache
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc, including native corpus-wide checks. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/archaeoglobus_lithotrophicus.yaml
  accessed_at: '2026-10-21T07:53:39Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:138903
  snapshot_sha256: 47ba0f6f0c9851f5c5639c2bbac34bd9dee01d3364aaea4b1e39844f69fc1912
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 1755: {"taxon_id":"NCBITaxon:2231","label":"Archaeoglobales","rank":"ORDER","parent_id":"NCBITaxon:183980"};
    line 1756: {"taxon_id":"NCBITaxon:2232","label":"Archaeoglobaceae","rank":"FAMILY","parent_id":"NCBITaxon:2231"};
    line 1757: {"taxon_id":"NCBITaxon:2233","label":"Archaeoglobus","rank":"GENUS","parent_id":"NCBITaxon:2232"};
    line 2981: {"taxon_id":"NCBITaxon:28890","label":"Methanobacteriota","rank":"PHYLUM","parent_id":"NCBITaxon:3366610"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 28042: {"taxon_id":"NCBITaxon:138903","label":"Archaeoglobus lithotrophicus","rank":"SPECIES","parent_id":"NCBITaxon:2233","genetic_code":"11","exact_synonyms":"","related_synonyms":"\"Archaeoglobus
    lithotrophicus\" Stetter et al. 1993|Archaeoglobus lithotrophicus TF2","broad_synonyms":"","attested_by":"ncbitaxon|madin_etal","retired_into":"","taxonomy_snapshot":"2026-09-13"};
    line 36620: {"taxon_id":"NCBITaxon:183980","label":"Archaeoglobi","rank":"CLASS","parent_id":"NCBITaxon:28890"};
    line 621140: {"taxon_id":"NCBITaxon:3366610","label":"Methanobacteriati","rank":"KINGDOM","parent_id":"NCBITaxon:2157"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 53995: {"identifier":"NCBITaxon:138903","added":"2026-09-12","reason":"attested
    rule: Archaeoglobus lithotrophicus, 2 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 141436: {"identifier":"NCBITaxon:138903","slug":"archaeoglobus_lithotrophicus"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2012529,2250530,1935016,2234,224325,1344584,403219,1121009,138903,2798580
  accessed_at: '2026-10-20T07:29:20Z'
  support: supports
  summary: 'Inspected the official response for this exact taxon: scientific name,
    rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='138903']; ten-target captured response
  snapshot_sha256: 8a3866adad1ff61fdfd0bfdd06ad5f4159708e114acc5cb803032f23e4828b9f
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected exact mapped and linked LPSN names; bounded inventory absence
    does not establish worldwide nomenclatural absence.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected direct mappings and selected clusters' reverse mappings, retaining
    each source predicate and taxon boundary.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected source species identifiers, labels, parent clusters and genome
    counts.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected exact culture-inventory associations; an isolate name or genome
    does not create an inferred deposit.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: 'line 13827: {"taxon_id":"NCBITaxon:138903","assertion_count":"2"}'
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-21T06:44:14Z'
  support: supports
  summary: Inspected the exact BactoTraits trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; exact target/subtree/source-identifier search has no match
  snapshot_sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
  search_scope: Full reads of explicitly named TSV inputs, including any ignored files;
    exact whole field/token matches. Does not assert worldwide absence.
- evidence_id: mapping-policy
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-21T07:53:39Z'
  support: supports
  summary: Policy permits one-to-one species closeMatch normalization and LPSN-linked
    species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage
    unchanged.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T07:53:39Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T07:53:39Z'
  support: supports
  summary: Inspected mapping ranking, qualified predicates, fixed broadMatch wording,
    synonym/xref construction, primary cluster counts and same-taxon type-strain derivation.
  locator: GTDB mapping construction lines 444–476; LPSN/type-strain and source-attestation
    construction
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T07:53:39Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T07:53:39Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: historical-madin-edge
  kind: search
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-19T07:30:22Z'
  support: partial
  summary: Retained configured-path source check found bytes differing from the manifest-pinned
    original; this does not establish global absence.
  locator: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv;
    expected=3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f; observed=c19bfc848e1b410548614c54a2b99e2c58452d58aeb61f972c99fcb3039a1d24
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
  search_scope: Exact configured historical input path, including ignored files; retained
    actual receipt, not a new source search.
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeoglobus_lithotrophicus.yaml
    --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-09.tsv
  accessed_at: '2026-10-20T07:30:33Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-20T07:30:31Z, finished 2026-10-20T07:30:33Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0012/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/strict-09.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: a90bcfe4c344ac902208389987c555df31c89793f4f4bd6901081b8322167b68
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-21T06:42:11Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;
    started 2026-10-21T06:42:09Z, finished 2026-10-21T06:42:11Z, exit 0. All 18 standalone
    history records; the generated seed event was also inspected in this target. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.

    history links: 18 record(s), 0 invalid

    No issues found

    18 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: All 18 standalone history records; the generated seed event was also inspected
    in this target. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: 98b39b3ec0f369362dd50578fb05797d78334edf5b6961dd70e82283af0ac3ca
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-21T06:48:01Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-21T06:42:09Z, finished 2026-10-21T06:48:01Z, exit 0. All 626,048\
    \ generated taxon YAMLs, not a focused approximation. Actual native gate execution\
    \ at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes\
    \ and terminal exit codes identify these runs. Expanded-corpus gate results are\
    \ represented only by the corresponding terminal receipts; running gates remain\
    \ unavailable in unsaved previews. Earlier unchanged-target strict receipts remain\
    \ explicitly historical; new review bundles still require individual validation/save/check.\n\
    uv run python scripts/verify_corpus.py \nexpected 626048 records, found 626048\
    \ on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces\
    \ exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 626,048 generated taxon YAMLs, not a focused approximation. Actual
    native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
    cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: 223185ba1237af69c7392ba3608374e92d93c219292d3303af5c06592b84b4e6
- evidence_id: products-receipt
  kind: validation
  reference: just validate-products
  accessed_at: '2026-10-21T07:19:10Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;
    started 2026-10-21T06:42:09Z, finished 2026-10-21T07:19:10Z, exit 0. Full configured
    corpus scan for curator-added graph nodes; this target contains no causal graph.
    Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4;
    retained cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-21T07:50:51Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0014/repo;\
    \ started 2026-10-21T06:42:09Z, finished 2026-10-21T07:50:51Z, exit 0. Repository-wide\
    \ just qc, including native corpus-wide checks. Actual native gate execution at\
    \ base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd, times, log hashes\
    \ and terminal exit codes identify these runs. Expanded-corpus gate results are\
    \ represented only by the corresponding terminal receipts; running gates remain\
    \ unavailable in unsaved previews. Earlier unchanged-target strict receipts remain\
    \ explicitly historical; new review bundles still require individual validation/save/check.\n\
    All checks passed!\n1073 passed, 3 skipped, 5 deselected in 1293.90s (0:21:33)\n\
    Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0014/src/taxonmech/schema/taxonmech.yaml\n\
    \  files scanned:      626048\nexpected 626048 records, found 626048 on disk\n\
    pages/ is current\nSite publication: 530,946,096 bytes (budget 950,000,000)\n\
    626048 taxon records\n  NCBITAXON        626048\nAll TaxonMech quality gates passed.\n\
    \  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890\
    \ strains (not genome counts)\n  Related STRAININFO_DEPOSIT: 107277 strain-record\
    \ pairs, 106843 identifiers, 53890 strains (not genome counts)\n  Related NUCLEOTIDE_SEQUENCE:\
    \ 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)\n\
    LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809\
    \ records mapped, 324404579 genomes summed across record attestations (not deduplicated)\n\
    Causal graphs: 0 records (0 evidence-backed edges)\n\nAll TaxonMech quality gates\
    \ passed."
  locator: Repository-wide just qc, including native corpus-wide checks. Actual native
    gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained cwd,
    times, log hashes and terminal exit codes identify these runs. Expanded-corpus
    gate results are represented only by the corresponding terminal receipts; running
    gates remain unavailable in unsaved previews. Earlier unchanged-target strict
    receipts remain explicitly historical; new review bundles still require individual
    validation/save/check.
  snapshot_sha256: dcb3f98d5c8ce264240732733ca70a5b93ee3e818d03f809d428748abffefca3
assessments:
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:138903 denotes Archaeoglobus lithotrophicus at SPECIES rank beneath
    NCBITaxon:2233, genetic code 11. All 9 carried ancestors agree with the pinned
    inventory and captured official NCBI response; the response omits only the root
    entry. Source name classes remain distinct from taxon classification.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  dimensions:
  - name: native-rank
    value: SPECIES
    definition: Rank of this exact NCBI target, distinct from source species mappings
      and strain genome records.
    evidence_ids:
    - record
    - taxonomy-inventory
    - ncbi-live
- assessment_id: nomenclature
  area: nomenclature
  topic: Name classes and nomenclatural scope
  outcome: supported
  summary: NCBI 138903 remains species Archaeoglobus lithotrophicus. The quoted 1993
    authority and includes-name Archaeoglobus lithotrophicus TF2 remain RELATED_SYNONYM,
    rather than strain equivalence or a valid-publication assertion. No LPSN nomenclature
    is asserted in this native record. Current independent nomenclatural status was
    not fetched; no unsupported claim of validation is inferred from taxonomy presence.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: 'Complete direct reads of twelve source/scope/path tables, including ignored
    files, support 0 imported BacDive strains over the exact target subtree (0 descendant
    taxa). All imported counts agree with their own source units: NCBITAXON 1 NAME;
    MADIN 2 TRAIT_ASSERTION. Counts of organisms, media, traits and genome assertions
    are not interchangeable and do not prove phenotype or biological genome equivalence.'
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - taxonomy-inventory
  - scope-row
  - path-row
  - bacdive-inventory
  - culture-inventory
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED status agree with NCBI identity. The sole seed
    event at 2026-09-13T17:54:04Z equals the latest raw/ATB/StrainInfo extraction
    time; no native status/history was changed.
  target_ids:
  - NCBITaxon:138903
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings: []
actions:
- action_id: recover-pinned-aggregate-inputs
  finding_ids: []
  target_ids:
  - NCBITaxon:138903
  description: Recover manifest-hash-matching original aggregate inputs and independently
    recount the exact target assertions through the maintained extractor; do not edit
    generated YAML.
  owner_paths:
  - repository: CultureBotAI/TaxonMech
    path: data/raw/MANIFEST.yaml
    role: Original source hashes
  - repository: CultureBotAI/TaxonMech
    path: src/taxonmech/extract.py
    role: Source-specific count semantics
  acceptance_checks:
  - Require exact original input SHA-256 before using it as historical evidence.
  - Recount only the exact target with each source's own assertion unit and compare
    to its pinned inventory row.
  - Record any discrepancy in a new review observation.
limitations:
- The review assesses exact identifiers, nomenclature, source placement and import
  completeness at the captured versions; it does not establish experimental phenotypes,
  assembly sequence equivalence or a phylogenetic species boundary.
- The original manifest-pinned aggregate source bytes were unavailable at the configured
  historical paths in retained hash observations. Inventory counts agree, but original
  aggregate-edge recounts remain unavailable; primary deposit chains do not replace
  those historical aggregates.
- No independent current nomenclatural authority was fetched for lithotrophicus; the
  record asserts only NCBI name classes and carries no valid-publication assertion.
- Actual native gate execution at base 01ca63effdf8c03a644df893ba6129b2d8448ea4; retained
  cwd, times, log hashes and terminal exit codes identify these runs. Expanded-corpus
  gate results are represented only by the corresponding terminal receipts; running
  gates remain unavailable in unsaved previews. Earlier unchanged-target strict receipts
  remain explicitly historical; new review bundles still require individual validation/save/check.
notes:
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base recapture preserves target/source-table bytes; five changed guidance/scope/path/seeder
  inputs were explicitly reassessed. Original captures and exact transition receipts
  remain retained.
- Every new bundle still requires its own validate/save/check recipe; baseline native
  receipts do not claim these later steps have run.
tags:
- record-review
- batch-0014
- archaea
- generated
- source-checked
```
