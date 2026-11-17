# YAML Record Review: Methylobacterium sp. T26

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_t26.yaml`
- Started UTC: 2026-10-06T17:17:58Z
- Finished UTC: 2026-10-06T17:20:15Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` identifies `NCBITaxon:1035234`, Methylobacterium sp. T26, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and status SEEDED. Its assertions comprise ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. It has no synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, phenotype/host claim, discussion or graph.

The unique path-lock row is `data/taxa/PATHS.tsv:14446`; scope is `curation/seed_scope.tsv:322230`. Seeded fields are generated, not directly curated. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Local review/curation guidance, checklist, repository instructions, documentation, schema, seeder and authoritative commands were inspected at this revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_t26.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_t26.yaml --out /private/tmp/mt26-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons checked identity, every ancestor, path/scope rows, attestation and seed-event text. They are manual evidence checks, not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. Inspection of `scripts/verify_corpus.py` confirms it has no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: `conf/id_label_targets.yaml` targets curator-added graph grounding, absent here, and skips NCBITaxon. Taxonomic identifiers were checked against pinned and live NCBI.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were read; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221955` supports the exact identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot. The full scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31423`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035234&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035234) agree with the record. The pinned labels and ranks agree for root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT identifies this NCBI concept, not valid nomenclature or a culture deposit. The full [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium) was inspected and searched for T26 without a target match. It supplies no isolate identity bridge; genus properties and nomenclature must not be transferred. The legacy NCBI browser failed through the web tool; the two authority APIs succeeded.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot note. This counts one source-name assertion, not genomes or strains. The event timestamp 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. There are no direct backbone children, hence no descendants to gather. The zero BacDive count agrees with `src/taxonmech/seed.py`'s own/subtree rule, not a claim that T26 was never cultivated.

The live exact query `txid1035234[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300731. Full [FR869830.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869830.1), excluding bases, was inspected: a 1333-nt partial 16S rRNA gene, strain T26, explicit `taxon:1035234`, host Trifolium repens and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA does not turn a partial marker into a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The bibliography and complete abstract fetched in the recent TS68 review were re-read for this target. Community-level comparisons across hosts, locations and land-use types do not establish named T26-specific growth, phenotype or collection locality. Its host comes from this marker's own metadata. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 23 rows: three genuine taxonomy/name/scope rows and 20 unrelated numeric hits. Every candidate was inspected in full. The five discovered `SOURCE.json` metadata files were separately parsed without a target hit; ignored-independent history filename enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bT[- _]?26\b|\bT[- _]?26\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. These variants are search leads, not asserted aliases. FR869830 produced no local accession hit in those roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for T26, T-26 and T 26. No eligible own-deposit/owning-strain bridge or required missing genome link was demonstrated. A marker is optional identity evidence, not an owning BacDive strain or a same-deposit StrainInfo sequence assertion. Empty optional definition, evidence and graph slots need not be filled without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Require the target's own eligible whole culture accession and source chain before adding links. StrainInfo sequences must explicitly name the same matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB requires exact existing BioSample evidence and an eligible available FASTA. Keep taxon, strain, deposit, sample, project, marker and genome identities separate.

After an authorized maintained-input change, run target schema/strict checks and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- `data/bvbrc/bvbrc-0006.jsonl.gz:6259` is Mycobacterium tuberculosis taxid 1773, genome 1773.18452, strain/run ERR1035234.
- Ten GOLD rows, `data/gold/projects.jsonl.gz` lines 376169 through 376178, are Gp0518933 through Gp0518942 with SAMN10352340 through SAMN10352349, respectively, and PRJNA503098. Each own organism-ID field is empty; the names describe Lake Taihu sediment-community samples 7 through 16. These are not a T26 isolate, eligible culture deposit or supported own-organism analysis chain.
- Four Lacticaseibacillus paracasei rows identify taxid 1597, strain 1001217st1_D2_RTP21198_201120, GCA/GCF_040925145.1, BV-BRC 1597.2006 and SAMN41035234: `data/catalog/ncbi_genbank-0037.jsonl.gz:20861`, `data/bvbrc/bvbrc-0004.jsonl.gz:17536`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20007`, `data/catalog/gtdb_genomes-0005.jsonl.gz:21074`.
- Two archaeal rows identify Halomicrobium sp. HArcel3, taxid 1679064, GCA/GCF_058933135.1, SAMN61035234: `data/catalog/ncbi_genbank-0054.jsonl.gz:28335` and `data/catalog/ncbi_refseq-0009.jsonl.gz:2054`.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6452` is Campylobacter jejuni taxid 197, strain PNUSAC014897, GCA_010352345.1, SAMN13763546.
- `data/catalog/allthebacteria.tsv.xz:569704` is Mycobacterium tuberculosis, ERR1035234, SAMEA3558767, ERZ3502589. Row 3215622 in that file is Salmonella enterica, SRR32737876, SAMN47417438, ERZ27175959; the numeric match is inside its SeqKit sum, not a taxid. Both have available FASTAs and PASS filters, which do not identify T26. SeqKit sums are not MD5 identifiers.
- Native fields were read losslessly; no unrelated strain, sample or genome was transferred. The target was re-read byte-identical. Only this report was written for T26; no YAML, history, status, generated product, Git or GitHub mutation was made.

