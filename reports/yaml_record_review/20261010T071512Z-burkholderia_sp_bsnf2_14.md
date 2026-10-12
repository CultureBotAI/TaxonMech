# YAML Record Review: Burkholderia sp. BSNF2(14)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf2_14.yaml`
- Started UTC: 2026-10-10T07:12:29Z
- Finished UTC: 2026-10-10T07:15:12Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037599`, Burkholderia sp. BSNF2(14). This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future fixes. Generated taxon YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf2_14.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf2_14.yaml --out /private/tmp/taxonmech-bsnf214-20261010-validation.tsv --workers 1`: one file, zero errors; output TSV was inspected and contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique ID/slug, scope reason, and seed-event wording. These are not full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or causal claims. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222814` agrees on ID, exact label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. The full root-first chain matches individual backbone rows for every label/rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037599&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037599), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037599) agree. All 74 parsed browser text lines were read. EFetch ancestry omits root while Datasets includes it. Datasets omits an assembly count, which is not evidence of zero assemblies. The marker's strain qualifier is compatible with the species-ranked placeholder; it does not establish formal nomenclature or a culture deposit.

The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32450` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15367` uniquely resolves this identifier/slug. `curation/seed_scope.tsv:323029` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. No status promotion is claimed.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate or unculturability.

Exact Nucleotide search `txid1037599[Organism:exp]` returned one UID, `345019046`. Complete [GenBank annotation JF779795.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779795.1) joins the exact organism, strain BSNF2(14), and `taxon:1037599`. It contains a 450-base 16S rRNA fragment incomplete at both ends, explicitly annotated from non-fertilized bulk soil in a beech forest. Actual/declared length and A/C/G/T checks passed; lowercase sequence SHA-256 is `310082c4c17c4885bb70da0613a2ebd9866e89070cda64099f190af16a26be83`. This is not a genome assembly. No collection country/date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

GenBank cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. The complete requested [HAL author-deposit metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Full article text and BSNF2(14)-specific assay results were not verified. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred from the citation, cohort, genus, or neighboring sequence.

Both non-target native catalog rows were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7609` is Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 14T0026, `GCA_010375995.1`, `SAMN12576339`, `PRJNA560345`, `JAAGIK000000000.1`. The matching field is its assembly name `ASM1037599v1`.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41582` is Acinetobacter baumannii, taxid 470, strain AB25, isolate 13UC190009763, `GCA_050716655.1`, `SAMN41037599`, `PRJNA514245`, `DBIYTO000000000.1`. The numeric match is inside its BioSample; PMID 30286803 is not a target citation.

Neither establishes a target genome, culture deposit, synonym, or extra attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, and punctuation/space/hyphen variants. The expanded pass added `JF779795`, `soilbio.2011.07.010`, and `S003807171100280X`. Both returned five lines: own backbone, scope, scientific name, and the two unrelated entries above. Ignored and compressed files were included. No further target-linked assertion, strain/genome association, or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism search supplied taxonomy-tree leads; accession search returned no result. No search snippet supported a scientific claim.

Unfilled optional fields do not by themselves indicate missing required representation, and no causal graph is required. iModulonDB is not applicable because this record asserts no gene function, regulator, expression module, or stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the taxonomy/name-only assertions. Unverified isolate-level assay results and unavailable article full text limit enrichment research but do not contradict recorded claims.

## Recommended Edits

None required. Preserve BSNF2(14) and its explicitly non-fertilized context in future enrichment; keep partial markers outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the cited paper and isolate-level table, resolve BSNF2(14)/JF779795 explicitly, and inspect assay conditions/results. Require an explicit source chain for any genome or culture-deposit link. After authorized input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Full taxonomy API responses, browser text, and marker annotation were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Previous access attempts for the same paper found ScienceDirect 403 and an ISTEX redirect to institutional-authentication HTML rather than PDF; those failed routes were not retried per isolate. No login, paid access, or full-text reading occurred.

YAML SHA-256: `4f8d3003b4d5ce1f30f8e08c6266498733862c8103d1a78f775d0dd238750f5a`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
