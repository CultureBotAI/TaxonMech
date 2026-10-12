# YAML Record Review: Burkholderia sp. BSF2(13)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf2_13.yaml`
- Started UTC: 2026-10-10T06:29:02Z
- Finished UTC: 2026-10-10T06:31:34Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037589`, Burkholderia sp. BSF2(13). This is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes; generated YAML must not be hand-edited.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf2_13.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf2_13.yaml --out /private/tmp/taxonmech-bsf213-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, all lineage labels/ranks, code, synonyms, name attestation, unique path, scope reason, and seed-event wording. These are not full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222804` matches the ID, exact label, rank, parent, genetic code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The complete root-first lineage matches individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. Every label and rank agrees.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037589&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037589), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037589) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count; that is not evidence of zero assemblies. A strain-qualified sequence is compatible with a species-ranked placeholder but does not establish a formally named species or culture deposit. No inferred reclassification is warranted.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32440` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15357` uniquely resolves the identifier and slug. `curation/seed_scope.tsv:323019` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. No human review promotion is claimed.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Optional strain, nomenclature, and mapping sections agree with those inputs. Zero inventoried strains does not imply unculturability or absence of a biological isolate.

Exact live Nucleotide search `txid1037589[Organism:exp]` returned one UID, `345019014`. The complete [GenBank annotation JF779763.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779763.1) joins the exact organism, strain BSF2(13), and `taxon:1037589`. It is a 450-base partial 16S rRNA gene, incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `39679b6897caa09a6835091fa5198905237ef6d1eff076e89acf9567004de81f`. This marker is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux institutional address are not sampling metadata.

The annotation directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Freshly retrieved complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1) independently confirm the citation and DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract provides cohort context, not BSF2(13)'s assay result. Full text was not inspected. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was transferred from cohort findings, the title, genus, or nearby accessions.

All three non-target catalog hits were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:20466` concerns Salmonella enterica subsp. enterica serovar Typhimurium (`taxid 90371`, species 28901), strain `1037589`, `GCA_015874005.1`, `SAMN16970849`, `PRJNA248792`, `AAXRQQ000000000.1`.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41529` concerns Acinetobacter baumannii (`taxid 470`), strain AB15, isolate 10RC190001306, `GCA_050715595.1`, `SAMN41037589`, `PRJNA514245`, `DBIYRR000000000.1`.
- `data/catalog/ncbi_genbank-0051.jsonl.gz:19513` concerns Streptococcus pneumoniae (`taxid 1313`), isolate `1037589`, `GCA_055615075.1`, `SAMEA120831699`, `PRJNA514245`, `DBMUMI000000000.1`. PMID 30286803 on this and the Acinetobacter row is not a target citation.

The matches are other organisms' strain/isolate numerals or a BioSample substring. None supports a target assembly, deposit, synonym, or extra attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, source organism/designation, and parenthesis/space/hyphen variants. An expanded pass added `JF779763`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both returned six lines: own backbone, scope, scientific name, and three unrelated genome rows. Ignored and compressed files were included. No extra target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

Independently enumerated and fully parsed all five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact organism and accession web searches supplied taxonomy/near-name leads or no accession result; no search snippet was treated as scientific evidence. The directly cited paper's author deposit was inspected as above.

Optional literature/source enrichment does not require filling every optional slot or constructing a graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only assertions agree with inspected pinned and live sources. Unverified isolate-level assays and unavailable full text are review limitations, not defects in claims the record does not make.

## Recommended Edits

None required. Do not hand-edit generated YAML, append a curation event, or promote status. Future verified literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF2(13) and keep partial marker sequences outside genome counts.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and any isolate-level table, explicitly resolve BSF2(13)/JF779763, and verify assay conditions/results. A later genome/deposit association requires an explicit source chain. After authorized maintained-input edits, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

Direct taxonomy-browser retrieval succeeded and all 74 parsed text lines were read. HAL's public API supplied complete requested metadata and abstract. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML rather than PDF; those routes were not repeatedly retried. No authentication, paid access, or full-text reading occurred.

YAML SHA-256: `701500f1c57dfca0a82edc28b34d84cf0c42936d7fccc228b7d9a16b8d05c2c9`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
