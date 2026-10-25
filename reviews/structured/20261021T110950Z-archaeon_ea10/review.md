# Record review: archaeon Ea10

- Review: 20261021T110950Z-archaeon_ea10
- Repository: CultureBotAI/TaxonMech
- Started UTC: 2026-10-21T09:44:07Z
- Finished UTC: 2026-10-21T11:09:50Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

archaeon Ea10 has consistent NCBI identity, lineage and generated source projections. The current misspelling archaeon BC19 differs from the complete pinned name evidence; the cause remains unresolved and no record-specific defect is established.

## Scope And Provenance

Entire single generated record, including all source assertions and imported strains.

Selection: Batch-0031 target 6; next unreviewed path-order selection after excluding 359 actual covered target paths. Canonical validated list on the current 40-bundle/59-target base and all 30 actually saved owned roots. Full ignored-inclusive YAML/Markdown bytes and duplicate metadata checked. All native YAML paths enumerated with os.walk including hidden/ignored files. Only explicit validated target paths count; reservations and inventories do not.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 662d24d9c1fd077eedc76fe87237e6822050638b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| NCBITaxon:910099 | data/taxa/archaea/archaeon_ea10.yaml | generated | archaeon Ea10 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Exact NCBI taxon, rank and lineage | passed | True | NCBITaxon:910099 | NCBITaxon:910099 identifies the exact SPECIES record archaeon Ea10, with immediate parent NCBITaxon:93506, unclassified Archaea. The four carried ancestors are root (NO_RANK), cellular organisms (CELLULAR_ROOT), Archaea (DOMAIN), and unclassified Archaea (NO_RANK). The identifiers, literal names and ranks, parent and genetic code 11 agree with the pinned NCBI projection and current official EFetch response; EFetch omits root. ARCHAEA follows this lineage; the EFetch Division metadata is not substituted for taxonomic domain. No genus or finer placement is inferred. |
| Complete exact identifier and name inventory search | passed | True | NCBITaxon:910099 | All twelve named source, scope and path tables were read completely, including ignored files, using the exact taxon identifier, full literal label, path slug and current misspelling archaeon BC19. The complete pinned NCBI parent graph has no descendant taxon for this target. Zero imported BacDive strains agrees with the target/subtree inventory and exact culture-inventory slice. The NCBITAXON 1 NAME attestation agrees with the taxon-presence projection. The pinned GTDB mapping and species tables have no exact query match, and the native record asserts no GTDB mapping or genome count. Other optional-source misses are confined to the complete pinned tables and recorded exact queries. No primary-genome census, worldwide culture/genome absence or lack of published biological observations is inferred. The separate complete pinned NCBI names census for this target found only its scientific-name row; the current misspelling discrepancy remains a bounded concern. |
| GTDB mapping applicability | not_applicable | False | NCBITaxon:910099 | The complete native record asserts no GTDB mapping or genome count. Exact target queries in the complete pinned GTDB mapping/species inventories have no matches; no whole-genome catalog scan was performed or claimed. |
| Imported strain links | not_applicable | False | NCBITaxon:910099 | This complete native record asserts no imported BacDive strain, culture deposit or strain-level genome link. A placeholder designation does not supply a deposit identity. |
| Nomenclatural publication authorities | not_applicable | False | NCBITaxon:910099 | No LPSN nomenclature, species-authority publication or type-strain sequence citation is asserted for this target; current NCBI name classes and bounded pinned LPSN inventory were checked. |
| Gene or transcriptomics evidence applicability | not_applicable | False | NCBITaxon:910099 | Not applicable: the complete native record asserts no gene, protein, regulator, pathway, experimental trait, mechanism or transcriptome link. |
| Historical aggregate edges | not_applicable | False | NCBITaxon:910099 | No historical medium, organism or trait aggregate is asserted in this target. |
| Current misspelling and complete pinned name-catalog comparison | passed | True | NCBITaxon:910099 | The pinned NCBI projection has empty exact, related and broad synonym columns. The current official EFetch response lists archaeon BC19 under OtherNames/Name with ClassCDE misspelling. All 16 pinned NCBI name shards were read completely (783107 rows), using the exact taxon identifier, full scientific name and current misspelling string without a name-class filter; only the scientific-name row for archaeon Ea10 matched. The complete twelve-table queries also included archaeon BC19. This is a bounded source-channel or snapshot discrepancy with unresolved cause, not an established importer defect. The current misspelling remains a related-name class; it is not promoted to an exact synonym, a published name or nomenclatural authority. The complete pinned LPSN query has no associated row. No type-deposit relationship or formal nomenclatural status is asserted. |
| Native strict record validation | passed | True | NCBITaxon:910099 | Actual terminal exit code 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. |
| Repository history validation | passed | True | NCBITaxon:910099 | Actual terminal exit code 0. The complete standalone history population; the generated seed event was also inspected in this target. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. |
| Full-corpus exact reproduction | passed | True | NCBITaxon:910099 | Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused approximation. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. |
| Native product ID/label gate | passed | True | NCBITaxon:910099 | Actual terminal exit code 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. |
| Authoritative complete quality gate | passed | True | NCBITaxon:910099 | Actual terminal exit code 0. Repository-wide just qc, including native corpus-wide checks. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. 1105 passed, 3 skipped, 5 deselected in 1597.49s (0:26:37) |

## Scientific And Domain Assessments

### Exact taxon and source lineage

identity: supported. Targets: NCBITaxon:910099.

NCBITaxon:910099 identifies the exact SPECIES record archaeon Ea10, with immediate parent NCBITaxon:93506, unclassified Archaea. The four carried ancestors are root (NO_RANK), cellular organisms (CELLULAR_ROOT), Archaea (DOMAIN), and unclassified Archaea (NO_RANK). The identifiers, literal names and ranks, parent and genetic code 11 agree with the pinned NCBI projection and current official EFetch response; EFetch omits root. ARCHAEA follows this lineage; the EFetch Division metadata is not substituted for taxonomic domain. No genus or finer placement is inferred.

### Name classes and nomenclatural scope

nomenclature: concern. Targets: NCBITaxon:910099.

The pinned NCBI projection has empty exact, related and broad synonym columns. The current official EFetch response lists archaeon BC19 under OtherNames/Name with ClassCDE misspelling. All 16 pinned NCBI name shards were read completely (783107 rows), using the exact taxon identifier, full scientific name and current misspelling string without a name-class filter; only the scientific-name row for archaeon Ea10 matched. The complete twelve-table queries also included archaeon BC19. This is a bounded source-channel or snapshot discrepancy with unresolved cause, not an established importer defect. The current misspelling remains a related-name class; it is not promoted to an exact synonym, a published name or nomenclatural authority. The complete pinned LPSN query has no associated row. No type-deposit relationship or formal nomenclatural status is asserted.

### Imported subtree and source assertion units

completeness: supported. Targets: NCBITaxon:910099.

All twelve named source, scope and path tables were read completely, including ignored files, using the exact taxon identifier, full literal label, path slug and current misspelling archaeon BC19. The complete pinned NCBI parent graph has no descendant taxon for this target. Zero imported BacDive strains agrees with the target/subtree inventory and exact culture-inventory slice. The NCBITAXON 1 NAME attestation agrees with the taxon-presence projection. The pinned GTDB mapping and species tables have no exact query match, and the native record asserts no GTDB mapping or genome count. Other optional-source misses are confined to the complete pinned tables and recorded exact queries. No primary-genome census, worldwide culture/genome absence or lack of published biological observations is inferred. The separate complete pinned NCBI names census for this target found only its scientific-name row; the current misspelling discrepancy remains a bounded concern.

### Unchanged native status and history

provenance: supported. Targets: NCBITaxon:910099.

