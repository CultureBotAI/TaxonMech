# YAML Record Review: Streptomyces sp. GZ57

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz57.yaml`
- Started UTC: 2026-10-09T02:35:42Z
- Finished UTC: 2026-10-09T02:39:19Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036529`: species rank, Bacteria, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It represents zero BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found this YAML and the separate `streptomyces_sp_gz57_2015.yaml`, but no prior target report. Both files were read completely to disambiguate their IDs. This review judges only 1036529, not the namesake 1607617. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_gz57.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_gz57.yaml --out /private/tmp/taxonmech-gz57-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, complete lineage, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker annotation consistency passed: declared/actual length 1414, submitted rRNA transcription equals DNA and no non-ACGT symbols. This is not an independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036529&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036529) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. No other names occur in EFetch; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated concept does not establish a formally described species. Exact grounding does not equate all isolates called GZ57.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222529`: identity, parent, rank, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32073`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15036`: identifier/slug.
- `curation/seed_scope.tsv:322776`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive records, not every external strain designation.

Exact Nuccore query `txid1036529[Organism:noexp]` returned only UID 334361397. Complete [JF806652.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806652.1) XML was read, including references, every feature and sequence. This 1414-base 16S marker is partial at both ends. Four source qualifiers identify Streptomyces sp. GZ57, genomic DNA, strain GZ57 and taxon 1036529. Only source and rRNA features occur; host, isolation-source, geography, culture-deposit and assembly qualifiers are not supplied.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. It is a marker, not a genome or phenotype assay.

[Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares GZ57 with Streptomyces levis at 99.36%, with all three PKS-I, PKS-II and NRPS screens positive. The asterisk denotes tree inclusion, not synonymy. Methods list accession range JF806641-JF806668, consistent with this marker. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) confirms DOI 10.5897/AJMR11.981. GenBank itself does not cite that DOI. Neither similarity nor screening establishes species reassignment or metabolite production.

The genus-constrained alias query also returned UID 752630692. Complete [KM979603.1](https://www.ncbi.nlm.nih.gov/nuccore/KM979603.1) XML identifies Streptomyces sp. GZ57(2015), taxon 1607617, a 1389-base partial 16S sequence, strain GZ57, leaf, Rosa chinensis and China: Yangling, Shannxi. Guo submitted it on 15-OCT-2014 from North West Agriculture and Forestry University. The distinct taxon, accession, submitter and source context do not establish identity with the 2011 target. Its Rosa and antimicrobial-study context must not transfer here. The separate local taxonomy/name/scope rows at `data/raw/ncbitaxon_taxa.tsv:415323`, `data/catalog/ncbi_names-0009.jsonl.gz:47144` and `curation/seed_scope.tsv:483321` were read in full.

Four further native rows were read completely and excluded:

- `data/catalog/ncbi_genbank-0049.jsonl.gz:480`: Klebsiella pneumoniae GZ_57, taxid 573, GCA_053067465.1, SAMN50315213, PRJNA1299787 and JBRQAR000000000.1.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:31791`: Clostridium perfringens GZ-57, taxid 1502, GCA_059011705.1, SAMN54296322, PRJNA1393274 and JBTGAC000000000.1.
- `data/catalog/ncbi_genbank-0064.jsonl.gz:23348` and `data/catalog/gtdb_genomes-0002.jsonl.gz:7425`: Pontimonas isolate AGTU_32_bin_31_permissive, NCBI taxid 2304492, GCA_965656395.1, SAMEA118800603, PRJEB90443 and CBFHKJ000000000.1. The matching number 1036529 is genome length, not the organism's taxid. GTDB calls it Pontimonas sp002172585.

## Completeness

Complete enough for supported taxonomy-seed claims. Empty optional nomenclature, deposits, genome links and graphs are appropriate without explicit evidence chains. An external marker does not require inventing a BacDive strain.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 1036529, label/slug and GZ57 with optional space, underscore or hyphen. Expansion added both marker accessions and word-bounded UIDs. Both scans returned the same ten fully inspected rows: three target, three namesake, and four excluded genome rows. Five SOURCE.json files were fully parsed separately for both term sets without matches; history filenames were independently inventoried. Absence statements are bounded to these roots and terms.

`GZ57[All Fields] AND Streptomyces[Organism]` returned the two fully inspected markers, not an audit of all 14 unfiltered GZ57 hits. Exact non-expanded Assembly query returned zero with missing-phrase/no-items diagnostics. PubMed queries `GZ57[All Fields] AND Streptomyces[All Fields]` and `JF806652[All Fields]` returned zero with missing-phrase diagnostics. Exact target-accession web search yielded no target result; label search located the independently inspected seagrass paper. Secondary thesis listings and a search hit involving KM979603 were not used as evidence about this target. Indexed misses do not prove universal literature or genome absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live sources. No unsupported namesake-derived host, genome, phenotype or species reassignment is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not merge the two GZ57 concepts by strain label or hand-edit generated output.

## Follow-up Checks

No corrective follow-up is needed for present claims. Optional enrichment requires an explicit strain/accession/deposit chain. Relevant primary table text, headings, methods and footnote were inspected, but the original PDF/figure was not visually verified. No full experiment audit or independent sequence alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036529`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, both full marker records and relevant primary text were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `7b4100bf881bf5eb8d7dc8bd8e00c469c6b360e82c1f021da2bda193cee76b0c`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
