# YAML Record Review: Burkholderia sp. MRhNF3(17)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf3_17.yaml`
- Started UTC: 2026-10-10T21:41:20Z
- Finished UTC: 2026-10-10T21:43:30Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF3(17), `NCBITaxon:1037641`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf3_17.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf3_17.yaml --out /private/tmp/taxonmech-mrhnf317-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222856` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Pseudomonadati 3379134 (kingdom); Pseudomonadota 1224 (phylum); Betaproteobacteria 28216 (class); Burkholderiales 80840 (order); Burkholderiaceae 119060 (family); Burkholderia 32008 (genus); unclassified Burkholderia 2613784 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037641&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037641), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037641) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32492` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15411` uniquely resolves ID/slug; `curation/seed_scope.tsv:323071` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037641[Organism:exp]` returned one UID, 345019071. Complete [GenBank annotation JF779820.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779820.1) explicitly joins organism, strain MRhNF3(17), and taxon 1037641. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `9fb9c4078c1b03324897ce84ae15d6782c74b4aadb235a566ca094b49a7a28a5`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for MRhNF3(14)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots. Cohort results do not establish MRhNF3(17)-specific assays; no weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 16 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7630`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 12T0062, GCA_010376415.1, PRJNA560345, SAMN12576319, JAAGHQ000000000.1. Assembly name ASM1037641v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:20412`: Salmonella enterica subsp. enterica serovar Mikawasima, taxid 149388/species 28901, strain 1037641, GCA_015872925.1, PRJNA248792, SAMN16970872, AAXRQS000000000.1. Its numeric strain designation is not a target identity bridge. Both assemblies are excluded from RefSeq as part of large multi-isolate projects.
- `data/catalog/ncbi_genbank-0057.jsonl.gz:42409` and `data/catalog/gtdb_genomes-0015.jsonl.gz:20066`: GCA_902604785.1 / GB_GCA_902604785.1, isolate AG-461-B18, uncultured Pelagibacteraceae bacterium, taxid/species 1667051, PRJEB33281, SAMEA6078902, CACLAC000000000.1. Genome/ungapped length 1037641 supplies the matches. GTDB classifies this as Pelagibacter sp902604785 in Alphaproteobacteria/Pelagibacterales/Pelagibacteraceae, not Burkholderia. Its source fields `gtdb_representative=t` and `gtdb_type_species_of_genus=f` are source-row flags, not independent nomenclatural conclusions. NCBI describes metagenome derivation and excludes it from RefSeq for that reason and undefined genus; marine-water context is not target context.
- `data/gold/analyses.jsonl.gz:437395`: Ga0653421, named Salmonella enterica enterica sv. Durban 170383, project Gp0811405, IMG 8103764194, GCA_007287895.1 and unversioned AAHNSJ000000000. The IMG substring supplies the match. The organism GOLD ID is empty; no target organism-project-analysis chain was established. GOLD analysis/project IDs are not genome IDs.
- Eleven AllTheBacteria rows match run-accession substrings. All have dataset r0.2, available FASTA, and passing assembly/Sylph filters. The first ten below have scientific name/current and prior Sylph E. coli; row 1716991 instead has Rhizorhabdus histidinilytica in all three fields. Ten rows pass HQ and have true prior HQ membership. Row 992980 instead has HQ `CHECKM2_MAX_CONTAM,MAX_CONTIG_NUM,MIN_N50` and false prior HQ membership. Complete SeqKit and download fields were inspected; no quality or identity was transferred to the target.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992777 | SAMEA9849980 | ERR10376419 | ERZ25464886 |
| 992778 | SAMEA9849981 | ERR10376417 | ERZ25464896 |
| 992817 | SAMEA9850028 | ERR10376418 | ERZ25465222 |
| 992980 | SAMEA9850407 | ERR10376413 | ERZ25466404 |
| 992981 | SAMEA9850408 | ERR10376411 | ERZ25466412 |
| 992982 | SAMEA9850410 | ERR10376415 | ERZ25466420 |
| 993032 | SAMEA9850614 | ERR10376410 | ERZ25466694 |
| 993033 | SAMEA9850615 | ERR10376412 | ERZ25466697 |
| 993034 | SAMEA9850616 | ERR10376414 | ERZ25466700 |
| 993035 | SAMEA9850617 | ERR10376416 | ERZ25466703 |
| 1716991 | SAMN13165553 | SRR10376418 | ERZ25668943 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779820, the DOI, and S003807171100280X. Both returned the same 19 lines: own backbone, scope, scientific name, and 16 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; snippets were not treated as evidence, and the dedicated primary page was independently inspected.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve MRhNF3(17)/JF779820.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF3(17)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

All requested NCBI taxonomy/marker responses succeeded. Marker annotation and native rows were inspected for this target; shared HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, contact, or full-text reading occurred.

YAML SHA-256: `2e4f5e6d178b2f2fd2ff888e0d3f1feb2c5f03e2e632ef9a9aadd55447020c7e`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged by this review.
