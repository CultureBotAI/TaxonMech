# YAML Record Review: Bacillus sp. HsCH8a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_hsch8a.yaml`
- Started UTC: 2026-10-09T07:52:11Z
- Finished UTC: 2026-10-09T07:59:36Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036659`, Bacillus sp. HsCH8a. It asserts species rank, Bacteria, parent 185979, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. The embedded seed event is dated 2026-09-13T17:54:04Z.

An ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and causal graphs are unasserted. This generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_hsch8a.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_hsch8a.yaml --out /private/tmp/taxonmech-bacillus-hsch8a-review-strict.tsv`: passed, one file and zero errors; the complete TSV was header-only.
- Structured source comparisons matched own identity, all ten ancestors, PATHS, scope reason, source attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Marker annotation consistency passed: declared and actual length 948, rRNA transcription identical to the DNA sequence, no non-ACGT symbols. This is not an independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product checks are inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036659&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036659) responses agree with identity, rank and lineage. EFetch confirms parent 185979 and genetic code 11; Datasets includes the root. Ancestors are root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Bacillus and unclassified Bacillus (in: firmicutes).

EFetch has no other names; pinned synonym fields are empty. No own row was found in the type-material, merged-ID or dropped-taxon inventories, and no backbone child was found. Species rank is the NCBI classification and does not establish formal nomenclatural standing or a named Bacillus species assignment.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222564`, `data/catalog/ncbi_names-0005.jsonl.gz:32108`, `data/taxa/PATHS.tsv:15080` and `curation/seed_scope.tsv:322811`. The 2026-09-13 snapshot, one-name unit and admission reason support the attestation and seed event. A `NAME` count is not a genome or experiment count. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories.

The exact Nuccore taxon query returned UID 334361643 alone. Complete [JF803875.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803875.1) XML was read, including references, features and sequence. It is a 948-base 16S marker, partial at both ends. Its six source qualifiers identify Bacillus sp. HsCH8a, genomic DNA, strain HsCH8a, host Haliclona simulans, taxon 1036659 and Ireland: Gurraig Sound Kilkieran Bay, Galway. There is no deposit or genome qualifier. References identify Phelan and colleagues and a University College Cork direct submission dated 13-APR-2011. GenBank creation and update dates are 31-DEC-2011 and 20-NOV-2013.

The exact JF803875 PubMed search retrieves [PMID 21985154](https://pubmed.ncbi.nlm.nih.gov/21985154/). Its complete abstract and selected bibliographic metadata (title, journal, publication date and identifiers, not author affiliations) verify [DOI 10.1111/j.1365-2672.2011.05173.x](https://doi.org/10.1111/j.1365-2672.2011.05173.x). Cohort results cannot establish HsCH8a-specific genes or phenotypes. The publisher page was inaccessible through the web tool during this review, so isolate-level full-text tables remain unverified. No experimental claim was imported.

## Completeness

Complete enough for the supported taxonomy-seed claims. Zero represented BacDive strains does not deny the cultured isolate's existence. Optional enrichment is possible, but no additional target deposit or genome relationship was established.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial regular expression was `\b1036659\b|bacillus_sp_hsch8a\b|\bHs[ _-]?ch[ _-]?8[ _-]?a\b`; expansion added word-bounded JF803875 with optional .1 and UID 334361643. Both searches returned the same three own rows, all read completely in native form: two TSV rows and one compressed JSON row. No non-target candidate required exclusion. Five SOURCE.json files were separately parsed in full for each term set, with no matching fields; history filenames were independently inventoried.

Exact Nuccore query `txid1036659[Organism:exp]` returned one result. The all-field query `HsCH8a[All Fields] OR "HsCH-8a"[All Fields] OR "Hs CH8a"[All Fields]`, without a genus restriction, also returned only the own marker. Its two quoted separator variants were reported missing and removed from translation. Exact Assembly query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence.

PubMed query `HsCH8a OR "HsCH-8a" OR "Hs CH8a"` returned zero, but reported the exact label and quoted variants unrecognized; the effective translation was an HS/ch8a combination. This is a weak name-index check, not evidence of absent literature. The exact accession query retrieved the GenBank-linked primary study. All returned query translations and diagnostics were inspected; no full-text literature census was performed.

iModulonDB was not run: no gene, regulator or expression assertion is present and no applicable target strain/dataset was established. Empty optional fields are not automatic defects. Absence conclusions are bounded to the stated local roots, terms and public indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. The marker and study link add context without establishing missing deposit, genome or phenotype claims.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. A partial 16S marker must not be treated as a whole genome or a verified species reassignment.

## Follow-up Checks

Optional enrichment requires isolate-specific primary text explicitly linked to HsCH8a/JF803875 and independent deposit/genome provenance. No independent alignment, genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036659`, inspect the output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran during this review.

## Additional Notes

Independent review followed the local skill and field checklist; no neighboring verdict was inherited. The entire YAML, own source rows, all three local candidates, complete live taxonomy, full marker and primary abstract with the metadata scope above were inspected.

Before/after YAML SHA-256: `c30e21c79fcc9201dbf5933e0fbba4ba36706876e8cb2d6c5f3bc271bc207259`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
