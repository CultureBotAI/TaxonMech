# YAML Record Review: Actinorectispora indica

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinorectispora_indica.yaml`
- Started UTC: 2026-10-05T20:31:37Z
- Finished UTC: 2026-10-05T20:39:13Z
- Verdict: pass

## Target

The complete 106-line generated `TaxonRecord` was read before judgment. Its identity is `NCBITaxon:1034798`, label Actinorectispora indica, rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`, and lifecycle `SEEDED`. It contains one LPSN nomenclatural entry, four related synonyms, one listed BacDive strain, and three source attestations.

The target resolves uniquely in `data/taxa/PATHS.tsv:14160` and `curation/seed_scope.tsv:30316`; its legacy page mapping is at `curation/legacy_page_paths.tsv:842`. Generated YAML, scope, source inventories, pages, and history were not edited. Eukaryota was not reviewed or changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/actinorectispora_indica.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/actinorectispora_indica.yaml --out /private/tmp/ari-strict-20261005.tsv`: exit 0, one file scanned, zero error rows. The output TSV was read and contains only its header.
- Structured, read-only comparisons against the complete backbone and seven source inventories passed for identity, parent, all nine lineage entries, synonym scope, source counts, pinned path, scope reason, and seed-event consistency. These comparisons are not a substitute for corpus reproduction.
- Authority checks used NCBI Taxonomy EFetch and Datasets, NCBI sequence and PubMed metadata, LPSN, BacDive, and publisher pages/previews on 2026-10-05.
- `just validate-products`: not applicable; the target has no curator-added causal-graph nodes or edges. No dedicated single-record reference validator is documented; citations and identifiers were checked directly.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, generated-site drift, documentation statistics, publication-size budget, and vendored synchronization. No focused equivalent was invented for these full-corpus gates.

## Identity and Grounding

The pinned backbone row `data/raw/ncbitaxon_taxa.tsv:221690` and live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034798) agree on species identity, parent `NCBITaxon:1769723`, bacterial domain, and genetic code 11. Datasets independently returns the same root-first ancestor IDs:

`1 > 131567 > 2 > 1783272 > 201174 > 1760 > 85010 > 2070 > 1769723`.

Ancestor labels and ranks match the record and pinned backbone. The root is represented explicitly in Datasets and the repository; its omission from EFetch's displayed lineage does not create a lineage discrepancy. The backbone comparison found no children of this species.

The four synonyms preserve NCBI name classes as related, not exact: the authority string and three former Actinosynnemataceae bacterium labels for YIM 75722, YIM 75726, and YIM 75728. Complete native name objects were inspected at `data/catalog/ncbi_names-0005.jsonl.gz:31080` through line 31084. The three isolate labels do not mean three aliases of one strain.

The raw merged-ID rows at `data/raw/ncbi_merged_ids.tsv:1033` and line 1034 redirect 1034802 and 1034804 to 1034798. These are source-taxonomy history, not grounds to invent replacement TaxonMech records. Live EFetch also exposes three misspellings not present in the pinned name rows; this does not contradict any synonym asserted by the YAML.

## Evidence

| Claim | Inspected evidence | Assessment |
|---|---|---|
| LPSN identity and nomenclature | `data/raw/lpsn_names.tsv:30410`; [LPSN 793801](https://lpsn.dsmz.de/species/actinorectispora-indica) | Same species, Quadri et al. 2016, valid ICNP publication and correct-name status. The seeded legitimate flag and complete status string match the inventory. |
| Nomenclatural type | LPSN, `data/raw/ncbi_type_material.tsv:1759` through line 1765, primary description | DSM 45410, CCTCC AA 209065, and YIM 75728 denote the type strain. Seven NCBI strings are formatting variants, not seven strains. |
| Listed BacDive strain | `data/raw/bacdive_strains.tsv:54691`; full native object `data/bacdive/records.jsonl.gz:54690`; [BacDive 132380](https://bacdive.dsmz.de/strain/132380) | Explicit species-level taxon 1034798, all three deposits, and type status agree. |
| Original description | [DOI 10.1099/ijsem.0.000814](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.000814), [PMID 26637823](https://pubmed.ncbi.nlm.nih.gov/26637823/) | Publisher abstract and full PubMed metadata/abstract identify the same species and type strain. The DOI and PMID identify one work, not two independent studies. |
| Notification citation | [DOI 10.1099/ijsem.0.001042](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001042?crawler=true), PubMed 27142866, publisher first-page preview | Title, authors, year, volume, and pages match the LPSN-associated notification list. The target's individual table entry was not independently read. |
| Nomenclatural sequence | [JF789453.1](https://www.ncbi.nlm.nih.gov/nuccore/JF789453.1); full EFetch metadata | A 1,445-base partial 16S rRNA gene from YIM 75728, taxon 1034798, explicitly marked type material and citing the original description. Retaining the inventory's unversioned `INSDC:JF789453` is appropriate. |

LPSN's current page lists three type designations; the pinned LPSN inventory contains DSM 45410 alone. The YAML faithfully carries that inventory subset, and its strain entry separately retains all three deposit identifiers. The seeder derives the type flag from their DSM overlap in `src/taxonmech/seed.py:405` and `src/taxonmech/seed.py:514`; the biological type is not missing.

Culture identifiers also resolve through `data/raw/culture_collection_strains.tsv:14523`, line 81412, and line 154712. The encoded space in `CCTCC-AA%20209065` preserves source spelling, as specified in `docs/HARMONIZATION.md`; it is not evidence that every retained alias qualifies as a genome-join key.

The notification's linked [erratum, DOI 10.1099/ijsem.0.001179](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001179), was read in the publisher's complete one-page preview. It restores a missing Table 2 heading about taxonomic opinions; it does not identify an Actinorectispora type-strain correction. Full article-body HTML retrieval failed for the description and notification, so neither is claimed as fully read.

The three attestations match their source rows: NCBI one NAME, LPSN one NAME with `skos:closeMatch`, and BacDive one STRAIN. These counts must not be summed as biological entities. The 2026-09-13 snapshot and 2026-09-13T17:54:04Z seed event match the inspected provenance context and scope reason.

## Completeness

Searches included ignored and hidden files, compressed sources, and the ten roots `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, using `rg --no-ignore --hidden -n -z -i`. Per-file `SOURCE.json` manifests were excluded from candidate content searches. Queries covered the taxon ID, label/slug, DSM 45410, CCTCC AA 209065, YIM 75722/75726/75728, JF789453, then DSM 45388, JF789454/JF789455, both merged IDs, both BacDive IDs, and NR_148608. All 33 distinct candidate rows were subsequently read with TSV headers or fully decoded JSON, not judged from snippets.