EXACT grounding and SEEDED mapping status preserve the generated source state. The sole SEEDED_FROM_SOURCES event at 2026-09-13T17:54:04Z agrees with the latest raw, ATB and StrainInfo manifest extraction. The exact seed-scope and PATHS rows preserve inclusion and path. No manual curation, scientific status promotion or new native history event is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/taxa/archaea/archaeon_ea10.yaml; entire TaxonRecord; identifier=NCBITaxon:910099 | supports | Read the entire generated YAML, including identity, lineage, names, mappings, source attestations, all imported strains and links, and seed history. |
| taxonomy-inventory | data/raw/ncbitaxon_taxa.tsv; line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""}; line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"}; line 15329: {"taxon_id":"NCBITaxon:93506","label":"unclassified Archaea","rank":"NO_RANK","parent_id":"NCBITaxon:2157"}; line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"}; line 191856: {"taxon_id":"NCBITaxon:910099","label":"archaeon Ea10","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon","retired_into":"","taxonomy_snapshot":"2026-09-13"} | supports | Inspected the target and each carried ancestor, rank, parent, genetic code and source name classes. |
| scope-row | curation/seed_scope.tsv; line 294876: {"identifier":"NCBITaxon:910099","added":"2026-09-13","reason":"attested rule: archaeon Ea10, 1 sources incl. NCBI"} | supports | Exact target is included in the declared seed scope. |
| path-row | data/taxa/PATHS.tsv; line 606965: {"identifier":"NCBITaxon:910099","slug":"archaeon_ea10"} | supports | Indexed path resolves to this exact NCBI taxon. |
| ncbi-live | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1293352,1293353,1293354,1293355,910093,910099,910114,388601,388602,1602747&amp;retmode=xml; TaxaSet/Taxon[TaxId='910099']; ten-target captured response | supports | Inspected the successful official response for this exact taxon: scientific name, rank, parent, source name classes, lineage and genetic code. Current authority and pinned September inventory remain distinct observations. |
| lpsn-inventory | data/raw/lpsn_names.tsv; complete table; recorded exact query terms have no match | supports | Complete exact target/name/slug queries, including any current alternate-name strings recorded in the query scope, found no associated LPSN inventory row; this observation is bounded to the pinned inventory. |
| gtdb-mappings | data/raw/gtdb_mappings.tsv; complete table; recorded exact query terms have no match | supports | Complete exact target queries found no matching GTDB mapping row; no source cluster or reverse-mapping claim is asserted for this target. |
| gtdb-species | data/raw/gtdb_species.tsv; complete table; recorded exact query terms have no match | supports | Complete exact target queries found no matching GTDB species inventory row; this is not a primary-genome absence claim. |
| bacdive-inventory | data/raw/bacdive_strains.tsv; complete table; recorded exact query terms have no match | supports | Complete inventory selection covers the exact target and descendants from the complete NCBI parent graph; its imported strain population was compared with the complete YAML. |
| culture-inventory | data/raw/culture_collection_strains.tsv; complete table; recorded exact query terms have no match | supports | Inspected exact culture-inventory associations; an isolate name or genome does not create an inferred deposit. |
| gold-organisms | data/raw/gold_organisms.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact GOLD organism count row or bounded absence, without converting counts to phenotypes. |
| mediadive-taxa | data/raw/mediadive_taxa.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact MediaDive medium count row or bounded absence, without converting counts to phenotypes. |
| madin-taxa | data/raw/madin_taxa.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact Madin trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| bactotraits-taxa | data/raw/bactotraits_taxa.tsv; complete table; recorded exact query terms have no match | supports | Inspected the exact BactoTraits trait-assertion count row or bounded absence, without converting counts to phenotypes. |
| mapping-policy | docs/HARMONIZATION.md; Mapping predicates; Which strains belong to a record | supports | Policy permits source-scoped species-level closeMatch normalization and LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries NCBI lineage unchanged. Multiple reverse target mappings do not alone establish a normalization defect or make genomes and physical strains identical. |
| equivalence-contract | src/taxonmech/schema/taxonmech.yaml; TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439 | supports | TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes under the source taxon. |
| seed-owner | src/taxonmech/seed.py; NCBI source attestation construction lines 551–560; seed history construction lines 630–647 | supports | Inspected the generated NCBI NAME attestation and seed history construction; source mapping and strain derivation remain distinct from this target without imported mappings or strains. |
| manifest | data/raw/MANIFEST.yaml; kg_microbe_source, inputs, extracted_at | supports | Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd, upstream input hashes and extraction time 2026-09-13T17:50:44Z. |
| overlay-manifests | data/atb/MANIFEST.yaml; extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml | supports | Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z, matching the sole seed event. StrainInfo manifest is independently captured in source.inputs. |
| ncbi-names-shard-1 | data/catalog/ncbi_names-0000.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-2 | data/catalog/ncbi_names-0001.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-3 | data/catalog/ncbi_names-0002.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-4 | data/catalog/ncbi_names-0003.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-5 | data/catalog/ncbi_names-0004.jsonl.gz; line 47353: {"name":"archaeon Ea10","name_class":"scientific name","taxon_id":"NCBITaxon:910099","unique_name":""} | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-6 | data/catalog/ncbi_names-0005.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-7 | data/catalog/ncbi_names-0006.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-8 | data/catalog/ncbi_names-0007.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-9 | data/catalog/ncbi_names-0008.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-10 | data/catalog/ncbi_names-0009.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-11 | data/catalog/ncbi_names-0010.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-12 | data/catalog/ncbi_names-0011.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-13 | data/catalog/ncbi_names-0012.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-14 | data/catalog/ncbi_names-0013.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-15 | data/catalog/ncbi_names-0014.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-shard-16 | data/catalog/ncbi_names-0015.jsonl.gz; complete shard; no recorded exact query matched | supports | Pinned NCBI name evidence for this exact target; original name classes are retained and any absence is confined to the complete recorded query scope. |
| ncbi-names-manifest | data/catalog/MANIFEST.json; sources[id=ncbi_names]; files, rows, scope and snapshot | supports | Manifest lists every bacterial/archaeal NCBI name class in 16 pinned shards with 783107 rows and snapshot 2026-09-13. |
| ncbi-name-full-scan | /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/current-name-catalog-comparison.json; targets[6]; query_terms, matches; all shards and input hashes | supports | Original owned28 full-shard scan found only this target's scientific-name row; the current EFetch misspelling string did not match any pinned name row. The unchanged report and inputs were imported without relabeling the original observation. |
| ncbi-name-input-recapture | /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/imported-name-capture-completion.json; actual_captures, inputs_unchanged, original_scan_root and destination_root | supports | Fresh owned31 canonical captures prove equality with the original owned28 name-scan inputs. The original scan time and checkout remain unchanged. |
| ncbi-names-catalog-policy | scripts/build_source_catalog.py; names() and save(ncbi_names), lines 92–112 | supports | The maintained catalog builder retains each original names.dmp name_class for prokaryotic taxa without filtering to synonyms or scientific names. |
| ncbi-name-class-policy | src/taxonmech/ncbi_taxdump.py; load_taxdump names.dmp branch, lines 82–94 | supports | The maintained projection distinguishes synonym/equivalent-name exact synonyms from other related-name classes. A current misspelling is not promoted to exact equivalence. |
| native-gate-certificate | /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/native-gate-certificate.json; mode, base, source_repository, destination_repository, anchor_certificate_path, gates, original start/runtime witnesses, destination_runtime_witness_path and input_proof_path | supports | Actual successful batch-0028 gate receipts and original launch witnesses are hash-bound through its actual-current-base certificate. This separate reuse certificate binds unchanged native inputs in owned28 and owned31 and the destination runtime observation. Each original gate command remains separately cited. |
| strict-receipt | just validate-strict data/taxa/archaea/archaeon_ea10.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/strict-06.tsv; This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0031; started 2026-10-21T09:44:18Z, finished 2026-10-21T09:44:20Z, exit 0. This exact generated YAML only; its captured bytes remain unchanged. Actual earlier per-target invocation; the receipt retains its original cwd and times.<br>Validating 1 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0031/src/taxonmech/schema/taxonmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/strict-06.tsv |
| history-receipt | just validate-history; The complete standalone history population; the generated seed event was also inspected in this target. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo; started 2026-10-21T09:22:04Z, finished 2026-10-21T09:22:09Z, exit 0. The complete standalone history population; the generated seed event was also inspected in this target. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check.<br>history links: 19 record(s), 0 invalid<br>No issues found<br>19 history record(s) valid against src/taxonmech/schema/history.yaml |
| corpus-receipt | just verify-corpus; All 626,048 generated taxon YAMLs, not a focused approximation. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo; started 2026-10-21T09:22:04Z, finished 2026-10-21T09:28:48Z, exit 0. All 626,048 generated taxon YAMLs, not a focused approximation. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check.<br>uv run python scripts/verify_corpus.py <br>expected 626048 records, found 626048 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ and curation/seed_scope.tsv |
| products-receipt | just validate-products; Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo; started 2026-10-21T09:22:04Z, finished 2026-10-21T10:02:42Z, exit 0. Full configured corpus scan for curator-added graph nodes; this target contains no causal graph. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml<br><br>id↔label correspondence summary:<br><br>✅ All id↔label pairs correspond. |
| qc-receipt | just qc; Repository-wide just qc, including native corpus-wide checks. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check. | supports | Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo; started 2026-10-21T09:22:04Z, finished 2026-10-21T10:27:42Z, exit 0. Repository-wide just qc, including native corpus-wide checks. Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check.<br>All checks passed!<br>1105 passed, 3 skipped, 5 deselected in 1597.49s (0:26:37)<br>Validating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0028/src/taxonmech/schema/taxonmech.yaml<br>  files scanned:      626048<br>expected 626048 records, found 626048 on disk<br>pages/ is current<br>Site publication: 530,946,096 bytes (budget 950,000,000)<br>626048 taxon records<br>  NCBITAXON        626048<br>All TaxonMech quality gates passed.<br>  Related STRAININFO_STRAIN: 54312 strain-record pairs, 53745 identifiers, 53890 strains (not genome counts)<br>  Related STRAININFO_DEPOSIT: 107277 strain-record pairs, 106843 identifiers, 53890 strains (not genome counts)<br>  Related NUCLEOTIDE_SEQUENCE: 51594 strain-record pairs, 51301 identifiers, 9984 strains (not genome counts)<br>LPSN: 22469 records carry nomenclature, 21254 with a correct name   GTDB: 117809 records mapped, 324404579 genomes summed across record attestations (not deduplicated)<br>Causal graphs: 0 records (0 evidence-backed edges)<br><br>All TaxonMech quality gates passed. |

