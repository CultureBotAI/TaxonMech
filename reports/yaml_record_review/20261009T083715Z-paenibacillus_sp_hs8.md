# YAML Record Review: Paenibacillus sp. Hs8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_hs8.yaml`
- Started UTC: 2026-10-09T08:33:28Z
- Finished UTC: 2026-10-09T08:37:15Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036663`, Paenibacillus sp. Hs8. It asserts species rank, Bacteria, parent 185978, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. Its seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_hs8.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_hs8.yaml --out /private/tmp/taxonmech-paenibacillus-hs8-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Own-marker annotation consistency passed: declared and actual length 944, rRNA transcription identical to DNA, no non-ACGT symbols. This is not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036663&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036663) responses agree with label, species rank and lineage. EFetch confirms parent 185978 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified Paenibacillus.

Live taxonomy has no other names; pinned synonym fields are empty. No own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank does not establish formal nomenclatural standing or a particular named Paenibacillus species. Bacillus sp. HS8, taxon 361623, is a separate source identity, not an alias supplied for this record.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222568`, `data/catalog/ncbi_names-0005.jsonl.gz:32112`, `data/taxa/PATHS.tsv:15085` and `curation/seed_scope.tsv:322815`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

Exact Nuccore taxon query returned UID 334361618 alone. Complete [JF803850.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803850.1) XML, references, features and sequence were read. This 944-base partial 16S marker is incomplete at both ends. Its six source qualifiers identify Paenibacillus sp. Hs8, genomic DNA, strain Hs8, host Haliclona simulans, taxon 1036663 and Ireland: Gurraig Sound Kilkieran Bay, Galway. No deposit or genome qualifier is present. References identify Phelan and colleagues and a 13-APR-2011 University College Cork direct submission. Creation/update dates are 31-DEC-2011 and 20-NOV-2013.

