# YAML Record Review: Bacillus sp. HsMMA7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_hsmma7.yaml`
- Started UTC: 2026-10-09T08:11:44Z
- Finished UTC: 2026-10-09T08:15:04Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036660`, Bacillus sp. HsMMA7. It asserts species rank, Bacteria, parent 185979, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. Its embedded seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_sp_hsmma7.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/bacillus_sp_hsmma7.yaml --out /private/tmp/taxonmech-bacillus-hsmma7-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, all ten ancestors, PATHS, scope reason, source attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Marker annotation consistency passed: declared and actual length 860, rRNA transcription identical to DNA, no non-ACGT symbols. This is not independent alignment or species identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product checks are inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036660&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036660) responses agree with identity, species rank and lineage. EFetch confirms parent 185979 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Bacillus and unclassified Bacillus (in: firmicutes).

Live taxonomy has no other names; pinned synonym fields are empty. No own type-material, merged-ID or dropped-taxon row, or backbone child, was found. NCBI species rank does not establish formal nomenclatural standing or identify a named Bacillus species.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222565`, `data/catalog/ncbi_names-0005.jsonl.gz:32109`, `data/taxa/PATHS.tsv:15082` and `curation/seed_scope.tsv:322812`. The 2026-09-13 snapshot, one-name unit and admission reason support the attestation and seed event. A `NAME` count is not a genome or experiment count. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories.

Exact Nuccore taxon search returned UID 334361642 alone. Complete [JF803874.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803874.1) XML was read, including references, features and sequence. It is an 860-base 16S marker, partial at both ends. Its six source qualifiers identify Bacillus sp. HsMMA7, genomic DNA, strain HsMMA7, host Haliclona simulans, taxon 1036660 and Ireland: Gurraig Sound Kilkieran Bay, Galway. There is no deposit or genome qualifier. References identify Phelan and colleagues and a 13-APR-2011 University College Cork direct submission. GenBank creation and update dates are 31-DEC-2011 and 20-NOV-2013.

Exact JF803874 PubMed search retrieves [PMID 21985154](https://pubmed.ncbi.nlm.nih.gov/21985154/). Its complete abstract and selected bibliographic metadata (title, journal, date and publication identifiers, not author affiliations) verify [DOI 10.1111/j.1365-2672.2011.05173.x](https://doi.org/10.1111/j.1365-2672.2011.05173.x). Cohort results cannot establish HsMMA7-specific genes or phenotypes. The DOI/publisher page was inaccessible through the web tool during this review, so isolate-level full-text tables remain unverified. No experimental claim was imported.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not deny the existence of a cultured isolate. Optional enrichment remains possible, but no additional target deposit or genome relationship was established.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 1036660, the exact slug and HsMMA7 with optional space, hyphen or underscore after Hs, MM and A. Expansion added word-bounded JF803874 with optional .1 and UID 334361642. Both searches returned the same three own rows, all read completely in native form: two TSV rows and one compressed JSON row. No non-target candidate required exclusion.

Five SOURCE.json files were separately parsed in full for both term sets, with no matching fields; history filenames were independently inventoried. These bounded searches do not establish absence under unsearched aliases or outside the named roots.

Exact Nuccore query `txid1036660[Organism:exp]` returned one result. All-field query `HsMMA7[All Fields] OR "HsMMA-7"[All Fields] OR "Hs MMA7"[All Fields]`, without a genus restriction, also returned only the own marker. Its two quoted separator variants were reported missing and removed from translation. Exact Assembly query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence.

PubMed query `HsMMA7 OR "HsMMA-7" OR "Hs MMA7"` returned zero, but reported the exact label and quoted variants unrecognized; the effective translation was an HS/mma7 combination. This is a weak name-index check, not evidence of absent literature. Exact accession search retrieved the GenBank-linked primary study. All query translations and diagnostics were inspected; no full-text literature census was performed.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable target strain/dataset was established. Empty optional fields are not automatic defects. Absence conclusions are bounded to the stated roots, terms and public indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, attestation and admission agree with pinned and live authorities. The marker and study link add context without establishing missing deposit, genome or phenotype claims.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not treat a partial 16S marker as a whole genome or verified species reassignment.

## Follow-up Checks

Optional enrichment requires isolate-specific primary text explicitly linked to HsMMA7/JF803874 and independent deposit/genome provenance. No independent alignment, genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036660`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all three local candidates, live taxonomy, complete marker and primary abstract with the metadata scope above were inspected.

Before/after YAML SHA-256: `7a2c877be62a9a038deddbb55cc2eb4a18831e815f9cb2069d28bf39809f0c6a`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
