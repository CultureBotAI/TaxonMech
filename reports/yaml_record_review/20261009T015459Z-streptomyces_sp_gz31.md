# YAML Record Review: Streptomyces sp. GZ31

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz31.yaml`
- Started UTC: 2026-10-09T01:50:33Z
- Finished UTC: 2026-10-09T01:54:59Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036521`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It contains zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one exact target YAML and no prior target report. Four additional filename matches contain longer SGZ31-prefixed designations in Pelorhabdus, Microbacterium or Jatrophihabitans; they are not the requested identifier/slug. The generated file is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz31.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz31.yaml --out /private/tmp/streptomycesGZ31-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched complete backbone/ancestor rows, lineage, attestation, PATHS, scope and seed-event wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared and actual length 1411, submitted rRNA transcription equals DNA, no non-ACGT symbols. This checks submitted annotation, not independent alignment or species identity.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. Embedded history was inspected; ignored-inclusive inventory found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036521&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036521) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching ancestor labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Live EFetch has no other names, and pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated taxon does not establish a formally described species. Exact grounding identifies this NCBI concept, not every isolate designated GZ31 or a nearest named species.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222521`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32065`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15028`: identifier/slug.
- `curation/seed_scope.tsv:322768`: admission date/reason matching the event.

The attestation counts one `NAME`, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Schema semantics make `strain_count: 0` a represented BacDive count, not a denial of the strain designation.

Exact Nuccore query `txid1036521[Organism:noexp]` returned only UID 334361405. Complete [JF806660.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806660.1) XML, including both references, all features and sequence, was read. This 1411-base 16S marker is partial at both ends. Source qualifiers explicitly name Streptomyces sp. GZ31, genomic DNA, strain GZ31 and taxon 1036521. They supply no host, isolation-source, geographic, culture-deposit or assembly qualifier. Only source and rRNA features occur.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No DOI or PMID is supplied. This marker is not a genome or phenotype assay; missing qualifiers cannot be inherited from other accessions.

Inspected [Wu et al. (2012) Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) compares GZ31 with Streptomyces corchorusii, 99.50%, with all three PKS-I/PKS-II/NRPS PCR screens positive. Its asterisk denotes tree inclusion, not synonymy or phenotype proof. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. The strain/study connection is plausible, not an explicit GenBank citation link.

The broader query `"GZ31"[All Fields] AND Streptomyces[Organism]` returned two UIDs: the target marker and 1966352208. Complete [MW534685.1](https://www.ncbi.nlm.nih.gov/nuccore/MW534685.1) XML was therefore also read, including references, comment, features and 1282-base sequence. It is a 2021 partial 16S submission by Backer, under generic Streptomyces sp. taxon 1931, with strain GZ31, isolation-source rhizosphere soil and host Black pepper. Its direct-submission address is in Kerala, India. The assembly-method comment describes marker processing, not a genome assembly accession.

The associated [2021 primary paper, Table 6](https://www.auctoresonline.org/uploads/articles/1624601606Plant_growth_promoting_actinobacteria_from_rhizosphere_soils_of_black_pepper_in_Wayanad.pdf), DOI 10.31579/2766-2314/031, maps MW534685 to Ptd-A, Streptomyces sp. from Puttad. Its methods describe black-pepper rhizosphere sampling in Wayanad. Neither inspected source establishes identity with JF806660.1 or taxon 1036521. The shared GZ31 designation is insufficient to import host, habitat, plant-growth assays or a Ptd-A alias into this record. No independent sequence alignment or isolate-equivalence claim was made.

Two extra local rows were read in full: `data/catalog/ncbi_genbank-0017.jsonl.gz:38721` and `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:42895`. They concern Escherichia coli GZ31, taxid 562, GCA_019366705.1 and historical suppressed GCF_019366705.1, BioSample SAMN17183408, with projects PRJNA688628 and PRJNA224116 respectively. They are excluded: a shared strain designation does not connect their genome to this Streptomyces.

## Completeness

Complete enough for the supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit evidence chains. The external marker does not require an invented BacDive strain. Prospective enrichment needs an appropriate maintained model/input and claim-level identity linkage.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036521, word-bounded GZ31 and slug. First expansion added JF806660 and word-bounded UID 334361405; a second added MW534685 and word-bounded UID 1966352208. All three searches returned the same five fully inspected rows: three own taxonomy/name/scope rows and two excluded E. coli genome rows. Five SOURCE.json files were fully parsed separately with each term set without a match; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed queries for GZ31 with Streptomyces and for JF806660 returned zero with quoted-phrase warnings. The own-accession web query returned no result; MW534685 search recovered the separately inspected 2021 study. The genus-constrained Nuccore result is not an audit of all 35 unfiltered GZ31 hits. These indexed misses do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported species reassignment, genome or phenotype is asserted. Unlinked same-label sequences are not evidence of a defect in the current exact-taxonomy record.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to join the 2021 isolate, E. coli genome or nearest-species comparisons.

## Follow-up Checks

No corrective follow-up is needed for current claims. Before any optional enrichment, resolve explicit strain/accession/deposit identity and inspect original paper visuals. The 2012 author-hosted table text, headings and footnote were inspected; its original PDF/figure was not visually verified. The 2021 publisher PDF text and matching author-hosted Table 6 text were inspected for accession linkage. Local PyMuPDF was unavailable in the repo environment; no rendered-image verification, full experiment audit or sequence-based equivalence test is claimed.

After any authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036521`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this independent review. Its own complete YAML, source candidates, live taxonomy, both marker records and relevant primary-source contexts were inspected; no neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `84276cd442203f02d21f9f81078632a98f489b3176c15d7b16233a26ec86ff58`. Only this new report was written for the target. YAML, sources, history, mapping status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
