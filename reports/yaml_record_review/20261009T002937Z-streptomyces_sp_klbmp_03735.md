# YAML Record Review: Streptomyces sp. KLBMP 03735

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03735.yaml`
- Started UTC: 2026-10-09T00:26:45Z
- Finished UTC: 2026-10-09T00:29:37Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036505`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03735.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03735.yaml --out /private/tmp/klbmp03735-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 660, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036505&retmode=xml) agrees with identifier, label, rank, parent, code and live ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036505) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222507`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32051`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15014`: identifier/slug.
- `curation/seed_scope.tsv:322754`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether a strain designation exists.

Exact Nuccore query `txid1036505[Organism:noexp]` returned UID 334303302. Complete [JF803778.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803778.1) XML, including both references, all source/rRNA features and sequence, explicitly names this taxon and KLBMP 03735. It is a 660-base partial 16S marker, partial at both ends. Its own source is rhizosphere, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied.

The references describe an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, with no study PMID or DOI. The title does not demonstrate disease control by this strain. The marker is neither a genome nor a functional experiment; source context applies to this accession.

All 54 additional local candidates were read completely and excluded. Their matches are numerical substrings in other samples, assemblies or GTDB identifiers, not this target's taxon field.

Thirty rows concern ten Salmonella samples. In this table, BV-BRC lines refer to `data/bvbrc/bvbrc-0017.jsonl.gz`, GenBank lines to `data/catalog/ncbi_genbank-0002.jsonl.gz`, and ATB lines to `data/catalog/allthebacteria.tsv.xz`. All BV-BRC rows classify the organisms as Salmonella enterica taxid 28901 and cite PRJNA242847; GenBank preserves subspecies/serovar detail.

| Sample | Strain | GenBank assembly | BV-BRC line | GenBank line | ATB line / analysis |
| --- | --- | --- | --- | --- | --- |
| SAMN10365050 | FSIS21822578 | GCA_003762255.1 | 10883 | 48439 | 1505327 / ERZ9093824 |
| SAMN10365051 | FSIS21822579 | GCA_003762325.1 | 10886 | 48442 | 1505328 / ERZ9093830 |
| SAMN10365052 | FSIS21822580 | GCA_003762225.1 | 10882 | 48437 | 1505329 / ERZ9093832 |
| SAMN10365053 | FSIS21822581 | GCA_003758305.1 | 10746 | 48241 | 1505330 / ERZ9093836 |
| SAMN10365054 | FSIS21822582 | GCA_003762305.1 | 10885 | 48441 | 1505331 / ERZ9093833 |
| SAMN10365055 | FSIS21822583 | GCA_003746485.1 | 10391 | 47658 | 1505332 / ERZ9093834 |
| SAMN10365056 | FSIS21822584 | GCA_003777305.1 | 11295 | 49183 | 1505333 / ERZ9093842 |
| SAMN10365057 | FSIS31801188 | GCA_003757945.1 | 10730 | 48223 | 1505334 / NA |
| SAMN10365058 | FSIS31801189 | GCA_003757845.1 | 10726 | 48218 | 1505335 / ERZ9093860 |
| SAMN10365059 | FSIS31801190 | GCA_003787925.1 | 11598 | 49711 | 1505336 / ERZ9093851 |

All ten ATB rows have HQ/sylph PASS and supplied FASTA URLs. Nine have assembly-pipeline PASS; SAMN10365057 instead has `ENA_ASM_SUBMIT_ERR`, no ENA analysis, and comment `error_serovar_only_occur_once`. That row retains run SRR8146906, its SeqKit sum and FASTA URL. Missing ENA analysis is not by itself an unavailable FASTA, nor a target link. Run IDs, checksums and source filters were fully read; SeqKit sum is not MD5, and common samples do not prove identical assemblies.

Eight more matches are complete GOLD sequencing-project rows in `data/gold/projects.jsonl.gz`: lines 274929, 274944, 274973, 274983, 274985, 274986, 274987 and 275019. Their project/organism pairs are Gp0387455/Go0503143, Gp0387470/Go0503158, Gp0387499/Go0503187, Gp0387509/Go0503197, Gp0387511/Go0503199, Gp0387512/Go0503200, Gp0387513/Go0503201 and Gp0387545/Go0503233, respectively. They explicitly name the same Salmonella strains/samples and PRJNA242847, not Streptomyces. GOLD calls FSIS21822578 serovar Reading, while inspected GenBank/ATB rows use the broader subspecies label; those source labels were not silently collapsed. GOLD project and organism IDs are not genome identifiers.

Five candidates describe Pseudomonas aeruginosa taxid 287, strain Pae_CF67.12c, GCA_001036505.1/GCF_001036505.1, sample SAMN03566446 and WGS LEJO00000000.1: `data/bvbrc/bvbrc-0016.jsonl.gz:22214`, `data/catalog/ncbi_genbank-0000.jsonl.gz:36104`, `data/catalog/ncbi_refseq-0000.jsonl.gz:30506`, `data/catalog/gtdb_genomes-0013.jsonl.gz:21678` and `data/gold/analyses.jsonl.gz:101384`. BV-BRC genome is 287.1677; projects are PRJNA282164/PRJNA224116. GTDB supplies sputum and Canada: Toronto, which must not be transferred. GOLD analysis Ga0158605 explicitly names Pae_CF67.12c and Gp0189855, but has empty organism and IMG fields; its GenBank cross-reference does not supply a target chain.

Six candidates concern Rhodoferax sp. taxid 50421, Bin2_7, GCA_010365055.1/GCF_010365055.1, ASM1036505v1 and sample SAMN12810505: `data/bvbrc/bvbrc-0021.jsonl.gz:23375`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7077`, `data/catalog/ncbi_refseq-0002.jsonl.gz:41246`, `data/catalog/gtdb_genomes-0001.jsonl.gz:2834`, `data/raw/gtdb_species.tsv:154218` and `data/raw/gtdb_mappings.tsv:293439`. BV-BRC genome is 50421.26. GTDB uses Rhodoferax sp010365055 and source H2-incubated subglacial sediment, Antarctica; the raw crosswalk maps to NCBITaxon:50421 by `skos:broadMatch`, with one genome. Its metagenome-derived status and NCBI/GTDB classification differences are retained. None belongs to the target.

