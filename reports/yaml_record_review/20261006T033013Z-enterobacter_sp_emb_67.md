# YAML Record Review: Enterobacter sp. EMB-67

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_emb_67.yaml`
- Started UTC: 2026-10-06T03:27:43Z
- Finished UTC: 2026-10-06T03:30:13Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034957`, Enterobacter sp. EMB-67. It asserts rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2608935`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14239` uniquely pairs the identifier and `enterobacter_sp_emb_67` stem. `curation/seed_scope.tsv:322064` records the corresponding NCBI-only attestation rule, added 2026-09-13. The generated target and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_emb_67.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_emb_67.yaml --out /private/tmp/emb67-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the complete pinned identity and lineage, genetic code, path/scope references, sole NCBI attestation and inline event reason. Seven additional source inventories returned no exact target-ID row. These bounded comparisons do not replace full corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone has no children under this target.
- Two gitignore-independent searches, including compressed files, returned the same four candidate rows. All four were read in full and reconciled. An ignored-inclusive prior-report/history search found no target reference before this report.
- Guidance has no diff against HEAD. The pre-report `git diff --exit-code HEAD --` check covering data, curation, history, code, configuration and guidance exited 0. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` was not applicable because there are no curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The full live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034957&retmode=xml) confirms taxon 1034957, Enterobacter sp. EMB-67, species rank, bacterial division, parent 2608935 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034957) agrees and supplies all ten ancestor IDs including root. The [NCBI Taxonomy Browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1034957&lvl=3&mode=node) was also inspected and agrees; an initial shorter HTML URL failed before this alternative succeeded.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. Every pinned identifier, label and rank matches the YAML; live NCBI agrees with the non-root chain. The direct parent is `NO_RANK`, but NCBI explicitly assigns the target `SPECIES` rank. The isolate-bearing placeholder therefore satisfies the repository's species-level eligibility rule without establishing a formally named species or requiring reranking to `STRAIN`.

`EXACT` denotes the NCBI concept, not nomenclatural validation or a named-species assignment. A number appearing as another organism's isolate designation is not an NCBI taxonomy cross-reference.

## Evidence

1. **Pinned identity and audit provenance.** `data/raw/ncbitaxon_taxa.tsv:221769` supplies the exact label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. `data/catalog/ncbi_names-0005.jsonl.gz:31192` supplies the same scientific name and taxon ID with an empty unique-name field. The sole attestation is `NCBITAXON`, the same identifier and label, count 1 and unit `NAME`. It counts a source name entry rather than a genome or phenotype. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not assert human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one record, [JF772128.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772128.1). Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 901-base partial 16S rRNA gene with organism Enterobacter sp. EMB-67, strain EMB-67, host strawberry and `taxon:1034957` explicitly recorded. The rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. This marker is not an assembly or a culture-collection deposit.

3. **Primary study.** GenBank cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/), verified against publisher metadata and the complete PubMed abstract. The accession paragraph in the [primary article text hosted on ResearchGate](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) explicitly pairs JF772128 with Enterobacter sp. EMB-67. Table 1 independently lists EMB-67 under that genus with isolate-specific screening results. The study's aggregate results cannot be applied to every isolate, and the abstract's strongest plant-growth result concerns B. subtilis NA-108, not EMB-67. No phenotype or species reassignment was inferred for the YAML.

4. **Numeric isolate-label collision.** The complete row `data/catalog/ncbi_genbank-0054.jsonl.gz:17285` concerns GCA_058711505.1, Streptococcus pneumoniae, with both `taxid` and `species_taxid` equal to 1313. The matching number 1034957 is its `isolate` value, not a taxon-ID field. The row names BioSample SAMEA120831637 and BioProject PRJNA514245, but supplies no EMB-67 marker or deposit chain. It is an unrelated catalogue candidate and cannot justify an Enterobacter strain/genome link. Its identifiers are retained here only to make that exclusion auditable.

5. **Coverage counts.** The BacDive inventory has no exact target row, and no descendant taxa contribute classified strains. `strain_count: 0` correctly reports imported BacDive coverage rather than absence of the biological isolate, marker or paper. Exact `txid1034957[Organism:noexp]` Assembly ESearch returned zero results with no-items/phrase-not-found diagnostics. That bounded query is not proof that no assembly exists under another classification or in another database.

## Completeness

No consequential omission was established under the seeded-record model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs, strains and causal graphs need not be fabricated. The direct marker and paper corroborate identity but do not establish an eligible BacDive/StrainInfo deposit association. Phenotypes and habitat assertions belong to the appropriate sibling repositories.

The initial search used `rg --no-ignore --hidden -z` through a row-address reader for taxon 1034957, the slug and case-insensitive EMB67 separator variants. It covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. A second search added JF772128 and its versioned spelling. Both returned the same four fully inspected rows: three target identity/scope rows and the unrelated Streptococcus assembly. No additional marker crosslink or eligible strain/genome candidate was found within these roots. This does not claim absence from every external snapshot archive or live database.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-review/history search included ignored files. The inline seed event remains present; no separate event or lifecycle promotion is authorized by this review.

iModulonDB was not applicable to these identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were leads; inspected source text supported the evidence checks.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record consistently carries the pinned and live NCBI concept and its limited imported coverage. The numeric isolate-label collision does not justify an added genome relationship. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including its label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status.

Future authority corrections belong to the maintained NCBI snapshot/import path (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`, `scripts/extract_source_inventory.py`). Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Future enrichment requires explicit source-owned links and an authorized maintained representation, not a hand edit or a numeric-text join.

## Follow-up Checks

- At a source refresh, repeat exact taxonomy and JF772128 authority reads, including retirement/replacement checks, before changing the backbone.
- Read candidate identifiers by field: an isolate designation equal to a taxon number is not a taxonomy match. Require explicit strain/deposit/genome provenance before enrichment.
- Keep marker sequences distinct from assemblies, and preserve isolate and condition boundaries in any future phenotype work.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. All external reads were public and unpaid; no commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred. Publisher metadata and abstract were available, but publisher full text was subscription-gated; relevant primary text was inspected through the public author-hosting page. The existing single worktree was retained. The full corpus-review goal remains incomplete.
