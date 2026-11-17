# YAML Record Review: NC10 bacterium enrichment culture clone SFBR 12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_12.yaml`
- Started UTC: 2026-10-06T19:41:20Z
- Finished UTC: 2026-10-06T19:44:56Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035282`, NC10 bacterium enrichment culture clone SFBR 12. It has NCBI species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. No synonym, nomenclature, mapping, genome, phenotype or causal graph is asserted.

Generated YAML is read-only. Future corrections belong to maintained source acquisition/projection, extraction, `src/taxonmech/seed.py` or scope, not this file. Neighboring clone records were not given a verdict through this review.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_12.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_12.yaml --out /private/tmp/n12-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Manual bounded source comparisons checked the complete lineage, inventories, name, path lock, scope, attestation and history. These are not a target-level reproduction validator.
- SHA-256 checks matched `data/raw/ncbitaxon_taxa.tsv` and `data/catalog/ncbi_names-0005.jsonl.gz` to their catalog manifest entries. The backbone hash also agrees with the raw manifest. This is not a full provenance gate.
- An attempted direct pinned-taxdump names/hash check failed with FileNotFoundError: the configured archive is unavailable locally. No archive hash or original names.dmp comparison is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. The reproduction script has no target selector; `--max-diffs` limits diagnostics only. `just validate-products` is not applicable because no curator-added graph nodes exist.
- The local `culturebotai-claw` iModulonDB dataset adapter ran before web follow-up. All 28 rows were read; none covers this NC10 clone or Methylomirabilota. No component query was applicable, and lack of coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221983`, path lock `data/taxa/PATHS.tsv:14474` and scope `curation/seed_scope.tsv:322257` agree on this exact taxon. The native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31459` agrees with the canonical label. Exact type-material, merged-ID and dropped-record scans found no target entry; the pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035282&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035282) confirm the active identity, species rank, parent and genetic code. Every stored ancestor agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets includes the root ID that the XML lineage display omits.

The XML division is Environmental samples; that is not a conflict with the YAML's BACTERIA domain, which follows ancestry. Species rank makes this clone taxon eligible under repository rules, but does not establish a described species, pure isolate, registered culture deposit or type strain. The phylum label is NCBI's carried lineage, not a SeqCode nomenclature assertion for this clone.

Live NCBI additionally records the full label ending in SFBR+ 12 as name class misspelling. The canonical SFBR 12 identity is not wrong. The absent alternate spelling is the minor finding below, not permission to rename the record or treat other SFBR clones as equivalent.

## Evidence

The single NCBITAXON attestation correctly counts one name and states the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. There are no descendants to contribute BacDive strains. `strain_count: 0` counts listed BacDive records, not environmental clones or growth in an enrichment.

An exact nonexpanded nucleotide search returned one sequence, [JF803481.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803481.1). All GenBank metadata were read, excluding sequence bases. It is a 417-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Its source organism and taxon xref identify 1035282; the definition and clone qualifier preserve SFBR+ 12. Metadata specify Ooijpolder, Netherlands, and collection date 15-Oct-2009. The marker is not a genome, sample accession, culture deposit or proof of a pure isolate.

The accession explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. PubMed EFetch verified their correspondence and supplied the full abstract. The [authors' institutional publication page](https://research.wur.nl/en/publications/enrichment-of-denitrifying-methanotrophic-bacteria-for-applicatio/) independently confirms the paper and abstract. It concerns enrichment of denitrifying methanotrophs resembling Candidatus Methylomirabilis oxyfera and reports reactor-level behavior. That context does not establish clone-specific rates, a genome, identity with that named species or the same phenotype for every NC10 lineage. Full text was not inspected, and no such claims are introduced into the record.

An exact nonexpanded NCBI Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome request](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035282/dataset_report) returned HTTP 200 and an empty object. These bound the current queries, not genome availability in every external resource.

The scope reason and seed-event text agree. The timestamp 2026-09-13T17:54:04Z is the newest raw/ATB/StrainInfo manifest timestamp, as `_seed_timestamp` in `src/taxonmech/seed.py:139` requires. Lifecycle stays SEEDED; an agent report is not human review promotion.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, clone designation, label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 11 candidate rows were read in full native JSON or TSV form, including nested data. Three concern this target: backbone, scientific name and scope.

Eight matches are unrelated numeric collisions: four Streptococcus anginosus rows contain BioSample SAMN41035282; two Mycobacterium tuberculosis rows contain run ERR1035282; one Salmonella GOLD analysis contains IMG ID 8103528262; one Campylobacter jejuni assembly contains GCA_010352825.1. Their genomes, source classifications, counts and sample relationships must not be transferred to SFBR 12.

A second ignored-inclusive search for JF803481 and the SFBR+ 12 spelling found no rows in the same ten roots. All five SOURCE.json files and history filenames were inspected separately for both searches; no target-specific external history or additional evidence appeared. Report-filename discovery included ignored files and found no earlier report for this stem.

The configured taxdump archive was not present at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`. An ignored-independent filename search for taxdump artifacts under `data` and `/private/tmp` also found none. This does not establish absence elsewhere on the machine. The two inspected committed projection hashes match their manifests, ruling out local byte drift in those files only.

