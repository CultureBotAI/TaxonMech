# YAML Record Review: Methylobacterium sp. C54b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c54b.yaml`
- Started UTC: 2026-10-06T17:25:36Z
- Finished UTC: 2026-10-06T17:27:49Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035236`, Methylobacterium sp. C54b, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and status SEEDED. Its material assertions are ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or causal graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14448`; scope is `curation/seed_scope.tsv:322232`. Seeded fields are generated from maintained inputs and logic, not editable YAML. HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Review skill, checklist and curation/history guidance were re-read; repository instructions, commands, documentation, schema and seeder had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c54b.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c54b.yaml --out /private/tmp/mc54b-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Bounded source comparisons confirmed identity, every ancestor, path/scope rows, attestation and event text. These manual comparisons are not the corpus reproduction gate.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates and global `just validate-history`. The reproduction gate has no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: its configuration targets curator-added graph grounding, absent here, and skips NCBITaxon. Pinned and live NCBI were used for taxonomic identifiers.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221957` supports the exact identity, rank, parent, code 11, empty synonyms and 2026-09-13 snapshot. The full scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31425`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035236&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035236) agree with identity and placement. All ancestor labels and ranks agree with the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT identifies this NCBI concept, not valid nomenclature or a culture deposit. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), fully inspected in the recent T26 review and specifically searched for C54b here, supplies no target identity bridge. Genus properties and nomenclature must not be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot. This counts one source-name assertion, not strains or genomes. The event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this target as parent. Zero BacDive records agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; it does not mean C54b was never cultivated.

The live exact query `txid1035236[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300733. Full [FR869832.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869832.1), excluding bases, was read: a 1334-nt partial 16S rRNA gene, strain C54b, explicit `taxon:1035236`, host Cerastium holosteoides and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA describes the molecule source, not a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The current bibliography and complete abstract were fetched and inspected. Their community-level comparisons across hosts, locations and land-use conditions do not establish named C54b-specific growth, phenotype or collection locality. Its host comes from this marker's own metadata. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 14 rows, all fully inspected: three genuine taxonomy/name/scope rows and 11 unrelated numeric matches. The five discovered `SOURCE.json` files were separately parsed without a target value; ignored-independent history filename enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bC[- _]?54[- _]?b\b|\bC[- _]?54[- _]?b\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants are search leads, not asserted aliases. FR869832 produced no local accession hit in those roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for C54b, C-54b and C 54b. No eligible own-deposit/owning-strain bridge or required missing genome link was established. A marker is optional identity evidence, not an owning BacDive strain or same-deposit StrainInfo sequence assertion. Empty optional definition, evidence and graph slots need not be populated without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require C54b's own eligible whole culture accession and source chain before adding links. StrainInfo sequences must explicitly name the matched SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB requires exact existing BioSample evidence and an eligible available FASTA. Preserve taxon, strain, deposit, sample, project, marker and genome identities separately; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict checks and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- `data/bvbrc/bvbrc-0006.jsonl.gz:6260` is Mycobacterium tuberculosis taxid 1773, genome 1773.18453, strain/run ERR1035236.
- `data/gold/analyses.jsonl.gz:437372` is Ga0653398, named Salmonella enterica enterica sv. Enteritidis 538396, project Gp0811486, IMG 8103523602 and GCA_007158105.1/AAHEGE000000000, with an empty own-organism field. The IMG substring is not C54b's taxid; no target chain is inferred.
- Four Lacticaseibacillus paracasei rows identify taxid 1597, strain 1001217st1_E6_RTP21198_201120, GCA/GCF_040925085.1, BV-BRC 1597.2003 and SAMN41035236: `data/catalog/ncbi_genbank-0037.jsonl.gz:20858`, `data/bvbrc/bvbrc-0004.jsonl.gz:17533`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20004`, `data/catalog/gtdb_genomes-0007.jsonl.gz:46137`.
- `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:15133` is suppressed GCA_010352365.1, Campylobacter jejuni taxid 197, strain PNUSAC013485, SAMN13337426. Its historical presence does not identify C54b.
- `data/catalog/ncbi_genbank-0018.jsonl.gz:21521` is Salmonella enterica taxid 28901, strain 1035236001, GCA_020045005.1 and SAMN21475425. `data/catalog/ncbi_genbank-0023.jsonl.gz:12331` is Salmonella enterica subsp. enterica serovar Hadar taxid 149385, isolate MS160169, GCA_025080355.1 and SAMEA103523668.
- `data/catalog/allthebacteria.tsv.xz:66147` is Salmonella serovar Hadar, ERR1865244, SAMEA103523668, ERZ3070647; row 569706 is Mycobacterium tuberculosis, ERR1035236, SAMEA3558769, ERZ3502599. Both have available FASTAs and PASS filters but neither identifies C54b. The Salmonella shared sample is not proof of genome equivalence.
- Candidate fields were read losslessly. The target was re-read byte-identical. Only this report was written for C54b; no YAML, history, mapping status, generated product, Git or GitHub mutation was made.