Exact JF803850 PubMed search retrieves [PMID 21985154](https://pubmed.ncbi.nlm.nih.gov/21985154/). Its complete abstract and selected bibliographic metadata (title, journal, date and publication identifiers, not author affiliations) verify [DOI 10.1111/j.1365-2672.2011.05173.x](https://doi.org/10.1111/j.1365-2672.2011.05173.x). Cohort findings do not establish this isolate's specific genes or phenotypes. The DOI/publisher page was inaccessible through the web tool during this review; isolate-level full-text tables remain unverified. No experimental claim was imported.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not deny the cultured isolate's existence. No additional target deposit or genome link was established within the inspected evidence.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 1036663, the exact slug and Hs8 with an optional space, hyphen or underscore. Expansion added word-bounded JF803850 with optional .1 and UID 334361618. Both searches returned the same 39 rows; all were read completely in native form using lossless common fields and differences: 14 TSV and 25 JSON rows.

Three rows concern the target; 36 concern other identities:

- Eighteen backbone/scope/name rows identify Bacillus sp. HS8 (361623), Rhodococcus sp. HS8 (393919), Methylobacterium sp. HS_8 (669935), Porphyromonadaceae bacterium S9 HS-8 (1344346), Synechococcus sp. HS-8 (1707508) and Herbaspirillum sp. HS8 (3740337).
- Seven rows across BV-BRC, GOLD, GenBank, RefSeq and GTDB concern Helicobacter suis HS8, taxon 104628, GCA/GCF_900196945.1, SAMEA104141508 and PRJEB21369 (RefSeq PRJNA224116). GOLD Go0496592/Gp0380655/Ga0347065 connects to IMG 8032186294; BV-BRC is 104628.24. GTDB's Campylobacteria versus NCBI's Epsilonproteobacteria class labels are retained as a non-target source difference. Gastric-mucosa metadata does not support an Irish sponge isolate link.
- Four rows concern Cutibacterium avidum HS8, taxon 33010, GCA/GCF_024105015.1, SAMN19186355 and PRJNA729908 (RefSeq PRJNA224116), including BV-BRC 33010.119 and GTDB healthy-skin/Madrid metadata.
- Two rows concern Pseudomonas aeruginosa HS_8, taxon 287, GCA_025238495.1 and historical GCF_025238495.1, SAMN24547553 and PRJNA793523 (RefSeq PRJNA224116). Both retain a large-multi-isolate-project exclusion; historical RefSeq is suppressed as of 2022-09-20.
- One GenBank row concerns Staphylococcus aureus HS8, taxon 1280, GCA_056622095.1, SAMD01831864 and PRJNA514245, assembly PDT003169277.1, with a large-multi-isolate-project exclusion.
- Three GOLD rows concern Pseudoalteromonas phage PSA-HS8: Go0097830/Gp0097830/Ga0053955, IMG 2582581235. One GOLD row, Gp0530387/SAMN13182794/PRJNA587220, concerns the Jilin soil fungal-community metatranscriptome raw.split.HS_8.1. Neither supplies a target bacterial genome or expression relationship.

Five SOURCE.json files were separately parsed in full for both term sets, with no matching keys or values; history filenames were independently inventoried. The search covers the stated local roots, not every possible external source or spelling. Non-target exclusions and classification differences are not defects in this Paenibacillus record.

The Nuccore query `(Paenibacillus[Organism] OR Bacillus[Organism]) AND (Hs8[All Fields] OR "Hs-8"[All Fields] OR "Hs 8"[All Fields])` returned eight records. All eight complete ESummary objects and query translations were inspected. This is a genus-restricted query, not an outside-genus sequence census.

Besides the own marker, four close candidates received complete GenBank XML reads:

- [OR858847.1](https://www.ncbi.nlm.nih.gov/nuccore/OR858847.1), 1,416 bases, is Bacillus sp. (in: firmicutes) HS8, taxon 1409, submitted by Zhu at Gansu Agricultural University on 27-NOV-2023. No provenance link to the Irish isolate is supplied.
- [KY649408.1](https://www.ncbi.nlm.nih.gov/nuccore/KY649408.1), 1,400 bases, is Bacillus pumilus HS-8, taxon 1408. Its unpublished reference concerns Salix rhizosphere bacteria in Horqin Sandy Land; Gao submitted it from Lanzhou University on 22-FEB-2017. The reference context is not an independently verified phenotype.
- [GU323369.1](https://www.ncbi.nlm.nih.gov/nuccore/GU323369.1), 1,451 bases, is Bacillus amyloliquefaciens HS8, taxon 1390. Zhu and Xie submitted it from Hainan Normal University on 14-DEC-2009, with an unpublished douchi-strain-library reference.
- [DQ309333.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ309333.1), 1,436 bases, is Bacillus sp. HS8, taxon 361623, submitted by Zhang and Xu from Shandong on 29-NOV-2005. Its linked [PMID 16944134](https://pubmed.ncbi.nlm.nih.gov/16944134/) abstract and selected bibliography identify a soil isolate called B. subtilis HS8; DOI is 10.1007/s00253-006-0544-x. That paper's named-species identification and the sequence's unclassified Bacillus label are preserved, not silently reconciled. Its metabolic findings cannot transfer to Paenibacillus Hs8.

Three other candidates were inspected at full-summary level, not full XML: MT312815.1 (B. subtilis HS8, Chinese Astragalus-associated root isolate), MN857715.1 (B. altitudinis HS8, Sikkim high-altitude soil) and JF899271.1 (Hs8-12, older B. amyloliquefaciens subsp. plantarum title but B. velezensis organism field). No independent alignment or equivalence inference was made.

Exact Assembly taxon query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence. `Paenibacillus AND (Hs8 OR "Hs-8" OR "Hs 8")` returned zero PubMed records, with genus MeSH/all-fields expansion and no quoted-phrase rejection. The exact marker query nevertheless retrieved the primary study. Index misses do not prove absent literature. No full-text literature census was performed.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable target strain/dataset was established. The unrelated GOLD community transcriptome does not change that. Optional empty fields are not automatic defects; absence conclusions remain bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. Name collisions and near-match sequences do not establish missing target deposit/genome relationships.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not join sources on the bare Hs8 code.

## Follow-up Checks

Optional enrichment requires isolate-specific primary text explicitly linked to Paenibacillus Hs8/JF803850 and independent deposit/genome provenance. Reassess named-species assignments only with direct provenance and appropriate sequence evidence. No genome comparison, experimental reanalysis or PDF/figure visual verification was performed. The distinct Bacillus study was checked at abstract level, not full text.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036663`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all 39 local candidates, live taxonomy, own marker, eight full sequence summaries, four full near-match markers and two primary abstracts with the metadata scope above were inspected.

Before/after YAML SHA-256: `bd45b101de961e7d0e80a36dc54ff2a4bb74566f1b550ee4062e69a3a8972826`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