The final five candidates are also numerical accession matches:

- `data/catalog/ncbi_genbank-0037.jsonl.gz:25713`: Klebsiella pneumoniae taxid 573, zj01071, GCA_041036505.1, SAMN37542577, PRJNA1021041.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:27352`: Klebsiella pneumoniae taxid 573, metagenome isolate 191_191J_C_1, GCA_061036505.1, SAMN60704030, PRJNA1464738.
- `data/catalog/ncbi_genbank-0047.jsonl.gz:6786` and `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:39040`: Vibrio parahaemolyticus taxid 670, VP19070, GCA_051036505.1/GCF_051036505.1, SAMN46338742. GenBank is latest; the historical RefSeq row is suppressed with not-live date 2025-06-27. That status must not be mistaken for a current target genome.
- `data/catalog/ncbi_genbank-0019.jsonl.gz:19057`: Salmonella enterica serovar Typhimurium taxid 90371, RK_D66, GCA_021036505.1, SAMEA5867062, PRJNA514245. Its publication field is not evidence about this Streptomyces.

Spaced/compact strain-name web searches returned the own NCBI taxon page and broad NCBI listings. Queries for `"JF803778" OR "JF803778.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Snippets did not support the biological verdict; full source records did.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs should remain empty without explicit identity chains. External marker/source context does not require an invented BacDive entry or genome link.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants and, on expansion, JF803778 and UID 334303302. Both searches returned the same 57 rows: three own taxonomy/name/scope rows and 54 unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence statements are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03735"[All Fields] OR "JF803778"[All Fields]` returned zero with quoted-phrase warnings. Neither establishes universal genome or literature absence; figure/supplement mentions can escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and unrelated source matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on numeric substrings, equate strains by KLBMP prefix, transfer another organism's metadata or infer formal species/phenotype from the marker or study title.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional marker/source-context enrichment requires maintained inputs and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment must explicitly connect this strain to any proposed deposit, genome or experiment. Preserve this accession's rhizosphere source and distinguish strain, sequence, sample, project and genome identities.

After an authorized input/seeder change, run a focused regression test, `just seed-canary NCBITaxon:1036505`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Local single-record review, checklist and ownership guidance governed this review. The target's own rows and accession were independently inspected. Before/after YAML SHA-256 was `4e41f3ddd31b8d3ebba0f5e9156fd484943ddde6c2ef37cbcf38da29784d1eb2`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
