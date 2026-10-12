# YAML Record Review: Burkholderia sp. BSF1(20)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf1_20.yaml`
- Started UTC: 2026-10-10T06:18:26Z
- Finished UTC: 2026-10-10T06:20:36Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1037586`, Burkholderia sp. BSF1(20). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes. Do not hand-edit generated taxon YAML.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf1_20.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf1_20.yaml --out /private/tmp/taxonmech-bsf120-20261010-validation.tsv --workers 1`: one file, zero errors; the inspected TSV has only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, complete lineage labels/ranks, code, synonyms, attestation, unique path, scope reason, and seed-event wording. These do not prove full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222801` matches the ID, name, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The root-first lineage agrees with individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. All labels and ranks agree.

Complete live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037586&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037586), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037586) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count, not reports a zero. Species rank is compatible with a strain-qualified sequence but does not establish a formally named species or culture deposit. No inferred reclassification is warranted.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32437` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15354` uniquely resolves the identifier and slug; `curation/seed_scope.tsv:323016` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. The record does not claim human review promotion.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections agree with those inputs. Zero inventoried strains is not evidence of unculturability or absence of an isolate.

Exact live Nucleotide search `txid1037586[Organism:exp]` returned one UID, `345019007`. The complete [GenBank annotation JF779756.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779756.1) directly joins this organism, strain BSF1(20), and `taxon:1037586`. It is a 450-base partial 16S rRNA gene, incomplete at both ends, with an isolation-source qualifier identifying fertilized bulk soil from a beech forest. Actual/declared length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `f6659eec93a8b49b40691eba0ee9757eb2378d6093d8fdef1c79d1b5d0bd0797`. This is a marker, not a genome assembly. There is no collection country/date, coordinate, or deposit qualifier. The 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

The sequence cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1), retrieved and read earlier in this same turn, independently confirm the exact citation and DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). They provide cohort context, not an isolate-specific BSF1(20) result. Full text was not inspected. No mineral-weathering, iron-release, chitin-degradation, or plant-growth claim was transferred from the paper title, cohort, genus, or neighboring accession.

All nine additional catalog hits were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:12332` is Shigella flexneri (`taxid 623`), strain `1037586`, `GCA_015708355.1`, `SAMN16961326`, `PRJNA315192`, `AAXMBT000000000.1`. Its strain numeral is not this taxon ID.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41605` is Acinetobacter baumannii (`taxid 470`), strain AB10, isolate 10RC170001218, `GCA_050717115.1`, `SAMN41037586`, `PRJNA514245`, `DBIYUH000000000.1`. The number occurs within another BioSample.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17230` is Streptococcus pneumoniae (`taxid 1313`), isolate `1037586`, `GCA_058710405.1`, `SAMEA120831716`, `PRJNA514245`, `DBOTCF000000000.1`. PMID 30286803 on this and the Acinetobacter row is not a target citation.
- Five complete `data/catalog/allthebacteria.tsv.xz` rows concern Salmonella enterica. Line 1716817 links `SAMN13162590` / `ERZ25667952` / `SRR10375865`; 1716819 links `SAMN13162592` / `ERZ25667974` / `SRR10375861`; 1716820 links `SAMN13162593` / `ERZ25667982` / `SRR10375862`; 1716821 links `SAMN13162594` / `ERZ25667992` / `SRR10375864`; 1716822 links `SAMN13162595` / `ERZ25668002` / `SRR10375863`. All have PASS filters, but matching run substrings are not target identity evidence.
- Line 3192108 of that ATB catalog is Escherichia coli, `SAMN46759401`, `ERZ27226287`, `SRR32302118`. The match is embedded in SeqKit sum `seqkit.v0.1_DLS_k0_d28911037586f1fc0825f559f46e32ff`, not a taxonomic field.

None provides a target-linked genome, deposit, synonym, or additional attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation strings, and parenthesis/space/hyphen variants; an expanded pass added `JF779756`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both returned 12 lines: own backbone, scope, scientific name, and nine unrelated rows. Ignored and compressed files were included. No extra target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

Independently enumerated and fully parsed the five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found only the target YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact-name and accession web queries supplied no additional inspected target evidence; no snippet was used as support. The directly cited paper's deposit was read as described above.

Optional source/literature enrichment does not require filling every optional slot or adding a graph. iModulonDB is not applicable because this record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only record agrees with inspected pinned and live sources. Unverified isolate-level assays and unavailable full text are review limitations, not defects in claims the YAML does not make.

## Recommended Edits

None required. Do not hand-edit the generated YAML, add a history event, or promote status. Verified future literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF1(20) and keep partial markers outside genome counts.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and any isolate-level table, resolve BSF1(20)/JF779756 explicitly, and verify assay conditions/results. A later genome/deposit association requires its own explicit source chain. After authorized maintained-input edits, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

Direct browser retrieval succeeded and all 74 parsed text lines were read. The shared HAL API metadata/abstract were inspected earlier this turn. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML rather than PDF; those failed routes were not repeatedly retried. No authentication, paid access, or full-text inspection occurred.

YAML SHA-256: `611ac555db41695218b672b03887fb9d9637bc23052475ec24aeedd85d88948e`. Only this new report was written for this target. Maintained sources, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