## Limits And Additional Notes

- SPECIES rank and a literal designation are source taxonomy assertions, not independent evidence of a formally named biological species, physical culture, phenotype or mechanism. Absence claims are limited to the specified complete pinned inputs and exact query terms.
- Ea10 is retained as the literal designation for this exact NCBI taxon. Its letters, digits and punctuation do not independently identify a culture deposit, genome accession, environmental measurement or experimental phenotype.
- The complete pinned NCBI names catalog and current EFetch name classes were compared for this target. The original names archive was not reconstructed; source-channel or snapshot cause remains unresolved. The whole-record UpdateDate in 2018 does not establish when the misspelling annotation was added. No worldwide literature or culture-collection search was performed.
- Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch witness, command, start/finish times and log hashes identify each execution. The batch-0031 certificate separately proves unchanged native inputs in both owned checkouts and observes the destination runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable. Exact-target strict receipts retain their own execution context. Every new review still requires individual validation/save/check.
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base source transitions are verified against retained original captures and exact changed-input receipts.
- Every new bundle still requires its own validate/save/check recipe; native gate receipts do not claim these later review lifecycle steps have run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110950Z-archaeon_ea10
kind: record
repository: CultureBotAI/TaxonMech
title: 'Record review: archaeon Ea10'
started_at: '2026-10-21T09:44:07Z'
finished_at: '2026-10-21T11:09:50Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: The reviewer did not author the existing generated target; this
    review changes only new review artifacts in an isolated checkout.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: archaeon Ea10 has consistent NCBI identity, lineage and generated source
  projections. The current misspelling archaeon BC19 differs from the complete pinned
  name evidence; the cause remains unresolved and no record-specific defect is established.
source:
  git_revision: 662d24d9c1fd077eedc76fe87237e6822050638b
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
  - path: data/catalog/MANIFEST.json
    sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
    role: context
  - path: data/catalog/ncbi_names-0000.jsonl.gz
    sha256: a873aeec2b2a9a391b1c210bd28827c9b6dad851eeccd7d1644373cb8c6ce802
    role: context
  - path: data/catalog/ncbi_names-0001.jsonl.gz
    sha256: fdb89eec80f04526f3f06fa49a6a03af586efaa5477404f1635d8c012c7ea999
    role: context
  - path: data/catalog/ncbi_names-0002.jsonl.gz
    sha256: 0d9a38612c08a7a78c93c18513328ccd7ecf44f5fff10489b26358814ec22149
    role: context
  - path: data/catalog/ncbi_names-0003.jsonl.gz
    sha256: 4ac5c4dfb9f0af855246461054ce5d9fa8f94ef6cfdecefb29870c972dd69dc4
    role: context
  - path: data/catalog/ncbi_names-0004.jsonl.gz
    sha256: ac8968aea5627fc73425a4f70942a74d4b666183762e4116b780384a1853f8a3
    role: context
  - path: data/catalog/ncbi_names-0005.jsonl.gz
    sha256: 31c672adade0c3485ee5d6817567f7972b06ce3b6853cf191159b76cad3b023c
    role: context
  - path: data/catalog/ncbi_names-0006.jsonl.gz
    sha256: 4c63f036b4707bfd7a66f7f85601ca11a5694cb19744857a506b8464b64bc8d2
    role: context
  - path: data/catalog/ncbi_names-0007.jsonl.gz
    sha256: e54bd96ed840ab4a6ffe0e251197fc9367a75e07dbdf89e070656bf38811ef34
    role: context
  - path: data/catalog/ncbi_names-0008.jsonl.gz
    sha256: c955a1d23e3e5b1e5a18f535755b423ae20efb6ca9ae4eef97a4c40dd0323f52
    role: context
  - path: data/catalog/ncbi_names-0009.jsonl.gz
    sha256: 7e1cbec759be96b0bd4b57f09ed075dc9cd7a22dc20cde8cc6f7a66cfb88da90
    role: context
  - path: data/catalog/ncbi_names-0010.jsonl.gz
    sha256: 7f4d714a5b982de851dc5ea21e981dadee3a77ac2fcadebbf9cb68bfaeb5dd25
    role: context
  - path: data/catalog/ncbi_names-0011.jsonl.gz
    sha256: 436b26d9d1510c958add8f0f4cf2371b489c169c9af900f74ebb8687e991b7d7
    role: context
  - path: data/catalog/ncbi_names-0012.jsonl.gz
    sha256: a9234414e4addc9780860a46cb9329a3a3837a70d22607c5446321508224a8fa
    role: context
  - path: data/catalog/ncbi_names-0013.jsonl.gz
    sha256: 8dee13292d2eececf3eab780149a1c5a0f669f36ba5c82119200323fb7554972
    role: context
  - path: data/catalog/ncbi_names-0014.jsonl.gz
    sha256: 4e22fb0532c498e145beae904ec2c4a78912421ae6864b93bc37d37b21e89e3a
    role: context
  - path: data/catalog/ncbi_names-0015.jsonl.gz
    sha256: 6d5de5074643b1d19f89c223bbfe01b35ccf4ad8167ae628f2f7f96745dee045
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
  - path: data/taxa/archaea/archaeon_ea10.yaml
    sha256: 878c8d6c839d099e37bd383bd02a6a2e8e07c03ea9a1ba7c472c201be0923faf
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
  - path: scripts/build_source_catalog.py
    sha256: 0e985fdbd74e5e58db2e28126bb8bc4f11a2d32929aa5d36f193d33142b5249e
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
  - path: src/taxonmech/source_catalog.py
    sha256: e941d67ede488ddf4dc1838c183f8ff0e5f7a0b9788e47651ea61e4e7d9c5d8f
    role: context
scope:
  description: Entire single generated record, including all source assertions and
    imported strains.
  selection: Batch-0031 target 6; next unreviewed path-order selection after excluding
    359 actual covered target paths. Canonical validated list on the current 40-bundle/59-target
    base and all 30 actually saved owned roots. Full ignored-inclusive YAML/Markdown
    bytes and duplicate metadata checked. All native YAML paths enumerated with os.walk
    including hidden/ignored files. Only explicit validated target paths count; reservations
    and inventories do not.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - NCBITaxon:910099
