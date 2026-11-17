# YAML Record Review: Streptomyces sp. KLBMP 03730

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03730.yaml`
- Started UTC: 2026-10-09T00:20:47Z
- Finished UTC: 2026-10-09T00:24:04Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036504`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03730.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03730.yaml --out /private/tmp/klbmp03730-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 676, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036504&retmode=xml) agrees with identifier, label, rank, parent, code and live ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036504) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222506`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32050`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15013`: identifier/slug.
- `curation/seed_scope.tsv:322753`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether a strain designation exists.

Exact Nuccore query `txid1036504[Organism:noexp]` returned UID 334303301. Complete [JF803777.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803777.1) XML, including both references, all source/rRNA features and sequence, explicitly names this taxon and KLBMP 03730. It is a 676-base partial 16S marker, partial at both ends. Its own source is rhizosphere, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied.

The references describe an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, with no study PMID or DOI. The title does not demonstrate disease control by this strain. The marker is neither a genome nor a functional experiment; source context applies to this accession.

Six unrelated native candidates were read completely and excluded. The digits 1036504 occur inside two Salmonella BioSample accessions, not as the target's taxon identifier:

- Sample SAMN10365048: `data/bvbrc/bvbrc-0017.jsonl.gz:11290` identifies Salmonella enterica taxid 28901, strain FSIS21822576, BV-BRC genome 28901.5830 and GCA_003777145.1. `data/catalog/ncbi_genbank-0002.jsonl.gz:49175` gives serovar Infantis taxid 595, species taxid 28901, the same strain, assembly PDT000402735.1, project PRJNA242847 and WGS ROIF00000000.1. `data/catalog/allthebacteria.tsv.xz:1505325` gives the same sample and serovar, run SRR8146895 and ENA analysis ERZ9093823.
- Sample SAMN10365049: `data/bvbrc/bvbrc-0017.jsonl.gz:11595` identifies Salmonella enterica taxid 28901, strain FSIS21822577, BV-BRC genome 28901.6126 and GCA_003787845.1. `data/catalog/ncbi_genbank-0002.jsonl.gz:49707` gives serovar Typhimurium taxid 90371, species taxid 28901, the same strain, assembly PDT000402743.1, project PRJNA242847 and WGS ROYZ00000000.1. `data/catalog/allthebacteria.tsv.xz:1505326` gives the same sample and serovar, run SRR8146903 and ENA analysis ERZ9093835.

Both ATB rows pass assembly, HQ and sylph filters, have provided FASTA URLs and retain their SeqKit sums. These source fields were read, not treated as MD5 checksums or proof of sequence equivalence. Shared sample links do not make the ATB and GenBank assemblies identical. BV-BRC's species-level and GenBank's serovar-level classifications were preserved. Neither sample supplies a target strain-genome, sample, project, culture-deposit or phenotype link.

Strain-name searches returned broad NCBI listings and an OUCI editorial lead. The full-strain search excluding NCBI also returned that lead; the separate `"JF803777" OR "JF803777.1"` web query returned no results. The [primary editorial](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.00944/full) was opened and its complete HTML text searched for `KLBMP|JF803777|03730`. The sole matched context was a reference naming Glutamicibacter halophytocola KLBMP 5180, not this strain. Neither the target accession nor 03730 occurred in that parsed text. No biological claim was transferred from the editorial or its cited organism. OUCI follow-up open/find returned internal errors; those errors were not treated as absence evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs should remain empty without explicit identity chains. External marker/source context does not require an invented BacDive entry or genome link.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants and, on expansion, JF803777 and UID 334303301. Both searches returned the same nine rows: three own taxonomy/name/scope rows and six unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence statements are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03730"[All Fields] OR "JF803777"[All Fields]` returned zero with quoted-phrase warnings. Neither establishes universal genome or literature absence; figure/supplement mentions can escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization, numerical sample matches and an unrelated literature lead do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on BioSample substrings, equate strains by KLBMP prefix, transfer another organism's metadata or infer formal species/phenotype from the marker or study title.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional marker/source-context enrichment requires maintained inputs and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment must explicitly connect this strain to any proposed deposit, genome or experiment. Preserve this accession's rhizosphere source and distinguish strain, sequence, sample, project and genome identities.

After an authorized input/seeder change, run a focused regression test, `just seed-canary NCBITaxon:1036504`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Local single-record review, checklist and ownership guidance governed this review. The target's own rows and accession were independently inspected. Before/after YAML SHA-256 was `9f54774ab658d847f67c92175604c9b52ffb202e62c5f91800b3e7a07d9adab5`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
