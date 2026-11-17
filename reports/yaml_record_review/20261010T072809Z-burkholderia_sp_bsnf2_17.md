# YAML Record Review: Burkholderia sp. BSNF2(17)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf2_17.yaml`
- Started UTC: 2026-10-10T07:25:32Z
- Finished UTC: 2026-10-10T07:28:09Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037600`, Burkholderia sp. BSNF2(17). It is a species-ranked bacterial placeholder under `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated taxon YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf2_17.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf2_17.yaml --out /private/tmp/taxonmech-bsnf217-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured identity, lineage labels/ranks, synonyms, genetic code, attestation, unique index, scope reason, and seed-event comparisons passed. This is not corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222815` agrees on ID, label, rank, parent, code, and 2026-09-13 snapshot. Synonym and retirement fields are empty. The complete root-first chain matches individual backbone labels/ranks: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037600&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037600), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037600) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count; this is not proof of zero assemblies. The marker's strain qualifier is compatible with this species-ranked placeholder, not proof of formal nomenclature or a culture deposit.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32451` agrees. Structured scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15369` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323030` supplies the exact reason in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, publication, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate.

Exact Nucleotide search `txid1037600[Organism:exp]` returned one UID, 345019054. Complete [GenBank annotation JF779803.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779803.1) explicitly joins organism, strain BSNF2(17), and taxon 1037600. It is a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `ec825daa0456b251920ba4ea810d42ba80a879c914312393fd315f0d4d255e22`. This is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied; the 5 April 2011 submission date and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. A fresh complete read of requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract describes an 80-isolate study, but full article text and BSNF2(17)-specific assays were not verified. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All four non-target native rows were read completely:

- `data/bvbrc/bvbrc-0018.jsonl.gz:45804` and `data/catalog/ncbi_genbank-0032.jsonl.gz:12166` describe Erwinia sp. HR93, taxid 3094840, GCA_034555055.1/GCF_034555055.1, BV-BRC 3094840.3, SAMN38194231, JAXUDP000000000. The numeric match is BioProject PRJNA1037600, not the target taxon.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20409` describes Salmonella enterica serovar Chester, taxid 149386/species 28901, strain 1037600, GCA_015872865.1, SAMN16972244, PRJNA248792, AAXRPZ000000000.1.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41525` describes Acinetobacter baumannii, taxid 470, strain AB36/isolate 10BC200048582, GCA_050715515.1, SAMN41037600, PRJNA514245, DBIYRM000000000.1. The matching number is within its BioSample. PMID 30286803 is not a target citation.

None establishes a target genome, culture deposit, synonym, or additional attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, and space/punctuation/hyphen variants. The expanded pass added JF779803, soilbio.2011.07.010, and S003807171100280X. Both returned seven lines: own backbone, scope, scientific name, and the four unrelated rows above. Ignored and compressed files were included; no further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/designation web searches yielded taxonomy-tree leads; no snippet supported a scientific claim.

Unfilled optional fields are not missing required representation. No causal graph is required. iModulonDB is not applicable because this record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unverified isolate-specific assays and unavailable full text limit enrichment research, not the validity of recorded assertions.

## Recommended Edits

None required. Preserve the exact BSNF2(17) designation and explicitly non-fertilized context if later enriching this record; keep the partial marker outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the cited article and isolate-level table, explicitly resolve BSNF2(17)/JF779803, and inspect assay conditions/results. Require a source-supported deposit/genome chain for such links. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Taxonomy API responses, browser text, marker annotation, and fresh HAL metadata/abstract were inspected for this review. Earlier attempts to access the same study encountered ScienceDirect 403 and an ISTEX institutional-authentication HTML redirect instead of PDF; those unavailable routes were not retried here. No login, paid access, or full-text reading occurred.

YAML SHA-256: `1c1e42167dcacc438961e1e3f76edbe19c186a233355be19102344336ac0999d`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
