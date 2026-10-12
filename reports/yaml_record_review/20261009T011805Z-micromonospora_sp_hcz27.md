# YAML Record Review: Micromonospora sp. HCZ27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_hcz27.yaml`
- Started UTC: 2026-10-09T01:14:13Z
- Finished UTC: 2026-10-09T01:18:05Z
- Verdict: pass

## Target

The full generated `TaxonRecord` for `NCBITaxon:1036514` was read: species rank, Bacteria domain, parent `NCBITaxon:2617518`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero BacDive records, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Synonyms, nomenclature, mappings, strain/genome links, record-level citations and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/micromonospora_sp_hcz27.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/micromonospora_sp_hcz27.yaml --out /private/tmp/micromonosporaHCZ27-strict.tsv`: passed, one file, zero errors; complete TSV was header-only.
- Structured source checks matched the complete backbone row, all ancestor rows, source attestation, PATHS entry, scope row and exact seed-event wording. Supplementary inventories, type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Complete own marker XML: length 1403 equals sequence length, submitted rRNA transcription matches DNA, and no non-ACGT symbols occur. This does not independently establish species identity.

Not checked: full-corpus reproduction (`just verify-corpus`), full schema/provenance/history gates, tests, `just qc`, vendored synchronization, generated-site drift and publication builds. Individual checks do not substitute for those gates. The embedded history event was inspected; no separate target history file was found in ignored-inclusive inventory. Graph validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036514&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036514) agree with the label, rank, identifier, parent, code and lineage. Datasets confirms all ten ancestor IDs including root; EFetch supplies ancestor labels/ranks while omitting root from its displayed lineage. These views are compatible.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae, Micromonospora and unclassified Micromonospora. No other names occur in the live EFetch response; pinned synonyms are empty. No target type-material, merged-ID or dropped row, or backbone child, was found.

Species rank for an unnamed strain-associated taxon is not evidence of a formally described species. Exact grounding refers to this NCBI concept, not equivalence to a named congener.

## Evidence

Full own source rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222514`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32058`: scientific-name object, empty unique name.
- `data/taxa/PATHS.tsv:15021`: identifier and slug.
- `curation/seed_scope.tsv:322761`: admission date/reason matching the seed event.

The NCBITAXON attestation counts one `NAME`, not a genome or experiment. Exact target scans returned no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw rows. Schema documentation defines `strain_count` as BacDive record coverage; zero does not deny the existence of strain HCZ27.

Exact Nuccore search `txid1036514[Organism:noexp]` returned UID 334361391. The complete [JF806646.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF806646.1), including sequence, both references and every feature, was read. It is a 1403-base partial 16S marker with both ends marked partial. Source qualifiers explicitly name HCZ27 and taxon 1036514; they do not supply host, isolation-source, geographic, culture-deposit or assembly qualifiers. Only source and rRNA features occur.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study, and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. It supplies no DOI or PMID. The marker cannot establish a genome link or phenotype, and missing qualifiers must not be filled from neighboring accessions.

An expanded Nuccore HCZ27 phrase search returned 33 records. All 32 additional ESummary objects were read losslessly: UIDs 1828776899 through 1828776931 excluding 1828776922. They consistently identify Listeria monocytogenes, taxid 1639, strain SCPM-O-B-8702, SAMN14422984 and project 224116, with WGS accessions NZ_JAATTZ010000001.1 through NZ_JAATTZ010000033.1 excluding 024. Their human clinical source context differs from the target. These primary identity summaries exclude them; no full-genome feature audit or locus-tag explanation is claimed.

[Wu et al. (2012), DOI 10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) has an inspected [author-hosted Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) listing HCZ27's closest species as Micromonospora echinospora, 99.50%, with positive PKS-I, PKS-II and NRPS PCR screens. The table header and footnote distinguish nearest-species comparison and screening from nomenclatural synonymy or demonstrated antimicrobial activity. Shared code, authors and topic suggest correspondence to the submission; that association is an inference, not an accession-level citation supplied by GenBank. No literature assertion was imported into the YAML.

## Completeness

Complete enough for the supported taxonomy-seed claims. Empty optional nomenclature, genome links, deposits, citations and graphs are not defects without supported identity chains. The external marker does not require an invented BacDive entry.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` scans covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial expression used word-bounded taxid 1036514, HCZ27 and the slug; the expanded expression added JF806646 and word-bounded UID 334361391. Both found only the three own taxonomy/name/scope rows, all read completely. This intentionally searches identifiers rather than matching their digits inside unrelated BioSamples or assembly names. Five SOURCE.json files were separately fully parsed without a match; history filenames were independently inventoried.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed search for HCZ27/JF806646/JF806646.1 returned zero with quoted-phrase warnings. An exact-accession web query returned no results; strain searches found the primary paper and taxonomy listings. These bounded misses do not establish universal absence of genomes or publications.

iModulonDB was not run because the record asserts no gene, regulator or expression-module claim and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, provenance and scope agree with the inspected pinned and live sources. Literature comparison does not establish a rename, and unrelated sequence-search hits do not supply target genome links.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI and then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection changes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Optional enrichment needs supported maintained-input/model behavior, not hand editing the output.

## Follow-up Checks

No corrective follow-up required for current claims. Before literature enrichment, verify an explicit accession/strain/deposit chain and visually check the original paper table/figure. The author-hosted HTML was inspected, but the original PDF was not visually verified; prior related-record attempts encountered inaccessible PDF/figure routes.

After an authorized maintained-input change, run focused regression tests, `just seed-canary NCBITaxon:1036514`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation ran in this review.

## Additional Notes

The local review skill and field checklist governed this individual review. This target was read and judged independently. The preceding HCZ26 literature discrepancy was not transferred to HCZ27.

Before/after YAML SHA-256: `ad09671e0d330f0515bcb401415df1ee5fa2a281a431ef337672914d7e7cbeee`. Only this timestamped report was written for this target. No YAML, source, history, status, generated page or GitHub object changed. Eukaryota and existing worktrees remained untouched.
