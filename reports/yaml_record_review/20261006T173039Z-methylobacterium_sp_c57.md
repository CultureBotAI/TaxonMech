# YAML Record Review: Methylobacterium sp. C57

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c57.yaml`
- Started UTC: 2026-10-06T17:28:52Z
- Finished UTC: 2026-10-06T17:30:39Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` identifies `NCBITaxon:1035237`, Methylobacterium sp. C57, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and status SEEDED. It asserts ten root-first ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14449`; scope is `curation/seed_scope.tsv:322233`. Seeded fields are generated from maintained inputs and logic. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Local review/curation guidance, checklist, repository instructions, documentation, schema, seeder and authoritative commands were inspected at this revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c57.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c57.yaml --out /private/tmp/mc57-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons confirmed identity, every ancestor, path/scope rows, attestation and seed-event text. These manual comparisons are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates and global `just validate-history`. The reproduction gate has no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: its configuration targets curator-added graph grounding, absent here, and skips NCBITaxon. Pinned and live NCBI were used for taxonomic identifiers.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were read; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221958` supports the exact identity, rank, parent, genetic code, empty synonyms and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31426`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035237&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035237) agree with identity and placement. Every stored ancestor label and rank agrees with the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT means exact grounding to this NCBI concept, not valid nomenclature or a culture deposit. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), fully inspected in the recent T26 review and specifically searched for C57 here, supplies no target identity bridge. Genus nomenclature and properties must not be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot note. It counts a source-name assertion, not strains or genomes. The event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. Zero BacDive records therefore agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; it does not deny that C57 was cultivated.

The exact live query `txid1035237[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300734. Full [FR869833.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869833.1), excluding bases, was read: a 1333-nt partial 16S rRNA gene, strain C57, explicit `taxon:1035237`, host Cerastium holosteoides and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA does not make this partial marker a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The bibliography and complete abstract fetched during the immediately preceding C54b review were re-read for C57. Community-level comparisons across hosts, locations and land-use conditions do not establish named C57-specific growth, phenotype or collection locality. Its host comes from this marker's own metadata. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced nine rows, all fully inspected: three genuine taxonomy/name/scope rows and six unrelated numeric hits. The five discovered `SOURCE.json` files were separately parsed without a target value; ignored-independent history filename enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bC[- _]?57\b|\bC[- _]?57\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants were leads, not asserted aliases. FR869833 produced no local accession hit in these roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for C57, C-57 and C 57. No eligible own-deposit/owning-strain bridge or required missing genome link was established. The marker is optional identity evidence, not an owning BacDive strain or same-deposit StrainInfo assertion. Empty optional definition, evidence and graph slots need not be filled without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Require C57's own eligible whole culture accession and source chain before adding links. StrainInfo sequences must explicitly name the matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB requires exact existing BioSample evidence and an eligible available FASTA. Preserve taxon, strain, deposit, sample, project, marker and genome identities separately; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict validation and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- Four excluded Lacticaseibacillus paracasei rows identify taxid 1597, strain 2201st1_C3_2201SCRN_220225, GCA/GCF_040925095.1, BV-BRC 1597.2005 and SAMN41035237: `data/bvbrc/bvbrc-0004.jsonl.gz:17535`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20859`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20005`, `data/catalog/gtdb_genomes-0015.jsonl.gz:41289`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6262` is Mycobacterium tuberculosis taxid 1773, genome 1773.18455, strain/run ERR1035237.
- `data/catalog/allthebacteria.tsv.xz:569707` is Mycobacterium tuberculosis, ERR1035237, SAMEA3558770, ERZ3502607. Its available FASTA and PASS filters do not identify C57.
- All candidate fields were read losslessly. The target was re-read byte-identical. Only this report was written for C57; no YAML, history, status, generated product, Git or GitHub mutation was made.

