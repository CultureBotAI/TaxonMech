# YAML Record Review: Pseudomonas sp. BSF3(3)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bsf3_3.yaml`
- Started UTC: 2026-10-10T22:37:10Z
- Finished UTC: 2026-10-10T22:42:36Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Pseudomonas sp. BSF3(3), `NCBITaxon:1037655`. It records species rank, bacterial domain, parent `NCBITaxon:196821`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories, `curation/seed_scope.tsv`, and extraction/seeding code own future changes; generated YAML is read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_bsf3_3.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_bsf3_3.yaml --out /private/tmp/taxonmech-pseudomonasbsf33-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, full lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. These do not establish full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222870` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1 (no rank); cellular organisms 131567 (cellular root); Bacteria 2 (domain); Pseudomonadati 3379134 (kingdom); Pseudomonadota 1224 (phylum); Gammaproteobacteria 1236 (class); Pseudomonadales 72274 (order); Pseudomonadaceae 135621 (family); Pseudomonas 286 (genus); unclassified Pseudomonas 196821 (no rank).

Complete live [EFetch taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037655&retmode=xml), [Datasets taxonomy JSON](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037655), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037655) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes this NCBI placeholder, not a validly published species name or culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32506` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15425` uniquely resolves ID/slug; `curation/seed_scope.tsv:323085` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037655[Organism:exp]` returned one UID, 345019013. Complete [GenBank annotation JF779762.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779762.1) explicitly joins organism, strain BSF3(3), and taxon 1037655. The 450-base 16S rRNA marker is partial at both ends and annotated from fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `081998b003227883b748581fc072956ab7703d63add18a4dadb7d165a0b244ad`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; this marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), read for this target, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate study compares mineral-amended and control forest plots. Its cohort results do not establish BSF3(3)-specific weathering, iron-release, chitin-degradation, or plant-growth phenotypes. Full text and isolate-level assay tables were not inspected.

All 28 non-target native matches were read completely, with source-specific labels, versions, and status retained:

- MGH85: BV-BRC `1686389.3`, GTDB, GenBank/RefSeq `GCA_001037655.1`/`GCF_001037655.1`, and GOLD analysis `Ga0106773` identify an unrelated isolate. The assembly pair is explicitly identical, with BioSample SAMN03280181. GenBank/BV-BRC project PRJNA271899 differs from RefSeq/GTDB PRJNA224116. NCBI/BV-BRC use Enterobacter sp. MGH85, taxid 1686389; GTDB uses Enterobacter intestinihominis; GOLD uses Enterobacter hormaechei MGH85 with project Gp0130904 and IMG 2660237976. The GOLD organism ID is empty. The source labels were not reconciled or transferred to BSF3(3).
- SMBSF33: BV-BRC `1869227.1977` and deprecated `1869227.2220`, GTDB, and GenBank `GCA_021107795.1` identify one unrelated metagenome-derived assembly, SAMN21083261, PRJNA758896, JAIOSB000000000.1. NCBI calls it bacterium, taxid 1869227; GTDB calls it UBA9296 sp021107795. Santa Monica Basin sediment-enrichment metadata do not describe BSF3(3). Its GTDB representative flag does not establish target identity or nomenclatural standing.
- P26: BV-BRC `573.30922`, GTDB, and GenBank/RefSeq `GCA_011037655.1`/`GCF_011037655.1` identify Klebsiella pneumoniae, taxid 573. The assembly pair is explicitly identical, with SAMN10592685 and SBCV00000000.1. GenBank/BV-BRC project PRJNA510003 differs from RefSeq/GTDB PRJNA224116. Its metadata do not support the target.
- Salmonella Typhimurium, taxid 90371/species 28901, has the bare strain number 1037655, not this taxon ID. Its assembly is GCA_015873425.1, SAMN16972259, PRJNA248792, AAXRPX000000000.1.
- Klebsiella pneumoniae isolate 2002175, taxid 573, has current GCA_031037655.3 and replaced versions .1 and .2, all linked to SAMN34589348 and PRJNA288601. WGS versions are ABLWKZ000000000.3, .1, and .2 respectively. These three rows are version history, not three target isolates.
- Mediterraneibacter torques isolate 1908_1908D_C_58, taxid 33039, has metagenome-derived GCA_061037655.1, SAMN60703972, PRJNA1464738, JCDDIR000000000.1. It matches an assembly-number substring only.

