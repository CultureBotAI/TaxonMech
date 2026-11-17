# YAML Record Review: uncultured marine bacterium D013

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d013.yaml`
- Started UTC: 2026-10-09T08:02:22Z
- Finished UTC: 2026-10-09T08:09:57Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:103666`, uncultured marine bacterium D013. It asserts species rank, Bacteria, parent 150608, five root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. The embedded seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved the target YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d013.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d013.yaml --out /private/tmp/taxonmech-marine-d013-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured source comparisons matched identity, all five ancestors, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Marker annotation consistency passed: declared and actual length 559, rRNA transcription identical to DNA, no non-ACGT symbols. This is not independent alignment or taxonomic inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103666&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103666) responses agree with the label, species rank and lineage. EFetch confirms parent 150608 and code 11; Datasets includes root. The chain is root (1), cellular organisms (131567), Bacteria (2), environmental samples (48479), marine bacteria D ensemble (150608).

EFetch's division is Environmental samples; this does not conflict with the Bacteria domain carried by the lineage. Live taxonomy has no other names; pinned synonym fields are empty. No own type-material, merged-ID or dropped-taxon row, or backbone child, was found. NCBI species rank does not establish a cultured species, formal nomenclature or a genus assignment.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:18531`, `data/catalog/ncbi_names-0000.jsonl.gz:38547`, `data/taxa/PATHS.tsv:15081` and `curation/seed_scope.tsv:144175`. The 2026-09-13 snapshot, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories.

Exact Nuccore taxon search returned UID 5882268 alone. Complete [AF177553.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177553.1) XML, references, features and sequence were read. It is a 559-base partial 16S marker, partial at both ends. Six source qualifiers identify the target organism, genomic DNA, taxon 103666, clone D013, environmental sampling and an uncultured surface-associated marine bacterium. There is no culture deposit, strain or genome qualifier. The record was created 15-SEP-1999 and updated 11-MAY-2004; its direct submission by Dang and Lovell is dated 13-AUG-1999, University of South Carolina.

The marker links [PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/), independently retrieved with its complete abstract and selected bibliographic metadata. PubMed and inspected PMC front matter agree on [DOI 10.1128/AEM.66.2.467-475.2000](https://doi.org/10.1128/AEM.66.2.467-475.2000) and [PMC91850](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/). The study examined marine-surface colonization using cloned rRNA sequences. Cohort-level phylogenetic results cannot assign D013 to a particular subgroup without clone-specific evidence.

The PMC web page presented a browser check, and DOI/publisher full-text requests were inaccessible. The PMC XML request exposed front matter, not usable body/table passages. Search snippets containing clone tables were treated only as leads. Clone-level frequencies, phylogenetic placement and figures remain unverified; none were imported into the record.

## Completeness

Complete enough for the supported taxonomy-seed claims. A clone is not a BacDive strain or a genome assembly, and zero represented strains is not a claim that no organisms were sampled.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 103666, the exact slug, and D013/D13 with an optional separator and zero. Expansion added AF177553 with optional .1 and UID 5882268. Both searches returned the same 683 candidate rows.

All 683 received structured identity triage. A conservative selection retained exact numeric/marker/zero-preserving D013 hits, marine contexts and rows without identity projections: 103 rows were then read completely in native form (80 TSV and 23 JSON), with lossless common-field/difference representations. The other 580 had distinct taxon, organism, strain or project identities in inspected projections; their remaining content was not audited. Only three selected rows concern this target. Examples of excluded evidence:

- CIP 103666 belongs to Finegoldia magna, species 1260/strain 334413, BacDive 17987, GOLD Go0299794 and StrainInfo SI-ID 92830/SI-DP 151137. Its source-specific classification levels are distinct from taxon 103666.
- BacDive 103666 is Rhodococcus sp. ST030131, taxon 194249. StrainInfo SI-DP 103666 is ATCC 25120, Mycobacterium intracellulare, taxon 1767. These are identifier-namespace collisions.
- Salmonella enterica D013 is GCA_010253635.1/SAMN09788965, taxon 28901. Escherichia coli D013-14, d013-05.2 and d013-06.4a concern GCA_016999335.1, GCA_014081405.1 and GCA_020269665.1, taxon 562.
- GTDB rows for GCA_964616705.1 and GCF_039534185.1 match scaffold N75 length 103666, not the target taxon. Other marine-water matches concern PRJEB33281 single-cell/metagenomic entries with longer AG/AH strain identifiers; Saanich Inlet GOLD projects Gp0297131, Gp0297233 and Gp0297430 likewise have different samples.
- Eleven complete ATB rows concern Parabacteroides, Firmicutes JGI 0000119-D13, Thiomicrospira JGI CrystG Aug3-3-D13, GAL15, Prochlorococcus, Synechococcus and Salipiger records. Their sample accessions and source filters do not create a D013 identity bridge.

Five SOURCE.json files were separately parsed in full for both term sets. The BacDive manifest hit is a fetch request for BacDive identifier 103666, resolved above as Rhodococcus, not an NCBI taxon assertion. History filenames were independently inventoried.

Exact Assembly query returned zero with missing-phrase/no-items diagnostics, not proof of global genome absence. Broad Nuccore all-field D013/separator query reported 677 matches and returned its first 100 UIDs; those broad results were not exhaustively fetched or adjudicated. No claim of a complete outside-taxon sequence census is made.

The PubMed full-label/marine-bacterium query and exact AF177553 search returned zero with quote/translation diagnostics; the explicit GenBank-linked PMID resolved the primary study. Index misses do not establish absent literature. No full-text literature census was performed.

iModulonDB was not run: the record asserts no gene, regulator or expression claim and no applicable strain/dataset was established. Optional empty fields are not automatic defects. No additional target deposit/genome link was established within the checked evidence, not a global absence finding.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. The environmental clone's NCBI identity, carried lineage, source attestation and admission agree. Similar labels and bare numeric matches do not justify adding cultured-strain or genome links.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not erase leading zeros or identifier namespaces when joining evidence.

## Follow-up Checks

Optional ecological or phylogenetic enrichment requires accessible primary clone-specific text or tables explicitly linked to D013/AF177553. A cultured-strain or genome relationship requires independent provenance, not the clone code alone. No independent alignment, genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:103666`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, 103 selected local candidate rows, identity projections for the remaining 580, live taxonomy, complete marker, primary abstract and PMC front matter were inspected. These are deliberately different evidence scopes.

Before/after YAML SHA-256: `0ffb262ca4e7d9c1938ecf51f4162267016debf18f0b7fa574f3f779874e591a`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
