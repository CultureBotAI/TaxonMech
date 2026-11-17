# YAML Record Review: Streptomyces sp. GZ39

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz39.yaml`
- Started UTC: 2026-10-09T02:09:56Z
- Finished UTC: 2026-10-09T02:12:41Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036524`: species rank, Bacteria, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no previous target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz39.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz39.yaml --out /private/tmp/streptomycesGZ39-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, lineage, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1406, submitted rRNA transcription equals DNA, no non-ACGT symbols. This checks annotation, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036524&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036524) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. An unnamed species-rank taxon need not be a formally described species. Exact grounding identifies this NCBI concept, not every GZ39 strain or a nearest species.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222524`: identity, parent, rank, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32068`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15031`: identifier/slug.
- `curation/seed_scope.tsv:322771`: admission date/reason matching the event.

One `NAME` attestation counts a source name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` is a represented BacDive count, not a denial of the strain designation.

Exact Nuccore query `txid1036524[Organism:noexp]` returned only UID 334361402. Complete [JF806657.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806657.1) XML was read, including references, all features and sequence. This 1406-base 16S marker is partial at both ends. Its four source qualifiers identify Streptomyces sp. GZ39, genomic DNA, strain GZ39 and taxon 1036524. Only source and rRNA features occur. No host, isolation-source, geographic, deposit or assembly qualifier is supplied.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. It is a marker, not a genome or phenotype assay.

Inspected [Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares GZ39 with Streptomyces celluloflavus at 99.93%, with PKS-I negative and PKS-II/NRPS positive. The asterisk denotes tree inclusion, not synonymy. PCR results do not establish a metabolite phenotype. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. The study link is plausible, not an explicit GenBank citation.

The inspected methods of the [2001 Mycobacterium PYR-1 dioxygenase paper](https://journals.asm.org/doi/full/10.1128/aem.67.8.3577-3585.2001) explicitly identify the GZ39 probe source as Comamonas testosteroni. This shared-label literature hit supplies no degradation-gene or phenotype evidence for Streptomyces sp. GZ39. The experimental study was not otherwise audited.

Two extra native rows were read in full: `data/catalog/ncbi_genbank-0063.jsonl.gz:30248` and `data/catalog/gtdb_genomes-0015.jsonl.gz:21280`. They concern metagenome-derived GCA_964557365.1, isolate SRP192927_co3_66, NCBI taxid 332614, SAMEA117290843 and PRJEB82487. NCBI labels it uncultured Pseudomonadales bacterium; GTDB places it in Patescibacteriota, species CAZKMY01 sp964557365. Their total genome length 1036524 caused the search match. Neither classification connects the genome to this Streptomyces; resolving the off-target source disagreement is outside this review.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit source chains. An external marker does not require inventing a BacDive entry.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036524, word-bounded GZ39 and slug; expansion added JF806657 and word-bounded UID 334361402. Both returned the same five fully inspected rows: three own taxonomy/name/scope rows and two excluded genome rows. Five SOURCE.json files were fully parsed separately with each term set without matches; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

Genus-constrained `GZ39[All Fields] AND Streptomyces[Organism]` returned only the own marker, not an audit of all 28 unfiltered GZ39 hits. Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed searches `GZ39[All Fields] AND Streptomyces[All Fields]` and `JF806657[All Fields]` returned zero; the latter reports a missing phrase. Exact-accession web search returned no result. Label-search primary hits were inspected separately. Indexed misses do not prove universal literature or genome absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported genome, species reassignment or phenotype is asserted. Off-target evidence does not create a defect in this exact-taxonomy record.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not join other genera's same-label strains, numeric genome-size matches or nearest-species comparisons by hand-editing generated output.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment requires explicit strain/accession/deposit linkage and original paper visual verification. Relevant seagrass table text, headings and footnote were inspected; the original PDF/figure was not visually verified. The separate dioxygenase paper was inspected for source identity in primary HTML; no full assay audit or independent sequence alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036524`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, marker and relevant primary contexts were inspected; no neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `a130399b10456095a799d2ccffaa1851a5d3c0b529012b5dce5085e702d21744`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