Native row addresses for these 18 JSON records are BV-BRC shards 0005:15496, 0007:5923 and 6193, 0024:28621; GTDB shards 0005:43928, 0008:47132, 0011:43363; GenBank shards 0000:36161, 0009:40288, 0014:20437, 0019:22531, 0028:43571, 0056:27410; historical GenBank 0001:21396 and 21397; RefSeq 0000:30561, 0002:42597; and `data/gold/analyses.jsonl.gz:58789`. All shards are under their corresponding `data/bvbrc/` or `data/catalog/` paths. Complete fields were inspected, including annotation/status differences; no unrelated genome was joined to the target.

Ten AllTheBacteria rows match run-accession substrings. All have scientific/current/prior Sylph E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Complete checksum and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992845 | SAMEA9850068 | ERR10376551 | ERZ25465367 |
| 992846 | SAMEA9850070 | ERR10376553 | ERZ25465374 |
| 992847 | SAMEA9850071 | ERR10376555 | ERZ25465378 |
| 992848 | SAMEA9850076 | ERR10376557 | ERZ25465382 |
| 992849 | SAMEA9850079 | ERR10376559 | ERZ25465389 |
| 992906 | SAMEA9850161 | ERR10376550 | ERZ25465657 |
| 992907 | SAMEA9850164 | ERR10376552 | ERZ25465662 |
| 992908 | SAMEA9850166 | ERR10376554 | ERZ25465676 |
| 992909 | SAMEA9850167 | ERR10376556 | ERZ25465681 |
| 992910 | SAMEA9850170 | ERR10376558 | ERZ25465688 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779762, the DOI, and S003807171100280X. Both returned the same 31 lines: own backbone, scope, scientific name, and 28 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/16S web searches supplied leads only; snippets were not treated as evidence. The dedicated NCBI primary page was independently inspected.

The unrepresented marker is contextual evidence, not a missing required genome/deposit representation. No unsupported phenotype or causal graph is asserted. iModulonDB is not applicable to this taxonomy-only record without a gene, regulator, expression-module, or stress-response dataset claim; its absence is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded evidence. Full-corpus quality gates and isolate-specific experimental conclusions remain outside this verdict.

## Recommended Edits

None required. Preserve `SEEDED` status and the existing event. Any future marker/context enrichment belongs in supported maintained inputs and extraction/seeding logic, or an explicitly supported curated overlay, not a manual generated-YAML edit. Do not infer a culture deposit or genome from the marker or transfer cohort phenotypes.

## Follow-up Checks

After a future maintained-input change, rerun the schema and strict validators, history validation where applicable, and documented corpus-reproduction/QC gates. Any phenotype enrichment needs inspected isolate-specific primary results; any genome link needs an explicit identity chain. No such enrichment was attempted here.

## Additional Notes

All target live NCBI requests succeeded. HAL metadata/abstract were inspected for this target; full text was not. Previously tested publisher and HAL-linked ISTEX routes were respectively HTTP 403 and institutional-login HTML; they were not retried in this review. No paid access, authentication, or contact was attempted.

Source-native content was read before the brief coverage-status interruption; the same target YAML, HEAD, and read-only boundaries were rechecked afterward, and expanded local searches and validators then completed. YAML SHA-256: `0c3a81a54a28423148712eff673407d935ea11050544e64262ede8bcfb21e9de`. No taxon record, source inventory, schema, history, generated page, GitHub item, branch, or worktree was changed; this report is the only repository write for this review.
