# YAML Record Review: Pseudomonas sp. EMB-48

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_emb_48.yaml`
- Started UTC: 2026-10-06T03:51:17Z
- Finished UTC: 2026-10-06T03:53:41Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034962`, Pseudomonas sp. EMB-48. It asserts `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:196821`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported BacDive strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14245` uniquely pairs the identifier and stem. `curation/seed_scope.tsv:322069` contains its NCBI-only attestation rule, added 2026-09-13. Generated records and maintained inputs remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_emb_48.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_emb_48.yaml --out /private/tmp/pemb48-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched the complete pinned identity, lineage, genetic code, path/scope references, sole attestation and inline event reason. Seven other inventories returned no exact target-ID row.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows. The pinned backbone has no children under the target.
- Both ignored-inclusive, compressed-file-inclusive source searches returned the same three fully inspected rows. An ignored-inclusive prior-report/history search found no target reference before this report.
- Pre-report `git diff --exit-code HEAD --` covering data, scope, history, code, configuration and guidance exited 0. Guidance is unchanged from its prior full read. HEAD remains `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not a corpus release certification.
- `just validate-products` is not applicable without curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

The complete live [NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034962&retmode=xml) confirms the identifier, label, species rank, bacterial division, parent 196821 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034962) agrees and includes the root in the ten ancestor identifiers. The inspected [Taxonomy Browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1034962&lvl=3&mode=node) independently agrees.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas. All pinned ancestor identifiers, labels and ranks match the YAML; live NCBI agrees with the non-root chain.

The direct parent is `NO_RANK`, while the target's NCBI rank is explicitly `SPECIES`. This isolate-bearing placeholder meets the repository's species-level eligibility rule without establishing a formally named species or requiring reranking to `STRAIN`. `EXACT` denotes the NCBI concept, not nomenclatural validation or human review.

## Evidence

1. **Pinned identity and provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221774` supplies the matching label, rank, parent, genetic code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31197` supplies the scientific name and target ID, with an empty unique-name field. The complete scope row matches the seed reason. The sole `NCBITAXON` attestation has this ID and label, count 1 and unit `NAME`: it counts a source name entry, not a genome or phenotype. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and agrees with the scope rule. `SEEDED` is not human sign-off.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one result, [JF772141.1](https://www.ncbi.nlm.nih.gov/nuccore/JF772141.1), UID 333595842. Complete EFetch metadata, references and feature qualifiers were inspected, excluding sequence bases. This is a 931-base partial 16S rRNA gene with organism Pseudomonas sp. EMB-48, strain EMB-48, host strawberry and explicit `taxon:1034962`. Its rRNA feature is partial at both ends. Submission was on 4 April 2011 through the Federal University of Lavras, release on 25 May 2011 and metadata update on 28 March 2012. The marker is not an assembly or culture-collection deposit.

3. **Primary article.** The sequence cites [DOI 10.1007/s00248-011-9919-3](https://link.springer.com/article/10.1007/s00248-011-9919-3) and [PMID 21837472](https://pubmed.ncbi.nlm.nih.gov/21837472/). The complete PubMed bibliography and abstract were read for this review and agree with the publisher metadata inspected earlier in this review run: Microbial Ecology 63, pages 405-417, 2012. The [primary article text](https://www.researchgate.net/publication/51567461_A_Multiphasic_Approach_for_the_Identification_of_Endophytic_Bacterial_in_Strawberry_Fruit_and_their_Potential_for_Plant_Growth_Promotion) explicitly pairs JF772141 with Pseudomonas sp. EMB-48 in its accession paragraph. The complete rendered Table 1 and surrounding results were inspected, including its EMB-48 row. Those assays do not establish a named species or warrant transferring another isolate's greenhouse effects to EMB-48. No phenotype was added to the YAML.

4. **Coverage counts.** The BacDive inventory has no exact target-ID row, and there are no descendant taxa contributing classified strains in the pinned backbone. `strain_count: 0` therefore describes imported BacDive coverage, not absence of this isolate, marker or study. Exact `txid1034962[Organism:noexp]` Assembly ESearch returned zero results with no-items/phrase-not-found diagnostics. This does not prove absence of assemblies under other classifications or in other databases.

## Completeness

No consequential omission was established under the seeded-record model. Empty optional definition, literature evidence, synonym, nomenclature, mapping, xref, strain/genome and graph slots are acceptable. The marker and study corroborate identity but do not establish an eligible BacDive/StrainInfo deposit relationship. Phenotype and habitat assertions belong to the appropriate sibling repositories.

Two searches used `rg --no-ignore --hidden -z` through a row-address reader across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. The first searched taxon 1034962, the slug and case-insensitive EMB48 separator variants; the second added JF772141 and its versioned spelling. Both returned only the three target backbone, native-name and scope rows, all read in full. No additional marker crosslink or eligible strain/genome candidate was found in those roots. Ignored files and compressed source rows were included; other snapshot archives and live databases are outside this bounded absence claim.

Exact target-ID comparisons of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The separate prior-report/history search included ignored files. The inline seed event remains present; no additional history event or lifecycle promotion is authorized.

iModulonDB was not applicable to this identity-only record. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were leads, not evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record consistently carries the pinned and live NCBI concept and limited imported coverage. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Leave the generated YAML unchanged, including its label, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` lifecycle status.

Future authority corrections belong to the maintained NCBI snapshot/import path: `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. New associations require explicit source-owned strain/deposit/genome relationships, not a bare-designation join.

## Follow-up Checks

- At a source refresh, repeat the exact taxonomy and JF772141 authority reads, including retirement/replacement checks.
- Require explicit deposit/genome provenance for new relationships and distinguish partial markers from assemblies.
- Preserve isolate and experimental-condition boundaries in any future phenotype work; the study's genus-level designation is not a formal species assignment.
- After an authorized extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews were left unchanged. All external reads were public and unpaid; no commits, GitHub mutations, provider-credit jobs, external contacts or lifecycle promotions occurred.

Publisher full text was subscription-gated. The relevant accession paragraph, complete Table 1 text and surrounding results were inspected through the public author-hosting page. The existing single worktree was retained; the other Codex session is closed. The full corpus-review goal remains incomplete.