targets:
- target_id: NCBITaxon:910099
  path: data/taxa/archaea/archaeon_ea10.yaml
  label: archaeon Ea10
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
  summary: NCBITaxon:910099 identifies the exact SPECIES record archaeon Ea10, with
    immediate parent NCBITaxon:93506, unclassified Archaea. The four carried ancestors
    are root (NO_RANK), cellular organisms (CELLULAR_ROOT), Archaea (DOMAIN), and
    unclassified Archaea (NO_RANK). The identifiers, literal names and ranks, parent
    and genetic code 11 agree with the pinned NCBI projection and current official
    EFetch response; EFetch omits root. ARCHAEA follows this lineage; the EFetch Division
    metadata is not substituted for taxonomic domain. No genus or finer placement
    is inferred.
  target_ids:
  - NCBITaxon:910099
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
  summary: All twelve named source, scope and path tables were read completely, including
    ignored files, using the exact taxon identifier, full literal label, path slug
    and current misspelling archaeon BC19. The complete pinned NCBI parent graph has
    no descendant taxon for this target. Zero imported BacDive strains agrees with
    the target/subtree inventory and exact culture-inventory slice. The NCBITAXON
    1 NAME attestation agrees with the taxon-presence projection. The pinned GTDB
    mapping and species tables have no exact query match, and the native record asserts
    no GTDB mapping or genome count. Other optional-source misses are confined to
    the complete pinned tables and recorded exact queries. No primary-genome census,
    worldwide culture/genome absence or lack of published biological observations
    is inferred. The separate complete pinned NCBI names census for this target found
    only its scientific-name row; the current misspelling discrepancy remains a bounded
    concern.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - taxonomy-inventory
  - lpsn-inventory
  - gtdb-mappings
  - gtdb-species
  - bacdive-inventory
  - culture-inventory
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - ncbi-live
  - scope-row
  - path-row
  - ncbi-names-shard-1
  - ncbi-names-shard-2
  - ncbi-names-shard-3
  - ncbi-names-shard-4
  - ncbi-names-shard-5
  - ncbi-names-shard-6
  - ncbi-names-shard-7
  - ncbi-names-shard-8
  - ncbi-names-shard-9
  - ncbi-names-shard-10
  - ncbi-names-shard-11
  - ncbi-names-shard-12
  - ncbi-names-shard-13
  - ncbi-names-shard-14
  - ncbi-names-shard-15
  - ncbi-names-shard-16
  - ncbi-names-manifest
  - ncbi-name-full-scan
  - ncbi-name-input-recapture
  - ncbi-names-catalog-policy
  - ncbi-name-class-policy
  scope_note: Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs.
- check_id: gtdb-native-mappings
  name: GTDB mapping applicability
  status: not_applicable
  required: false
  summary: The complete native record asserts no GTDB mapping or genome count. Exact
    target queries in the complete pinned GTDB mapping/species inventories have no
    matches; no whole-genome catalog scan was performed or claimed.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - gtdb-mappings
  - gtdb-species
- check_id: strain-genome-evidence
  name: Imported strain links
  status: not_applicable
  required: false
  summary: This complete native record asserts no imported BacDive strain, culture
    deposit or strain-level genome link. A placeholder designation does not supply
    a deposit identity.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - bacdive-inventory
  - culture-inventory
- check_id: nomenclature-authorities
  name: Nomenclatural publication authorities
  status: not_applicable
  required: false
  summary: No LPSN nomenclature, species-authority publication or type-strain sequence
    citation is asserted for this target; current NCBI name classes and bounded pinned
    LPSN inventory were checked.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
- check_id: structured-adapter-applicability
  name: Gene or transcriptomics evidence applicability
  status: not_applicable
  required: false
  summary: 'Not applicable: the complete native record asserts no gene, protein, regulator,
    pathway, experimental trait, mechanism or transcriptome link.'
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
- check_id: historical-source-counts
  name: Historical aggregate edges
  status: not_applicable
  required: false
  summary: No historical medium, organism or trait aggregate is asserted in this target.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
- check_id: ncbi-name-source-comparison
  name: Current misspelling and complete pinned name-catalog comparison
  status: passed
  required: true
  summary: The pinned NCBI projection has empty exact, related and broad synonym columns.
    The current official EFetch response lists archaeon BC19 under OtherNames/Name
    with ClassCDE misspelling. All 16 pinned NCBI name shards were read completely
    (783107 rows), using the exact taxon identifier, full scientific name and current
    misspelling string without a name-class filter; only the scientific-name row for
    archaeon Ea10 matched. The complete twelve-table queries also included archaeon
    BC19. This is a bounded source-channel or snapshot discrepancy with unresolved
    cause, not an established importer defect. The current misspelling remains a related-name
    class; it is not promoted to an exact synonym, a published name or nomenclatural
    authority. The complete pinned LPSN query has no associated row. No type-deposit
    relationship or formal nomenclatural status is asserted.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - ncbi-names-shard-1
  - ncbi-names-shard-2
  - ncbi-names-shard-3
  - ncbi-names-shard-4
  - ncbi-names-shard-5
  - ncbi-names-shard-6
  - ncbi-names-shard-7
  - ncbi-names-shard-8
  - ncbi-names-shard-9
  - ncbi-names-shard-10
  - ncbi-names-shard-11
  - ncbi-names-shard-12
  - ncbi-names-shard-13
  - ncbi-names-shard-14
  - ncbi-names-shard-15
  - ncbi-names-shard-16
  - ncbi-names-manifest
  - ncbi-name-full-scan
  - ncbi-name-input-recapture
  - ncbi-names-catalog-policy
  - ncbi-name-class-policy
  scope_note: Current EFetch and pinned full-name catalog are separate observations;
    source-channel/snapshot cause remains unresolved. Whole-record UpdateDate does
    not date the annotation. No exact-synonym promotion or seeder defect is asserted.
- check_id: strict
  name: Native strict record validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. This exact generated YAML only; its captured
    bytes remain unchanged. Actual earlier per-target invocation; the receipt retains
    its original cwd and times.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - strict-receipt
  command: just validate-strict data/taxa/archaea/archaeon_ea10.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/strict-06.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: This exact generated YAML only; its captured bytes remain unchanged.
    Actual earlier per-target invocation; the receipt retains its original cwd and
    times.
- check_id: history
  name: Repository history validation
  status: passed
  required: true
  summary: Actual terminal exit code 0. The complete standalone history population;
    the generated seed event was also inspected in this target. Same-base reuse of
    actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
    the original batch-0028 cwd, launch witness, command, start/finish times and log
    hashes identify each execution. The batch-0031 certificate separately proves unchanged
    native inputs in both owned checkouts and observes the destination runtime under
    its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
    certificates remain unavailable. Exact-target strict receipts retain their own
    execution context. Every new review still requires individual validation/save/check.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - history-receipt
  - native-gate-certificate
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  scope_note: The complete standalone history population; the generated seed event
    was also inspected in this target. Same-base reuse of actual batch-0028 native
    gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original
    batch-0028 cwd, launch witness, command, start/finish times and log hashes identify
    each execution. The batch-0031 certificate separately proves unchanged native
    inputs in both owned checkouts and observes the destination runtime under its
    explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates
    remain unavailable. Exact-target strict receipts retain their own execution context.
    Every new review still requires individual validation/save/check.
- check_id: corpus
  name: Full-corpus exact reproduction
  status: passed
  required: true
  summary: Actual terminal exit code 0. All 626,048 generated taxon YAMLs, not a focused
    approximation. Same-base reuse of actual batch-0028 native gate executions at
    base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch
    witness, command, start/finish times and log hashes identify each execution. The
    batch-0031 certificate separately proves unchanged native inputs in both owned
    checkouts and observes the destination runtime under its explicit PYTHONPATH.
    No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable.
    Exact-target strict receipts retain their own execution context. Every new review
    still requires individual validation/save/check.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - corpus-receipt
  - native-gate-certificate
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  scope_note: All 626,048 generated taxon YAMLs, not a focused approximation. Same-base
    reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
    the original batch-0028 cwd, launch witness, command, start/finish times and log
    hashes identify each execution. The batch-0031 certificate separately proves unchanged
    native inputs in both owned checkouts and observes the destination runtime under
    its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
    certificates remain unavailable. Exact-target strict receipts retain their own
    execution context. Every new review still requires individual validation/save/check.