No supported missing strain-genome join, nomenclature entry or source attestation was found within these bounds. Optional gene/marker citations and causal graphs are not compulsory for a seeded NCBI-only record. The missing current misspelling alias is narrow and does not justify a broader biological claim.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: a current NCBI misspelling alias is absent from the pinned name representation.** Live Taxonomy associates NC10 bacterium enrichment culture clone SFBR+ 12 with taxon 1035282, and JF803481.1 retains that spelling in its definition and clone qualifier. The native name catalog, raw backbone synonym fields and YAML contain only the canonical form. Retaining the alternate spelling as related, not exact, would improve traceability to the sequence submission without changing identity.

The two relevant committed projections are hash-consistent. The unavailable original pinned archive prevents distinguishing a snapshot/API difference from an acquisition/projection omission. `src/taxonmech/ncbi_taxdump.py:81` maps non-scientific names other than synonym/equivalent-name classes to RELATED_SYNONYM; `scripts/build_source_catalog.py:92` retains the original classes. No evidence supports blaming `seed.py` alone or overriding source classes by hand.

Maintained owners are `conf/ncbi_taxdump.yaml`, the pinned source capture, `src/taxonmech/ncbi_taxdump.py` and `scripts/build_source_catalog.py`; regeneration follows maintained raw inputs through `src/taxonmech/seed.py`. This is a non-blocking name-coverage gap, not an incorrect canonical label, taxon or genome relationship.

## Recommended Edits

At an authorized source refresh, reconcile the exact SFBR+ 12 name with a verified primary names.dmp snapshot or an explicitly modeled API overlay. Preserve its misspelling class in the native catalog and related-synonym scope in the generated record if supplied by that maintained input. Do not promote it to an exact synonym, alter the canonical SFBR 12 label or patch YAML directly.

No other edit is required. Preserve the distinction between environmental clone, enrichment culture, partial marker and genome assembly. Literature enrichment would require a maintained overlay and claim-specific evidence, not transplanting reactor results into this clone record.

## Follow-up Checks

Recover the original archive with SHA-256 `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955` and inspect every names.dmp row for 1035282. If it lacks the alias, document the source/snapshot difference; if it contains the alias, trace its loss through extraction and catalog projection. Test preservation of plus signs and related scope without merging similarly named SFBR clones.

After authorized maintained-input changes, regenerate through the validated writer, rerun both target validators, then full `just verify-corpus` and `just qc`. Any optional physiological claim also needs inspected primary methods/results at the appropriate clone or culture scope. No refresh, reclassification or lifecycle promotion occurred here.

## Additional Notes

The DOI and ScienceDirect pages were unavailable through the web tool, the PubMed browser page presented a challenge, and the institutional thesis PDF returned HTTP 403. These are access limits, not inspected full text. Independent public PubMed EFetch and the institutional publication abstract supplied the literature evidence actually used. Search snippets and ResearchGate metadata were leads only.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The entire target was reread unchanged. Only this new report was written for this target; records, history, lifecycle, site and Git/GitHub state were not changed. Eukaryota remained untouched.