One genuine unmapped candidate remains preserved upstream: [BacDive 130973](https://bacdive.dsmz.de/strain/130973), DSM 45388 / YIM 75722. Its native object at `data/bacdive/records.jsonl.gz:53283` has no General NCBI mapping and still labels the organism Actinobacteria sp.; its marker metadata identifies A. indica. The raw strain row `data/raw/bacdive_strains.tsv:53284` therefore has empty taxon IDs, and `data/raw/dropped.tsv:1330` explicitly records no NCBI parent. This is a source-mapping reconciliation opportunity, not a lost catalog record, false type alias, or miscomputed mapped-strain count.

NCBI's exact, non-expanded query `txid1034798[Organism:noexp]` returned zero Assembly records, with phrase-not-found/no-items diagnostics, and four Nuccore records. Complete metadata for all four was read: JF789453.1 / NR_148608.1 concern the type strain; JF789455.1 and JF789454.1 concern YIM 75722 and YIM 75726 respectively. All are partial 16S records, not genomes. NR_148608.1 explicitly derives from JF789453 and carries RefSeq targeted-loci project PRJNA33175; that project is not a strain-specific assembly.

No target-supported assembly, GTDB, BV-BRC, IMG, GOLD, ATB, or StrainInfo genome link was found in the bounded ignored-inclusive source search. Numeric near-matches were rejected after full-row inspection: tuberculosis runs ERR1034798/ERR1034802/ERR1034804 and Salmonella strain 1034798 are unrelated. The SeqCode hit `data/seqcode/names.jsonl.gz:1266` is a name-index entry, not proof of SeqCode validation or a type-genome assertion. These checks do not establish global absence of genomes.

The five other taxon-attestation inventories contain no exact target row. BacDive medium count zero is the pinned MediaDive-link count, not a claim of no growth media; optional phenotypes, definitions, causal graphs, discussions, and record-level evidence need not be invented. iModulonDB is not applicable because the target asserts no gene, regulator, expression module, or transcriptomic dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted record. The bounded source-mapping opportunity and access limitations above do not invalidate its identity, type strain, declared inventory count, or source provenance.

## Recommended Edits

No required edits to this generated record.

An optional future reconciliation should resolve the BacDive 130973 source classification before changing counts. The maintained import boundary is `src/taxonmech/bacdive_v2.py:59`, which uses explicit General taxon mappings; do not copy arbitrary marker-taxonomy values into that field or merge the isolate with the type strain. Prefer an upstream source correction, then re-extract and re-seed under authorization.

Optional expansion of the LPSN type-designation subset belongs in the maintained upstream LPSN transform/input and `src/taxonmech/extract.py`, not hand edits to `data/raw/lpsn_names.tsv` or YAML. The present DSM designation already supports the flag.

## Follow-up Checks

After any authorized source correction, inspect the complete refreshed native rows, preserve distinct strain identities and source evidence, then run the documented extraction and seed dry runs, a single-record seed canary, schema and strict validation, corpus reproduction, and full QC. Confirm any marker references remain outside genome counts.

For this read-only review, retain the scoped validator results and report QA; do not promote `mapping_status`, append a curation event, or create external issues. Repeat the ignored-inclusive report search before any future review of this target.

## Additional Notes

- Work was performed on `codex/record-review-extensimonas-20261003` at `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The user said the parallel session was closed; only one worktree was present.
- Before report creation, an ignored-inclusive target search of `reports/yaml_record_review` and `history` returned no prior report or history match. This report is new; earlier reports are untouched.
- Direct DSMZ culture links for DSM 45410 and DSM 45388 redirected to the generic search page. Deposit identity was checked through the inspected LPSN, BacDive, original description, and sequence evidence rather than claiming usable DSMZ culture-page retrieval.
- No paid research, source refresh, GitHub mutation, generated-product write, or external contact occurred. Only this new report was added in the repository; validator output and publisher previews were kept in `/private/tmp`.
