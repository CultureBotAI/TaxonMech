# YAML Record Review: Methylobacterium sp. C4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c4.yaml`
- Started UTC: 2026-10-06T17:11:10Z
- Finished UTC: 2026-10-06T17:16:43Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035233`, Methylobacterium sp. C4, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT and mapping status SEEDED. It asserts ten root-first ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or causal graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14445`; scope is `curation/seed_scope.tsv:322229`. Seeded fields are generated from maintained inventories and seeding logic. HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` across the resumed review.

## Validation

The local review skill, curation guidance, checklist, repository instructions, documentation, schema and authoritative commands were inspected at this revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c4.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c4.yaml --out /private/tmp/mc4-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read, including after resumption, and contains only its header.
- Bounded structured comparisons confirmed identity, every ancestor, path/scope rows, attestation and event text. These manual comparisons are not the corpus reproduction gate.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. The reproduction gate has no target selector. No corpus-wide reproducibility or reference-integrity claim is made.
- `just validate-products` was not run: its configuration targets curator-added graph grounding, absent here, and skips NCBITaxon. Taxonomic identifiers were checked against pinned and live NCBI.
- Ignored-inclusive content/path searches found no target external history artifact. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; none covers Methylobacterium/Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221954` supports the exact taxid, label, species rank, parent, code 11, empty synonym fields and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31422`. Exact type-material, merged-ID and dropped-record scans found no target rows.

The complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035233&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035233) agree. Each stored ancestor label and rank matches the pinned chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML LineageEx omits root; Datasets includes it.

EXACT identifies this NCBI concept, not a validly published binomial or a culture deposit. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), previously fully inspected and searched specifically for C4, supplies no target identity bridge. Genus nomenclature and properties do not transfer to the isolate. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole NCBITAXON attestation matches its identifier, label, count 1, unit NAME and snapshot. It counts a source-name assertion, not strains or genomes. The `seed_from_sources` event at 2026-09-13T17:54:04Z, action SEEDED_FROM_SOURCES, matches the one-source scope reason.

No exact target row occurs in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone taxon has C4's taxid as its parent. Zero BacDive records agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; this is not a claim that C4 was never cultivated.

The exact live query `txid1035233[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300730. Full [FR869829.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869829.1), excluding bases, was inspected: a 1333-nt partial 16S rRNA gene, strain C4, explicit `taxon:1035233`, host Cerastium holosteoides and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA does not make this marker a genome assembly.

The marker cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The bibliography and complete abstract fetched during the immediately preceding TS68 review were re-read for C4. The study compares phyllosphere communities across hosts, locations and land-use conditions; the abstract does not establish C4-specific growth, phenotype or collection locality. C4's host comes from its own marker metadata. Full text and supplements were not inspected.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 23 rows, all read in full: three genuine taxonomy/name/scope rows and 20 unrelated numeric matches detailed below. Five discovered `SOURCE.json` files were separately parsed; no target value matched. Ignored-independent history filename enumeration found no target artifact.

The expanded query `(Methylobacterium|Methylorubrum).*\bC[- _]?4\b|\bC[- _]?4\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants were search leads, not asserted aliases. The FR869829 accession search found no row in the same roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

`normalize_culture_identifier` returned empty for C4, C-4 and C 4. No eligible own-deposit or owning BacDive strain bridge was established. No required missing strain/genome link was demonstrated. The marker is optional identity evidence, not a supported same-deposit StrainInfo link. Empty optional definition, evidence and graph slots need not be populated without supported claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertions and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full text.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require C4's own eligible whole culture accession and supported source chain before adding strain/genome links. StrainInfo sequences must explicitly name the matched SI-DP. GOLD must resolve a consistent own-organism/project/analysis chain. ATB requires exact existing BioSample evidence and an eligible available FASTA. Keep taxon, strain, deposit, sample, project, marker and assembly identities separate; a shared sample is not genome equivalence.

After an authorized maintained-input change, run target schema/strict validation and relevant join tests, then `just verify-corpus` and `just qc`. Inspect full text or supplements before asserting isolate-specific growth, phenotype or locality.

## Additional Notes

- Four excluded Lactobacillus gasseri rows identify taxid 1596, strain 1001217st1_D2_RTP21277_210401, GCA/GCF_040925165.1, BV-BRC 1596.1051 and SAMN41035233: `data/bvbrc/bvbrc-0004.jsonl.gz:16795`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20862`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20008`, `data/catalog/gtdb_genomes-0001.jsonl.gz:45383`.
- Five native Sinomicrobium pectinilyticum rows identify taxid 1084421, strain 5DNS001, GCA/GCF_003725735.1, BV-BRC 1084421.4 and SAMN10352333: `data/bvbrc/bvbrc-0000.jsonl.gz:8786`, `data/catalog/ncbi_genbank-0002.jsonl.gz:46818`, `data/catalog/ncbi_refseq-0002.jsonl.gz:5851`, `data/catalog/gtdb_genomes-0004.jsonl.gz:18730`, `data/gold/projects.jsonl.gz:364102`. The GOLD row is Gp0504389, Go0552107, PRJNA503099.
- Two transformed Sinomicrobium BIOSAMPLE assertions, `data/raw/strain_related_records.tsv:264034` and `data/raw/strain_related_records.tsv:264035`, attach SAMN10352333 to `kgmicrobe.strain:bacdive_168890`, taxid 1084421, matched deposit `kgmicrobe.strain:KCTC-23776`. BV-BRC supplies KCTC:23776; GOLD supplies KCTC 23776 and the explicit Gp0504389/Go0552107 chain. These valid deposit links belong to another taxon and cannot establish C4 identity.
- Six GOLD sediment-community projects at `data/gold/projects.jsonl.gz:376163`, `:376164`, `:376165`, `:376166`, `:376167` and `:376168` are Gp0518927 through Gp0518932, respectively, with SAMN10352334 through SAMN10352339 and PRJNA503098. Their own organism-ID fields are empty. They describe Lake Taihu sediment communities, not a C4 isolate or eligible own culture; no strain/genome chain is inferred.
- Two excluded archaeal rows identify Halomicrobium sp. HArcht3-1, taxid 1679067, GCA/GCF_058933345.1, SAMN61035233: `data/catalog/ncbi_refseq-0009.jsonl.gz:2056` and `data/catalog/ncbi_genbank-0054.jsonl.gz:28344`.
- `data/catalog/allthebacteria.tsv.xz:569703` is Mycobacterium tuberculosis, ERR1035233, SAMEA3558766, ERZ3502590. Its available FASTA and PASS filters do not identify C4.
- All candidate fields were inspected losslessly. No unrelated strain, sample or genome was transferred. The target was re-read byte-identical before reporting. Only this new report was written; no YAML, history, status, generated product, Git or GitHub mutation was made.

