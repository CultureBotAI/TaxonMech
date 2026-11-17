# YAML Record Review: Enterobacter sp. EMB-71

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_emb_71.yaml`
- Started UTC: 2026-10-06T03:35:15Z
- Finished UTC: 2026-10-06T03:38:19Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034959`, Enterobacter sp. EMB-71. It asserts rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2608935`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14241` uniquely pairs the identifier and `enterobacter_sp_emb_71` stem. `curation/seed_scope.tsv:322066` records its NCBI-only attestation rule, added 2026-09-13. The generated target and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_emb_71.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_emb_71.yaml --out /private/tmp/emb71-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the complete pinned identity, lineage, genetic code, path/scope references, sole source attestation and inline event reason. Seven additional inventories returned no exact target-ID row. These bounded checks do not replace full corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone has no children under this target.
- Two gitignore-independent searches, including compressed files, returned the same eleven candidate rows. A separate search for the article's alternative designation returned four more. All fifteen were read in full. An ignored-inclusive prior-report/history search found no target reference before this report.
- Guidance remains unchanged from its full read in the preceding review batch. The pre-report `git diff --exit-code HEAD --` check covering data, scope, history, code, configuration and guidance exited 0. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` was not applicable because there are no curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The full live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034959&retmode=xml) confirms taxon 1034959, Enterobacter sp. EMB-71, species rank, bacterial division, parent 2608935 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034959) agrees and supplies all ten ancestor IDs including root. The inspected [NCBI Taxonomy Browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1034959&lvl=3&mode=node) also agrees.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. All pinned identifiers, labels and ranks match the YAML, and live NCBI agrees with the non-root chain. The direct parent is `NO_RANK`, but the target's explicit NCBI rank is `SPECIES`. This isolate-bearing placeholder meets the repository's species-level eligibility rule without establishing a formally named species or requiring reranking to `STRAIN`.

`EXACT` denotes this NCBI concept, not nomenclatural validation or a named-species assignment. Similar isolate labels in different taxa are not equivalent identities. The article designation discussed below is not an established synonym in the pinned or live authority record.

## Evidence

1. **Pinned identity and audit provenance.** `data/raw/ncbitaxon_taxa.tsv:221771` supplies the exact label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. `data/catalog/ncbi_names-0005.jsonl.gz:31194` supplies the same scientific name and taxon ID with an empty unique-name field. The sole attestation is `NCBITAXON`, the same identifier and label, count 1 and unit `NAME`; it counts a source name entry rather than a genome or phenotype. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not assert human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one record, [JF772127.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772127.1). Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 911-base partial 16S rRNA gene with organism Enterobacter sp. EMB-71, strain EMB-71, host strawberry and `taxon:1034959` explicitly recorded. The rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. This marker is not an assembly or a culture-collection deposit.

3. **Primary study and designation caveat.** GenBank cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/), verified against publisher metadata and the complete PubMed abstract. The inspected [primary article text](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) maps JF772127 to EMB-71, but Table 1 labels an Enterobacter row NA-71. This HTML-text discrepancy remains unresolved; it is not a confirmed typographical error or sufficient synonym/phenotype evidence. The YAML does not import those table results.

4. **Hydrogenophaga designation collision.** Eight candidate rows concern Hydrogenophaga caeni, `NCBITaxon:370976`, not the target: `data/raw/ncbitaxon_taxa.tsv:77824`, `data/raw/bacdive_strains.tsv:2871`, `data/raw/ncbi_type_material.tsv:197131`, `data/raw/ncbi_type_material.tsv:197132`, `data/bacdive/records.jsonl.gz:2870`, `data/catalog/ncbi_names-0002.jsonl.gz:13241`, `data/gold/organisms.jsonl.gz:460129` and `data/straininfo/records.jsonl.gz:306240`. They explicitly classify EMB71 under that taxon. BacDive 2972 names DSM 17962 and KCTC 12613 and marker DQ372983; the GOLD row is Go0629569. StrainInfo SI-ID 408351 carries DSM 17962 deposit SI-DP 915796 with status `available` under Hydrogenophaga, with the same BacDive reference. The native NCBI name is an `includes` entry for Hydrogenophaga sp. EMB71, not an Enterobacter synonym. None provides a source chain to JF772127 or taxon 1034959.

5. **Independent collision check.** The inspected [BacDive 2972 page](https://bacdive.dsmz.de/strain/2972) confirms Hydrogenophaga, taxon 370976, those deposits and a Korean collection history. [LPSN](https://lpsn.dsmz.de/species/hydrogenophaga-caeni) independently pairs the type designation with DSM 17962, KCTC 12613 and DQ372983. The complete [primary description abstract, PMID 17473270](https://pubmed.ncbi.nlm.nih.gov/17473270/), published in 2007, describes an activated-sludge isolate and the same type deposits. Its linked DOI is 10.1099/ijs.0.64629-0. This distinct publication, classification and deposit chain must not be transferred to the strawberry Enterobacter isolate merely because the designation resembles EMB-71.

6. **Alternative-designation search.** NA71 candidates were also read in full. `data/raw/ncbitaxon_taxa.tsv:148347`, `curation/seed_scope.tsv:256594` and `data/catalog/ncbi_names-0003.jsonl.gz:46793` concern Pedobacter sp. NA71, `NCBITaxon:642191`. `data/gold/projects.jsonl.gz:615654` is Gp0840976, a Tibetan-lake freshwater-community project labelled NA71, with PRJNA982183, SAMN35688712 and no organism GOLD ID. None establishes a link to the target marker or deposit identity. A community project is not a cultured strain or genome.

7. **Coverage counts.** The BacDive inventory has no exact target row, and no descendant taxa contribute classified strains. `strain_count: 0` therefore reports imported BacDive coverage, not absence of the isolate, marker or publication. Exact `txid1034959[Organism:noexp]` Assembly ESearch returned zero results with no-items/phrase-not-found diagnostics. This bounded query does not prove absence of assemblies under other classifications or in other databases.

## Completeness

No consequential omission was established under the seeded-record model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs, strains and causal graphs may remain empty. The marker corroborates identity but does not establish an eligible BacDive/StrainInfo deposit relationship. Phenotype and habitat assertions belong to the appropriate sibling repositories.

The first search used `rg --no-ignore --hidden -z` through a row-address reader for taxon 1034959, the slug and case-insensitive EMB71 separator variants. It covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. A second search added JF772127 and its versioned spelling. Both returned the same eleven rows: three target identity/scope rows and eight Hydrogenophaga rows. A third search in the same roots for NA71 separator variants returned the four excluded rows described above. All fifteen candidates were fully inspected. No eligible additional strain/genome link was established in these roots; this is not an absence claim about every external snapshot archive or live database.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-review/history search included ignored files. The inline seed event remains present; no separate history event or lifecycle promotion is authorized here.

iModulonDB was not applicable to these identity-only assertions. No marker alignment, genome comparison, published-page-image comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were leads; inspected source text supported the checks.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. The record consistently carries the pinned and live NCBI concept. The external designation discrepancy is a literature-use caveat, not a demonstrated defect in an identity-only record that does not assert those phenotypes. The excluded catalogue candidates do not justify new synonyms, type deposits or genome links.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including the label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not add NA-71 or Hydrogenophaga designations as synonyms on this evidence.

Future authority corrections belong to the maintained NCBI snapshot/import path (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`, `scripts/extract_source_inventory.py`). Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Enrichment requires explicit source-owned links and an authorized maintained representation, not a hand edit or a bare-designation join.

## Follow-up Checks

- At a source refresh, repeat exact taxonomy and JF772127 authority reads, including retirement/replacement checks, before changing the backbone.
- Resolve the article designation against published page images and any correction before transferring table measurements. Do not silently normalize it into a synonym.
- Require explicit taxon/deposit/marker provenance for new links. Keep Hydrogenophaga type deposits, Pedobacter identity and the GOLD community project separate from this target.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. All external reads were public and unpaid; no commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred. Publisher metadata and abstract were available, but publisher full text was subscription-gated; relevant primary text was inspected through the public author-hosting page. The existing single worktree was retained. The full corpus-review goal remains incomplete.
