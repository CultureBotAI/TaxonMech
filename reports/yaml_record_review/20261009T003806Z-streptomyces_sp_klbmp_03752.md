# YAML Record Review: Streptomyces sp. KLBMP 03752

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03752.yaml`
- Started UTC: 2026-10-09T00:35:46Z
- Finished UTC: 2026-10-09T00:38:06Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036507`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03752.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03752.yaml --out /private/tmp/klbmp03752-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 579, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036507&retmode=xml) agrees with identifier, label, rank, parent, code and live ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036507) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222509`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32053`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15016`: identifier/slug.
- `curation/seed_scope.tsv:322756`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether a strain designation exists.

Exact Nuccore query `txid1036507[Organism:noexp]` returned UID 334303303. Complete [JF803779.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803779.1) XML, including both references, all source/rRNA features and sequence, explicitly names this taxon and KLBMP 03752. It is a 579-base partial 16S marker, partial at both ends. Its own source is rhizosphere, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied.

The references describe an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, with no study PMID or DOI. The title does not demonstrate disease control by this strain. The marker is neither a genome nor a functional experiment; source context applies to this accession.

All 16 additional local candidates were read completely and excluded:

- Four describe Staphylococcus aureus taxid 1280, strain 47-073, GCA_010365075.1/GCF_010365075.1, ASM1036507v1, sample SAMN13948067 and WGS JAAFMC000000000.1: `data/bvbrc/bvbrc-0000.jsonl.gz:44394`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7078`, `data/catalog/ncbi_refseq-0002.jsonl.gz:41247` and `data/catalog/gtdb_genomes-0011.jsonl.gz:4351`. BV-BRC genome is 1280.25761; projects are PRJNA604020/PRJNA224116. GTDB source blood and USA: Texas are not target metadata. The matched assembly digits do not denote this Streptomyces.
- Four concern Salmonella enterica serovar Kentucky, strain FSIS31801204, sample SAMN10365071, GCA_003761525.1, WGS RMTF00000000.1 and project PRJNA242847: `data/bvbrc/bvbrc-0017.jsonl.gz:10854`, `data/catalog/ncbi_genbank-0002.jsonl.gz:48402`, `data/gold/projects.jsonl.gz:274941` and `data/catalog/allthebacteria.tsv.xz:1505348`. BV-BRC genome is 28901.5393; GenBank serovar taxid is 192955, species taxid 28901. GOLD gives Gp0387467/Go0503155. ATB gives run SRR8146911 and analysis ERZ9093877.
- Four concern Salmonella enterica serovar Thompson, strain FSIS31801203, sample SAMN10365070, GCA_003762485.1, WGS RMTX00000000.1 and project PRJNA242847: `data/bvbrc/bvbrc-0017.jsonl.gz:10894`, `data/catalog/ncbi_genbank-0002.jsonl.gz:48450`, `data/gold/projects.jsonl.gz:275010` and `data/catalog/allthebacteria.tsv.xz:1505347`. BV-BRC genome is 28901.5433; GenBank serovar taxid is 600, species taxid 28901. GOLD gives Gp0387536/Go0503224. ATB gives run SRR8146902 and analysis ERZ9093875.
- Three concern Listeria monocytogenes taxid 1639, strain PNUSAL004493, sample SAMN10365076, GCA_003787465.1, WGS ROZB00000000.1 and project PRJNA212117: `data/bvbrc/bvbrc-0004.jsonl.gz:38808`, `data/catalog/ncbi_genbank-0002.jsonl.gz:49688` and `data/catalog/allthebacteria.tsv.xz:1505349`. BV-BRC genome is 1639.5825. ATB gives run SRR8147015 and analysis ERZ9093870.
- `data/catalog/ncbi_genbank-0064.jsonl.gz:15715` describes Christensenellales bacterium taxid 3083246, GCA_965309985.1, isolate S7491_NS37_NS81_metabat2_refined_bins.tsv.039, sample SAMEA118405731, project PRJEB89408 and WGS CBDMIP000000000.1. The matched value 1036507 is total genome size, not taxid. The source flags metagenome origin, fragmentation, large multi-isolate project and undefined genus; these do not implicate the target record.

Salmonella species/serovar labels and GOLD organism/project relationships were preserved. GOLD IDs are not genome identifiers. All three inspected ATB rows have assembly, HQ and sylph PASS and supplied FASTA URLs. Their source filters, run IDs, SeqKit sums and URLs were fully read; a SeqKit sum is not MD5 and a common sample does not prove identical assemblies. None of these candidates supplies a target strain-genome, sample, project, culture-deposit or phenotype link.

Spaced/compact strain-name web searches returned broad NCBI listings. Queries for `"JF803779" OR "JF803779.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Snippets did not support the biological verdict; full source records did.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs should remain empty without explicit identity chains. External marker/source context does not require an invented BacDive entry or genome link.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants and, on expansion, JF803779 and UID 334303303. Both searches returned the same 19 rows: three own taxonomy/name/scope rows and 16 unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence statements are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03752"[All Fields] OR "JF803779"[All Fields]` returned zero with quoted-phrase warnings. Neither establishes universal genome or literature absence; figure/supplement mentions can escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and unrelated numeric matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on sample/accession substrings or genome length, equate strains by KLBMP prefix, transfer another organism's metadata or infer formal species/phenotype from the marker or study title.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional marker/source-context enrichment requires maintained inputs and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment must explicitly connect this strain to any proposed deposit, genome or experiment. Preserve this accession's rhizosphere source and distinguish strain, sequence, sample, project and genome identities.

After an authorized input/seeder change, run a focused regression test, `just seed-canary NCBITaxon:1036507`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Local single-record review, checklist and ownership guidance governed this review. The target's own rows and accession were independently inspected. Before/after YAML SHA-256 was `99de9335fb33887e72b939340b7090aab2925d9d8ed92eaa2a4b79aab5afcef7`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
