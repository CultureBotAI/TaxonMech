# YAML Record Review: Chromohalobacter sp. YIM 94221

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chromohalobacter_sp_yim_94221.yaml`
- Started UTC: 2026-10-06T05:10:16Z
- Finished UTC: 2026-10-06T05:12:14Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034981`, Chromohalobacter sp. YIM 94221. It carries species rank, bacterial domain, parent `NCBITaxon:2628571`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. Definition, synonyms, nomenclature, mappings, xrefs, literature evidence, strain/genome links and causal graphs are not asserted.

`data/taxa/PATHS.tsv:14266` uniquely pairs ID and stem. `curation/seed_scope.tsv:322086` records the NCBI-only scope rule, added 2026-09-13. This review concerns the exact isolate-bearing NCBI concept, not the genus or another YIM isolate.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/chromohalobacter_sp_yim_94221.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/chromohalobacter_sp_yim_94221.yaml --out /private/tmp/chyim94221-validation.tsv`: exit 0, one file, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured source comparisons verified complete pinned identity, all lineage entries, genetic code, unique path/scope references, sole attestation and inline event reason. The pinned backbone has no classified children of this target.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target row. Seven other source inventories have no exact target-ID row.
- Initial and marker-expanded ignored-inclusive compressed-source searches each returned the same three rows, all fully read and reconciled by address. The ignored-inclusive exact ID/full-label/slug search of prior reports and `history` returned no target match.
- Pre-report tracked-file diff against HEAD exited 0 across data, curation, history, code, configuration and guidance. Guidance/schema remain unchanged from prior full reads; the review skill, checklist, `CLAUDE.md`, curate skill and `justfile` were reread this turn. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No separate target history artifact was found to validate; the inline event was checked with the YAML and source comparison.
- `just validate-products` is not applicable without curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented. This review is not corpus release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034981&retmode=xml) confirms the ID, label, species rank, bacterial division, parent 2628571 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034981) agrees and supplies the ten ancestor IDs including root.

The chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Oceanospirillales, Halomonadaceae, Chromohalobacter and unclassified Chromohalobacter. Every pinned ancestor ID, label and rank matches the YAML, and live taxonomy confirms the non-root entries. Class `NCBITaxon:1236`, order `NCBITaxon:135619`, family `NCBITaxon:28256`, genus `NCBITaxon:42054` and parent `NCBITaxon:2628571` are independently supported, not carried over from the preceding Chelativorans review.

The unclassified parent has `NO_RANK`, while NCBI explicitly ranks the target as `SPECIES`. An isolate designation in the label does not require rewriting that rank to `STRAIN`. `EXACT` denotes an exact NCBI concept match, not a formally validated species name or curator sign-off.

## Evidence

1. **Pinned source and audit trail.** Complete `data/raw/ncbitaxon_taxa.tsv:221793` supplies the matching identity, parent, code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31216` carries the same ID/scientific name and empty unique name. The complete scope row matches the seed reason. The `NCBITAXON` attestation has count 1 and unit `NAME`, not a strain, genome or phenotype count. The inline event at `2026-09-13T17:54:04Z` names `seed_from_sources`, action `SEEDED_FROM_SOURCES`, and the same scope reason. `SEEDED` does not imply human review.

2. **Sequence evidence.** Exact Nuccore search returned one record: [JF792159.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792159.1), UID 333798085. Full metadata, references and feature qualifiers were read, excluding sequence bases. This is a 691-base partial 16S rRNA gene, partial at both ends, with organism Chromohalobacter sp. YIM 94221, strain YIM 94221 and explicit `taxon:1034981`. Sequence taxonomy also agrees with Gammaproteobacteria, Oceanospirillales, Halomonadaceae and Chromohalobacter. C. Chen submitted it on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University; it was created 28 May 2011 and updated 26 August 2015. The inspected metadata supplies no culture-collection, BioSample or assembly identifier. A marker accession is not a genome or deposit accession.

3. **Publication limits.** The sequence record describes C. Chen's study of culturable bacteria from Qijiaojing Lake and enzyme production as unpublished, with no DOI or PMID. Exact full-name and marker-accession web searches returned no results. These bounded searches do not establish worldwide publication absence. The study title alone does not establish this isolate's enzyme activity, habitat or culture requirements, and none was inferred.

4. **Imported coverage.** No exact BacDive target row or classified descendant was found, so `strain_count: 0` agrees with imported coverage rather than denying the isolate's existence. Assembly search for `txid1034981[Organism:noexp]` returned zero with no-items/phrase-not-found diagnostics. This is bounded to that exact taxonomy query, not proof that no assembly exists under another classification or source.

## Completeness

No consequential omission was established under the seeded-record model. Empty optional slots are appropriate where no supporting claim is carried. The matching marker corroborates identity without establishing an eligible deposit/genome relationship; the laboratory strain designation alone is not a registered culture-collection identifier.

Both searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the word-bounded numeric ID, full label, slug and YIM94221 separator variants; the second added JF792159 and its versioned spelling. Both found only the backbone, native name and scope row described above, all fully inspected. No additional strain/genome or marker crosslink was found in those roots. Ignored files and compressed rows were included, not every external database or separate snapshot archive.

Exact-ID comparisons of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target row. The prior-report/history search also included ignored files. The inline seed event remains present.

iModulonDB was not applicable to identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were not accepted as evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The current identity, lineage, grounding, provenance and imported coverage match the inspected sources. This pass does not certify formal nomenclature, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status unchanged. Do not infer enzyme activity from an unpublished title or treat the partial 16S sequence as a genome.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation belongs to `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; actual scope changes belong to `curation/seed_scope.tsv`. Any future enrichment requires explicit source-owned strain/deposit/genome evidence.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, replacement/retirement and JF792159 authority reads.
- Require whole culture identifiers and explicit sequence/genome relationships before enrichment. Keep partial markers outside genome counts.
- Inspect a primary publication with isolate-specific results before phenotype or habitat curation in the appropriate sibling repository.
- After an authorized source or generation change, use the documented dry run and single-record canary, repeat both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Records, inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid; no commits, GitHub mutations, contacts, provider-credit jobs or lifecycle promotions occurred.

The existing single worktree was retained because the other Codex session is closed. The full corpus-review goal remains incomplete.
