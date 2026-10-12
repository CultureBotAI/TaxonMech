# YAML Record Review: Alicyclobacillus sp. FP1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alicyclobacillus_sp_fp1.yaml`
- Started UTC: 2026-10-06T04:01:41Z
- Finished UTC: 2026-10-06T04:08:19Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034965`, Alicyclobacillus sp. FP1. It asserts species rank, bacterial domain, parent `NCBITaxon:2622400`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. It asserts no definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs.

`data/taxa/PATHS.tsv:14248` uniquely pairs the identifier and stem. `curation/seed_scope.tsv:322072` contains its NCBI-only attestation rule, added 2026-09-13. Neither the generated target nor its maintained inputs was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/alicyclobacillus_sp_fp1.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/alicyclobacillus_sp_fp1.yaml --out /private/tmp/afp1-validation.tsv`: exit 0, one file scanned, zero ERROR rows. The diagnostic TSV was read and contains only its header.
- Structured comparisons matched the complete pinned identity, lineage, code, path/scope references, sole attestation and inline seed reason. Seven other source inventories have no exact target-ID row. The pinned backbone has no children under the target.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- Ignored-inclusive prior-report/history search returned no exact identifier, full-label or slug match. The expanded compressed-source search returned 128 candidate rows; all were read in full, with lossless common-field/delta reconstruction for grouped native records.
- Pre-report `git diff --exit-code HEAD --` covering data, curation, history, code, configuration and guidance exited 0. HEAD remains `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This review is not corpus release certification.
- `just validate-products` is not applicable without curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The complete live [NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034965&retmode=xml) agrees on ID, label, species rank, bacterial division, parent 2622400 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034965) agrees and supplies all ten ancestor IDs including root. Taxonomy Browser HTML was unavailable; both structured authority reads succeeded.

The carried lineage is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Alicyclobacillaceae, Alicyclobacillus and unclassified Alicyclobacillus. All pinned ancestor IDs, labels and ranks match the YAML; live NCBI confirms the non-root chain.

The unclassified direct parent has `NO_RANK`; the target has explicit NCBI `SPECIES` rank. An isolate-bearing placeholder can meet the species-level scope rule without being a formally named species or requiring a change to `STRAIN`. `EXACT` means an exact NCBI concept match, not nomenclatural validation or curator sign-off.

## Evidence

1. **Pinned identity and provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221777` supplies the matching identity, parent, code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31200` supplies the scientific name and ID with empty unique name. The sole `NCBITAXON` attestation has the same ID/label, count 1 and unit `NAME`: it counts a name entry, not a genome or trait. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and matches the scope reason.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one sequence, [JF798341.1](https://www.ncbi.nlm.nih.gov/nuccore/JF798341.1), UID 333595900. Complete metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 1,474-base partial 16S rRNA gene, partial at both ends, explicitly assigned to `taxon:1034965` and strain FP1. Its source is copper-mine raffinate process water in Western Australia; F. Perrot is named as collector and identifier. Submission was 7 April 2011 through CSIRO, with creation/update on 25 May 2011. The biological reference is marked unpublished and has no PMID or DOI. Later papers are not silently substituted for that reference. A partial marker is not an assembly.

3. **A real deposit crosslink, with different source classification.** Complete `data/bacdive/records.jsonl.gz:82722` is BacDive 160486, FP-1, DSM 25985, with source DOI `10.13145/bacdive160486.20260601.11`. Its 16S section explicitly supplies JF798341, length 1474 and taxon 1034965, establishing a source-asserted marker/deposit connection beyond a short-name resemblance. However, its general taxon assignment is `NCBITaxon:61169` with species-level matching, and its name is Alicyclobacillus sp. It marks type strain no and supplies no genome section in the inspected projection. Complete `data/raw/bacdive_strains.tsv:82723` and `data/raw/culture_collection_strains.tsv:74176` faithfully classify the local strain/deposit at 61169, not 1034965.

4. **StrainInfo linkage is already represented in its component.** Complete `data/straininfo/records.jsonl.gz:299415` and the live [rich StrainInfo API record](https://api.straininfo.dsmz.de/v2/data/strain/max/401526) agree on SI-ID401526, DOI `10.60712/SI-ID401526.2`, BacDive 160486, designation FP-1 and deposit DSM 25985 / SI-DP908469. The source is published online, the deposit is available, its relation is not erroneous and its collection is not deprecated. It is not marked as a type strain. Both the strain and deposit are classified at genus Alicyclobacillus, NCBI 29330; neither inspected version supplies a sequence list. Complete `strain_links.tsv:59808` and `related_records.tsv.gz:140579-140580` retain the eligible DSM 25985 culture match, source IDs, DOI and nested evidence. These links are not missing from the repository.

5. **Import boundary explains zero.** `src/taxonmech/bacdive_v2.py:55` derives strain classification from general NCBI matches, preferring explicit strain-level matches. It does not use 16S sequence taxon IDs to reclassify deposits. `src/taxonmech/seed.py` indexes imported strains by those taxon IDs. As documented in `docs/STRAININFO.md`, StrainInfo joins existing strains and does not change their taxonomic classification. Therefore the exact marker crosslink is a useful enrichment lead, but does not demonstrate a dropped eligible strain row under this target's current contract. `strain_count: 0` describes imported classification coverage, not absence of a biological strain or deposit.

6. **Primary research context and informal name.** The [primary article XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5023253/fullTextXML) and [PubMed metadata](https://pubmed.ncbi.nlm.nih.gov/27682094/) confirm DOI 10.3390/microorganisms3030364, PMID 27682094, PMCID PMC5023253, Watling, Shiers and Collinson, Microorganisms 3(3):364-390 (2015). The inspected organism paragraph explicitly describes the Alicyclobacillus-like FP1 designation and informal name Ab. cupritolerans. This supports a bounded research-name association, not a formally valid species name. Inspected primary publisher abstracts for [DOI 10.4028/www.scientific.net/AMR.1130.308](https://www.scientific.net/AMR.1130.308) and [DOI 10.4028/www.scientific.net/AMR.1130.218](https://www.scientific.net/AMR.1130.218) also concern the Alicyclobacillus-like FP1 isolate from copper-heap process water. Their full texts were not inspected. No experimental phenotype or culture recipe was transferred into this identity record.

## Completeness

No required representation is missing under the current seeded-record/import model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs and graphs can remain empty. Deposit classification deserves a future source-owned reconciliation, but the reviewed record does not assert that FP1 lacks deposits.

The first source search used taxon 1034965, the slug and case-insensitive FP1 separator variants and returned 88 rows. The second added JF798341, DSM 25985, ATCC BAA-2457, source IDs 160486/401526/908469 and cupritolerans; it returned 128 rows, including all 88 original candidates. Both used `rg --no-ignore --hidden -z` through a row-address reader across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Ignored files and compressed source rows were included, not every separate snapshot archive or live database.

All 128 candidates were resolved without bare-name or bare-number joins. FP1 collisions include Planktothrix, Bacillus, Pseudomonas, Rhodococcus, Pantoea, Pediococcus, Lysobacter, fungi, viral records and environmental samples. The archaeal FP1 is Natrinema hispanicum, DSM 18328 / ATCC BAA-1310, with different marker accessions and GCA_004217335. Clostridium FP1 has GCA/GCF_011065975 and a New Zealand beef source; Faecalibacterium Fp1 has GCA/GCF_019968075 and a Japanese fecal source. Sinorhizobium fp1-2/fp1-3 genomes also differ.

The expanded numerical search recovered Thermosinus carboxydivorans Nor1, whose NCBI taxon 401526 is not StrainInfo SI-ID401526; its GCA/GCF_000169155 and DSM 14886 cannot transfer. StrainInfo deposit 160486 is DSM 7029 in SI-ID43289, not BacDive 160486; its GCA_001017435 cannot transfer. StrainInfo strain 160486 is Pestalotiopsis fici. Other hits were an E. coli genome-ID suffix and Salmonella assembly N50 values. These namespace and measurement collisions do not support target enrichment.

The exact-ID comparison found no target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Live Assembly ESearch for `txid1034965[Organism:noexp]` returned zero results with no-items/phrase-not-found diagnostics. This bounded query does not prove worldwide assembly absence or absence under other classifications.

iModulonDB was not applicable to identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. The inspected identity, grounding, provenance and imported strain count are consistent with the authority sources and documented import boundary. The marker/deposit association is real source evidence, but changing source classification is a separate curation decision, not an automatic consequence of that association. This pass does not certify nomenclatural status, a type-strain claim, phenotypes or complete genome/deposit coverage.

## Recommended Edits

None required for the current assertions. Keep the generated YAML and `SEEDED` status unchanged. Do not rename the record to the informal research name, assert type status from an uninspected catalogue snippet, reclassify by 16S metadata alone or attach unrelated FP1 genomes.

A future authorized enrichment should reconcile BacDive 160486's general classification with its explicit JF798341 association and DSM 25985. The maintained import owners are `src/taxonmech/bacdive_v2.py` and `src/taxonmech/extract.py`; source provenance is declared in `conf/sources.yaml`. Any deliberate classification-policy change needs an explicit evidence model and regression tests, not a direct patch to generated YAML. StrainInfo ownership is `conf/straininfo.yaml`, `src/taxonmech/straininfo_snapshot.py` and its link adapter, with the boundary documented in `docs/STRAININFO.md`.

Authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

- At source refresh, repeat exact NCBI taxonomy, retirement/replacement and JF798341 reads, and inspect complete BacDive/DSMZ identity evidence for DSM 25985.
- Preserve the source classification discrepancy until an explicit authority correction or authorized import-policy change resolves it. Verify whole culture identifiers and same-deposit sequence assertions; do not join naked numeric IDs.
- Before formal-name or type-material enrichment, verify a nomenclatural authority and directly inspect the relevant collection records. The primary paper explicitly uses an informal name.
- After authorized source/import changes, rebuild the StrainInfo component as documented, run a seed dry run and single-record canary, rerun `just validate` and `just validate-strict`, and run full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews remain unchanged. No history event, lifecycle promotion, commit, GitHub mutation, external contact or paid research occurred.

BacDive and DSMZ catalogue HTML reads failed. ATCC BAA-2457 appeared as a search lead, but direct web requests failed and the public HTTP fallback returned 403; its purported name/type/accession assertions were not accepted as inspected evidence. Publisher/PMC web routes for the Microorganisms paper failed or presented access checks; public Europe PMC XML supplied the inspected identity paragraph. A first supplemental helper stopped because optional BeautifulSoup was unavailable; the retry used standard-library XML/HTML parsers and successfully read the primary XML and StrainInfo API.

The existing single worktree was retained; the other Codex session is closed. The full corpus-review goal remains incomplete.