- check_id: products
  name: Native product ID/label gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Full configured corpus scan for curator-added
    graph nodes; this target contains no causal graph. Same-base reuse of actual batch-0028
    native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original
    batch-0028 cwd, launch witness, command, start/finish times and log hashes identify
    each execution. The batch-0031 certificate separately proves unchanged native
    inputs in both owned checkouts and observes the destination runtime under its
    explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates
    remain unavailable. Exact-target strict receipts retain their own execution context.
    Every new review still requires individual validation/save/check.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - products-receipt
  - native-gate-certificate
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Same-base reuse of actual batch-0028 native gate executions
    at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd,
    launch witness, command, start/finish times and log hashes identify each execution.
    The batch-0031 certificate separately proves unchanged native inputs in both owned
    checkouts and observes the destination runtime under its explicit PYTHONPATH.
    No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable.
    Exact-target strict receipts retain their own execution context. Every new review
    still requires individual validation/save/check.
- check_id: qc
  name: Authoritative complete quality gate
  status: passed
  required: true
  summary: Actual terminal exit code 0. Repository-wide just qc, including native
    corpus-wide checks. Same-base reuse of actual batch-0028 native gate executions
    at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd,
    launch witness, command, start/finish times and log hashes identify each execution.
    The batch-0031 certificate separately proves unchanged native inputs in both owned
    checkouts and observes the destination runtime under its explicit PYTHONPATH.
    No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable.
    Exact-target strict receipts retain their own execution context. Every new review
    still requires individual validation/save/check. 1105 passed, 3 skipped, 5 deselected
    in 1597.49s (0:26:37)
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - qc-receipt
  - native-gate-certificate
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Repository-wide just qc, including native corpus-wide checks. Same-base
    reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
    the original batch-0028 cwd, launch witness, command, start/finish times and log
    hashes identify each execution. The batch-0031 certificate separately proves unchanged
    native inputs in both owned checkouts and observes the destination runtime under
    its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
    certificates remain unavailable. Exact-target strict receipts retain their own
    execution context. Every new review still requires individual validation/save/check.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/taxa/archaea/archaeon_ea10.yaml
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: Read the entire generated YAML, including identity, lineage, names, mappings,
    source attestations, all imported strains and links, and seed history.
  locator: entire TaxonRecord; identifier=NCBITaxon:910099
  snapshot_sha256: 878c8d6c839d099e37bd383bd02a6a2e8e07c03ea9a1ba7c472c201be0923faf
- evidence_id: taxonomy-inventory
  kind: database
  reference: data/raw/ncbitaxon_taxa.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Inspected the target and each carried ancestor, rank, parent, genetic code
    and source name classes.
  locator: 'line 2: {"taxon_id":"NCBITaxon:1","label":"root","rank":"NO_RANK","parent_id":""};
    line 1698: {"taxon_id":"NCBITaxon:2157","label":"Archaea","rank":"DOMAIN","parent_id":"NCBITaxon:131567"};
    line 15329: {"taxon_id":"NCBITaxon:93506","label":"unclassified Archaea","rank":"NO_RANK","parent_id":"NCBITaxon:2157"};
    line 25334: {"taxon_id":"NCBITaxon:131567","label":"cellular organisms","rank":"CELLULAR_ROOT","parent_id":"NCBITaxon:1"};
    line 191856: {"taxon_id":"NCBITaxon:910099","label":"archaeon Ea10","rank":"SPECIES","parent_id":"NCBITaxon:93506","genetic_code":"11","exact_synonyms":"","related_synonyms":"","broad_synonyms":"","attested_by":"ncbitaxon","retired_into":"","taxonomy_snapshot":"2026-09-13"}'
  snapshot_sha256: 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 650767.'
- evidence_id: scope-row
  kind: database
  reference: curation/seed_scope.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Exact target is included in the declared seed scope.
  locator: 'line 294876: {"identifier":"NCBITaxon:910099","added":"2026-09-13","reason":"attested
    rule: archaeon Ea10, 1 sources incl. NCBI"}'
  snapshot_sha256: 95589ac7f548dcd27951c6afe432895c7409717df5f6e789a93dcb9229535963
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 626048.'
- evidence_id: path-row
  kind: database
  reference: data/taxa/PATHS.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Indexed path resolves to this exact NCBI taxon.
  locator: 'line 606965: {"identifier":"NCBITaxon:910099","slug":"archaeon_ea10"}'
  snapshot_sha256: f8f2e0721cb6839b30530b44be0d3004b9f0e6e2d4be8736f235b10117a8bd99
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 626048.'
- evidence_id: ncbi-live
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1293352,1293353,1293354,1293355,910093,910099,910114,388601,388602,1602747&retmode=xml
  accessed_at: '2026-10-21T09:38:51Z'
  support: supports
  summary: 'Inspected the successful official response for this exact taxon: scientific
    name, rank, parent, source name classes, lineage and genetic code. Current authority
    and pinned September inventory remain distinct observations.'
  locator: TaxaSet/Taxon[TaxId='910099']; ten-target captured response
  snapshot_sha256: 156d877bb571b397c210b79124131b53f988f1b3de0f21c2d14f6fa247dfbd06
- evidence_id: lpsn-inventory
  kind: database
  reference: data/raw/lpsn_names.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Complete exact target/name/slug queries, including any current alternate-name
    strings recorded in the query scope, found no associated LPSN inventory row; this
    observation is bounded to the pinned inventory.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 097f8f4ba3fd077d02e48f2c298a0af88fe02db79cc862f9af1c05141b0baa57
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 34301.'
- evidence_id: gtdb-mappings
  kind: database
  reference: data/raw/gtdb_mappings.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Complete exact target queries found no matching GTDB mapping row; no source
    cluster or reverse-mapping claim is asserted for this target.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 322327.'
- evidence_id: gtdb-species
  kind: database
  reference: data/raw/gtdb_species.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Complete exact target queries found no matching GTDB species inventory
    row; this is not a primary-genome absence claim.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 24eddf08fe8fdd1fed534a1b7fd411561eec612c58c3709a36032998fdab8f21
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 199923.'
- evidence_id: bacdive-inventory
  kind: database
  reference: data/raw/bacdive_strains.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Complete inventory selection covers the exact target and descendants from
    the complete NCBI parent graph; its imported strain population was compared with
    the complete YAML.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 029fd6d1f53ef7f90684130bf0d644ed3edd1d8fbeb065a511ae928f160b1eea
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 101417.'
- evidence_id: culture-inventory
  kind: database
  reference: data/raw/culture_collection_strains.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Inspected exact culture-inventory associations; an isolate name or genome
    does not create an inferred deposit.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 810fdcb16abd6330fb15bb03d4c74b18db86be36a7c599df7c6b2498d9735c95
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 154969.'
- evidence_id: gold-organisms
  kind: database
  reference: data/raw/gold_organisms.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Inspected the exact GOLD organism count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 0680971a156eef0b79de46c71a1f2138eaee5212ad8193eec943bd8e6257e473
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 45616.'
- evidence_id: mediadive-taxa
  kind: database
  reference: data/raw/mediadive_taxa.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Inspected the exact MediaDive medium count row or bounded absence, without
    converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 3f74b78cadfcdb6aeae953e09fdb39e34fd9c5d5ed0be65a04a5d7fb02355905
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 14225.'
- evidence_id: madin-taxa
  kind: database
  reference: data/raw/madin_taxa.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Inspected the exact Madin trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 7620448834f1b86daa83f2e338160ec3291a2ec3900ea4cec449418b1dc8b148
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 34148.'
- evidence_id: bactotraits-taxa
  kind: database
  reference: data/raw/bactotraits_taxa.tsv
  accessed_at: '2026-10-21T09:46:14Z'
  support: supports
  summary: Inspected the exact BactoTraits trait-assertion count row or bounded absence,
    without converting counts to phenotypes.
  locator: complete table; recorded exact query terms have no match
  snapshot_sha256: 976d109cef832d8bf27cc105f67a42efbe900b6946736298602ef6d11158b197
  search_scope: 'Full direct reads of all explicitly named TSV files, including ignored
    files; exact case-folded whole-field and pipe-token ID/full-label/slug/synonym/source-ID
    search. All claims of no rows are limited to these complete pinned inputs. Exact
    case-folded query terms: ["archaeon bc19","archaeon ea10","archaeon_ea10","ncbitaxon:910099"];
    complete table data rows: 9658.'
