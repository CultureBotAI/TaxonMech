# YAML Record Review: Streptomyces sp. KLBMP 03721

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_klbmp_03721.yaml`
- Started UTC: 2026-10-09T00:17:22Z
- Finished UTC: 2026-10-09T00:19:36Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036503`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_klbmp_03721.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_klbmp_03721.yaml --out /private/tmp/klbmp03721-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 681, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036503&retmode=xml) agrees with identifier, label, rank, parent, code and live ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036503) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222505`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32049`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15012`: identifier/slug.
- `curation/seed_scope.tsv:322752`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether a strain designation exists.

Exact Nuccore query `txid1036503[Organism:noexp]` returned UID 334303300. Complete [JF803776.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803776.1) XML, including both references, all source/rRNA features and sequence, explicitly names this taxon and KLBMP 03721. It is a 681-base partial 16S marker, partial at both ends. Its own source is rhizosphere, host Pinus massoniana, location China: Panzhihua. No culture-deposit qualifier, assembly cross-reference or CDS is supplied.

The references describe an unpublished pine-wilt biocontrol-screening study by Wang, Jiang and Qin and direct submission on 11-APR-2011, with no study PMID or DOI. The title does not demonstrate disease control by this strain. The marker is neither a genome nor a functional experiment; source context applies to this accession.

Five unrelated native candidates were read completely and excluded. Four describe Staphylococcus aureus taxid 1280, strain 48-075, genome GCA_010365035.1/GCF_010365035.1, assembly name ASM1036503v1, sample SAMN13948071 and WGS JAAFLY000000000.1:

- `data/bvbrc/bvbrc-0000.jsonl.gz:44396`: genome 1280.25763, project PRJNA604020.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7076`: GenBank assembly, project PRJNA604020.
- `data/catalog/ncbi_refseq-0002.jsonl.gz:41245`: paired RefSeq assembly, project PRJNA224116. The pair is marked identical, with separate annotation fields preserved.
- `data/catalog/gtdb_genomes-0002.jsonl.gz:9865`: RS_GCF_010365035.1, strain 48-075, skin source and USA: Texas.

Their matches are assembly-name/accession substrings, not target taxon identifiers. The fifth row, `data/catalog/gtdb_genomes-0009.jsonl.gz:49560`, describes RS_GCF_032079985.1/GCA_032079985.1, NCBI Pulveribacter sp. taxid 2678893, isolate CTOTU48475, sample SAMN29161140, project PRJNA224116 and WGS DAMATK000000000.1. Its matched value 1036503 is scaffold N50. GTDB classifies this metagenome-derived assembly as Melaminivora sp002434305; that source-specific disagreement is retained, not resolved as the target Streptomyces. None of these rows provides a target strain-genome, sample, project, deposit or phenotype link.

Spaced/compact strain-name web searches returned the own NCBI taxon page and broad NCBI listings. Queries for `"JF803776" OR "JF803776.1"` and the full strain with Streptomyces excluding NCBI domains returned no results. Snippets did not support the biological verdict; full taxonomy APIs did.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs should remain empty without explicit identity chains. External marker/source context does not require an invented BacDive entry or genome link.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug, strain variants and, on expansion, JF803776 and UID 334303300. Both searches returned the same eight rows: three own taxonomy/name/scope rows and five unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence statements are bounded to those roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed query `"KLBMP 03721"[All Fields] OR "JF803776"[All Fields]` returned zero with quoted-phrase warnings. Neither establishes universal genome or literature absence; figure/supplement mentions can escape indexed queries.

iModulonDB was not run: there is no asserted gene, regulator or expression claim and no covered strain/dataset was identified. The marker does not establish coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Sparse characterization and numerical matches do not invalidate the grounded seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on assembly-name substrings or metrics, equate strains by KLBMP prefix, transfer another organism's metadata or infer formal species/phenotype from the marker or study title.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional marker/source-context enrichment requires maintained inputs and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required. Future enrichment must explicitly connect this strain to any proposed deposit, genome or experiment. Preserve this accession's rhizosphere source and distinguish strain, sequence, sample, project and genome identities.

After an authorized input/seeder change, run a focused regression test, `just seed-canary NCBITaxon:1036503`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Local single-record review, checklist and ownership guidance governed this review. The target's own rows and accession were independently inspected. Before/after YAML SHA-256 was `bcbedfa791d9498678d23a14a65bc13bb51a0633314b1672a1955e35178ba700`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
