# YAML Record Review: Burkholderia sp. BSNF2(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf2_12.yaml`
- Started UTC: 2026-10-10T07:09:00Z
- Finished UTC: 2026-10-10T07:11:31Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1037598`, Burkholderia sp. BSNF2(12). It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future corrections. Generated YAML is read-only.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf2_12.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf2_12.yaml --out /private/tmp/taxonmech-bsnf212-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique identifier/slug, scope reason, and seed-event wording. These checks do not replace corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or causal claims. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222813` agrees on ID, exact label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every root-first ancestor label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037598&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037598), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037598) agree. All 74 parsed browser text lines were read. EFetch omits root from ancestry; Datasets includes it. Datasets omits an assembly count, not evidence of zero assemblies. A strain-qualified marker is compatible with a species-ranked placeholder and does not establish formal nomenclature or a culture deposit.

The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32449` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15366` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323028` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. Read-only review does not promote status.

## Evidence

The source attestation counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate or unculturability.

Exact Nucleotide search `txid1037598[Organism:exp]` returned one UID, `345019042`. Complete [GenBank annotation JF779791.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779791.1) joins the exact organism, strain BSNF2(12), and `taxon:1037598`. It describes a 450-base 16S rRNA fragment incomplete at both ends, with explicit isolation annotation for non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `77c17e10af92c85a02a9e76046e1d662abaca7862df6f8c1c8ab1705ea514606`. This marker is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The sequence cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study in Soil Biology and Biochemistry 43(11):2275-2282. The complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Article full text and BSNF2(12)-specific assay outcomes were not verified. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred from the citation, cohort, genus, or neighboring accession.

All four non-target catalog rows were read completely, including the compressed TSV:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7608` is Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 14T0053, `GCA_010375985.1`, `SAMN12576342`, `PRJNA560345`, `JAAGIN000000000.1`. Its matching field is assembly name `ASM1037598v1`.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12443` is Salmonella enterica subsp. enterica serovar Stanleyville, taxid 286782/species 28901, strain `1037598`, `GCA_015711395.1`, `SAMN16972246`, `PRJNA248792`, `AAXMEI000000000.1`. A numeric strain designation is not a target taxon join.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41462` is Acinetobacter baumannii, taxid 470, strain AB24, isolate 10UC180072622, `GCA_050714255.1`, `SAMN41037598`, `PRJNA514245`, `DBIYQD000000000.1`. The match is inside its BioSample; PMID 30286803 is not target evidence.
- `data/catalog/allthebacteria.tsv.xz:1248371` concerns Salmonella enterica subsp. enterica serovar Poona, with PASS filters and available FASTA, sample `SAMN06621940`, analysis `ERZ5095078`, run `SRR5366174`. The numeric match is inside SeqKit sum `seqkit.v0.1_DLS_k0_3943ee991d15bb2187631037598f5d07`, not an identity field.

None establishes a target genome, culture deposit, synonym, or extra attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and punctuation/space/hyphen variants. An expanded pass added `JF779791`, `soilbio.2011.07.010`, and `S003807171100280X`. Both returned seven lines: own backbone, scope, scientific name, and four unrelated entries above. Ignored and compressed files were included. No additional target assertion, strain/genome association, or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed; none matched. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism web search supplied taxonomy-tree leads; accession search returned no result. Search snippets supported no scientific claim.

Optional slots need not be filled without source support and no causal graph is required. iModulonDB is not applicable because this record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the taxonomy/name-only assertions. Unverified isolate-level assays and unavailable article full text limit enrichment research but are not unsupported recorded claims.

## Recommended Edits

None required. Preserve BSNF2(12) and the explicit non-fertilized context in future enrichment; keep partial markers outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, resolve BSNF2(12)/JF779791 explicitly, and verify assay conditions/results. Require an explicit source chain for any genome or culture-deposit association. After authorized input changes, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Full primary taxonomy API responses, browser text, and sequence annotation were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Earlier access attempts for the shared article found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML rather than PDF; those failed routes were not retried per isolate. No login, paid access, or article full-text reading occurred.

YAML SHA-256: `4d73d99f975e5ae658e951ecf6a8f0df7ddd5a2460ff21d1702b81f2edbccc1e`. Only this new report was written for the target. Maintained inputs, generated YAML, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
