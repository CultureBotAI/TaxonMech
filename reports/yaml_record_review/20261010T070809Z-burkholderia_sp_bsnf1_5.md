# YAML Record Review: Burkholderia sp. BSNF1(5)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf1_5.yaml`
- Started UTC: 2026-10-10T07:05:35Z
- Finished UTC: 2026-10-10T07:08:09Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037597`, Burkholderia sp. BSNF1(5). It is a bacterial species-ranked placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes; generated taxon YAML is read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf1_5.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf1_5.yaml --out /private/tmp/taxonmech-bsnf15-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, name attestation, unique identifier/slug, scope reason, and seed-event wording. These do not replace corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or causal claims. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222812` matches the ID, label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every ancestor label/rank matches its own backbone row in root-first order: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037597&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037597), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037597) agree. All 74 parsed browser text lines were inspected. EFetch omits root from ancestry while Datasets includes it. Datasets omits an assembly count, not a statement of zero assemblies. A strain-qualified marker is compatible with a species-ranked placeholder and does not establish formal nomenclature or a culture deposit.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32448` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15365` uniquely resolves the identifier/slug. `curation/seed_scope.tsv:323027` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. No human-review promotion is claimed.

## Evidence

The source attestation counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections agree with those inputs. Zero inventoried strains does not imply no biological isolate or unculturability.

Exact Nucleotide search `txid1037597[Organism:exp]` returned one UID, `345019049`. Complete [GenBank annotation JF779798.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779798.1) explicitly joins the organism, strain BSNF1(5), and `taxon:1037597`. It describes a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. The non-fertilized qualifier is explicit rather than inferred from the designation. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `283f4e2b1153980f6577f35550b47df1798b360088c705b754740802941b97c1`. This is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not sampling metadata.

The sequence cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Fresh inspection of the complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1) confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Full article text and BSNF1(5)-specific assay results were not verified. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred from the citation, cohort, genus, or neighboring sequence.

All four non-target native catalog rows were read completely:

- `data/catalog/ncbi_genbank-0042.jsonl.gz:4948` is Chryseobacterium sp. HR92, taxid 3094839, strain HR92, complete genome `GCA_045689405.1`, paired `GCF_045689405.1`, `SAMN38194222`, and BioProject `PRJNA1037597`. Its complete BV-BRC counterpart at `data/bvbrc/bvbrc-0018.jsonl.gz:45803` is genome `3094839.3`, accession `CP139139`, with the same sample/project. The two project-number matches cannot establish target taxonomy or strain identity.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41461` is Acinetobacter baumannii, taxid 470, strain AB23, isolate 10RC170003478, `GCA_050714235.1`, `SAMN41037597`, `PRJNA514245`, `DBIYQC000000000.1`. The number matches inside its BioSample.
- `data/catalog/ncbi_genbank-0054.jsonl.gz:17224` is Streptococcus pneumoniae, taxid 1313, isolate `1037597`, `GCA_058710285.1`, `SAMEA120831697`, `PRJNA514245`, `DBOTCC000000000.1`. The numeric isolate designation is not a target taxon join. PMID 30286803 on this and the Acinetobacter row is not target evidence.

None establishes a target genome, culture deposit, synonym, or additional attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and punctuation/space/hyphen variants. The expanded pass added `JF779798`, `soilbio.2011.07.010`, and `S003807171100280X`. Both returned seven lines: own backbone, scope, scientific name, and four unrelated catalog entries. Ignored and compressed files were included. No additional target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism web search supplied taxonomy-tree leads; accession search returned no result. Search snippets supported no scientific claim.

Optional enrichment does not require filling every optional slot or inventing a causal graph. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the taxonomy/name-only assertions. Unverified isolate-specific assays and unavailable article full text are enrichment limitations, not unsupported recorded claims.

## Recommended Edits

None required. Preserve BSNF1(5) and its explicitly non-fertilized context in any future enrichment; keep partial markers outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, explicitly resolve BSNF1(5)/JF779798, and inspect assay conditions/results. Genome/deposit associations require an explicit source chain. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Full primary taxonomy API responses, browser text, marker annotation, and requested HAL metadata/abstract were inspected. Earlier access attempts for the same paper found ScienceDirect 403 and an ISTEX redirect to institutional-authentication HTML rather than PDF; those failed routes were not retried per isolate. No login, paid access, or full-text reading occurred.

YAML SHA-256: `7f99b0dccadcc1b2df83d7926bdad5eb5f7591b6693c6d63987b6c16ca2c6869`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
