# YAML Record Review: Burkholderia sp. MRh1(1)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh1_1.yaml`
- Started UTC: 2026-10-10T08:21:06Z
- Finished UTC: 2026-10-10T08:25:00Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for Burkholderia sp. MRh1(1), `NCBITaxon:1037609`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; do not hand-edit generated YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh1_1.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh1_1.yaml --out /private/tmp/taxonmech-mrh11-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. This is not full corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222824` agrees on ID, label, species rank, parent, code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037609&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037609), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037609) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count, not a statement of zero assemblies. Exact grounding preserves NCBI's placeholder identity, not formal nomenclatural standing or a culture-deposit identity.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32460` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15378` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323039` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. Lineage remains NCBI's carried parent chain.

The broader designation search also matched Burkholderia sp. SaMRH11, `NCBITaxon:1181191`. Its complete rows at `data/raw/ncbitaxon_taxa.tsv:263750`, `data/catalog/ncbi_names-0006.jsonl.gz:31533`, and `curation/seed_scope.tsv:356245` identify a different taxon, not an MRh1(1) synonym. No identity merge was inferred from the overlapping character string.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. The empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide search `txid1037609[Organism:exp]` returned one UID, 345019075. Complete [GenBank annotation JF779824.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779824.1) explicitly joins organism, strain MRh1(1), and taxon 1037609. This is a 450-base 16S rRNA fragment incomplete at both ends, annotated from fertilized ectomycorrhizosphere in a beech forest. It is not a bulk-soil annotation. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `c4da6a7a7407c9ae84d0c8752e6b42b6f2f5c9938330f7ca6312c503025838d6`. This marker is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), freshly inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract describes 80 isolates from beech ectomycorrhizosphere and bulk soil under control and calcium-amended conditions. It does not establish individual MRh1(1) assay results. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 15 non-target native search matches were read completely: the three SaMRH11 rows above, three GenBank assembly rows, and nine AllTheBacteria rows.

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7614` is Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0110, GCA_010376095.1, SAMN12576334, PRJNA560345, and JAAGIF000000000.1. The match is assembly name ASM1037609v1.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:13343` is Salmonella enterica subsp. enterica serovar Enteritidis, taxid 149539/species 28901, GCA_015729485.1, SAMN16983215, PRJNA248792, and AAXMEU000000000.1. The match is strain name 1037609, not a taxonomy identifier.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41534` is Acinetobacter baumannii, taxid 470, strain AB26/isolate 10UC190036177, GCA_050715695.1, SAMN41037609, PRJNA514245, and DBIYRV000000000.1. The match is within BioSample; PMID 30286803 is not a target citation.
- Nine AllTheBacteria rows have Escherichia coli in scientific-name and Sylph fields, available FASTA, and passing assembly/Sylph/HQ filters. Complete dataset, SeqKit, filter, and download fields were read. Each numeric match is within a run accession.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992633 | SAMEA9849817 | ERR10376090 | ERZ25463742 |
| 992634 | SAMEA9849830 | ERR10376092 | ERZ25576465 |
| 992635 | SAMEA9849838 | ERR10376094 | ERZ25463754 |
| 992636 | SAMEA9849839 | ERR10376098 | ERZ25576476 |
| 992637 | SAMEA9849840 | ERR10376096 | ERZ25463767 |
| 992686 | SAMEA9849889 | ERR10376091 | ERZ25464125 |
| 992687 | SAMEA9849890 | ERR10376095 | ERZ25464134 |
| 992688 | SAMEA9849891 | ERR10376099 | ERZ25464144 |
| 992689 | SAMEA9849892 | ERR10376097 | ERZ25464152 |

None establishes another target attestation, synonym, deposit, or genome. Sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779824, the study DOI, and S003807171100280X. Both returned 18 lines: three own rows and 15 non-target rows described above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found this YAML and the separate SaMRH11 YAML, but no pre-existing target report/history filename. The separate taxon's YAML contents were not needed to classify its complete native identity rows. Eukaryota contents were not opened. Exact organism/accession web searches yielded taxonomy-tree leads, not evidence for additional isolate-level claims.

Optional blanks do not establish a missing required representation; no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting the record.

## Recommended Edits

None required. Preserve exact MRh1(1)/JF779824 identity and the fertilized ectomycorrhizosphere context in any later enrichment. Do not merge SaMRH11 or treat a partial marker as a genome. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect MRh1(1)-specific conditions/results. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and candidate native rows were inspected for this target. The shared study's requested HAL metadata and abstract were read earlier this turn. Previous attempts for that study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried for this isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `572300bc8d9f07d0d88c6877e0cf48cc13a7d91453798c2e98fcbd605c49f19b`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