- evidence_id: mapping-policy
  kind: record_content
  reference: docs/HARMONIZATION.md
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: Policy permits source-scoped species-level closeMatch normalization and
    LPSN-linked species xrefs/synonyms, retains pooled broadMatch entries and carries
    NCBI lineage unchanged. Multiple reverse target mappings do not alone establish
    a normalization defect or make genomes and physical strains identical.
  locator: Mapping predicates; Which strains belong to a record
  snapshot_sha256: 9c676a03a226d7fdce82f064acd01807a1a783497ffbbb1aabb8fdd393ac250d
- evidence_id: equivalence-contract
  kind: record_content
  reference: src/taxonmech/schema/taxonmech.yaml
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: TaxonRecord.xrefs denotes equivalent identifiers; broader/narrower relations
    remain qualified taxonomy mappings. TaxonomyMapping.genome_count counts genomes
    under the source taxon.
  locator: TaxonRecord.xrefs, lines 180–187; TaxonomyMapping, lines 417–439
  snapshot_sha256: aab25fee94c73eb70e5197a4f3ab8ddf0fa6731785974364963906d4f4d87fc3
- evidence_id: seed-owner
  kind: record_content
  reference: src/taxonmech/seed.py
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: Inspected the generated NCBI NAME attestation and seed history construction;
    source mapping and strain derivation remain distinct from this target without
    imported mappings or strains.
  locator: NCBI source attestation construction lines 551–560; seed history construction
    lines 630–647
  snapshot_sha256: 3cc30f6413a293165385dfc1860505fe389e5adfe9aa3d168f76aa4cb2ac36bd
- evidence_id: manifest
  kind: record_content
  reference: data/raw/MANIFEST.yaml
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: Manifest pins kg-microbe revision 30405b70ef762aa46c08278b2b3e06bffb0b34cd,
    upstream input hashes and extraction time 2026-09-13T17:50:44Z.
  locator: kg_microbe_source, inputs, extracted_at
  snapshot_sha256: ee76711683b1b579d1561dcf40187e10e4f0027ae1b89f108eb18e865e7e7d38
- evidence_id: overlay-manifests
  kind: record_content
  reference: data/atb/MANIFEST.yaml
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: Raw, ATB and StrainInfo extraction times have maximum 2026-09-13T17:54:04Z,
    matching the sole seed event. StrainInfo manifest is independently captured in
    source.inputs.
  locator: extracted_at, together with data/raw/MANIFEST.yaml and data/straininfo/MANIFEST.yaml
  snapshot_sha256: 1358809b2af7e8d4a6c8bb4c122781f48ae40b2c4f0f1c7ad3f37ad8907d7315
