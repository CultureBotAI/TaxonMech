# YAML Record Review: Burkholderia sp. BSF1(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf1_12.yaml`
- Started UTC: 2026-10-10T06:15:07Z
- Finished UTC: 2026-10-10T06:17:31Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037585`, Burkholderia sp. BSF1(12). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes; generated taxon YAML must not be hand-edited.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf1_12.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf1_12.yaml --out /private/tmp/taxonmech-bsf112-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, every lineage label/rank, code, synonyms, attestation, unique path, scope reason, and seed-event wording. They are bounded checks, not corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222800` matches the ID, exact name, species rank, parent, genetic code, and 2026-09-13 snapshot. Its exact/related/broad synonym and retirement fields are empty. The full root-first lineage agrees with individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. Every label and rank matches.

Complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037585&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037585), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037585) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count; that is not evidence of zero assemblies. A strain-qualified sequence is compatible with this species-ranked placeholder, but does not establish a formally named species, culture-collection deposit, or a different genus placement.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32436` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15353` uniquely resolves the identifier and slug; `curation/seed_scope.tsv:323015` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. The record does not claim human review promotion.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, paper, or assay. The seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories contain no own rows in the structured comparisons. Empty optional strain, nomenclature, and mapping sections agree with those inputs. Zero inventoried strains does not mean no isolate exists or that it is unculturable.

Exact live Nucleotide search `txid1037585[Organism:exp]` returned one UID, `345019002`. The complete [GenBank annotation JF779751.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779751.1) directly joins the exact organism, strain BSF1(12), and `taxon:1037585`. It describes a 450-base partial 16S rRNA gene, incomplete at both ends, with an isolation-source qualifier identifying fertilized bulk soil from a beech forest. Declared and actual length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `d277369aa7537544e43c894f50ad8f9eab7dc04e3e1227ec2ab8c69061d9f4fc`. This marker is not an assembly. The annotation supplies no collection country/date, coordinates, or deposit ID. The 5 April 2011 submission date and INRA Champenoux address are not sampling metadata.

The sequence directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Freshly retrieved complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1) independently confirm the citation and DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract gives cohort-level context, not BSF1(12)'s individual assay result. Full text was not inspected. No mineral-weathering, chitin-degradation, iron-release, or plant-growth phenotype was transferred from cohort results, genus, paper title, or nearby accessions.

All 14 other source-native search hits were read completely, including the compressed TSV row:

- Seven concern Citrobacter sp. BIDMC108 (`taxid 1686385`, `SAMN03280170`): `data/bvbrc/bvbrc-0005.jsonl.gz:15492`; `data/catalog/gtdb_genomes-0000.jsonl.gz:47229`; `data/catalog/ncbi_genbank-0000.jsonl.gz:36158`; `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:6280`; `data/catalog/ncbi_refseq-0000.jsonl.gz:30558`; `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:8510`; and `data/gold/analyses.jsonl.gz:58780`. Their matches arise from `GCA_001037585`/`GCF_001037585`, with current version .2 and historical .1; BV-BRC retains .1. GOLD `Ga0106764`, `Gp0130902`, IMG `2663763292` concern the same other organism. GTDB labels that genome Citrobacter portucalensis; neither its classification nor its assembly chain belongs to this target.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7603` is Francisella tularensis subsp. holarctica (`taxid 119857`, species 263), strain 14T0067, `GCA_010375855.1`, `SAMN12576345`; the match is `ASM1037585v1`.
- `data/catalog/ncbi_genbank-0019.jsonl.gz:19111` is Listeria monocytogenes (`taxid 1639`), isolate Lm-2014-35114, `GCA_021037585.1`, `SAMEA9563568`.
- `data/catalog/ncbi_genbank-0037.jsonl.gz:25767` is Klebsiella pneumoniae (`taxid 573`), strain zj21080, `GCA_041037585.1`, `SAMN37544746`.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45941` is Acinetobacter baumannii (`taxid 470`), strain AB1, isolate 10BC170004679, `GCA_050821385.1`, `SAMN41037585`.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17238` is Streptococcus pneumoniae (`taxid 1313`), isolate `1037585`, `GCA_058710565.1`, `SAMEA120831702`. The PMID 30286803 seen on this and other excluded genome rows is not a target citation.
- `data/gold/analyses.jsonl.gz:191194` concerns Brucella anthropi RH4WT86, `Ga0326522`, `Gp0348330`, `GCA_014138145.1`; the substring match is IMG taxon `2821037585`.
- `data/catalog/allthebacteria.tsv.xz:1716818` concerns Salmonella enterica, `SAMN13162591`, `ERZ25667963`, run `SRR10375859`, with PASS filters. The run substring does not establish a target association.

These numerical coincidences supply no target-linked genome, deposit, synonym, or extra attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, source name/designation, and parenthesis/space/hyphen variants. An expanded pass added `JF779751`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both passes returned 17 lines: own backbone, scope, name, and 14 unrelated rows. Ignored and compressed files were included; no extra target-linked assertion or strain/genome/history association was established on these bounded surfaces.

Independently enumerated and fully parsed all five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened.

Web queries covered the exact name, BSF1 designation, and JF779751. Near-name and general biological results were leads only; no snippet supplied an identity or trait claim. The directly cited paper's deposit was inspected as above. Optional context enrichment does not require filling every empty slot or creating a graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's taxonomy/name-only assertions agree with inspected pinned and live sources. Unverified isolate-level assay results are a review limitation, not a defect in claims the record does not make.

## Recommended Edits

None required. Do not hand-edit the generated YAML, add a curation event, or promote status. Future verified literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve the whole BSF1(12) designation and keep marker sequences outside genome counts.

## Follow-up Checks

Before adding a function, obtain the cited paper and isolate-level table, explicitly resolve BSF1(12)/JF779751, and verify assay conditions/results. Later culture-deposit or genome links require an explicit source chain. After authorized maintained-input changes, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off remains separate from this report.

## Additional Notes

The web reader failed on the taxonomy browser; direct retrieval succeeded and all 74 parsed text lines were read. HAL's public API succeeded. Earlier shared-paper checks found ScienceDirect 403 and an ISTEX redirect to institutional authentication, returning HTML instead of PDF; those failed routes were not repeated here. No paid access, authentication, or full-text reading occurred.

YAML SHA-256: `54bd8a4b4b384883b9e545d9b6a4625c19fb7c26dae8e7ed9f9ffde898c75943`. Only this new report was written for the target. Maintained sources, generated data, history, schema, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
