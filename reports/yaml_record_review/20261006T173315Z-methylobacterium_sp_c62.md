# YAML Record Review: Methylobacterium sp. C62

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c62.yaml`
- Started UTC: 2026-10-06T17:31:25Z
- Finished UTC: 2026-10-06T17:33:15Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` identifies `NCBITaxon:1035238`, Methylobacterium sp. C62, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and status SEEDED. It asserts ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14450`; scope is `curation/seed_scope.tsv:322234`. Seeded fields are generated from maintained inputs and logic. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Local review/curation guidance, checklist, repository instructions, documentation, schema, seeder and authoritative commands were inspected at this revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c62.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c62.yaml --out /private/tmp/mc62-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons confirmed identity, every ancestor, path/scope rows, attestation and event text. These manual comparisons are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction gate has no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: its configuration targets curator-added graph grounding, absent here, and skips NCBITaxon. Pinned and live NCBI were used for taxonomic identifiers.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221959` supports the exact identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31427`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035238&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035238) agree with identity and placement. All stored ancestor labels and ranks agree with the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT grounds this NCBI concept; it is not a valid-nomenclature or culture-deposit assertion. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), fully inspected in the recent T26 review and specifically searched for C62 here, supplies no target identity bridge. Genus properties and nomenclature must not be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot note. It counts a source-name assertion, not strains or genomes. The event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. Zero BacDive records agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; it does not deny that C62 was cultivated.

The exact live query `txid1035238[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300735. Full [FR869834.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869834.1), excluding bases, was read: a 1335-nt partial 16S rRNA gene, strain C62, explicit `taxon:1035238`, host Cerastium holosteoides and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA describes the molecule source, not a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The bibliography and complete abstract fetched during this session's C54b review were re-read for C62. Community comparisons across hosts, locations and land-use conditions do not establish named C62-specific growth, phenotype or collection locality. Its host comes from its own marker metadata, not an adjacent isolate or the submission address. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 13 rows, all fully inspected: three genuine taxonomy/name/scope rows and ten unrelated numeric matches. The five discovered `SOURCE.json` files were separately parsed without a target value; ignored-independent history filename enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bC[- _]?62\b|\bC[- _]?62\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants were leads, not asserted aliases. FR869834 produced no local accession hit in these roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for C62, C-62 and C 62. No eligible own-deposit/owning-strain bridge or required missing genome link was established. The marker is optional identity evidence, not an owning BacDive strain or same-deposit StrainInfo assertion. Optional definition, evidence and graph slots need not be filled without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require C62's own eligible whole culture accession and source chain before adding links. StrainInfo sequences must explicitly name the matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB requires exact existing BioSample evidence and an eligible available FASTA. Preserve taxon, strain, deposit, sample, project, marker and genome identities separately; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict checks and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- Four excluded Lacticaseibacillus rhamnosus rows identify taxid 47715, strain 1001216st2_A2_RTP21198_201120, GCA/GCF_040925065.1, BV-BRC 47715.1902 and SAMN41035238: `data/bvbrc/bvbrc-0020.jsonl.gz:45791`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20857`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20003`, `data/catalog/gtdb_genomes-0014.jsonl.gz:7344`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6261` is Mycobacterium tuberculosis taxid 1773, genome 1773.18454, strain/run ERR1035238.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6453` is Campylobacter jejuni taxid 197, strain PNUSAC013483, GCA_010352385.1 and SAMN13337313.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:28181` is Bacteroidota bacterium taxid 1898104, MAG BILL18-1_SAMN07137097_MAG_00000001, GCA_982674215.1 and SAMEA122230561. The exact number 1035238 is its gapped genome size, not a taxid.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:17428` and `data/catalog/gtdb_genomes-0015.jsonl.gz:3804` concern GCA_964428755.1, isolate binchicken_co245_258, SAMEA117365511, NCBI taxid 395355, uncultured Bdellovibrionales bacterium. GTDB instead places it in Patescibacteriota, species JAGOTT01 sp964428755. These differing source classifications are preserved as context, not reconciled or transferred to C62. Both matches are to the ungapped length 1035238, not C62's taxid.
- `data/catalog/allthebacteria.tsv.xz:569708` is Mycobacterium tuberculosis, ERR1035238, SAMEA3558771, ERZ3502603. Its available FASTA and PASS filters do not identify C62.
- Candidate fields were read losslessly. The target was re-read byte-identical. Only this report was written for C62; no YAML, history, status, generated product, Git or GitHub mutation was made.

