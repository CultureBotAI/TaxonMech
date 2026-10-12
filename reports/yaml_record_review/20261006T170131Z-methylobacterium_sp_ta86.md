# YAML Record Review: Methylobacterium sp. TA86

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_ta86.yaml`
- Started UTC: 2026-10-06T16:59:14Z
- Finished UTC: 2026-10-06T17:01:31Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` denotes `NCBITaxon:1035230`, Methylobacterium sp. TA86, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT, mapping status SEEDED. It contains ten ancestors, zero inventoried strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, taxonomy mappings, strain entries, genome links, definition, record-level evidence, discussions or causal graphs occur.

The unique path-lock row is `data/taxa/PATHS.tsv:14442`; scope is `curation/seed_scope.tsv:322226`. Generated fields are owned by maintained source inputs and seeding logic, not editable YAML. The reviewed revision is `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Local guidance, field checklist, schema and command recipes were inspected at the unchanged revision. Project commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_ta86.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_ta86.yaml --out /private/tmp/mta86-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read and contains only the header.
- Bounded structured comparisons passed for identity, full lineage, path/scope rows, attestation and seed-event text. These are manual source checks, not corpus reproduction.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates and global `just validate-history`. The inspected `scripts/verify_corpus.py` exposes only a full-corpus gate; `--max-diffs` limits displayed diffs, not verification scope. No invented target-only reproduction validator was substituted.
- `just validate-products` was not run: its configured OAK surface is curator-added graph grounding, absent here; NCBITaxon is excluded from OAK by `conf/id_label_targets.yaml`. Taxonomic identifiers were checked against NCBI directly.
- No target external history artifact was found in ignored-inclusive content/path searches, so no focused external history record was available to validate. No history or status change was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; no Methylobacterium/Methylorubrum dataset applies. This absence is not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221951` supports the exact identity, species rank, parent, code 11, empty synonym fields and snapshot 2026-09-13. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31419`. Exact scans of type-material, merged-ID and dropped-record tables returned no target rows.

The full current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035230&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035230) agree. Every stored ancestor label and rank matches the pinned root-first chain: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). XML omits root in LineageEx; Datasets includes it.

EXACT is grounding to this NCBI taxon, not valid nomenclature or a strain/deposit equivalence. The [LPSN genus record](https://lpsn.dsmz.de/genus/methylobacterium), previously fully inspected and specifically searched for TA86, supplies no target identity bridge. Genus-level name status and properties cannot be transferred. The legacy NCBI browser failed through the web tool; both authority APIs succeeded.

## Evidence

The sole attestation matches source NCBITAXON, exact identifier and label, count 1, unit NAME and snapshot note. One source-name assertion is not a genome or biological strain count. The `seed_from_sources` event at 2026-09-13T17:54:04Z, action SEEDED_FROM_SOURCES, exactly matches the one-source scope reason.

No exact target rows were found in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. There are no direct backbone children. Thus zero inventoried BacDive strains agrees with the seeder's own/subtree rule; it does not deny that TA86 was cultured.

The live exact query `txid1035230[Organism:noexp]` returned zero assemblies, with phrases-not-found/no-items diagnostics, and one nucleotide UID, 347300727. The full [FR869826.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869826.1), excluding bases, was read: a 1335-nt partial 16S rRNA gene, strain TA86, explicit `taxon:1035230`, host Trifolium repens, isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. The genomic-DNA qualifier describes the source molecule; this marker is not a genome.

The marker explicitly cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The current bibliography and complete abstract fetched earlier this session were re-read for TA86. They concern phyllosphere community comparisons across hosts, locations and land-use conditions, not named TA86-specific growth, phenotype or collection locality. The host comes from the target's own marker metadata. Full text and supplements were not inspected.

## Completeness

Ignored/compressed content was searched with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug yielded 19 rows. Every candidate was fully read: three genuine taxonomy/name/scope rows, plus 16 unrelated numeric matches detailed below. All five discovered `SOURCE.json` metadata files were separately parsed for target values, with no match; ignored-independent history path enumeration found no target artifact.

The same-root expanded query `(Methylobacterium|Methylorubrum).*\bTA[- _]?86\b|\bTA[- _]?86\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. These variants were leads, not established aliases. A follow-up FR869826 search found no rows in the same roots. These are bounded local and exact live-query results, not claims about every external resource.

