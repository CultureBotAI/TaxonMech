# YAML Record Review: Kitasatospora sp. BSNF1(1)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kitasatospora_sp_bsnf1_1.yaml`
- Started UTC: 2026-10-10T22:07:56Z
- Finished UTC: 2026-10-10T22:10:34Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Kitasatospora sp. BSNF1(1), `NCBITaxon:1037647`. Species rank, bacterial domain, parent `NCBITaxon:2633591`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event are recorded. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/kitasatospora_sp_bsnf1_1.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/kitasatospora_sp_bsnf1_1.yaml --out /private/tmp/taxonmech-kitasatosporabsnf11-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222862` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Bacillati 1783272 (kingdom); Actinomycetota 201174 (phylum); Actinomycetes 1760 (class); Kitasatosporales 85011 (order); Streptomycetaceae 2062 (family); Kitasatospora 2063 (genus); unclassified Kitasatospora 2633591 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037647&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037647), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037647) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32498` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15417` uniquely resolves ID/slug; `curation/seed_scope.tsv:323077` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037647[Organism:exp]` returned one UID, 345019047. Complete [GenBank annotation JF779796.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779796.1) explicitly joins organism, strain BSNF1(1), and taxon 1037647. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `538a328d6f492c96d98bd7bcb2b5a15b1cb589a2e05d589516c9b924dca1ec04`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly inspected [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish BSNF1(1)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected.

All 13 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:20438`: Salmonella Enteritidis, taxid 149539/species 28901, strain 1037647, GCA_015873445.1, PRJNA248792, SAMN16972262, AAXRPP000000000.1, assembly PDT000901570.1. The bare strain number is not this NCBI taxon ID.
- `data/catalog/ncbi_genbank-0016.jsonl.gz:41787`: Salmonella Kentucky, taxid 192955/species 28901, strain FSIS22131403, GCA_018385985.1, PRJNA242847, SAMN19222432, ABALZY000000000.1. Assembly name PDT001037647.1 supplies the match. Both assemblies are excluded from RefSeq as parts of large multi-isolate projects.
- Eleven AllTheBacteria rows have available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. The first ten below have scientific name/current and prior Sylph E. coli, dataset r0.2, and match run-accession substrings. Row 2714309 instead has scientific name/current and prior Sylph Neisseria gonorrhoeae, dataset Incr_release.202408, and matches its SeqKit checksum. Complete checksum, filter, and download fields were inspected; none was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992932 | SAMEA9850287 | ERR10376479 | ERZ25576630 |
| 992994 | SAMEA9850426 | ERR10376471 | ERZ25466528 |
| 992995 | SAMEA9850427 | ERR10376475 | ERZ25466535 |
| 992996 | SAMEA9850428 | ERR10376473 | ERZ25466541 |
| 992997 | SAMEA9850430 | ERR10376477 | ERZ25466547 |
| 993043 | SAMEA9850625 | ERR10376470 | ERZ25466727 |
| 993047 | SAMEA9850629 | ERR10376474 | ERZ25466745 |
| 993048 | SAMEA9850630 | ERR10376472 | ERZ25466749 |
| 993049 | SAMEA9850631 | ERR10376476 | ERZ25466753 |
| 993050 | SAMEA9850632 | ERR10376478 | ERZ25466758 |
| 2714309 | SAMN37774126 | SRR26356875 | ERZ26610989 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Initial numeric ID, organism/designation, slug, and punctuation/spacing patterns returned 16 lines. Expanded search included hyphen variants, an exact slug boundary, JF779796, the DOI, and S003807171100280X; it returned the same 16 lines: own backbone, scope, scientific name, and 13 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/accession web searches returned taxonomy-tree leads; snippets were not treated as evidence, and the dedicated NCBI primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve BSNF1(1)/JF779796.1 identity and non-fertilized bulk-soil context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding BSNF1(1)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

All requested NCBI taxonomy/marker responses succeeded. HAL requested metadata and the complete abstract were freshly read for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `4eae3449b9eb7731a0f1b360d0641ccce4f6aad02a8cc1fcae372088fe9ac76c`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
