# YAML Record Review: Paenibacillus sp. BSF2(2)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_bsf2_2.yaml`
- Started UTC: 2026-10-10T22:29:17Z
- Finished UTC: 2026-10-10T22:31:58Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Paenibacillus sp. BSF2(2), `NCBITaxon:1037653`. Species rank, bacterial domain, parent `NCBITaxon:185978`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event are recorded. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_sp_bsf2_2.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_sp_bsf2_2.yaml --out /private/tmp/taxonmech-paenibacillusbsf22-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222868` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Bacillati 1783272 (kingdom); Bacillota 1239 (phylum); Bacilli 91061 (class); Caryophanales 1385 (order); Paenibacillaceae 186822 (family); Paenibacillus 44249 (genus); unclassified Paenibacillus 185978 (no rank).

Complete live [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037653), all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037653) lines, and complete [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037653&retmode=xml) from a successful bounded retry agree. The first EFetch attempt returned HTTP 400 containing an internal portal107 HTTP 500 diagnostic; it was not treated as taxonomy content. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32504` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15423` uniquely resolves ID/slug; `curation/seed_scope.tsv:323083` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037653[Organism:exp]` returned one UID, 345019006. Complete [GenBank annotation JF779755.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779755.1) explicitly joins organism, strain BSF2(2), and taxon 1037653. The 450-base 16S rRNA marker is partial at both ends and annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `088256c3e8444b98d9f34bf2287650c3e4ba41be6275b15604ab837a8af8aa21`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly inspected [HAL metadata and complete abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish BSF2(2)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected.

All 16 non-target native matches were read completely:

- `data/bvbrc/bvbrc-0011.jsonl.gz:38553` and `:38622`, `data/catalog/gtdb_genomes-0017.jsonl.gz:23368`, and `data/catalog/ncbi_genbank-0019.jsonl.gz:22543`: Bacteroidales bacterium SMBSF22, taxid 2030927, GCA_021108035.1, PRJNA758896, SAMN21083250. BV-BRC genome 2030927.2283 has status WGS; 2030927.2345 is Deprecated. GenBank/GTDB WGS is JAIORQ000000000.1; BV-BRC stores the unversioned prefix. GTDB assigns JAADGE01 sp021108035, representative true and type-species-of-genus false; these are source flags, not independent nomenclature conclusions. GTDB describes a Santa Monica Basin seep-sediment enrichment culture, not the target's forest soil. GenBank reports exclusion from RefSeq for metagenomic origin and undefined genus. Four source rows do not establish four target strains or genomes.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20442`: Salmonella Enteritidis, taxid 149539/species 28901, strain 1037653, GCA_015873525.1, PRJNA248792, SAMN16972236, AAXRQB000000000.1, assembly PDT000901552.1. The bare strain number is not this NCBI taxon ID. The assembly is excluded from RefSeq as part of a large multi-isolate project.
- `data/catalog/ncbi_genbank-0065.jsonl.gz:49804`: Atopobium sp., taxid/species 1872650, isolate ERS5710624-metaspades_003, GCA_982215985.1, PRJEB104944, SAMEA121743404, CEUXYH000000000.1. Total genome size 1037653 supplies the match; ungapped length is 1035443. The assembly is excluded from RefSeq for metagenomic origin.
- Ten AllTheBacteria rows have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. They match run-accession substrings. Complete checksum, filter, and download fields were inspected; none was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992942 | SAMEA9850297 | ERR10376531 | ERZ25466072 |
| 992943 | SAMEA9850298 | ERR10376533 | ERZ25466083 |
| 992944 | SAMEA9850299 | ERR10376537 | ERZ25466092 |
| 992945 | SAMEA9850300 | ERR10376535 | ERZ25466099 |
| 992946 | SAMEA9850301 | ERR10376539 | ERZ25466108 |
| 993060 | SAMEA9850642 | ERR10376530 | ERZ25466808 |
| 993061 | SAMEA9850643 | ERR10376532 | ERZ25466813 |
| 993062 | SAMEA9850644 | ERR10376536 | ERZ25466816 |
| 993063 | SAMEA9850645 | ERR10376534 | ERZ25466819 |
| 993064 | SAMEA9850646 | ERR10376538 | ERZ25466822 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779755, the DOI, and S003807171100280X. Both returned the same 19 lines: own backbone, scope, scientific name, and 16 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned taxonomy-tree and other terminology leads; snippets were not treated as target evidence. The dedicated NCBI primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims. The recovered transient network error is not a record defect.

## Recommended Edits

None required. Preserve BSF2(2)/JF779755.1 identity and fertilized bulk-soil context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding BSF2(2)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Datasets, Taxonomy Browser, and marker requests succeeded. EFetch taxonomy initially failed with HTTP 400/internal 500 and succeeded on one bounded retry; the complete returned taxonomy was inspected. HAL requested metadata and the complete abstract were freshly read for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `3fd45a44810c0780edfddcaa69c895fd92fececc6120a2b2fbbbad94ae4aa28f`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
