# YAML Record Review: Methylobacterium sp. C38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c38.yaml`
- Started UTC: 2026-10-06T17:21:18Z
- Finished UTC: 2026-10-06T17:23:37Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035235`, Methylobacterium sp. C38, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and mapping status SEEDED. Material assertions are ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, phenotype/host claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14447`; scope is `curation/seed_scope.tsv:322231`. Seeded fields are generated, not directly curated. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Local review/curation guidance, checklist, repository instructions, documentation, schema, seeder and authoritative commands were inspected at this revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c38.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c38.yaml --out /private/tmp/mc38-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons confirmed identity, every ancestor, path/scope rows, attestation and event text. These manual comparisons are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction gate has no target selector. No claim of corpus-wide reproducibility or reference integrity is made.
- `just validate-products` was not run: its configuration targets curator-added graph grounding, absent here, and skips NCBITaxon. Taxonomic identifiers were checked against pinned and live NCBI.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were read; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221956` supports the exact taxid, label, species rank, parent, code 11, empty synonyms and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31424`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035235&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035235) agree with identity and placement. All stored ancestor labels and ranks agree with the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT means exact grounding to this NCBI concept, not valid nomenclature or culture-deposit identity. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), fully inspected in the immediately preceding T26 review and specifically searched for C38 here, supplies no target identity bridge. Genus nomenclature and properties must not be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot. It counts a source-name assertion, not biological strains or genomes. The event timestamp 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. Zero BacDive records therefore agrees with the own/subtree rule in `src/taxonmech/seed.py`, not a claim that C38 was never cultivated.

The live exact query `txid1035235[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300732. Full [FR869831.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869831.1), excluding bases, was read: a 1326-nt partial 16S rRNA gene, strain C38, explicit `taxon:1035235`, host Cerastium holosteoides and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA describes the molecule source, not a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The bibliography and complete abstract fetched in the recent TS68 review were re-read for C38. The community-level study does not establish named C38-specific growth, phenotype or collection locality. C38's host comes from its own marker metadata, not the submission address or an adjacent isolate. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 25 rows, all fully inspected: three genuine taxonomy/name/scope rows and 22 unrelated numeric hits. Five discovered `SOURCE.json` files were separately parsed without a target match. Ignored-independent history path enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bC[- _]?38\b|\bC[- _]?38\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants were leads, not asserted aliases. FR869831 produced no local accession hit in those roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for C38, C-38 and C 38. No eligible own-deposit/owning-strain bridge or required missing genome link was established. The marker is optional identity evidence, not an owning BacDive strain or a same-deposit StrainInfo assertion. Optional definition, evidence and graph slots need not be filled without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Require the target's own eligible whole culture accession and source chain before adding strain/genome links. StrainInfo sequences must name the same matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB requires exact existing BioSample evidence and an eligible available FASTA. Keep taxon, strain, deposit, sample, project, marker and genome identities separate; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict validation and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- Five excluded Pseudomonas aeruginosa rows concern taxid 287, strain Pae_CF67.08s, GCA/GCF_001035235.1, BV-BRC 287.1613 and SAMN03566383: `data/bvbrc/bvbrc-0016.jsonl.gz:22048`, `data/gold/analyses.jsonl.gz:101321`, `data/catalog/ncbi_refseq-0000.jsonl.gz:30445`, `data/catalog/gtdb_genomes-0008.jsonl.gz:19433`, `data/catalog/ncbi_genbank-0000.jsonl.gz:36040`. GOLD Ga0158542 names that Pseudomonas isolate, project Gp0189773 and GCA_001035235.1/LEHD00000000, with empty own-organism and IMG fields. It is unrelated to C38; no C38 chain is inferred.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6254` is Mycobacterium tuberculosis taxid 1773, genome 1773.18448, strain/run ERR1035235.
- Four Lacticaseibacillus paracasei rows identify taxid 1597, strain 1001217st1_E3_RTP21198_201120, GCA/GCF_040925115.1, BV-BRC 1597.2004 and SAMN41035235: `data/catalog/ncbi_genbank-0037.jsonl.gz:20860`, `data/bvbrc/bvbrc-0004.jsonl.gz:17534`, `data/catalog/gtdb_genomes-0013.jsonl.gz:21514`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20006`.
- Seven GOLD rows in `data/gold/projects.jsonl.gz`, lines 376179 through 376185, are Gp0518943 through Gp0518949 with SAMN10352350 through SAMN10352356, respectively, and PRJNA503098. Each own organism-ID field is empty. Their names identify Lake Taihu sediment-community samples 17 through 23, not a C38 isolate, eligible deposit or own-organism analysis chain.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:27288` is Agathobacter rectalis taxid 39491, metagenome-derived isolate 1945_1945B_C_5, GCA_061035235.1 and SAMN60704093.
- Three Klebsiella aerogenes rows identify taxid 548, isolate 1900120 and SAMN34998165. `data/catalog/ncbi_genbank_historical-0001.jsonl.gz:21195` and `:21196` are replaced GCA_031035235.1 and GCA_031035235.2; `data/catalog/ncbi_genbank-0028.jsonl.gz:43450` is latest GCA_031035235.3. Historical presence does not make any version a C38 assembly.
- `data/catalog/allthebacteria.tsv.xz:569705` is Mycobacterium tuberculosis, ERR1035235, SAMEA3558768, ERZ3502587. Its available FASTA and PASS filters do not identify C38.
- Native candidate fields were read losslessly; no unrelated strain, sample or genome was transferred. The target was re-read byte-identical. Only this report was written for C38; no YAML, history, status, generated product, Git or GitHub mutation was made.

