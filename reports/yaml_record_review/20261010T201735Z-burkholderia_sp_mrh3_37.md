# YAML Record Review: Burkholderia sp. MRh3(37)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_37.yaml`
- Started UTC: 2026-10-10T20:15:05Z
- Finished UTC: 2026-10-10T20:17:35Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRh3(37), `NCBITaxon:1037622`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained source inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_37.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_37.yaml --out /private/tmp/taxonmech-mrh337-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222837` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037622&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037622), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037622) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32473` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15392` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323052` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037622[Organism:exp]` returned one UID, 345019025. Complete [GenBank annotation JF779774.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779774.1) explicitly joins organism, strain MRh3(37), and taxon 1037622. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `6331e2dc0f0f55202d7abdaa312d80339adbc59b606eae48d48feee247b57f58`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly inspected for this review, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings from 80 isolates do not establish individual MRh3(37) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 22 non-target native matches were read completely:

- Seven rows describe Campylobacter concisus AAUH-2010376221, taxid 199, SAMN08200444, paired GCA_002912895.1/GCF_002912895.1, and POZX00000000.1 (unversioned POZX00000000 in BV-BRC/GOLD). Addresses: `data/bvbrc/bvbrc-0010.jsonl.gz:30759`; `data/catalog/gtdb_genomes-0000.jsonl.gz:46651`; `data/catalog/ncbi_genbank-0002.jsonl.gz:15523`; `data/catalog/ncbi_refseq-0001.jsonl.gz:36275`; `data/gold/analyses.jsonl.gz:212449`; `data/gold/organisms.jsonl.gz:342980`; `data/gold/projects.jsonl.gz:265132`. BV-BRC genome is 199.789; GOLD joins Ga0352598/Gp0377551/Go0493556, with IMG 8038145678. GTDB labels RS_GCF_002912895.1 as representative Campylobacter_A concisus_G; its PRJNA224116 RefSeq project differs from PRJNA395841 on the GenBank/BV-BRC/GOLD surfaces. RefSeq has annotation absent from the GenBank row. PMID 29382867 belongs to these unrelated records. The match is inside strain designation, not taxon identity.
- Four rows describe Sulfolobus tengchongensis HGQ25, archaeal taxid 207809, SAMN41037622, paired GCA_038747945.1/GCF_038747945.1. Addresses: `data/bvbrc/bvbrc-0012.jsonl.gz:37142`; `data/catalog/gtdb_genomes-0017.jsonl.gz:33945`; `data/catalog/ncbi_genbank-0035.jsonl.gz:46418`; `data/catalog/ncbi_refseq-0006.jsonl.gz:1447`. BV-BRC genome 207809.13 lists CP152368/CP152369 and PRJNA1102941. GTDB instead assigns nonrepresentative GB_GCA_038747945.1 to Saccharolobus shibatae. GenBank uses PRJNA1102941; RefSeq uses PRJNA224116, with different annotation date/counts. These source differences are preserved, not reconciled into the target. The match is within BioSample.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12333` describes E. coli strain 1037622, taxid 562, GCA_015708425.1, PRJNA315192, SAMN16961270, and AAXMBU000000000.1, excluded from RefSeq as part of a large multi-isolate project. A bare numeric strain designation equal to this target's taxid is not an identity bridge.
- Ten AllTheBacteria rows match run-accession substrings. Each has scientific/current/prior Sylph name E. coli, r0.2 dataset, available FASTA, and passing assembly/Sylph/HQ filters. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992443 | SAMEA9849525 | ERR10376228 | ERZ25462436 |
| 992444 | SAMEA9849526 | ERR10376226 | ERZ25462445 |
| 992539 | SAMEA9849649 | ERR10376227 | ERZ25463070 |
| 992541 | SAMEA9849651 | ERR10376229 | ERZ25463085 |
| 992556 | SAMEA9849668 | ERR10376224 | ERZ25463199 |
| 992675 | SAMEA9849878 | ERR10376220 | ERZ25464021 |
| 992677 | SAMEA9849880 | ERR10376222 | ERZ25464040 |
| 992726 | SAMEA9849929 | ERR10376221 | ERZ25464470 |
| 992728 | SAMEA9849931 | ERR10376223 | ERZ25464496 |
| 992729 | SAMEA9849932 | ERR10376225 | ERZ25464505 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779774, the study DOI, and S003807171100280X. Both returned 25 lines: own backbone, scope, scientific name, and 22 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism web query returned NCBI genus/family tree listings; these were leads, not independent evidence or an exhaustive literature search.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(37)/JF779774 identity and its fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(37)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, native candidate rows, and requested HAL metadata/abstract were inspected. Earlier reviews of the shared study encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `1a03f6edc3b847d67d401853679b306f2e3cc170fde2eca665dac73d1be42251`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
