# YAML Record Review: Streptomyces sp. GZ33

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz33.yaml`
- Started UTC: 2026-10-09T01:57:49Z
- Finished UTC: 2026-10-09T02:03:15Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036522`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It contains zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one exact target YAML and no prior target report. Another filename match, bacterium enrichment culture clone ALO1_GLFRUDD03GZ331, is a longer unrelated designation, not this identifier or slug. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz33.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz33.yaml --out /private/tmp/streptomycesGZ33-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, ancestor chain, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories and type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared and actual length 1410; submitted rRNA transcription equals DNA; no non-ACGT symbols. This is annotation consistency, not independent alignment or species inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused checks do not establish corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036522&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036522) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Live EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated taxon does not establish a formally described species. Exact grounding denotes this NCBI concept, not a nearest named species or any isolate sharing the label.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222522`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32066`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15029`: identifier and slug.
- `curation/seed_scope.tsv:322769`: admission date/reason matching the seed event.

The attestation counts one `NAME`, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries; it does not deny the strain designation.

Exact Nuccore query `txid1036522[Organism:noexp]` returned only UID 334361404. Complete [JF806659.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806659.1) XML was read, including references, all features and sequence. This is a 1410-base 16S marker partial at both ends. Its four source qualifiers identify Streptomyces sp. GZ33, genomic DNA, strain GZ33 and taxon 1036522. Only source and rRNA features occur; there is no host, isolation-source, geographic, deposit or assembly qualifier.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology. It supplies no DOI or PMID. A marker is not a genome or phenotype assay, and absent qualifiers must not be filled from neighboring accessions.

Inspected [Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), lists GZ33 against Streptomyces flocculus at 98.44%, with positive PKS-I/PKS-II/NRPS PCR screens. The asterisk denotes tree inclusion. These are not synonymy or metabolite-production evidence. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. The study connection is plausible, not an explicit GenBank publication link.

In [Park et al. (2012), PMID 22816309](https://pmc.ncbi.nlm.nih.gov/articles/PMC3678979/), the inspected collection/phylogeny and cultivation sections use GZ33 only as a reported 93% 16S comparator for the separate Chilean isolate CNY-325. Neither that isolate's sediment origin nor the paper's thienodolin results belong to GZ33. No independent alignment or chemistry audit was performed.

Three additional native catalog rows were read in full: `data/catalog/ncbi_refseq-0000.jsonl.gz:37427`, `data/catalog/gtdb_genomes-0009.jsonl.gz:16094` and `data/catalog/ncbi_genbank-0000.jsonl.gz:44590`. All concern Chlamydia trachomatis Swab6, taxid 813, GCA/GCF_001213045.1 and BioSample SAMEA901486. They matched because ungapped genome length is 1036522, not because their taxon matches. Exclude their genomes and environmental metadata from this Streptomyces record.

## Completeness

Complete enough for its supported taxonomy-seed claims. Empty optional nomenclature, deposits, genome links and graphs are appropriate without explicit source chains. An external marker does not require inventing a BacDive entry.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036522, word-bounded GZ33 and slug; expansion added JF806659 and word-bounded UID 334361404. Both returned the same six fully inspected rows: three own taxonomy/name/scope rows and three excluded Chlamydia rows. Five SOURCE.json files were fully parsed separately without a term match; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

The genus-constrained Nuccore query `GZ33[All Fields] AND Streptomyces[Organism]` returned only the own marker; it is not an audit of all 22 unfiltered GZ33 hits. Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. The GZ33/Streptomyces PubMed query returned zero with a quoted-phrase warning, despite the independently inspected full-text comparator paper. Label/accession web searches were supplementary leads, not proof of universal literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The record asserts no unsupported species reassignment, genome or phenotype. Literature enrichment opportunities do not invalidate these taxonomy-seed claims.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to join nearest-species comparisons, another isolate's assays or numeric genome-size collisions.

## Follow-up Checks

No corrective follow-up is needed for current claims. Before optional enrichment, establish explicit strain/accession/deposit linkage and inspect original paper visuals. The 2012 seagrass table text, column headings and footnote were inspected, but its original PDF/figure was not visually verified. The separate comparator paper was inspected as primary HTML text; no figure or full experimental audit is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036522`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this individual review. Its complete YAML, native candidates, live taxonomy, own marker and relevant primary-source contexts were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `8ad9bf9839adeaeb4464d86e38cd7a3ebf0bb95c4b18a9c655aeb90ea4873172`. Only this new report was written for the target. YAML, sources, history, mapping status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
