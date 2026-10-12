# YAML Record Review: NC10 bacterium enrichment culture clone SFBR 7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_7.yaml`
- Started UTC: 2026-10-06T19:46:10Z
- Finished UTC: 2026-10-06T19:51:27Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035283`, NC10 bacterium enrichment culture clone SFBR 7. It has NCBI species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. No synonym, nomenclature, mapping, genome, phenotype or causal graph is asserted.

Generated YAML is read-only. Future corrections belong to maintained source acquisition/projection, extraction, `src/taxonmech/seed.py` or scope. This report judges only SFBR 7; neither another SFBR clone nor the whole enrichment is interchangeable with this target.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_7.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_7.yaml --out /private/tmp/n7-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Manual bounded comparisons checked the complete lineage, source inventories, name, path lock, scope, attestation and history. They are not a target-level reproduction validator.
- SHA-256 checks performed during this session matched the shared `data/raw/ncbitaxon_taxa.tsv` and `data/catalog/ncbi_names-0005.jsonl.gz` files to their catalog manifest entries. The backbone also matches the raw manifest. This checks local byte consistency, not complete provenance.
- The configured original taxdump archive is unavailable locally. The session's attempted direct archive check failed with FileNotFoundError before a hash or names.dmp comparison; no original archive verification is claimed.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. The reproduction script has no target selector; `--max-diffs` only limits diagnostics. `just validate-products` is not applicable because no curator-added graph nodes exist.
- Before external follow-up, the local `culturebotai-claw` iModulonDB dataset adapter ran and all 28 rows were read. None covers this NC10 clone or Methylomirabilota, so component queries were not applicable. Missing coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221984`, path lock `data/taxa/PATHS.tsv:14475` and scope `curation/seed_scope.tsv:322258` agree on the exact identity. The native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31460` agrees with the canonical label. Exact type-material, merged-ID and dropped-record scans found no target entry; the pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035283&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035283) confirm the active identity, rank, parent and genetic code. Every stored ancestor agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets supplies the root ID omitted from the XML lineage display.

The XML division Environmental samples does not conflict with the ancestry-derived BACTERIA domain. NCBI species rank does not establish a formally described species, pure isolate, registered deposit or type strain. The phylum label is carried taxonomy, not a SeqCode nomenclature assertion for this clone.

Live NCBI also associates the full label ending SFBR+ 7 with this taxon as name class misspelling. The canonical SFBR 7 identity remains correct. The absent alternate spelling is the minor finding, not justification for renaming the target or merging neighboring clones.

## Evidence

The single NCBITAXON attestation correctly counts one pinned name and records the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits entry. With no descendants or listed BacDive strains, `strain_count: 0` is consistent; it is not a statement that no enrichment culture existed.

An exact nonexpanded nucleotide query returned one accession, [JF803480.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803480.1), UID 337730220. The full GenBank metadata were read, excluding sequence bases. It is a 416-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Its organism and taxon xref identify 1035283; its definition and clone qualifier preserve SFBR+ 7. Metadata specify Ooijpolder, Netherlands, collection date 15-Oct-2009 and direct submission on 13-Apr-2011. This marker is not a genome assembly, culture deposit or evidence of a pure isolate.

The accession explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. Their correspondence and full abstract were inspected through PubMed EFetch during this session; the [authors' institutional publication page](https://research.wur.nl/en/publications/enrichment-of-denitrifying-methanotrophic-bacteria-for-applicatio/) independently confirms the paper and abstract. It concerns reactor enrichment of denitrifying methanotrophs resembling Candidatus Methylomirabilis oxyfera. That supports experimental context, not clone-specific physiological rates, a genome or identity with that named species. The full article was not inspected. No reactor-level phenotype is added to the record.

An exact nonexpanded NCBI Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035283/dataset_report) succeeded and returned an empty object. These are bounded query results, not a claim of universal genome absence.

Scope and seed-event wording agree. The timestamp 2026-09-13T17:54:04Z matches the newest raw/ATB/StrainInfo manifest timestamp used by `_seed_timestamp` in `src/taxonmech/seed.py:139`. This review does not promote lifecycle status.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for the taxon identifier, clone designation, label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 136 candidate rows were read in full native form, including nested content: three TSV rows, 42 BV-BRC JSON rows, 14 other core JSON rows, 53 additional GenBank JSON rows and 24 GTDB JSON rows. Only backbone, scientific-name and scope rows concern this target.

The other 133 rows are numeric collisions. Most refer to Staphylococcus BioProject PRJNA1035283, whose project identifier is not NCBITaxon:1035283. Other collisions include Streptococcus anginosus BioSample SAMN41035283, Mycobacterium tuberculosis run ERR1035283, Campylobacter jejuni assembly GCA_010352835.1, GOLD saliva-metagenome sample name CCIS11035283OR-31-0 and the numeric scaffold N75 of Staphylococcus aureus assembly GCF_051258385.1. Native taxon, organism, accession and sample fields establish the mismatches. Neither GTDB reclassification of those assemblies nor historical Staphylococcus assembly versions supplies evidence for this clone.

A second ignored-inclusive search for JF803480 and the SFBR+ 7 spelling found no rows in those same ten roots. All five SOURCE.json files and history filenames were inspected separately for both queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no previous review for this stem.

The original archive was unavailable at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`. The session's ignored-independent filename search for taxdump artifacts under `data` and `/private/tmp` also found none; no claim is made about the rest of the machine. Matching hashes for the two committed projections rule out local drift in those files only.

