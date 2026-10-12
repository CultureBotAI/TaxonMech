# YAML Record Review: Burkholderia sp. BSNF1(13)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf1_13.yaml`
- Started UTC: 2026-10-10T07:00:28Z
- Finished UTC: 2026-10-10T07:03:02Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037596`, Burkholderia sp. BSNF1(13). The record carries species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own any future correction. Generated taxon YAML is read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf1_13.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf1_13.yaml --out /private/tmp/taxonmech-bsnf113-20261010-validation.tsv --workers 1`: one file, zero errors; the inspected output TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, name attestation, unique identifier/slug, scope reason, and seed-event wording. These do not replace corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or causal claims. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222811` matches the exact ID, label, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The root-first chain matches individual backbone rows for every label/rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037596&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037596), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037596) agree. All 74 parsed browser text lines were inspected. EFetch omits root from ancestry while Datasets includes it. Datasets omits an assembly count, which is not evidence of zero assemblies. The strain-qualified marker is compatible with a species-ranked placeholder and does not establish formal nomenclature or a culture deposit.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32447` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15364` uniquely resolves the identifier/slug. `curation/seed_scope.tsv:323026` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. No human-review status promotion is claimed.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional strain, nomenclature, and mapping sections are correctly empty relative to those inputs. Zero inventoried strains does not imply absence of the biological isolate or unculturability.

Exact Nucleotide search `txid1037596[Organism:exp]` returned one UID, `345019048`. Complete [GenBank annotation JF779797.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779797.1) joins the exact organism, strain BSNF1(13), and `taxon:1037596`. It contains a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. The non-fertilized qualifier is explicit, not inferred from the designation. Declared/actual length and A/C/G/T checks agree; lowercase sequence SHA-256 is `e3a10f9a2a94c48e6be7a3e4df972c45bd1a6c88728eb6734df8aec2178f6040`. This fragment is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is provided. The 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

GenBank cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The full article and BSNF1(13)-specific assay outcomes were not verified. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred from the citation, cohort, genus, or nearby accession.

All five non-target native catalog rows were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7607` is Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 14T0051, `GCA_010375965.1`, `SAMN12576341`, `PRJNA560345`, `JAAGIM000000000.1`. The match is its assembly name `ASM1037596v1`.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12396` is Salmonella enterica subsp. enterica serovar Oranienburg, taxid 28147/species 28901, strain `1037596`, `GCA_015710455.1`, `SAMN16972241`, `PRJNA248792`, `AAXMCT000000000.1`. The numeric strain designation is not this taxon identifier.
- `data/catalog/ncbi_genbank-0021.jsonl.gz:33093` and `data/catalog/gtdb_genomes-0006.jsonl.gz:40061` concern metagenome-derived Bacillota bacterium, taxid 1879010, isolate OH_HFB_57, `GCA_023407495.1`, `SAMN17045912`, `PRJNA682348`, `JAEYMA000000000.1`. GTDB places `GB_GCA_023407495.1` in Bacillota/Clostridia/Christensenellales, species UMGS1975 sp900546685. Both entries match genome length `1037596`, not taxonomy. Their fecal provenance and GTDB classification do not transfer to BSNF1(13).
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41459` is Acinetobacter baumannii, taxid 470, strain AB21, isolate 10UC170003129, `GCA_050714195.1`, `SAMN41037596`, `PRJNA514245`, `DBIYQB000000000.1`. The match is inside its BioSample; PMID 30286803 is not a target citation.

None establishes an additional target genome, culture deposit, synonym, or attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered the numeric ID, exact slug, organism/designation, and punctuation/space/hyphen variants. The expanded pass added `JF779797`, `soilbio.2011.07.010`, and `S003807171100280X`. Both returned eight lines: own backbone, scope, scientific name, and the five unrelated entries above. Ignored and compressed files were included. No further target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed; none matched. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. No Eukaryota contents were opened. Exact organism web search supplied taxonomy-tree leads, and accession search returned no result. Search snippets supported no scientific claim.

Optional enrichment does not require filling every optional field or constructing a causal graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the taxonomy/name-only assertions. Unverified isolate-level assays and unavailable article full text are limitations on enrichment, not unsupported recorded claims.

## Recommended Edits

None required. Preserve the BSNF1(13) designation and the explicitly non-fertilized isolation context if future evidence is curated. Keep partial markers outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, resolve BSNF1(13)/JF779797, and verify assay conditions/results. Any genome or culture-deposit link needs an explicit source chain. After authorized input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Full primary taxonomy API responses, browser text, and GenBank annotation were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Earlier access attempts for the shared article found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML instead of PDF; those failed routes were not retried per isolate. No login, paid access, or full-text reading occurred.

YAML SHA-256: `06b0fb0971609071b5175916b03c05f06843f376fb3447d363da38473c37a012`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
