# YAML Record Review: Streptomyces sp. KLBMP 03746

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03746.yaml`
- Started UTC: 2026-10-09T00:31:26Z
- Finished UTC: 2026-10-09T00:34:25Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036506`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03746.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03746.yaml --out /private/tmp/klbmp03746-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 682, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036506&retmode=xml) agrees with identifier, label, rank, parent, code and live ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036506) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222508`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32052`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15015`: identifier/slug.
- `curation/seed_scope.tsv:322755`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether a strain designation exists.

Exact Nuccore query `txid1036506[Organism:noexp]` returned UID 334303280. Complete [JF803756.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803756.1) XML, including both references, all source/rRNA features and sequence, explicitly names this taxon and KLBMP 03746. It is a 682-base partial 16S marker, partial at both ends. Its own source is leaf, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied.

The references describe an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, with no study PMID or DOI. The title does not demonstrate disease control by this strain. The marker is neither a genome nor a functional experiment; collection context applies to this accession. Other KLBMP strains' source qualifiers must not be substituted.

All 23 additional local candidates were read completely and excluded. Fifteen concern five Salmonella samples whose accessions contain 1036506. In this table, BV-BRC lines refer to `data/bvbrc/bvbrc-0017.jsonl.gz`, GenBank lines to `data/catalog/ncbi_genbank-0002.jsonl.gz`, and ATB lines to `data/catalog/allthebacteria.tsv.xz`.

| Sample | Strain / serovar | GenBank assembly | BV-BRC line | GenBank line | ATB line / analysis |
| --- | --- | --- | --- | --- | --- |
| SAMN10365060 | FSIS31801191 / Cerro | GCA_003787865.1 | 11596 | 49708 | 1505337 / ERZ9093859 |
| SAMN10365061 | FSIS31801192 / Thompson | GCA_003761045.1 | 10836 | 48378 | 1505338 / ERZ9093858 |
| SAMN10365062 | FSIS31801193 / Kentucky | GCA_003777245.1 | 11293 | 49180 | 1505339 / ERZ9093854 |
| SAMN10365063 | FSIS31801194 / Kentucky | GCA_003777265.1 | 11292 | 49181 | 1505340 / ERZ9093856 |
| SAMN10365069 | FSIS31801202 / Kentucky | GCA_003758325.1 | 10747 | 48242 | 1505346 / ERZ9093876 |

BV-BRC uses species taxid 28901 and project PRJNA242847. GenBank retains serovar taxids 340188, 600 and 192955, respectively; none is the target. Its assembly exclusions concern a large multi-isolate project. Species and serovar classifications were preserved, not flattened into an identity with Streptomyces.

Two complete GOLD project rows are also unrelated: `data/gold/projects.jsonl.gz:275008` names FSIS31801202, sample SAMN10365069, Gp0387534/Go0503222; line 275018 names FSIS31801192, sample SAMN10365061, Gp0387544/Go0503232. Both cite PRJNA242847. Project and organism IDs are not genome identifiers and provide no target chain.

Five additional ATB rows, `data/catalog/allthebacteria.tsv.xz` lines 1505341, 1505342, 1505343, 1505344 and 1505345, name Campylobacter coli, samples SAMN10365064 through SAMN10365068, respectively. Their analyses are ERZ9093855, ERZ9093857, ERZ9093853, ERZ9093872 and ERZ9093869; runs are SRR8146893, SRR8146894, SRR8146889, SRR8146899 and SRR8146890. Sylph labels them Campylobacter_D coli. The matching sample digits do not create target associations.

The final candidate, `data/catalog/allthebacteria.tsv.xz:150755`, names Streptococcus pneumoniae TIGR4, sample SAMEA110664933, run ERR10310960 and analysis ERZ25127078. Its match is within SeqKit sum `seqkit.v0.1_DLS_k0_9c995d10365062dd1ddb88aa203806a6`, not a taxon identifier. All eleven inspected ATB rows have assembly, HQ and sylph PASS and supplied FASTA URLs. Filters, runs, SeqKit sums and URLs were fully read; a SeqKit sum is not MD5 and a common sample does not prove genome equivalence. None supplies a target genome, sample, project, deposit or phenotype link.

Spaced/compact strain-name web searches returned broad NCBI listings. Queries for `"JF803756" OR "JF803756.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Snippets did not support the biological verdict; full source records did.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs should remain empty without explicit identity chains. External marker/source context does not require an invented BacDive entry or genome link.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants and, on expansion, JF803756 and UID 334303280. Both searches returned the same 26 rows: three own taxonomy/name/scope rows and 23 unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence statements are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03746"[All Fields] OR "JF803756"[All Fields]` returned zero with quoted-phrase warnings. Neither establishes universal genome or literature absence; figure/supplement mentions can escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and unrelated sample/checksum matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on sample or checksum substrings, equate strains by KLBMP prefix, transfer another organism's metadata or infer formal species/phenotype from the marker or study title.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional marker/source-context enrichment requires maintained inputs and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment must explicitly connect this strain to any proposed deposit, genome or experiment. Preserve this accession's leaf source and distinguish strain, sequence, sample, project and genome identities.

After an authorized input/seeder change, run a focused regression test, `just seed-canary NCBITaxon:1036506`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Local single-record review, checklist and ownership guidance governed this review. The target's own rows and accession were independently inspected. Before/after YAML SHA-256 was `acac6e24f33758b93f4d4446e3f243d0b9481120f4b247745b25ae2823455961`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
