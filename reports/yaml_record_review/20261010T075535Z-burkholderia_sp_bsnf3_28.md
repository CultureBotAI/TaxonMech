# YAML Record Review: Burkholderia sp. BSNF3(28)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf3_28.yaml`
- Started UTC: 2026-10-10T07:51:47Z
- Finished UTC: 2026-10-10T07:55:35Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037606`, Burkholderia sp. BSNF3(28). This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf3_28.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf3_28.yaml --out /private/tmp/taxonmech-bsnf328-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, unique index, scope reason, and seed-event wording. This is not full corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222821` agrees on ID, label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037606&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037606), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037606) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count, not a statement of zero assemblies. The marker's strain qualifier is compatible with the species-ranked placeholder, not proof of formal nomenclature or a culture deposit.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32457` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15375` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323036` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate.

Exact Nucleotide search `txid1037606[Organism:exp]` returned one UID, 345019039. Complete [GenBank annotation JF779788.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779788.1) joins the exact organism, strain BSNF3(28), and taxon 1037606. It is a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `bc9bb21865e4308230dd738e39843ffec51ae0c96fc64c4f09646e2a5ff70cdc`. It is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), freshly inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The cohort abstract does not establish individual BSNF3(28) assays. Full text and isolate-specific results were not verified; no mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 17 non-target native rows were read completely:

- `data/bvbrc/bvbrc-0000.jsonl.gz:2923` and `data/catalog/ncbi_genbank-0031.jsonl.gz:37629` describe Pseudomonas sp. HR96, taxid 1027966, GCA_034059295.1/GCF_034059295.1, BV-BRC 1027966.3, SAMN38194383, and CP139141/CP139142/CP139143/CP139144. The numeric match is BioProject PRJNA1037606, not the target taxon.
- `data/catalog/gtdb_genomes-0017.jsonl.gz:34128` and `data/catalog/ncbi_genbank-0029.jsonl.gz:43340` describe MAG GCA_032123335.1, taxid 2250274, isolate MAG_440_bin-23, SAMN31710543, PRJNA891615, JAQBFN000000000.1. The match is total/ungapped length 1,037,606. GTDB retains the NCBI organism label Candidatus Micrarchaeota archaeon and assigns CAIKOA01 sp032123335, whereas the GenBank catalog labels the same taxid Microcaldota archaeon. This non-target source-label difference is not a conflict in BSNF3(28); PMID 36973336 is not its citation.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7612` is Francisella tularensis subsp. holarctica, taxid 119857/species 263, 14T0003, GCA_010376065.1, SAMN12576337, PRJNA560345, JAAGII000000000.1. The match is assembly name ASM1037606v1.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41509` is Acinetobacter baumannii, taxid 470, AB33/isolate 14UC170046428, GCA_050715195.1, SAMN41037606, PRJNA514245, DBIYRG000000000.1. The match is within BioSample; PMID 30286803 is not a target citation.
- Eleven AllTheBacteria rows have Escherichia coli in both scientific-name and Sylph fields, available FASTA, and passing assembly/Sylph/HQ filters. Full filter, SeqKit, and download fields were read. Ten r0.2 rows match run-accession substrings, as listed below; one 202408 incremental row matches a checksum.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992597 | SAMEA9849709 | ERR10376061 | ERZ25576370 |
| 992598 | SAMEA9849710 | ERR10376063 | ERZ25576379 |
| 992622 | SAMEA9849780 | ERR10376060 | ERZ25463641 |
| 992623 | SAMEA9849783 | ERR10376064 | ERZ25463653 |
| 992624 | SAMEA9849784 | ERR10376062 | ERZ25463655 |
| 992625 | SAMEA9849790 | ERR10376066 | ERZ25463664 |
| 992626 | SAMEA9849795 | ERR10376068 | ERZ25463672 |
| 992676 | SAMEA9849879 | ERR10376065 | ERZ25464031 |
| 992678 | SAMEA9849881 | ERR10376069 | ERZ25464049 |
| 992679 | SAMEA9849882 | ERR10376067 | ERZ25464059 |
| 2490290 | SAMN32104147 | SRR22571390 | ERZ26473894 |

Row 2490290 matches SeqKit sum `seqkit.v0.1_DLS_k0_aa3a9246e1037606c6a0d769417d969e`, not a taxon identifier or MD5 assertion. None of the 17 non-target rows establishes another target attestation, synonym, deposit, or genome.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, and space/punctuation/hyphen variants, bounding the terminal designation number. Expanded search added JF779788, soilbio.2011.07.010, and S003807171100280X. Both searches returned 20 lines: own backbone, scope, scientific name, and the 17 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism web search yielded taxonomy-tree leads; no snippets supported scientific claims.

Optional blanks do not establish missing required representation, and no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unavailable full text and unverified isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve exact BSNF3(28)/JF779788 identity and explicitly non-fertilized context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF3(28)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and candidate native rows were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Previous attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried per isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `6fcaf4751fb84ad63e06ae68f277a2a5b818c7b79ab0a07059b219a0fe28c73e`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
