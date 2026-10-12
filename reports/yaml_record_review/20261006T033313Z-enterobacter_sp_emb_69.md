# YAML Record Review: Enterobacter sp. EMB-69

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_emb_69.yaml`
- Started UTC: 2026-10-06T03:31:23Z
- Finished UTC: 2026-10-06T03:33:13Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034958`, Enterobacter sp. EMB-69. It asserts rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2608935`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14240` uniquely pairs the identifier and `enterobacter_sp_emb_69` stem. `curation/seed_scope.tsv:322065` supplies its NCBI-only attestation rule, added 2026-09-13. The generated target and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_emb_69.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_emb_69.yaml --out /private/tmp/emb69-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the full pinned identity and lineage, genetic code, path/scope references, sole NCBI attestation and inline event reason. Seven additional inventories returned no exact target-ID row. These bounded checks do not replace full corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone has no children under this target.
- Two gitignore-independent searches, including compressed files, returned the same four fully inspected candidate rows. An ignored-inclusive prior-report/history search found no target reference before this report.
- The pre-report `git diff --exit-code HEAD --` check covering data, scope, history, code, configuration and guidance exited 0. Guidance is unchanged from its full read in this review batch. HEAD remains `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` was not applicable because there are no curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The full live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034958&retmode=xml) confirms taxon 1034958, Enterobacter sp. EMB-69, species rank, bacterial division, parent 2608935 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034958) agrees and supplies all ten ancestor IDs including root. The inspected [NCBI Taxonomy Browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1034958&lvl=3&mode=node) also agrees.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. All pinned identifiers, labels and ranks match the YAML, and live NCBI agrees with the non-root chain. The direct parent is `NO_RANK`, but the target's explicit NCBI rank is `SPECIES`. This isolate-bearing placeholder meets the repository's species-level eligibility rule without proving a formally named species or warranting reranking to `STRAIN`.

`EXACT` denotes this NCBI concept, not nomenclatural validation or a named-species assignment. Genome assembly statistics that happen to equal a taxon number do not identify that taxon.

## Evidence

1. **Pinned identity and audit provenance.** `data/raw/ncbitaxon_taxa.tsv:221770` supplies the exact label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. `data/catalog/ncbi_names-0005.jsonl.gz:31193` supplies the same scientific name and identifier with an empty unique-name field. The sole attestation is `NCBITAXON`, the same ID and label, count 1 and unit `NAME`; it counts a source name entry, not a genome or phenotype. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not claim human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one record, [JF772124.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772124.1). Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 920-base partial 16S rRNA gene with organism Enterobacter sp. EMB-69, strain EMB-69, host strawberry and `taxon:1034958` explicitly recorded. The rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. This is a marker sequence, not an assembly or culture-collection deposit.

3. **Primary study.** GenBank cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/), matched to the publisher metadata and complete PubMed abstract inspected earlier in this review batch. The [primary article text](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) pairs JF772124 with Enterobacter sp. EMB-69 and lists that isolate under Enterobacter in Table 1. These passages were inspected specifically for this target. They support isolate identity, not a transfer of other isolates' traits into this record.

4. **Assembly-statistic collision.** The complete row `data/catalog/gtdb_genomes-0017.jsonl.gz:12957` concerns `RS_GCF_004110845.1`, paired GenBank accession GCA_004110845.1, Mycobacterium tuberculosis. Both NCBI taxon fields equal 1773; the matching value 1034958 occurs only in `ncbi_scaffold_n75`. It names strain M0014025-2, BioSample SAMN10697571 and BioProject PRJNA224116, with a patient isolation source in Lima, Peru. It supplies no EMB-69 marker or deposit chain. This numeric collision is not a GTDB mapping or an Enterobacter genome association. These identifiers are retained only to make the exclusion auditable.

5. **Coverage counts.** The BacDive inventory has no exact target row, and no descendant taxa contribute classified strains. `strain_count: 0` correctly describes imported BacDive coverage rather than absence of the biological isolate, marker or publication. Exact `txid1034958[Organism:noexp]` Assembly ESearch returned zero results with no-items/phrase-not-found diagnostics. This bounded query does not prove that assemblies are absent under every classification or in other databases.

## Completeness

No consequential omission was established under the seeded-record model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs, strains and causal graphs may remain empty. The marker and paper corroborate identity but do not establish an eligible BacDive/StrainInfo deposit relationship. Phenotype and habitat assertions belong to the appropriate sibling repositories.

The first search used `rg --no-ignore --hidden -z` through a row-address reader for taxon 1034958, the slug and case-insensitive EMB69 separator variants. It covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. A second search added JF772124 and its versioned spelling. Both returned the same four fully inspected rows: three target identity/scope rows and the unrelated Mycobacterium assembly statistic. No additional marker crosslink or eligible strain/genome candidate was found in those roots. This is not an absence claim about every external snapshot archive or live database.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-review/history search included ignored files. The inline seed event remains present; no separate history event or lifecycle promotion is authorized here.

iModulonDB was not applicable to these identity-only assertions. No new marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were leads, while inspected primary text supplied the literature check.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record consistently carries the pinned and live NCBI concept and its limited imported coverage. The unrelated assembly-statistic match does not justify new taxonomy or genome links. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including the label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` lifecycle status.

Future authority corrections belong to the maintained NCBI snapshot/import path (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`, `scripts/extract_source_inventory.py`). Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Enrichment requires an explicit source-owned relationship and an authorized maintained representation, not a hand edit, numeric coincidence or bare-name join.

## Follow-up Checks

- At a source refresh, repeat exact taxonomy and JF772124 authority reads, including retirement/replacement checks, before changing the backbone.
- Distinguish taxonomy fields from assembly statistics and require explicit source provenance for strain/deposit/genome associations.
- Keep partial markers separate from assemblies and preserve the tested isolate and conditions in any future phenotype work.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. All external reads were public and unpaid; no commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred. Publisher metadata and abstract were available, but publisher full text was subscription-gated; relevant primary text was inspected through the public author-hosting page. The existing single worktree was retained. The full corpus-review goal remains incomplete.
