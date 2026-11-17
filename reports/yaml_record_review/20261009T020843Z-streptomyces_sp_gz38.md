# YAML Record Review: Streptomyces sp. GZ38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz38.yaml`
- Started UTC: 2026-10-09T02:05:42Z
- Finished UTC: 2026-10-09T02:08:43Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036523`: species rank, Bacteria, parent `NCBITaxon:2593676`, ten root-first ancestors, code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one exact target YAML and no previous target report. Laribacter clone filenames containing FLHGZ38 and LHGZ38 are not this taxon. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz38.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz38.yaml --out /private/tmp/streptomycesGZ38-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, lineage, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1412, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not independent alignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused checks do not prove corpus reproduction. Embedded history was inspected; no separate target history artifact was found in the ignored-inclusive inventory. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036523&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036523) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. An unnamed strain-associated species-rank taxon is not necessarily a formally described species. Exact grounding identifies this NCBI concept, not a nearest named species or another GZ38 isolate.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222523`: identity, parent, rank, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32067`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15030`: identifier/slug.
- `curation/seed_scope.tsv:322770`: admission date/reason matching the event.

One `NAME` attestation counts a source name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` is a represented BacDive count, not a denial of the strain designation.

Exact Nuccore query `txid1036523[Organism:noexp]` returned only UID 334361403. Complete [JF806658.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806658.1) XML was read, including references, all features and sequence. This 1412-base 16S marker is partial at both ends. Its four source qualifiers identify Streptomyces sp. GZ38, genomic DNA, strain GZ38 and taxon 1036523. Only source and rRNA features occur. No host, isolation-source, geographic, deposit or assembly qualifier is supplied.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. This is a marker, not a genome or phenotype assay.

Inspected [Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares GZ38 with Streptomyces carpaticus at 99.72%, with negative PKS-I/PKS-II/NRPS PCR screens. Its asterisk denotes tree inclusion. Neither species reassignment nor universal biosynthetic incapacity follows. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. The study connection is plausible, not an explicit GenBank publication link.

The extra native row `data/catalog/ncbi_genbank-0042.jsonl.gz:40970` was read in full. It is Pseudomonas aeruginosa GZ38, taxid 287, GCA_046480205.1, SAMN33717506, PRJNA891673 and WGS JARIZY000000000.1. Its shared strain label does not link that genome to this Streptomyces record.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are correctly unasserted without explicit evidence chains. An external 16S marker does not require an invented BacDive entry.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036523, word-bounded GZ38 and slug; expansion added JF806658 and word-bounded UID 334361403. Both returned the same four fully inspected rows: three own taxonomy/name/scope rows and the excluded Pseudomonas genome. Five SOURCE.json files were fully parsed separately with each term set without matches; history filenames were independently inventoried. These are bounded absence checks, not universal claims.

Genus-constrained `GZ38[All Fields] AND Streptomyces[Organism]` returned only the own marker, not an audit of all 24 unfiltered GZ38 hits. Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. The first PubMed query returned 6153 broad results while reporting GZ38 missing; it was not accepted as strain-specific evidence. Corrected `GZ38[All Fields] AND Streptomyces[All Fields]` and `JF806658[All Fields]` each returned zero with phrase-not-found diagnostics. Exact-accession web search returned no results; label search recovered the separately inspected primary paper. Indexed misses do not prove literature or genome absence.

iModulonDB was not applicable to the stored claims: no gene, regulator or expression assertion and no identified strain/dataset match. It was not run; this is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported genome, species reassignment or phenotype is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to incorporate nearest-species comparisons, unlinked genomes or overgeneralized negative PCR results.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment needs explicit strain/accession/deposit linkage and original paper visual verification. Relevant table text, headings and footnote were inspected; the original PDF/figure was not visually verified. No full experiment audit or independent sequence alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036523`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, marker and relevant primary text were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `fd5473330c77493225d0dac21bfee11316babc5f47a0809bd4c8d61c46318c8b`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