- evidence_id: ncbi-names-shard-1
  kind: primary_source
  reference: data/catalog/ncbi_names-0000.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: a873aeec2b2a9a391b1c210bd28827c9b6dad851eeccd7d1644373cb8c6ce802
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-2
  kind: primary_source
  reference: data/catalog/ncbi_names-0001.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: fdb89eec80f04526f3f06fa49a6a03af586efaa5477404f1635d8c012c7ea999
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-3
  kind: primary_source
  reference: data/catalog/ncbi_names-0002.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 0d9a38612c08a7a78c93c18513328ccd7ecf44f5fff10489b26358814ec22149
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-4
  kind: primary_source
  reference: data/catalog/ncbi_names-0003.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 4ac5c4dfb9f0af855246461054ce5d9fa8f94ef6cfdecefb29870c972dd69dc4
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-5
  kind: primary_source
  reference: data/catalog/ncbi_names-0004.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: 'line 47353: {"name":"archaeon Ea10","name_class":"scientific name","taxon_id":"NCBITaxon:910099","unique_name":""}'
  snapshot_sha256: ac8968aea5627fc73425a4f70942a74d4b666183762e4116b780384a1853f8a3
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-6
  kind: primary_source
  reference: data/catalog/ncbi_names-0005.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 31c672adade0c3485ee5d6817567f7972b06ce3b6853cf191159b76cad3b023c
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-7
  kind: primary_source
  reference: data/catalog/ncbi_names-0006.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 4c63f036b4707bfd7a66f7f85601ca11a5694cb19744857a506b8464b64bc8d2
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-8
  kind: primary_source
  reference: data/catalog/ncbi_names-0007.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: e54bd96ed840ab4a6ffe0e251197fc9367a75e07dbdf89e070656bf38811ef34
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-9
  kind: primary_source
  reference: data/catalog/ncbi_names-0008.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: c955a1d23e3e5b1e5a18f535755b423ae20efb6ca9ae4eef97a4c40dd0323f52
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-10
  kind: primary_source
  reference: data/catalog/ncbi_names-0009.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 7e1cbec759be96b0bd4b57f09ed075dc9cd7a22dc20cde8cc6f7a66cfb88da90
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-11
  kind: primary_source
  reference: data/catalog/ncbi_names-0010.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 7f4d714a5b982de851dc5ea21e981dadee3a77ac2fcadebbf9cb68bfaeb5dd25
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-12
  kind: primary_source
  reference: data/catalog/ncbi_names-0011.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 436b26d9d1510c958add8f0f4cf2371b489c169c9af900f74ebb8687e991b7d7
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-13
  kind: primary_source
  reference: data/catalog/ncbi_names-0012.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: a9234414e4addc9780860a46cb9329a3a3837a70d22607c5446321508224a8fa
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-14
  kind: primary_source
  reference: data/catalog/ncbi_names-0013.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 8dee13292d2eececf3eab780149a1c5a0f669f36ba5c82119200323fb7554972
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-15
  kind: primary_source
  reference: data/catalog/ncbi_names-0014.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 4e22fb0532c498e145beae904ec2c4a78912421ae6864b93bc37d37b21e89e3a
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 50000; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-shard-16
  kind: primary_source
  reference: data/catalog/ncbi_names-0015.jsonl.gz
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Pinned NCBI name evidence for this exact target; original name classes
    are retained and any absence is confined to the complete recorded query scope.
  locator: complete shard; no recorded exact query matched
  snapshot_sha256: 6d5de5074643b1d19f89c223bbfe01b35ccf4ad8167ae628f2f7f96745dee045
  search_scope: 'Complete direct shard read, including ignored files and every stored
    name class. Exact case-folded whole-field queries: ["archaeon bc19","archaeon
    ea10","ncbitaxon:910099"]; shard data rows: 33107; all 16 shards total 783107
    rows. Original scan occurred in owned28; identical source bytes were captured
    in owned31.'
- evidence_id: ncbi-names-manifest
  kind: database
  reference: data/catalog/MANIFEST.json
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Manifest lists every bacterial/archaeal NCBI name class in 16 pinned shards
    with 783107 rows and snapshot 2026-09-13.
  locator: sources[id=ncbi_names]; files, rows, scope and snapshot
  snapshot_sha256: 15b5cfe42be7919faf2a6feb5ac4f7084009e84b2d6da669f7101aacc3586299
- evidence_id: ncbi-name-full-scan
  kind: primary_source
  reference: /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/current-name-catalog-comparison.json
  accessed_at: '2026-10-21T09:40:18Z'
  support: supports
  summary: Original owned28 full-shard scan found only this target's scientific-name
    row; the current EFetch misspelling string did not match any pinned name row.
    The unchanged report and inputs were imported without relabeling the original
    observation.
  locator: targets[6]; query_terms, matches; all shards and input hashes
  snapshot_sha256: ccd54d16f09fd539e949bbd4589aa2a1c758773f542ef190f728cd503b06c1a2
  search_scope: 'Complete direct decompression of all manifest-listed NCBI names shards,
    including ignored files, using each exact target ID/full scientific name/current
    alternate-name string. No name-class filter. Exact target queries: ["archaeon
    bc19","archaeon ea10","ncbitaxon:910099"]'
- evidence_id: ncbi-name-input-recapture
  kind: validation
  reference: /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/imported-name-capture-completion.json
  accessed_at: '2026-10-21T09:45:34Z'
  support: supports
  summary: Fresh owned31 canonical captures prove equality with the original owned28
    name-scan inputs. The original scan time and checkout remain unchanged.
  locator: actual_captures, inputs_unchanged, original_scan_root and destination_root
  snapshot_sha256: 264f28f83ae595ff4ddddfdf48d097e7aef565eb2de759e2177a345fa5fde148
- evidence_id: ncbi-names-catalog-policy
  kind: record_content
  reference: scripts/build_source_catalog.py
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: The maintained catalog builder retains each original names.dmp name_class
    for prokaryotic taxa without filtering to synonyms or scientific names.
  locator: names() and save(ncbi_names), lines 92–112
  snapshot_sha256: 0e985fdbd74e5e58db2e28126bb8bc4f11a2d32929aa5d36f193d33142b5249e
- evidence_id: ncbi-name-class-policy
  kind: record_content
  reference: src/taxonmech/ncbi_taxdump.py
  accessed_at: '2026-10-21T11:09:50Z'
  support: supports
  summary: The maintained projection distinguishes synonym/equivalent-name exact synonyms
    from other related-name classes. A current misspelling is not promoted to exact
    equivalence.
  locator: load_taxdump names.dmp branch, lines 82–94
  snapshot_sha256: 83e3bfd53721a1f85291022511de6504d84caa58e899c0fd8d1797e9f00f67cf
- evidence_id: native-gate-certificate
  kind: validation
  reference: /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/native-gate-certificate.json
  accessed_at: '2026-10-21T10:29:22Z'
  support: supports
  summary: Actual successful batch-0028 gate receipts and original launch witnesses
    are hash-bound through its actual-current-base certificate. This separate reuse
    certificate binds unchanged native inputs in owned28 and owned31 and the destination
    runtime observation. Each original gate command remains separately cited.
  locator: mode, base, source_repository, destination_repository, anchor_certificate_path,
    gates, original start/runtime witnesses, destination_runtime_witness_path and
    input_proof_path
  snapshot_sha256: fb5c2f51fb9e814727263866eda4cd95c6b576b8176753c9e85b061c9be0af6a
- evidence_id: strict-receipt
  kind: validation
  reference: just validate-strict data/taxa/archaea/archaeon_ea10.yaml --out /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/strict-06.tsv
  accessed_at: '2026-10-21T09:44:20Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0031;\
    \ started 2026-10-21T09:44:18Z, finished 2026-10-21T09:44:20Z, exit 0. This exact\
    \ generated YAML only; its captured bytes remain unchanged. Actual earlier per-target\
    \ invocation; the receipt retains its original cwd and times.\nValidating 1 files\
    \ with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0031/src/taxonmech/schema/taxonmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0031/strict-06.tsv"
  locator: This exact generated YAML only; its captured bytes remain unchanged. Actual
    earlier per-target invocation; the receipt retains its original cwd and times.
  snapshot_sha256: a803e2c20d9d7151adf061e250510b43c45e0dc940173e8b2945bfd3c87143ab
- evidence_id: history-receipt
  kind: validation
  reference: just validate-history
  accessed_at: '2026-10-21T09:22:09Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo;
    started 2026-10-21T09:22:04Z, finished 2026-10-21T09:22:09Z, exit 0. The complete
    standalone history population; the generated seed event was also inspected in
    this target. Same-base reuse of actual batch-0028 native gate executions at base
    662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd, launch
    witness, command, start/finish times and log hashes identify each execution. The
    batch-0031 certificate separately proves unchanged native inputs in both owned
    checkouts and observes the destination runtime under its explicit PYTHONPATH.
    No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable.
    Exact-target strict receipts retain their own execution context. Every new review
    still requires individual validation/save/check.

    history links: 19 record(s), 0 invalid

    No issues found

    19 history record(s) valid against src/taxonmech/schema/history.yaml'
  locator: The complete standalone history population; the generated seed event was
    also inspected in this target. Same-base reuse of actual batch-0028 native gate
    executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028
    cwd, launch witness, command, start/finish times and log hashes identify each
    execution. The batch-0031 certificate separately proves unchanged native inputs
    in both owned checkouts and observes the destination runtime under its explicit
    PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing certificates
    remain unavailable. Exact-target strict receipts retain their own execution context.
    Every new review still requires individual validation/save/check.
  snapshot_sha256: 34f263c8ab283595798ff0a3db83159c013e2993ef490bc9da439b1e73ad811b
- evidence_id: corpus-receipt
  kind: validation
  reference: just verify-corpus
  accessed_at: '2026-10-21T09:28:48Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo;\
    \ started 2026-10-21T09:22:04Z, finished 2026-10-21T09:28:48Z, exit 0. All 626,048\
    \ generated taxon YAMLs, not a focused approximation. Same-base reuse of actual\
    \ batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;\
    \ the original batch-0028 cwd, launch witness, command, start/finish times and\
    \ log hashes identify each execution. The batch-0031 certificate separately proves\
    \ unchanged native inputs in both owned checkouts and observes the destination\
    \ runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is\
    \ claimed. Missing certificates remain unavailable. Exact-target strict receipts\
    \ retain their own execution context. Every new review still requires individual\
    \ validation/save/check.\nuv run python scripts/verify_corpus.py \nexpected 626048\
    \ records, found 626048 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/ and curation/seed_scope.tsv"
  locator: All 626,048 generated taxon YAMLs, not a focused approximation. Same-base
    reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
    the original batch-0028 cwd, launch witness, command, start/finish times and log
    hashes identify each execution. The batch-0031 certificate separately proves unchanged
    native inputs in both owned checkouts and observes the destination runtime under
    its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
    certificates remain unavailable. Exact-target strict receipts retain their own
    execution context. Every new review still requires individual validation/save/check.
  snapshot_sha256: 223185ba1237af69c7392ba3608374e92d93c219292d3303af5c06592b84b4e6
- evidence_id: products-receipt
  kind: validation
  reference: just validate-products
  accessed_at: '2026-10-21T10:02:42Z'
  support: supports
  summary: 'Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo;
    started 2026-10-21T09:22:04Z, finished 2026-10-21T10:02:42Z, exit 0. Full configured
    corpus scan for curator-added graph nodes; this target contains no causal graph.
    Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
    the original batch-0028 cwd, launch witness, command, start/finish times and log
    hashes identify each execution. The batch-0031 certificate separately proves unchanged
    native inputs in both owned checkouts and observes the destination runtime under
    its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
    certificates remain unavailable. Exact-target strict receipts retain their own
    execution context. Every new review still requires individual validation/save/check.

    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml


    id↔label correspondence summary:


    ✅ All id↔label pairs correspond.'
  locator: Full configured corpus scan for curator-added graph nodes; this target
    contains no causal graph. Same-base reuse of actual batch-0028 native gate executions
    at base 662d24d9c1fd077eedc76fe87237e6822050638b; the original batch-0028 cwd,
    launch witness, command, start/finish times and log hashes identify each execution.
    The batch-0031 certificate separately proves unchanged native inputs in both owned
    checkouts and observes the destination runtime under its explicit PYTHONPATH.
    No batch-0031 broad gate execution is claimed. Missing certificates remain unavailable.
    Exact-target strict receipts retain their own execution context. Every new review
    still requires individual validation/save/check.
  snapshot_sha256: 48dd07515706dc62199fc2205c4b0bfdd5750028037d9b800179f254d2f1eb07
- evidence_id: qc-receipt
  kind: validation
  reference: just qc
  accessed_at: '2026-10-21T10:27:42Z'
  support: supports
  summary: "Actual command ran from /private/tmp/taxonmech-record-reviews-k0MubV/prefetch-batch-0028/repo;\
    \ started 2026-10-21T09:22:04Z, finished 2026-10-21T10:27:42Z, exit 0. Repository-wide\
    \ just qc, including native corpus-wide checks. Same-base reuse of actual batch-0028\
    \ native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b; the\
    \ original batch-0028 cwd, launch witness, command, start/finish times and log\
    \ hashes identify each execution. The batch-0031 certificate separately proves\
    \ unchanged native inputs in both owned checkouts and observes the destination\
    \ runtime under its explicit PYTHONPATH. No batch-0031 broad gate execution is\
    \ claimed. Missing certificates remain unavailable. Exact-target strict receipts\
    \ retain their own execution context. Every new review still requires individual\
    \ validation/save/check.\nAll checks passed!\n1105 passed, 3 skipped, 5 deselected\
    \ in 1597.49s (0:26:37)\nValidating 626048 files with 4 workers; schema=/private/tmp/taxonmech-record-reviews-k0MubV/repo-batch-0028/src/taxonmech/schema/taxonmech.yaml\n\
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
  locator: Repository-wide just qc, including native corpus-wide checks. Same-base
    reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
    the original batch-0028 cwd, launch witness, command, start/finish times and log
    hashes identify each execution. The batch-0031 certificate separately proves unchanged
    native inputs in both owned checkouts and observes the destination runtime under
    its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
    certificates remain unavailable. Exact-target strict receipts retain their own
    execution context. Every new review still requires individual validation/save/check.
  snapshot_sha256: bca9d99a07dbd5430ec8693e43b4027f09afc1eef6b8bd101efed0d30c778184
assessments:
- assessment_id: identity
  area: identity
  topic: Exact taxon and source lineage
  outcome: supported
  summary: NCBITaxon:910099 identifies the exact SPECIES record archaeon Ea10, with
    immediate parent NCBITaxon:93506, unclassified Archaea. The four carried ancestors
    are root (NO_RANK), cellular organisms (CELLULAR_ROOT), Archaea (DOMAIN), and
    unclassified Archaea (NO_RANK). The identifiers, literal names and ranks, parent
    and genetic code 11 agree with the pinned NCBI projection and current official
    EFetch response; EFetch omits root. ARCHAEA follows this lineage; the EFetch Division
    metadata is not substituted for taxonomic domain. No genus or finer placement
    is inferred.
  target_ids:
  - NCBITaxon:910099
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
  outcome: concern
  summary: The pinned NCBI projection has empty exact, related and broad synonym columns.
    The current official EFetch response lists archaeon BC19 under OtherNames/Name
    with ClassCDE misspelling. All 16 pinned NCBI name shards were read completely
    (783107 rows), using the exact taxon identifier, full scientific name and current
    misspelling string without a name-class filter; only the scientific-name row for
    archaeon Ea10 matched. The complete twelve-table queries also included archaeon
    BC19. This is a bounded source-channel or snapshot discrepancy with unresolved
    cause, not an established importer defect. The current misspelling remains a related-name
    class; it is not promoted to an exact synonym, a published name or nomenclatural
    authority. The complete pinned LPSN query has no associated row. No type-deposit
    relationship or formal nomenclatural status is asserted.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - lpsn-inventory
  - mapping-policy
  - ncbi-names-shard-1
  - ncbi-names-shard-2
  - ncbi-names-shard-3
  - ncbi-names-shard-4
  - ncbi-names-shard-5
  - ncbi-names-shard-6
  - ncbi-names-shard-7
  - ncbi-names-shard-8
  - ncbi-names-shard-9
  - ncbi-names-shard-10
  - ncbi-names-shard-11
  - ncbi-names-shard-12
  - ncbi-names-shard-13
  - ncbi-names-shard-14
  - ncbi-names-shard-15
  - ncbi-names-shard-16
  - ncbi-names-manifest
  - ncbi-name-full-scan
  - ncbi-name-input-recapture
  - ncbi-names-catalog-policy
  - ncbi-name-class-policy
- assessment_id: completeness
  area: completeness
  topic: Imported subtree and source assertion units
  outcome: supported
  summary: All twelve named source, scope and path tables were read completely, including
    ignored files, using the exact taxon identifier, full literal label, path slug
    and current misspelling archaeon BC19. The complete pinned NCBI parent graph has
    no descendant taxon for this target. Zero imported BacDive strains agrees with
    the target/subtree inventory and exact culture-inventory slice. The NCBITAXON
    1 NAME attestation agrees with the taxon-presence projection. The pinned GTDB
    mapping and species tables have no exact query match, and the native record asserts
    no GTDB mapping or genome count. Other optional-source misses are confined to
    the complete pinned tables and recorded exact queries. No primary-genome census,
    worldwide culture/genome absence or lack of published biological observations
    is inferred. The separate complete pinned NCBI names census for this target found
    only its scientific-name row; the current misspelling discrepancy remains a bounded
    concern.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - taxonomy-inventory
  - ncbi-live
  - scope-row
  - path-row
  - lpsn-inventory
  - bacdive-inventory
  - culture-inventory
  - gtdb-mappings
  - gtdb-species
  - gold-organisms
  - mediadive-taxa
  - madin-taxa
  - bactotraits-taxa
  - ncbi-names-shard-1
  - ncbi-names-shard-2
  - ncbi-names-shard-3
  - ncbi-names-shard-4
  - ncbi-names-shard-5
  - ncbi-names-shard-6
  - ncbi-names-shard-7
  - ncbi-names-shard-8
  - ncbi-names-shard-9
  - ncbi-names-shard-10
  - ncbi-names-shard-11
  - ncbi-names-shard-12
  - ncbi-names-shard-13
  - ncbi-names-shard-14
  - ncbi-names-shard-15
  - ncbi-names-shard-16
  - ncbi-names-manifest
  - ncbi-name-full-scan
  - ncbi-name-input-recapture
  - ncbi-names-catalog-policy
  - ncbi-name-class-policy
- assessment_id: native-status
  area: provenance
  topic: Unchanged native status and history
  outcome: supported
  summary: EXACT grounding and SEEDED mapping status preserve the generated source
    state. The sole SEEDED_FROM_SOURCES event at 2026-09-13T17:54:04Z agrees with
    the latest raw, ATB and StrainInfo manifest extraction. The exact seed-scope and
    PATHS rows preserve inclusion and path. No manual curation, scientific status
    promotion or new native history event is inferred.
  target_ids:
  - NCBITaxon:910099
  evidence_ids:
  - record
  - manifest
  - overlay-manifests
  - scope-row
  - path-row
findings: []
actions: []
limitations:
- SPECIES rank and a literal designation are source taxonomy assertions, not independent
  evidence of a formally named biological species, physical culture, phenotype or
  mechanism. Absence claims are limited to the specified complete pinned inputs and
  exact query terms.
- Ea10 is retained as the literal designation for this exact NCBI taxon. Its letters,
  digits and punctuation do not independently identify a culture deposit, genome accession,
  environmental measurement or experimental phenotype.
- The complete pinned NCBI names catalog and current EFetch name classes were compared
  for this target. The original names archive was not reconstructed; source-channel
  or snapshot cause remains unresolved. The whole-record UpdateDate in 2018 does not
  establish when the misspelling annotation was added. No worldwide literature or
  culture-collection search was performed.
- Same-base reuse of actual batch-0028 native gate executions at base 662d24d9c1fd077eedc76fe87237e6822050638b;
  the original batch-0028 cwd, launch witness, command, start/finish times and log
  hashes identify each execution. The batch-0031 certificate separately proves unchanged
  native inputs in both owned checkouts and observes the destination runtime under
  its explicit PYTHONPATH. No batch-0031 broad gate execution is claimed. Missing
  certificates remain unavailable. Exact-target strict receipts retain their own execution
  context. Every new review still requires individual validation/save/check.
notes:
- No generated record or history was edited; curation actions remain proposed.
- Fresh-base source transitions are verified against retained original captures and
  exact changed-input receipts.
- Every new bundle still requires its own validate/save/check recipe; native gate
  receipts do not claim these later review lifecycle steps have run.
tags:
- record-review
- batch-0031
- archaea
- generated
- source-checked
```
