# YAML Record Review: uncultured marine bacterium D010

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d010.yaml`
- Started UTC: 2026-10-09T06:48:14Z
- Finished UTC: 2026-10-09T06:53:15Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:103665`, uncultured marine bacterium D010. It asserts species rank, Bacteria, parent 150608, five root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status, zero represented BacDive strains and one NCBITAXON name attestation. Its seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussions and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d010.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d010.yaml --out /private/tmp/taxonmech-marine-d010-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched identity, all ancestor IDs/labels/ranks, attestation, PATHS, admission reason and seed wording. Exact scans covered seven supplementary raw inventories, type material, merged IDs and dropped taxa.
- Own marker annotation consistency passed: declared/actual length 559, rRNA transcription identical to DNA and no non-ACGT symbols. No independent alignment or species assignment was performed.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift or publication builds. Focused checks do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact in the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103665&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103665) agree with ID, label, species rank and ancestry. EFetch confirms parent and code 11; Datasets includes root. The chain is root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. Both final ancestors are unranked.

The NCBI division is Environmental samples; the domain remains Bacteria because taxon 2 is in the authoritative lineage. These are different fields, not contradictory placements. The record preserves NCBI's environmental grouping without inferring a phylum or genus. Species rank here does not imply formal nomenclatural standing, a cultured species, or a deposited strain.

No other names occur in the live authority response; pinned synonym fields are empty. No exact own type-material, merged-ID or dropped row, or backbone child, was found.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:18530`, `data/catalog/ncbi_names-0000.jsonl.gz:38546`, `data/taxa/PATHS.tsv:15070` and `curation/seed_scope.tsv:144174`. Snapshot 2026-09-13, the one-name unit and admission reason support the attestation and seed event. A `NAME` is not a genome or culture. Exact raw scans found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row.

Exact Nuccore taxon query returned UID 5882267 alone. Complete [AF177552.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177552.1) XML, references, features and sequence were read. This 559-base 16S marker is partial at both ends. Its source qualifiers name the organism and taxon 103665, genomic DNA, clone D010 and an environmental-sample flag; its note identifies surface-associated marine material. It supplies no strain, culture-deposit, genome, BioSample or geographic qualifier. Clone D010 must not be converted into a culture-collection identifier.

The marker explicitly cites Dang and Lovell, [PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/), and a 13-AUG-1999 University of South Carolina submission. Complete PubMed abstract/metadata and the available [PMC91850 XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=91850&retmode=xml) verify [DOI 10.1128/AEM.66.2.467-475.2000](https://doi.org/10.1128/AEM.66.2.467-475.2000). The study used culture-independent analyses of early surface colonization in estuarine water. Its aggregate phylogenetic results do not identify which placement applies specifically to D010.

The PMC browser page returned an access challenge; the DOI page was inaccessible. The complete 7,755-byte PMC XML response contains bibliographic/abstract material and an explicit publisher restriction on full-text XML, but no article body. Thus no D010-specific table, tree or experimental result was verified. Missing accessible text is not evidence that the paper lacks D010.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive entries is consistent with this environmental clone; optional empty fields are not automatic defects. No target culture-deposit or genome relationship was established.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms were word-bounded 103665, the exact slug and D010 with an optional separator after D. Expansion added AF177552 and UID 5882267. Both searches returned the same 24 rows: ten TSV and 14 JSON rows, all read completely in native form using common fields and lossless differences. Five SOURCE.json files were separately parsed in full for each term set; history filenames were independently inventoried.

Three matched rows concern this target; the remaining 21 have distinct namespaces or biological identities:

- BacDive 103665 denotes Rhodococcus sp., taxon 194249, designations ST019278(HKI)/BI 08974. The SOURCE.json request for BacDive ID 103665 is the same namespace collision, not NCBI taxon support.
- CIP 103665 belongs to Neisseria lactamica, taxon 486, BacDive 135325, StrainInfo 42318/deposit 153224 and GOLD Go0265694. Its aliases include ATCC 49142 and ACM 4759. Own-deposit and GOLD rows do not link it to the environmental clone.
- StrainInfo deposit 103665 is ATCC 25119 in strain record 38363, Mycobacterium intracellulare, taxon 1767. IMI 103665 belongs to Chaetomella raphigera, taxon 241714, strain record 74092. Its sequence links explicitly name CBS 130.64, not D010.
- Escherichia coli d010-14 has GCA_014082145.1 / SAMN11319306. Salmonella Stanley strain 103665 has GCA_009522215.1 / SAMN08100355. Klebsiella variicola assembly name KLP-ELB-HUB-103665 has GCA/GCF_901521625.1 / SAMEA5605373. These names and accession chains are not the target taxon.
- Two GTDB rows match assembly statistics equal to 103665: Leuconostoc gelidum PB4d, GCF_020089285.1, and Bacteroides fragilis S_284, GCA_034131265.1. The number is not their taxonomic grounding.

Both the exact taxon-ID and full-name Nuccore queries returned only AF177552.1. A broader query using the separate taxon name "uncultured marine bacterium" plus D010 returned zero because that taxon expansion does not retrieve the own hit; it cannot support absence. D010 alone produced an all-field diagnostic count of 424, not an audited set. Exact Assembly query returned zero with missing-phrase/no-items diagnostics, which does not prove global genome absence.

The exact accession PubMed query returned zero despite the inspected GenBank-linked publication, demonstrating an index limitation. The D010 plus marine/bacterial-term query returned eight other papers. Complete abstracts/metadata were inspected: [42075706](https://pubmed.ncbi.nlm.nih.gov/42075706/) concerns Leptospira regulators; [41719992](https://pubmed.ncbi.nlm.nih.gov/41719992/) is a feeding trial; [41471981](https://pubmed.ncbi.nlm.nih.gov/41471981/), [38731579](https://pubmed.ncbi.nlm.nih.gov/38731579/), [37764358](https://pubmed.ncbi.nlm.nih.gov/37764358/) and [35008891](https://pubmed.ncbi.nlm.nih.gov/35008891/) discuss stress, trehalose, aggregation or Klebsiella resistance; [31541512](https://pubmed.ncbi.nlm.nih.gov/31541512/) concerns tumor immunohistochemistry; [15254725](https://pubmed.ncbi.nlm.nih.gov/15254725/) concerns viral expression vectors and includes D010 in an institutional address. None of these abstracts establishes this clone's identity or supports enrichment. This was not a full-text audit of the eight papers.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was established. Absence conclusions are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. The environmental taxon, lineage, admission and provenance agree with pinned and live authorities. Numerical identifiers from other namespaces and similarly named isolates must remain separate.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not replace the carried environmental lineage with a placement inferred from the study cohort.

## Follow-up Checks

Optional enrichment requires primary passages or figures explicitly naming D010/AF177552, with any experimental or phylogenetic interpretation scoped to that clone. No independent alignment, genome comparison, experimental reanalysis or PDF/figure visual verification was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:103665`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, own source rows, all 24 local candidates, live taxonomy, complete own marker, nine PubMed abstracts/metadata and the complete available front-matter-only PMC response were inspected.

Before/after YAML SHA-256: `1708c4b13a6f8b7d9d4cbc45f6e66038000f0ec45201b7f508d09c9fb6b6f64a`. Only this new report was written for the target. YAML, sources, status, history, pages, Eukaryota, GitHub objects and worktrees were unchanged.
