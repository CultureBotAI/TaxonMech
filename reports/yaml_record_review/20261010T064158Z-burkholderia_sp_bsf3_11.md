# YAML Record Review: Burkholderia sp. BSF3(11)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsf3_11.yaml`
- Started UTC: 2026-10-10T06:39:21Z
- Finished UTC: 2026-10-10T06:41:58Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1037592`, Burkholderia sp. BSF3(11). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and a seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes. Generated taxon YAML must not be hand-edited.

## Validation

Used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsf3_11.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsf3_11.yaml --out /private/tmp/taxonmech-bsf311-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique path, scope reason, and seed-event wording. These are not full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or ontology-grounded causal claims. No separately documented focused term/reference validator applies; taxon references were checked directly.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222807` matches the ID, exact label, species rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The full root-first lineage matches individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784. All labels and ranks agree.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037592&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037592), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037592) agree. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count, which is not evidence of zero assemblies. A strain-qualified sequence is compatible with a species-ranked placeholder; neither establishes a formally named species or culture-collection deposit. No inferred reclassification is warranted.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32443` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15360` uniquely resolves the identifier/slug; `curation/seed_scope.tsv:323022` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. No human review promotion is claimed.

## Evidence

The attestation correctly counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains does not imply unculturability or absence of a biological isolate.

Exact live Nucleotide search `txid1037592[Organism:exp]` returned one UID, `345019015`. The complete [GenBank annotation JF779764.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779764.1) directly joins the exact organism label, strain BSF3(11), and `taxon:1037592`. It describes a 450-base partial 16S rRNA gene, incomplete at both ends, annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase-sequence SHA-256 is `159fb3a7ca222d53c9347f40c8d6f9dad941e19601faff1e707f9c144622a7d9`. This marker is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

The sequence directly cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The [HAL author deposit](https://hal.science/hal-02916138v1), whose complete requested metadata and abstract were inspected earlier in this turn, confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). No BSF3(11)-specific assay result was verified; full text was not inspected. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred from the citation, cohort, genus, or neighboring accession.

All ten non-target native catalog rows were read completely, including the compressed TSV entries:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7605` is Francisella tularensis subsp. holarctica (`taxid 119857`, species 263), strain 14T0055, `GCA_010375925.1`, `SAMN12576344`, `PRJNA560345`, `JAAGIP000000000.1`. Its matching assembly name is `ASM1037592v1`.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45980` is Acinetobacter baumannii (`taxid 470`), strain AB18, isolate 10RC190006606, `GCA_050822125.1`, `SAMN41037592`, `PRJNA514245`, `DBJBBB000000000.1`. The number occurs inside its BioSample.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17227` is Streptococcus pneumoniae (`taxid 1313`), isolate `1037592`, `GCA_058710345.1`, `SAMEA120831700`, `PRJNA514245`, `DBOTCE000000000.1`. PMID 30286803 on this and the Acinetobacter row is not a target citation.
- Seven `data/catalog/allthebacteria.tsv.xz` rows all concern Salmonella enterica with PASS filters and available FASTAs. Line 1716827 links `SAMN13162637` / `ERZ25668055` / `SRR10375929`; 1716832 links `SAMN13162642` / `ERZ25668104` / `SRR10375928`; 1716833 links `SAMN13162643` / `ERZ25668113` / `SRR10375927`; 1716836 links `SAMN13162646` / `ERZ25668142` / `SRR10375923`; 1716837 links `SAMN13162647` / `ERZ25668152` / `SRR10375924`; 1716838 links `SAMN13162648` / `ERZ25668161` / `SRR10375925`; 1716839 links `SAMN13162649` / `ERZ25668172` / `SRR10375926`. The matching run substrings are not target identity evidence.

None establishes a target-linked genome, culture deposit, synonym, or extra attestation.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, source organism/designation, and parenthesis/space/hyphen variants. An expanded pass added `JF779764`, DOI suffix `soilbio.2011.07.010`, and publisher ID `S003807171100280X`. Both returned 13 lines: own backbone, scope, scientific name, and ten unrelated rows. Ignored and compressed files were included. No extra target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

Independently enumerated and fully parsed the five source `SOURCE.json` files for the expanded pattern; none matched. Ignored-independent filename scans found the exact YAML and no pre-existing target report/history filename. Eukaryota YAML contents were not opened. Exact organism and accession web queries supplied taxonomy/near-name leads or no accession result; no snippet supported a scientific claim. The directly cited study's author deposit was inspected as above.

Optional source/literature enrichment does not require filling every optional field or creating a causal graph. iModulonDB is not applicable because this record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The taxonomy/name-only assertions agree with inspected pinned and live sources. Unverified isolate-level assays and unavailable full text are review limitations, not defects in claims the record does not make.

## Recommended Edits

None required. Do not hand-edit generated YAML, append a history event, or promote status. Verified future literature/strain enrichment belongs in maintained source inputs or an explicitly supported curation overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Preserve BSF3(11) and keep partial markers outside genome counts.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, resolve BSF3(11)/JF779764 explicitly, and verify assay conditions/results. A future genome/deposit association requires an explicit source chain. After authorized maintained-input edits, rerun focused schema/strict/history validation and the documented dry run, seed canary, corpus reproduction, and full quality gates. Human sign-off is separately required for review-status promotion.

## Additional Notes

Direct taxonomy-browser retrieval succeeded and all 74 parsed text lines were read. The shared HAL metadata and abstract were inspected earlier this turn. Earlier shared-paper access checks found ScienceDirect 403 and an ISTEX redirect returning institutional-authentication HTML instead of PDF; those failed routes were not repeatedly retried. No login, paid access, or full-text reading occurred.

YAML SHA-256: `ba161defe608379510ec50df480ff945068a0b51fc184882647e22dbf888e798`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
