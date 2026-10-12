# YAML Record Review: Paenibacillus sp. Hs22

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_hs22.yaml`
- Started UTC: 2026-10-09T08:24:34Z
- Finished UTC: 2026-10-09T08:30:23Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036662`, Paenibacillus sp. Hs22. It asserts species rank, Bacteria, parent 185978, ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. Its seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_hs22.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_hs22.yaml --out /private/tmp/taxonmech-paenibacillus-hs22-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Own-marker annotation consistency passed: declared and actual length 769, rRNA transcription identical to DNA, no non-ACGT symbols. This is not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036662&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036662) responses agree with label, species rank and lineage. EFetch confirms parent 185978 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and unclassified Paenibacillus.

Live taxonomy has no other names; pinned synonym fields are empty. No own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank does not establish formal nomenclatural standing or a particular named Paenibacillus species. The HS_22 and HS-22-14 identities detailed below are not target aliases.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222567`, `data/catalog/ncbi_names-0005.jsonl.gz:32111`, `data/taxa/PATHS.tsv:15084` and `curation/seed_scope.tsv:322814`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

Exact Nuccore taxon query returned UID 334361624 alone. Complete [JF803856.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803856.1) XML, references, features and sequence were read. This 769-base partial 16S marker is incomplete at both ends. Its six source qualifiers identify Paenibacillus sp. Hs22, genomic DNA, strain Hs22, host Haliclona simulans, taxon 1036662 and Ireland: Gurraig Sound Kilkieran Bay, Galway. No deposit or genome qualifier is present. References identify Phelan and colleagues and a 13-APR-2011 University College Cork direct submission. Creation/update dates are 31-DEC-2011 and 20-NOV-2013.

Exact JF803856 PubMed search retrieves [PMID 21985154](https://pubmed.ncbi.nlm.nih.gov/21985154/). Its complete abstract and selected bibliographic metadata (title, journal, date and publication identifiers, not author affiliations) verify [DOI 10.1111/j.1365-2672.2011.05173.x](https://doi.org/10.1111/j.1365-2672.2011.05173.x). Cohort findings do not establish this isolate's specific genes or phenotypes. The DOI/publisher page was inaccessible through the web tool during this review; isolate-level full-text tables remain unverified. No experimental claim was imported.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not deny the cultured isolate's existence. No additional target deposit or genome link was established within the inspected evidence.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 1036662, the exact slug and Hs22 with an optional space, hyphen or underscore. Expansion added word-bounded JF803856 with optional .1 and UID 334361624. Both searches returned the same 15 rows; all were read completely in native form using lossless common fields and differences: two TSV and 13 JSON rows.

Three rows concern the target; twelve concern other identities:

- Seven rows identify Vibrio parahaemolyticus HS-22-14, taxon 670: GOLD organism/project/analysis, BV-BRC, GenBank, historical RefSeq and GTDB. Shared identifiers are GCA_001280625.1, historical GCF_001280625.1, SAMN03799831 and PRJNA288141 (RefSeq project PRJNA224116). GOLD IDs are Go0124685, Gp0132943 and Ga0112472; IMG is 2693429695 and BV-BRC is 670.465. GenBank and historical RefSeq retain an unverified-source-organism exclusion; RefSeq is suppressed as of 2017-05-18. GTDB assigns Vibrio diabolicus/Enterobacterales, whereas its NCBI fields assign V. parahaemolyticus/Vibrionales; Canada and clam metadata further distinguish this sample. These conflicts and flags concern the non-target genome, not the Paenibacillus record.
- Enterococcus faecalis HS_22, taxon 1351, has GCA_060033145.1, SAMN60612262 and PRJNA1474811, released 2026-08-11, with a large-multi-isolate-project exclusion.
- Two rows identify Pseudomonas aeruginosa HS_22, taxon 287, with GCA_025236025.1, historical GCF_025236025.1, SAMN24547480 and PRJNA793523 (RefSeq project PRJNA224116). They retain a large-multi-isolate-project exclusion; historical RefSeq is suppressed as of 2022-09-20.
- Streptococcus pyogenes HS_22, taxon 1314, has GCA_043322175.1, SAMEA14315100 and PRJNA514245, assembly name PDT002269770.1, released 2024-10-17, with a large-multi-isolate-project exclusion.
- GOLD Gp0530401, SAMN13182808 and PRJNA587220 concern a Jilin soil fungal-community metatranscriptome named raw.split.HS_22.1, not a target strain or expression dataset.

Candidate addresses beyond the two own TSV rows were `data/gold/organisms.jsonl.gz:73667`, `data/gold/projects.jsonl.gz:80825` and `:387369`, `data/gold/analyses.jsonl.gz:62241`, `data/catalog/ncbi_names-0005.jsonl.gz:32111`, `data/bvbrc/bvbrc-0026.jsonl.gz:20294`, `data/catalog/ncbi_genbank-0055.jsonl.gz:29541`, `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:10235`, `data/catalog/ncbi_genbank-0023.jsonl.gz:19684`, `data/catalog/ncbi_genbank-0000.jsonl.gz:47793`, `data/catalog/gtdb_genomes-0011.jsonl.gz:21815`, `data/catalog/ncbi_genbank-0039.jsonl.gz:37138` and `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:5294`.

Five SOURCE.json files were separately parsed in full for both term sets, with no matching keys or values; history filenames were independently inventoried. This covers the stated local roots, not every possible external source or spelling.

The Nuccore query `(Paenibacillus[Organism] OR Bacillus[Organism]) AND (Hs22[All Fields] OR "Hs-22"[All Fields] OR "Hs 22"[All Fields])` returned only the own marker. Full translations and diagnostics were inspected, including genus expansion and the three effective all-fields terms. This is a genus-restricted query, not an outside-genus sequence census.

Exact Assembly taxon query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence. `Paenibacillus AND (Hs22 OR "Hs-22" OR "Hs 22")` returned zero PubMed records, with genus MeSH/all-fields expansion and no quoted-phrase rejection. The exact marker query nevertheless retrieved the primary study. Index misses do not prove absent literature. No full-text literature census was performed.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable target strain/dataset was established. The unrelated GOLD community transcriptome does not change that. Optional empty fields are not automatic defects; absence conclusions remain bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. Name collisions do not establish missing target deposit/genome relationships.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not join sources on the bare Hs22 code.

## Follow-up Checks

Optional enrichment requires isolate-specific primary text explicitly linked to Paenibacillus Hs22/JF803856 and independent deposit/genome provenance. Reassess named-species assignments only with direct provenance and appropriate sequence evidence. No genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036662`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all 15 local candidates, live taxonomy, own marker and primary abstract with the metadata scope above were inspected.

Before/after YAML SHA-256: `10a71dfade64635412e9df298bd4f75fe836d75d4f9851dcf12f5d88742dbd62`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
