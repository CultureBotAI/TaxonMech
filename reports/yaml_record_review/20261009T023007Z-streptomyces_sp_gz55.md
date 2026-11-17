# YAML Record Review: Streptomyces sp. GZ55

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz55.yaml`
- Started UTC: 2026-10-09T02:26:50Z
- Finished UTC: 2026-10-09T02:30:07Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036528`: species rank, Bacteria, parent `NCBITaxon:2593676`, ten root-first ancestors, code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz55.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz55.yaml --out /private/tmp/streptomycesGZ55-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, lineage, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1402, submitted rRNA transcription equals DNA, no non-ACGT symbols. This checks annotation, not independent alignment or species identity.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036528&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036528) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated concept does not establish a formally described species. Exact grounding identifies this NCBI concept, not every isolate called GZ55 or a nearest named species.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222528`: identity, parent, rank, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32072`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15035`: identifier/slug.
- `curation/seed_scope.tsv:322775`: admission date/reason matching the event.

One `NAME` attestation counts a source name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not every strain designation in external sources.

Exact Nuccore query `txid1036528[Organism:noexp]` returned only UID 334361398. Complete [JF806653.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806653.1) XML was read, including references, all features and sequence. This 1402-base 16S marker is partial at both ends. Its four source qualifiers identify Streptomyces sp. GZ55, genomic DNA, strain GZ55 and taxon 1036528. Only source and rRNA features occur. No host, isolation-source, geographic, culture-deposit or assembly qualifier is supplied.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. It is a marker, not a genome or phenotype assay.

Inspected [Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares GZ55 with Streptomyces luteosporeus at 98.0%, with PKS-I negative and PKS-II/NRPS positive. The asterisk denotes tree inclusion; neither synonymy nor metabolite production follows. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) confirms DOI 10.5897/AJMR11.981. The accession-study connection is plausible, not explicitly cited in GenBank.

Two additional native rows were read in full: `data/catalog/ncbi_genbank-0017.jsonl.gz:38717` and `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:42891`. They concern Escherichia coli GZ55, taxid 562, GCA_019366625.1 and historical suppressed GCF_019366625.1, BioSample SAMN17183413 and WGS JAEOHU000000000.1. The GenBank and RefSeq projects are PRJNA688628 and PRJNA224116 respectively. A shared strain label is not an identity link across these organisms; neither genome belongs in this Streptomyces record on that basis.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit evidence chains. An external marker does not require inventing a BacDive strain.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036528, word-bounded GZ55 and slug; expansion added JF806653 and word-bounded UID 334361398. Both returned the same five fully inspected rows: three own taxonomy/name/scope rows and two excluded E. coli genome rows. Five SOURCE.json files were fully parsed separately with each term set without matches; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

Genus-constrained `GZ55[All Fields] AND Streptomyces[Organism]` returned only the own marker, not an audit of all 25 unfiltered GZ55 hits. Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed searches `GZ55[All Fields] AND Streptomyces[All Fields]` and `JF806653[All Fields]` returned zero with missing-phrase diagnostics. Exact-accession web search returned no result; label search found the separately inspected primary paper. Indexed misses do not prove universal literature or genome absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported genome, species reassignment or phenotype is asserted. Excluded same-label genomes do not create a defect in the exact-taxonomy record.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to incorporate E. coli genomes or nearest-species comparisons.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment requires explicit strain/accession/deposit linkage and original paper visual verification. Relevant table text, headings and footnote were inspected; the original PDF/figure was not visually verified. No full experiment audit or independent sequence alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036528`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, marker and relevant primary text were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `3efc0e5fcacc7c59f86fc9ba42306c790b0b85f74d20ad7d393caa2c47fd33c5`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