`normalize_culture_identifier` returned empty for TA86, TA-86 and TA 86. No eligible whole culture deposit or owning strain bridge was established. The marker is optional identity evidence but supplies no owning BacDive strain or own-deposit StrainInfo link. Consequently no required missing strain/genome association is demonstrated, and optional definition, evidence and graph slots need not be invented.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the inspected assertions and bounded completeness checks. Unrun corpus gates and uninspected full text remain limitations, not established record defects.

## Recommended Edits

None required. Keep the generated YAML and SEEDED status unchanged.

Future supported strain/deposit/genome additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope changes belong in `curation/seed_scope.tsv`; upstream mapping fixes belong in kg-microbe. Do not patch generated YAML or pages.

## Follow-up Checks

Require the target's own eligible culture accession and a supported source chain before adding links. StrainInfo sequences must name that same SI-DP; GOLD must resolve a consistent own-organism/project/analysis chain; ATB must join an exact already-supported BioSample with an eligible available FASTA. The unrelated GOLD project below does not establish any TA86 culture match, so following its other analyses would not repair a target gap.

After an authorized maintained-input change, run target schema/strict validation and relevant regression tests, then `just verify-corpus` and `just qc`. Inspect full text/supplements before claiming isolate-specific phenotype or locality. Preserve the distinction among taxon, strain, deposit, sample, project, marker and assembly; shared samples do not establish genome equivalence.

## Additional Notes

- Four excluded rows are Lactobacillus gasseri taxid 1596, strain 1001285st1_E1_RTP21277_210401, GCA/GCF_040925225.1, BV-BRC 1596.1054, BioSample SAMN41035230: `data/catalog/ncbi_genbank-0037.jsonl.gz:20865`, `data/bvbrc/bvbrc-0004.jsonl.gz:16798`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20011`, `data/catalog/gtdb_genomes-0009.jsonl.gz:42853`.
- Five excluded rows concern Absicoccus porci YH-panp20 and BioSample SAMN10352300: `data/gold/projects.jsonl.gz:353625` (Gp0492673, Go0541823, PRJNA503000); `data/bvbrc/bvbrc-0014.jsonl.gz:30621` (genome 2486714.3, taxon_id 2486576, source genome name Clostridium sp. YH-panp20); `data/catalog/ncbi_genbank-0002.jsonl.gz:46802`; `data/catalog/ncbi_refseq-0002.jsonl.gz:5837`; and `data/catalog/gtdb_genomes-0011.jsonl.gz:1248` (GCA/GCF_003725415.1, NCBI taxid 2486576). These are not TA86; the opaque BV-BRC identifier prefix is not substituted for its explicit taxon_id.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6258` is Mycobacterium tuberculosis taxid 1773, genome 1773.18451, strain/run ERR1035230.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6450` is Campylobacter jejuni taxid 197, strain 214575, GCA_010352305.1, sample SAMN13326932.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35470` is Streptococcus pneumoniae taxid 1313, isolate 469, GCA_036051515.1, sample SAMN11116955, assembly name PDT001035230.1. Its publication is not target evidence.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:35095` is Pseudothioglobus singularis (SeqCode), taxid 1427364, GCA_982756975.1, sample SAMEA122249149; ungapped genome length 1035230 triggered the match.
- `data/catalog/ncbi_genbank-0053.jsonl.gz:47917` is Vibrio cholerae taxid 666, strain PNUSAV007788, GCA_058323055.1, sample SAMN61035230.
- `data/catalog/allthebacteria.tsv.xz:569700` is Mycobacterium tuberculosis, ERR1035230, SAMEA3558763, ERZ3502573. Row `data/catalog/allthebacteria.tsv.xz:2484507` is Salmonella enterica, SRR22450308, SAMN31931021, ERZ26590998, with 1035230 in its SeqKit sum. Both have available FASTAs and PASS filters, but neither has TA86 identity.
- All candidate source fields were inspected losslessly; no unrelated strain, sample, project or genome was transferred.
- The target was re-read and byte-identical before reporting. Only this new report was written; no YAML, history, status, generated product, Git or GitHub mutation was performed.

