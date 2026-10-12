# YAML Record Review: Methylobacterium sp. TS68

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_ts68.yaml`
- Started UTC: 2026-10-06T17:07:55Z
- Finished UTC: 2026-10-06T17:10:18Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035232`, Methylobacterium sp. TS68, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and mapping status SEEDED. Its material assertions are ten root-first ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, taxonomy mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or causal graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14444`; scope is `curation/seed_scope.tsv:322228`. Seeded fields are generated from maintained inventories and seeding logic, not editable YAML. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

The review skill and checklist were re-read; curation guidance, documentation, schema and authoritative commands had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_ts68.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_ts68.yaml --out /private/tmp/mts68-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read and contains only its header.
- Bounded structured comparisons confirmed identity, every ancestor, path/scope rows, attestation and seed-event text. These manual comparisons are not the corpus reproduction gate.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates and global `just validate-history`. No claim of corpus-wide reproducibility or reference integrity is made. The documented reproduction gate has no target selector.
- `just validate-products` was not run: `conf/id_label_targets.yaml` targets curator-added graph grounding, absent here, and skips NCBITaxon. Taxonomic identifiers were checked against pinned and live NCBI.
- Ignored-inclusive content/path searches found no target external history artifact to validate. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 dataset rows were inspected; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221953` supports the exact taxid, label, species rank, parent, code 11, empty synonym fields and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31421`. Exact type-material, merged-ID and dropped-record table scans found no target rows.

The complete current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035232&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035232) agree with identity and placement. Every stored ancestor label and rank matches the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT means exact grounding to this NCBI concept, not valid nomenclature or a strain/deposit equivalence. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), previously fully inspected and specifically searched for TS68, supplies no target identity bridge. Genus nomenclature and properties must not be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole NCBITAXON attestation matches its identifier and label, count 1, unit NAME and snapshot note. It counts one source-name assertion, not biological strains or genomes. The `seed_from_sources` event at 2026-09-13T17:54:04Z, action SEEDED_FROM_SOURCES, exactly matches the scope's one-source reason.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. No backbone taxon has this target as its parent. Zero BacDive strain records therefore agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; it does not deny that TS68 was cultivated.

The live exact query `txid1035232[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics, and one nucleotide UID, 347300729. Full [FR869828.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869828.1), excluding bases, was read: a 1326-nt partial 16S rRNA gene, strain TS68, explicit `taxon:1035232`, host Trifolium repens and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA describes the molecule source, not a genome assembly.

The marker explicitly cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The current bibliography and complete abstract were fetched and inspected. They describe phyllosphere community comparisons across hosts, locations and land-use conditions; they do not establish named TS68-specific growth, phenotype or collection locality. The host comes from this marker's own metadata, not an adjacent isolate or the submission address. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug yielded 12 rows, all fully inspected: three genuine taxonomy/name/scope rows and nine unrelated numeric matches listed below. The five discovered `SOURCE.json` metadata files were separately parsed for target values; none matched. Ignored-independent history path enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bTS[- _]?68\b|\bTS[- _]?68\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants were leads, not asserted aliases. A follow-up FR869828 search found no local row in these roots. These are bounded local-catalog and exact live-query results, not universal external absence claims.

`normalize_culture_identifier` returned empty for TS68, TS-68 and TS 68. No eligible deposit or owning strain identity bridge was established, and no required missing strain/genome link was demonstrated. The marker is optional identity evidence but supplies neither an owning BacDive strain nor a same-deposit StrainInfo assertion. Empty optional definition, evidence and graph slots need not be filled without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported strain/deposit/genome additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require the target's own eligible whole culture accession and supported source chain before adding links. StrainInfo sequences must name the same matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB must match existing exact BioSample evidence and an eligible available FASTA. Preserve taxon, strain, deposit, sample, project, marker and assembly identity separately; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict validation and relevant join tests, then `just verify-corpus` and `just qc`. Inspect full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- Four excluded rows are Lactobacillus gasseri taxid 1596, strain 1001285st1_G5_RTP21277_210401, GCA/GCF_040925175.1, BV-BRC 1596.1052, sample SAMN41035232: `data/bvbrc/bvbrc-0004.jsonl.gz:16796`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20863`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20009`, and `data/catalog/gtdb_genomes-0015.jsonl.gz:22326`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6257` is Mycobacterium tuberculosis taxid 1773, genome 1773.18450, strain/run ERR1035232.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6451` is Campylobacter jejuni taxid 197, strain PNUSAC013492, GCA_010352325.1, sample SAMN13336275.
- Two rows are the archaeon Halomicrobium sp. HArcht1-1, taxid 1679065, GCA/GCF_058933285.1, sample SAMN61035232: `data/catalog/ncbi_refseq-0009.jsonl.gz:2055` and `data/catalog/ncbi_genbank-0054.jsonl.gz:28341`. The BioSample digit substring is not the target taxid.
- `data/catalog/allthebacteria.tsv.xz:569702` is Mycobacterium tuberculosis, run ERR1035232, sample SAMEA3558765, analysis ERZ3502583. Its available FASTA and PASS filters do not identify TS68.
- Native candidate fields were read losslessly; no unrelated strain, sample or genome was transferred.
- The target was re-read and byte-identical before reporting. Only this new report was written; no YAML, history, mapping status, generated product, Git or GitHub mutation was performed.

