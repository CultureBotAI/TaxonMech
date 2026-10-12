# YAML Record Review: Enterobacter sp. EMB-79

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_emb_79.yaml`
- Started UTC: 2026-10-06T03:39:57Z
- Finished UTC: 2026-10-06T03:42:22Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034960`, Enterobacter sp. EMB-79. It asserts rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2608935`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14243` uniquely pairs the identifier and `enterobacter_sp_emb_79` stem. `curation/seed_scope.tsv:322067` records the corresponding NCBI-only attestation rule, added 2026-09-13. The generated target and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_emb_79.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_emb_79.yaml --out /private/tmp/emb79-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the complete pinned identity, lineage, genetic code, path/scope references, sole source attestation and inline event reason. Seven additional inventories returned no exact target-ID row. These bounded checks do not replace full corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone has no children under this target.
- Two gitignore-independent searches, including compressed files, returned the same six fully inspected candidate rows. An ignored-inclusive prior-report/history search found no target reference before this report.
- The pre-report `git diff --exit-code HEAD --` check covering data, scope, history, code, configuration and guidance exited 0. Guidance remains unchanged from its full read in the preceding review batch. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` was not applicable because there are no curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The complete live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034960&retmode=xml) confirms taxon 1034960, Enterobacter sp. EMB-79, species rank, bacterial division, parent 2608935 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034960) agrees and supplies all ten ancestor IDs including root. The inspected [NCBI Taxonomy Browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1034960&lvl=3&mode=node) also agrees.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. All pinned identifiers, labels and ranks match the YAML, and live NCBI agrees with the non-root chain. The direct parent is `NO_RANK`, but the target's explicit NCBI rank is `SPECIES`. This isolate-bearing placeholder meets the repository's species-level eligibility rule without establishing a formally named species or requiring reranking to `STRAIN`.

`EXACT` denotes the NCBI concept, not nomenclatural validation or a named-species assignment. The similar designation under Thermomonas is not an equivalent taxon or a source-backed synonym of this record.

## Evidence

1. **Pinned identity and audit provenance.** `data/raw/ncbitaxon_taxa.tsv:221772` supplies the exact label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. `data/catalog/ncbi_names-0005.jsonl.gz:31195` supplies the same scientific name and identifier with an empty unique-name field. The sole attestation is `NCBITAXON`, the same ID and label, count 1 and unit `NAME`. It counts a source name entry rather than a genome or phenotype. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not assert human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one record, [JF772126.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772126.1). Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 799-base partial 16S rRNA gene with organism Enterobacter sp. EMB-79, strain EMB-79, host strawberry and `taxon:1034960` explicitly recorded. The rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. This marker is not an assembly or a culture-collection deposit.

3. **Primary study.** GenBank cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/), matched to the publisher metadata and complete PubMed abstract inspected in this review batch. The [primary article text](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) explicitly maps JF772126 to EMB-79. Table 1 and greenhouse-results passages were inspected for this isolate. Those experiments neither establish a named species nor justify extending their results to other isolates; no phenotype was added to the YAML.

4. **Thermomonas designation collision.** `data/raw/ncbitaxon_taxa.tsv:78603`, `curation/seed_scope.tsv:194285` and `data/catalog/ncbi_names-0002.jsonl.gz:14267` concern Thermomonas sp. EMB 79, `NCBITaxon:374865`, parent 2633315. All three complete rows were read. They supply a different taxon identity and no source chain to JF772126 or the target. The complete [live NCBI taxonomy response for 374865](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=374865&retmode=xml) and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/374865) independently confirm the Thermomonas concept, under Lysobacterales and Lysobacteraceae rather than Enterobacterales and Enterobacteriaceae. Its HTML taxonomy request failed, but the structured authority reads succeeded. A shared designation fragment cannot supply a taxon, strain or genome equivalence.

5. **Coverage counts.** The BacDive inventory has no exact target row, and no descendant taxa contribute classified strains. `strain_count: 0` correctly reports imported BacDive coverage rather than absence of the isolate, marker or paper. Exact `txid1034960[Organism:noexp]` Assembly ESearch returned zero results with no-items/phrase-not-found diagnostics. This bounded query does not prove absence of assemblies under other classifications or in other databases.

## Completeness

No consequential omission was established under the seeded-record model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs, strains and causal graphs may remain empty. The marker and paper corroborate identity but do not establish an eligible BacDive/StrainInfo deposit relationship. Phenotype and habitat assertions belong to the appropriate sibling repositories.

The first search used `rg --no-ignore --hidden -z` through a row-address reader for taxon 1034960, the slug and case-insensitive EMB79 separator variants. It covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. A second search added JF772126 and its versioned spelling. Both returned the same six fully inspected rows: three target identity/scope rows and three Thermomonas rows. No additional marker crosslink or eligible strain/genome candidate was found in those roots. This is not an absence claim about every external snapshot archive or live database.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-review/history search included ignored files. The inline seed event remains present; no separate event or lifecycle promotion is authorized here.

iModulonDB was not applicable to these identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets and secondary summaries were leads; inspected primary text supported the literature check.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record consistently carries the pinned and live NCBI concept and its limited imported coverage. The Thermomonas matches do not justify new synonyms or strain/genome relationships. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including its label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` lifecycle status.

Future authority corrections belong to the maintained NCBI snapshot/import path (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`, `scripts/extract_source_inventory.py`). Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Enrichment requires an explicit source-owned relationship and an authorized maintained representation, not a hand edit or bare-designation join.

## Follow-up Checks

- At a source refresh, repeat exact taxonomy and JF772126 authority reads, including retirement/replacement checks, before changing the backbone.
- Keep the Thermomonas concept separate unless an authority supplies a genuine identity correction. Require explicit strain/deposit/genome provenance for new associations.
- Distinguish partial markers from assemblies, and preserve isolate and experimental-condition boundaries in any future phenotype work.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. All external reads were public and unpaid; no commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred. Publisher metadata and abstract were available, but publisher full text was subscription-gated; relevant primary text was inspected through the public author-hosting page. The existing single worktree was retained. The full corpus-review goal remains incomplete.
