# YAML Record Review: Streptomyces sp. GZ14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz14.yaml`
- Started UTC: 2026-10-09T01:32:38Z
- Finished UTC: 2026-10-09T01:38:36Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036518`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. The record contains zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional names, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. This generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz14.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz14.yaml --out /private/tmp/streptomycesGZ14-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched complete backbone/ancestor rows, lineage, attestation, PATHS, scope and seed-event wording. Seven supplementary raw inventories and the type-material, merged-ID and dropped tables were checked for exact target identifiers.
- Own marker consistency passed: declared and actual length 1416, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is an annotation check, not independent alignment or species inference.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused checks do not establish corpus reproduction. Embedded history was inspected; ignored-inclusive history inventory found no separate target artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036518&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036518) agree with the identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching ancestor labels/ranks while omitting root from its displayed lineage.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Pinned synonyms are empty and live EFetch has no other names. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated taxon does not establish a formally described species. `EXACT` identifies this NCBI concept, not a neighboring named species or every isolate called GZ14.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222518`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32062`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15025`: identifier/slug.
- `curation/seed_scope.tsv:322765`: admission date/reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact target scans returned no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw row. Schema semantics make `strain_count: 0` a represented BacDive count, not denial of a strain designation.

Exact Nuccore query `txid1036518[Organism:noexp]` returned only UID 334361408 after one retried HTTP 502. The genus-constrained alias query `"GZ14"[All Fields] AND Streptomyces[Organism]` returned the same one record. Complete [JF806663.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806663.1) XML, including all references, features and sequence, was read. It is a 1416-base partial 16S marker with both ends marked partial. Source qualifiers explicitly name Streptomyces sp. GZ14, genomic DNA, strain GZ14 and taxon 1036518. No host, geography, isolation-source, culture-deposit or assembly qualifier is supplied; only source and rRNA features occur.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No DOI or PMID is supplied. It is not a genome or phenotype experiment, and adjacent accessions cannot fill its missing qualifiers.

Inspected [Wu et al. (2012) Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) compares GZ14 with Streptomyces flocculus at 98.30% and reports positive PKS-I, PKS-II and NRPS PCR screens. Its asterisk denotes phylogenetic-tree inclusion. This is comparison/screening, not synonymy or demonstrated antimicrobial activity. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. Connection to the accession is plausible from strain/study context, not an explicit GenBank publication link.

All 22 off-target local candidates were read in full native form. Twenty-one belong to three distinct GZ14 genome identities:

| Excluded identity | Distinguishing identifiers | Inspected source rows |
| --- | --- | --- |
| Escherichia coli GZ14 | taxid 562; GCA/GCF_003292015.1; SAMN08148358 | GOLD organism 319014/project 231828/analysis 188412; BV-BRC shard 0023 row 33859; GTDB shard 0015 row 29798; GenBank shard 0002 row 29811; RefSeq shard 0001 row 45873 |
| Clostridioides difficile GZ14 | taxid 1496; GCA/GCF_003327375.1; SAMN09579890 | GOLD organism 338767/project 260747/analysis 201682; BV-BRC shard 0003 row 28241; GTDB shard 0001 row 40499; GenBank shard 0002 row 31351; historical RefSeq shard 0000 row 17337 |
| Streptococcus agalactiae serogroup III GZ14 | taxid 216495; GCA/GCF_001880605.1; SAMN05213959 | GOLD organism 382568/project 355131/analysis 282687; BV-BRC shard 0013 row 6830; GTDB shard 0005 row 15406; GenBank shard 0001 row 23859; RefSeq shard 0001 row 10061 |

The remaining candidate, `data/catalog/ncbi_genbank-0065.jsonl.gz:32538`, is uncultured archaeon MarMAG_072977, taxid 115547, GCA_978022395.1: its genome-size value 1036518 caused the numeric match. No excluded assembly, phenotype or provenance was transferred to the target.

A separate [Zhou et al. (2023) primary paper](https://pdfs.semanticscholar.org/ab52/a43a267209b485b8d15b9992236911e7db79.pdf), DOI 10.3390/agronomy13102500, lists lowercase gz14 in Table 3. Its methods concern newly isolated terrestrial-soil Streptomyces, with GZ denoting Guizhou; data are available on request. Inspected methods, table and data statement supply no link to JF806663.1. Treating that isolate's biocontrol result as this taxon's phenotype is unjustified. No such claim appears in the YAML.

## Completeness

Complete enough for the asserted taxonomy-seed claims. Optional nomenclature, culture deposits, genome links and graphs are appropriately unasserted without evidence chains. The external marker does not require inventing a BacDive entry. Prospective literature enrichment needs explicit identity linkage and an appropriate maintained model/input.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036518, word-bounded GZ14 and slug; expansion added JF806663 and word-bounded UID 334361408. Both searches found the same 25 rows: three own taxonomy/name/scope rows and the 22 excluded rows above. All were fully inspected. Numeric boundaries avoid substring matches, but cannot prevent a coincidentally equal genome size. Five SOURCE.json files were fully parsed separately, including expanded terms, without a target hit; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed searches for GZ14 with Streptomyces, and JF806663, returned zero; the accession query included a quoted-phrase warning. Strain/accession web searches were bounded leads, not proof of universal publication absence. The genus-constrained Nuccore result is not a review of all 494 unfiltered GZ14 hits across organisms.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with inspected pinned and live authorities. No unsupported reassignment, genome or phenotype is asserted; unlinked external candidates do not make the existing taxonomy record incorrect.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to add literature or collisions.

## Follow-up Checks

No corrective follow-up is required for current claims. Before optional enrichment, verify an explicit strain/accession/deposit chain and inspect original paper visuals. The 2012 author-hosted table text, headings and footnote were inspected; its original PDF was not visually verified. The 2023 paper's methods, Table 3 and data statement were read through PDF text; screenshot calls did not expose inspectable image content in this tool path, and local rendering was unavailable through system `pdftoppm`/`python3` PyMuPDF. No visual verification or supplementary-data audit is claimed. The MDPI page returned HTTP 429 and its author-hosted mirror failed; the primary PDF mirror was readable.

After any authorized maintained-input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036518`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this independent review. Its own complete YAML, source rows, live taxonomy, marker and paper row were inspected. No adjacent target's accession or verdict was inherited.

Before/after YAML SHA-256: `2422e851565f4a0504c01316119ec348f2aab674d7a109ee0b4ae88e45e7806e`. Only this new report was written for this target. YAML, sources, history, mapping status, generated pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
