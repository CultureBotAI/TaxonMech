# YAML Record Review: Burkholderia sp. BSF3(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf3_12.yaml`
- Started UTC: 2026-10-10T06:44:26Z
- Finished UTC: 2026-10-10T06:51:07Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1037593`, Burkholderia sp. BSF3(12), including a fresh read after interruption. It carries species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future corrections. Do not hand-edit generated YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf3_12.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf3_12.yaml --out /private/tmp/taxonmech-bsf312-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for the complete lineage, identity, synonyms, genetic code, attestation, unique identifier/slug, scope reason, and seed-event wording. These checks do not replace corpus reproduction.
- `just validate-products`: not applicable because there are no curator-added graph nodes or causal claims. Taxon references were checked directly; no separately documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222808` matches the identifier, label, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every ancestor label and rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037593&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037593), and the [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037593) agree. EFetch omits root from ancestry while Datasets includes it. Datasets omits an assembly count; this is not a zero-assembly result. The strain-qualified marker does not conflict with the species-ranked placeholder or establish a formally named species or deposited culture.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32444` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15361` uniquely resolves this identifier/slug. `curation/seed_scope.tsv:323023` supplies the reason reproduced in the 2026-09-13T17:54:04Z event. Read-only review does not promote `SEEDED` to human-reviewed status.

## Evidence

The attestation counts one NCBI `NAME`, not one strain, genome, publication, or assay. Structured scans found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections agree with those inputs. Zero inventoried strains does not imply absence of a biological isolate or unculturability.

Exact Nucleotide search `txid1037593[Organism:exp]` returned one UID, `345019009`. Complete [GenBank annotation JF779758.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779758.1), inspected again after resumption, explicitly joins the organism, strain BSF3(12), and `taxon:1037593`. It describes a 450-base 16S rRNA fragment incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Actual/declared lengths and A/C/G/T checks agree; lowercase sequence SHA-256 is `27dbecc610d03b269245746cef43d2cb7e368eca79d5477bd1c7807990bee7e0`. This is not a genome assembly. The record supplies no collection country/date, coordinates, or deposit qualifier; the 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

GenBank cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Fresh inspection of the [HAL deposit metadata and abstract](https://hal.science/hal-02916138v1) confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Full text was not inspected and no BSF3(12)-specific assay result was verified. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was transferred from the study cohort, genus, or neighboring accession.

All 15 non-target native catalog rows were read completely, including compressed TSV rows:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7606`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 14T0054, `GCA_010375935.1`, `SAMN12576343`, `PRJNA560345`, `JAAGIO000000000.1`. The numeric match is its assembly name `ASM1037593v1`.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12246`: Shigella flexneri, taxid 623, strain `1037593`, `GCA_015706635.1`, `SAMN16961265`, `PRJNA315192`, `AAXLZM000000000.1`. A shared numeric strain designation is not a taxon join.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41469`: Acinetobacter baumannii, taxid 470, strain AB19, isolate 10RC190008528, `GCA_050714395.1`, `SAMN41037593`, `PRJNA514245`, `DBIYQH000000000.1`. Its BioSample contains the number; PMID 30286803 is not a target citation.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:7777`: uncultured bacterium, taxid 77133, metagenome-derived isolate MarMAG_027948, `GCA_977591545.1`, `SAMEA120728535`, `PRJEB104710`, `CDUTUZ000000000.1`. Its genome length, not taxonomy, is `1037593`.
- `data/gold/analyses.jsonl.gz:437394`: Salmonella enterica enterica sv. Elisabethville 570817, analysis `Ga0653420`, project `Gp0811498`, IMG taxon `8103759317`, GenBank `AAHNPG000000000`, assembly `GCA_007286995.1`, empty organism GOLD ID. This is an unrelated IMG identifier substring.
- Ten `data/catalog/allthebacteria.tsv.xz` rows concern Salmonella enterica, with PASS filters and available FASTAs. Line 1716824 links `SAMN13162634` / `ERZ25668023` / `SRR10375934`; 1716825 links `SAMN13162635` / `ERZ25668033` / `SRR10375931`; 1716826 links `SAMN13162636` / `ERZ25668043` / `SRR10375933`; 1716828 links `SAMN13162638` / `ERZ25668065` / `SRR10375930`; 1716829 links `SAMN13162639` / `ERZ25668074` / `SRR10375938`; 1716830 links `SAMN13162640` / `ERZ25668083` / `SRR10375936`; 1716831 links `SAMN13162641` / `ERZ25668093` / `SRR10375937`; 1716834 links `SAMN13162644` / `ERZ25668123` / `SRR10375935`; 1716835 links `SAMN13162645` / `ERZ25668131` / `SRR10375932`; 1716847 links `SAMN13162659` / `ERZ25668250` / `SRR10375939`. Run substrings do not establish target identity.

None of these rows establishes a target genome, deposit, synonym, or additional attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns included numeric ID, exact slug, organism/designation, and parenthesis/space/hyphen variants. The expanded search included `JF779758`, `soilbio.2011.07.010`, and `S003807171100280X`. Both passes returned 18 lines: own backbone, scope, scientific name, and the 15 unrelated rows above. Ignored and compressed files were included; no extra target-linked assertion, genome/strain association, or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed; none matched the expanded pattern. Ignored-independent filename scans found the exact YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact organism web search supplied taxonomy and unrelated leads; accession search returned no result. Search snippets supported no scientific claim.

Optional source enrichment does not require filling all optional fields or inventing a causal graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only assertions agree with inspected pinned and live sources. Unverified isolate-specific assays and unavailable full text are limitations of enrichment research, not defects in claims this record does not make.

## Recommended Edits

None required. Preserve BSF3(12), the placeholder rank, and the name-only count. Do not hand-edit YAML, append history, or promote status. Verified future enrichment belongs in maintained source inputs or an explicitly supported curation overlay; extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules. Scope changes belong in `curation/seed_scope.tsv`. Keep partial markers outside genome counts.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, explicitly resolve BSF3(12)/JF779758, and verify assay conditions/results. Require an explicit source chain before assigning a genome or culture deposit. After authorized input changes, rerun schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Direct taxonomy-browser retrieval before interruption succeeded; all 74 parsed text lines were inspected. Taxonomy APIs and complete marker annotation were refreshed after resumption. HAL API metadata and abstract were freshly read. Earlier checks of the shared study encountered ScienceDirect 403 and an ISTEX redirect to institutional-authentication HTML instead of PDF; these failed routes were not repeatedly retried. No login, paid access, or full-text reading occurred.

YAML SHA-256: `ced33a3b9efffbc387f75dab873794c4dff3ea3d2047ad81d8c5a27885cccbae`. Only this new report was written for this target. Maintained inputs, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were left unchanged.
