# YAML Record Review: Enterobacter sp. EMB-65

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_emb_65.yaml`
- Started UTC: 2026-10-06T03:21:11Z
- Finished UTC: 2026-10-06T03:25:45Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034956`, Enterobacter sp. EMB-65. It asserts rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2608935`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, mappings, xrefs, literature evidence, strains, genomes or causal graphs are asserted.

`data/taxa/PATHS.tsv:14238` uniquely pairs the identifier and `enterobacter_sp_emb_65` stem. `curation/seed_scope.tsv:322063` records its NCBI-only attestation rule, added 2026-09-13. The generated target and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterobacter_sp_emb_65.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterobacter_sp_emb_65.yaml --out /private/tmp/emb65-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the complete pinned identity, lineage, genetic code, path/scope references, sole source attestation and inline event reason. Seven additional inventories returned no exact target-ID row. These bounded checks do not replace full corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone has no children under this target.
- Two gitignore-independent searches, including compressed files, returned the same three candidate rows; all were read in full. An ignored-inclusive prior-report/history search found no target reference before this report.
- Local guidance has no diff against HEAD. `git diff --exit-code HEAD --` for data, scope, history, source code, configuration and guidance exited 0. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` was not applicable because there are no curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The complete live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034956&retmode=xml) confirms taxon 1034956, Enterobacter sp. EMB-65, species rank, bacterial division, parent 2608935 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034956) agrees and supplies all ten ancestor IDs including root. The HTML taxonomy request failed through the web tool; successful structured authority reads supplied verification.

The complete carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. All pinned identifiers, labels and ranks match the YAML exactly, and live NCBI agrees with the non-root chain. The direct parent is `NO_RANK`, but NCBI explicitly assigns the target `SPECIES` rank. This isolate-bearing placeholder meets the repository's species-level eligibility rule without establishing a formally named species or requiring reranking to `STRAIN`.

`EXACT` denotes this NCBI concept, not nomenclatural validation or identification to a named species. The conflicting article labels discussed below are not authority-backed synonyms or grounds for reparenting this concept.

## Evidence

1. **Pinned identity and provenance.** `data/raw/ncbitaxon_taxa.tsv:221768` supplies the exact label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. `data/catalog/ncbi_names-0005.jsonl.gz:31191` supplies the scientific name and same taxon ID with an empty unique-name field. The sole attestation has source `NCBITAXON`, the same identifier and label, assertion count 1 and unit `NAME`. It counts a source name entry, not a genome or phenotype. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not claim human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one record, [JF772125.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772125.1). Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 913-base partial 16S rRNA gene with organism Enterobacter sp. EMB-65, strain EMB-65, host strawberry and `taxon:1034956` explicitly recorded. The rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. The HTML sequence request failed through the web tool, while the structured metadata succeeded. This marker is not an assembly or culture-collection deposit.

3. **Primary study and label conflict.** GenBank cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/), verified against publisher metadata and the full PubMed abstract. The accession paragraph in the [primary article text hosted on ResearchGate](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) maps JF772125 to Enterobacter sp. EMB-65. Table 1 and the siderophore discussion also use Enterobacter, whereas two greenhouse-results passages call EMB-65 Pseudomonas. This discrepancy is preserved, not silently resolved as a confirmed typographical error. The inspected HTML transcription, rather than a page-image comparison, supports this observation. No conflicting-label phenotype claim is carried in the YAML, and neither a Pseudomonas synonym nor a genus reassignment is justified by those passages. The abstract's strongest growth result concerns B. subtilis NA-108, not this target.

4. **Coverage counts.** The BacDive inventory has no exact target row, and no descendant taxa contribute classified strains. `strain_count: 0` therefore reports imported BacDive coverage, not absence of the biological isolate, marker or publication. Exact `txid1034956[Organism:noexp]` Assembly ESearch returned zero results with no-items/phrase-not-found diagnostics. This bounded query does not establish absence of assemblies under another classification or in other databases.

## Completeness

No consequential omission was established under the current seeded-record model. Optional definition, evidence, synonyms, nomenclature, mappings, xrefs, strain/genome links and causal graphs may remain empty. The marker and publication corroborate identity but do not establish a missing eligible BacDive or StrainInfo deposit association. Habitat and phenotype assertions belong to the appropriate sibling repositories.

The first search used `rg --no-ignore --hidden -z` through a row-address reader for taxon 1034956, the slug and case-insensitive EMB65 separator variants. It covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. A second search added JF772125 and its versioned spelling. Both returned only the same three fully inspected identity/scope rows. No additional marker crosslink or eligible strain/genome candidate was found within those roots; this is not an exhaustive claim about every external snapshot archive or live database.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-review/history search included ignored files. The inline seed event remains present; this review does not authorize another event or lifecycle promotion.

iModulonDB was not applicable to these identity-only assertions. No new marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were leads, while inspected source text supplied the evidence checks.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. It consistently carries the pinned and live NCBI identity and its limited imported coverage. The external label conflict remains an unresolved literature-use caveat, not a demonstrated record defect: the YAML neither cites those experimental passages nor asserts their phenotypes. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including the Enterobacter label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` lifecycle status. Do not add the conflicting article label as a synonym.

Any future taxonomy correction belongs to the maintained NCBI snapshot/import path (`conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`, `scripts/extract_source_inventory.py`), not a hand edit of the generated record. Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Future enrichment requires an explicit source-owned relationship and an authorized maintained representation.

## Follow-up Checks

- At a source refresh, repeat exact taxonomy and JF772125 authority reads, including retirement/replacement checks, before changing the backbone.
- Before using the conflicting experimental passages, compare the published page images and any correction, preserving the unresolved attribution until verified. No such check or author contact was performed here.
- Require explicit deposit/genome crosslinks before enrichment; distinguish a partial marker from an assembly and imported coverage from biological absence.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written. Records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. The other Codex session is closed, and the existing single worktree was retained for this report-only review. All external reads were public and unpaid; no commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred. Publisher metadata and abstract were available, but publisher full text was subscription-gated; relevant primary text was inspected through the public author-hosting page. The full corpus-review goal remains incomplete.
