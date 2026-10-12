# YAML Record Review: Pseudomonas sp. EMB-45

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_emb_45.yaml`
- Started UTC: 2026-10-06T03:44:46Z
- Finished UTC: 2026-10-06T03:49:11Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034961`, Pseudomonas sp. EMB-45. The record asserts species rank, bacterial domain, parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. It contains no definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs.

`data/taxa/PATHS.tsv:14244` uniquely pairs this identifier with `pseudomonas_sp_emb_45`. The corresponding NCBI-only scope rule is at `curation/seed_scope.tsv:322068`, added 2026-09-13. The generated target and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_emb_45.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_emb_45.yaml --out /private/tmp/pemb45-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the complete pinned identity, lineage, genetic code, path/scope references, sole attestation and inline event reason. Seven additional source inventories returned no exact target-ID rows.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone contains no children of this target.
- Two gitignore-independent, compressed-file-inclusive source searches each returned the same three fully inspected rows. A separate ignored-inclusive prior-report/history search found no target reference before this report.
- Pre-report `git diff --exit-code HEAD --` covering data, scope, history, code, configuration and guidance exited 0. Guidance remains unchanged from its full read in the preceding review batch. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` was not applicable because the record has no curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The complete live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034961&retmode=xml) confirms taxon 1034961, Pseudomonas sp. EMB-45, species rank, bacterial division, parent 196821 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034961) agrees and includes all ten ancestor identifiers including root. The inspected [NCBI Taxonomy Browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1034961&lvl=3&mode=node) also agrees.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. Every pinned ancestor identifier, label and rank matches the YAML; live NCBI agrees with the non-root chain. The direct parent has `NO_RANK`, while the target explicitly has NCBI species rank.

This isolate-bearing placeholder meets the repository's species-level eligibility rule. It does not establish a formally named species, require reranking to `STRAIN`, or justify assignment to a named Pseudomonas species. `EXACT` denotes the NCBI concept, not nomenclatural validation or human review.

## Evidence

1. **Pinned identity and provenance.** `data/raw/ncbitaxon_taxa.tsv:221773` supplies the exact label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. `data/catalog/ncbi_names-0005.jsonl.gz:31196` supplies the same scientific name and identifier with an empty unique-name field. Both complete rows and the complete scope row were read. The sole attestation is `NCBITAXON`, matching ID and label, count 1, unit `NAME`. This counts a source name entry, not genomes or phenotypes. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not assert human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one result, [JF772143.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772143.1), UID 333595844. Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. This is a 924-base partial 16S rRNA gene with organism Pseudomonas sp. EMB-45, strain EMB-45, host strawberry and explicit `taxon:1034961`. The rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. A partial marker is not a genome assembly or culture-collection deposit.

3. **Primary study and isolate boundary.** GenBank cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/). Publisher metadata and abstract were inspected, agreeing with the sequence citation: Microbial Ecology 63, pages 405-417, 2012, first published online on 12 August 2011. The [primary article's accession paragraph](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) explicitly pairs JF772143 with Pseudomonas sp. EMB-45. Its complete rendered Table 1 was also inspected: the Pseudomonas rows are EMB-48, EMB-55, EMB-50 and EMB-52, not EMB-45. That difference does not establish EMB-50 as an alias or prove a typographical error. No Table 1 phenotype or result from another isolate is transferred to this target. The current YAML makes no such biological assertions.

4. **Coverage counts.** The BacDive inventory has no exact target-ID row, and the pinned backbone has no descendants contributing classified strains. `strain_count: 0` correctly reports imported BacDive coverage, not absence of this isolate or its marker. Exact `txid1034961[Organism:noexp]` Assembly ESearch returned zero results, with no-items/phrase-not-found diagnostics. This bounded query does not prove that no assembly exists under another classification or in another database.

## Completeness

No consequential omission was established under the seeded-record model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs, strain/genome links and causal graphs can remain empty. The marker and article corroborate identity without supplying an eligible BacDive/StrainInfo deposit relationship. Phenotype and habitat assertions belong to the appropriate sibling repositories and must retain isolate-level evidence boundaries.

The first source search used `rg --no-ignore --hidden -z` through a row-address reader for taxon 1034961, the slug and case-insensitive EMB45 separator variants. It covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. A second search added JF772143 and its versioned spelling. Each returned only the three target backbone, native-name and scope rows, all read in full. No additional marker crosslink or eligible strain/genome candidate was found in those roots. This bounded result includes ignored files; it is not an absence claim about every external snapshot archive or live database.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-report/history search also included ignored files. The inline seed event is present; this review does not authorize a separate curation event or lifecycle promotion.

iModulonDB was not applicable to these identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were leads, not evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. Its identity and limited coverage claims agree with the inspected pinned and live NCBI sources. The paper's differing accession-list and Table 1 designations constrain future phenotype interpretation but do not contradict a phenotype assertion in this record, which has none. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including the label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not add EMB-50 as a synonym or transfer its assay results without an explicit identity correction.

Future authority corrections belong to the maintained NCBI snapshot/import path: `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Any enrichment needs a source-owned relationship and an authorized maintained representation, not a hand edit or a join on a short isolate designation.

## Follow-up Checks

- At a source refresh, repeat the exact taxonomy and JF772143 authority reads, including retirement/replacement checks, before changing the backbone.
- Require explicit strain/deposit/genome provenance before adding relationships; distinguish partial markers from assemblies.
- Resolve the accession-list versus phenotype-table designation boundary before attributing Table 1 results to EMB-45. Do not assume an unverified alias.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped review report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. All external reads were public and unpaid. No commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred.

Publisher full text was subscription-gated; the relevant primary accession paragraph and complete Table 1 text were inspected through the public author-hosting page. An additional search lead at SSRN abstract 5129453 could not be opened through either attempted HTML URL and was not used to support a finding or relationship.

The other Codex session is closed, and the existing single worktree was retained. The corpus-review goal remains incomplete.