No supported missing strain-genome join, nomenclature entry or additional source attestation was found within these bounds. Marker/literature enrichment and causal graphs are optional for this seeded NCBI-only record. The live alternate spelling is the narrow traceability gap.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: the current NCBI misspelling alias is absent from the pinned name representation.** Taxonomy explicitly links NC10 bacterium enrichment culture clone SFBR+ 7 to 1035283, and JF803480.1 independently preserves SFBR+ 7 in its definition and clone qualifier. The native name catalog, raw backbone synonym fields and YAML retain only the canonical form. Preserving the alternate name as related, not exact, would improve submission traceability without changing identity.

The two committed projections are hash-consistent. Because the original pinned archive is unavailable, this review cannot distinguish a snapshot/API difference from acquisition or projection loss. `src/taxonmech/ncbi_taxdump.py:81` maps non-scientific names other than synonym/equivalent-name classes to RELATED_SYNONYM, while `scripts/build_source_catalog.py:92` preserves original name classes. An extractor bug is not established.

Maintained owners are `conf/ncbi_taxdump.yaml`, the pinned capture, `src/taxonmech/ncbi_taxdump.py` and `scripts/build_source_catalog.py`; generated YAML follows those inputs through `src/taxonmech/seed.py`. The finding is a non-blocking name-coverage/provenance gap, not an incorrect canonical identity.

## Recommended Edits

At an authorized source refresh, reconcile SFBR+ 7 against a verified primary names.dmp snapshot or explicitly modeled API overlay. Preserve the source misspelling class in the native catalog and related-synonym scope downstream when supported by that maintained input. Do not promote the spelling to an exact synonym, rename SFBR 7, merge clones or patch generated YAML directly.

No other edit is required by the inspected evidence. Optional literature enrichment requires a maintained overlay and claim-specific support; clone markers, enrichment cultures, BioProjects, BioSamples and genome assemblies must remain distinct.

## Follow-up Checks

Recover the archive with SHA-256 `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955` and inspect every names.dmp row for 1035283. If the alias is absent, document the source/snapshot discrepancy; if present, trace the loss through extraction and catalog projection. Test plus-sign preservation and related scope without merging SFBR clones.

After authorized maintained-input changes, regenerate through the validated writer, rerun the two target validators, then full `just verify-corpus` and `just qc`. Any added physiological claim also needs primary methods/results at the correct clone or culture scope. No source refresh or lifecycle promotion occurred here.

## Additional Notes

The shared paper's DOI/ScienceDirect and browser PubMed routes were unavailable or challenged during this session; an institutional thesis PDF returned HTTP 403. None supplied inspected full text. Public PubMed EFetch and the institutional abstract are the literature sources actually used. Search snippets were not used as evidence.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The complete target was reread byte-for-byte unchanged. Only this new report was written for this target; no record, history, lifecycle, generated site or Git/GitHub mutation occurred. Eukaryota remained untouched.

