# YAML Record Review: Acinetobacter sp. ChST7.6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_chst7_6.yaml`
- Started UTC: 2026-10-06T20:36:41Z
- Finished UTC: 2026-10-06T20:39:13Z
- Verdict: pass

## Target

The full generated `TaxonRecord` was read. It represents `NCBITaxon:1035293`, Acinetobacter sp. ChST7.6, at `SPECIES` rank in `BACTERIA`. Parent `NCBITaxon:196816`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event are present. No synonyms, nomenclature, taxonomy mappings, strain listings, genomes, phenotypes, citations, or causal graph are asserted.

All seeded values are generated and read-only. Any future correction belongs in maintained source transforms, inventory extraction, scope inputs, or `src/taxonmech/seed.py`, not in the YAML or generated pages.

## Validation

Project commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/acinetobacter_sp_chst7_6.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/acinetobacter_sp_chst7_6.yaml --out /private/tmp/a76-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read and contains only its header.
- Read-only structured comparisons checked the complete backbone row, all ancestors in order, direct children, seven non-NCBI inventories, PATHS, seed scope, source attestation, and the complete seed-event text. All compared values agree.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` returned no target entries.
- Ignored-inclusive source searches and lossless native candidate reads completed as detailed below.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected. Acinetobacter baumannii coverage is not coverage of ChST7.6. No matching organism/dataset was found; iModulonDB is not applicable.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query completed successfully.
- The cited primary paper was inspected at the exact-isolate table. Printed page 887 was extracted, rendered with macOS PDFKit, and visually checked; the same downloaded paper's methods on page 884 were already read and visually checked during this continuation. This target's table row was evaluated independently.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance checks, full tests, taxon-page rendering, original-taxdump regeneration, and source-file hash verification. The manual comparisons do not substitute for any corpus-only gate.

## Identity and Grounding

The pinned backbone `data/raw/ncbitaxon_taxa.tsv:221994`, native scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31470`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035293&retmode=xml) agree on the exact identifier, label, rank, parent, bacterial division, and genetic code. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035293) confirms its label, rank, and root-inclusive ancestor-ID chain.

The full lineage is root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; unclassified Acinetobacter. All ancestor IDs, labels, and normalized ranks match. EFetch omits root from its displayed lineage; Datasets supplies root ID 1.

The pinned synonym fields and live alternate-name content are empty. There are no direct children of this target in the pinned backbone. Species rank is the authority's rank for this placeholder label, not a formally established binomial or type-strain designation. ChST7.6 is not interchangeable with similarly named study isolates.

## Evidence

- The sole NCBITAXON attestation accurately counts one NAME assertion at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14485` supplies the exact identifier-to-stem mapping. `curation/seed_scope.tsv:322268` supplies the exact inclusion reason reproduced in the seed event.
- Raw, ATB, and StrainInfo manifest extraction times were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum matches the event timestamp and the inspected seeder rule. This is source-snapshot provenance, not a human-review event.
- Exact-organism nuccore searching returned one record, UID 334899413, [JF935128.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935128.1). Its full GenBank metadata, excluding nucleotide bases, describes a 1,001 bp partial 16S rRNA gene, with strain ChST7.6 and taxon cross-reference 1035293. Source qualifiers give male epaulettes, Sturnira lilium, Venezuela, and collection date 15-Feb-2010. Direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. These are sequence/isolate annotations, not a genome, type status, or species-wide host claim.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II continuation on page 887, pairs JF935128 with ChST7.6, Acinetobacter sp., male S. lilium, and epaulettes. This independently confirms the exact isolate association; it does not establish an odor-production mechanism. No DOI or PMID is supplied in the sequence's reference metadata.
- Exact-organism Assembly searching returned count 0 and a no-items warning. The independent [Datasets genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035293/dataset_report) returned an empty object. These bounded query outcomes do not exclude undiscovered genomes or records filed under another identity.

## Completeness

The supported seeded identity is complete enough to pass. Optional biological evidence need not be inserted merely because it is discoverable. In particular, `strain_count: 0` counts inventoried BacDive-backed entries, not the number of cultures that have ever existed; a sequence strain qualifier cannot be counted as a BacDive accession.

The search used `rg --no-ignore --hidden -n -z -i` with `1035293|ChST[-_ ]?7[._ -]?6\b|acinetobacter_sp_chst7_6` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content was included. All five source-native SOURCE.json files were separately parsed completely, and history filenames were searched independently.

All 30 candidate lines were inspected in full native form: 19 JSON objects and 11 TSV rows. Shared fields plus value columns preserved all JSON values with a reconstruction assertion; TSV values were parsed without dropping nested content. Three are the exact backbone, name, and scope records. Twenty-seven are unrelated:

| Candidates | Why excluded |
| --- | --- |
| 13 E. coli records | Three BV-BRC, three current GenBank, four historical GenBank, and three ATB rows match BioSamples SAMN10352937, SAMN10352938, or SAMN10352939. Their strains are PNUSAE019614, PNUSAE019612, and PNUSAE019545; taxonomy-bearing records use taxon 562. |
| 11 Shigella sonnei records | One BV-BRC, one GOLD project, four current GenBank, and five ATB rows match BioSamples SAMN10352932, SAMN10352933, SAMN10352934, SAMN10352935, or SAMN10352936. GOLD Gp0447983/Go0523439 and GCA_003916115.1 concern PNUSAE019196. Some ATB computational labels say E. coli or unknown; none identifies this Acinetobacter. |
| Two M. tuberculosis records | BV-BRC 1773.18303 and an ATB row match strain/run ERR1035293. The ATB row links SAMEA3558826 and ERZ9334426, not taxon 1035293. |
| One metagenomic assembly | GCA_982624155.1, Candidatus Nanopelagicaceae bacterium, taxon 2518609, matches an ungapped genome length of 1035293. Its BioSample is SAMEA122203465 and BioProject is PRJEB72909. A sequence length is not an identity link. |

A separate ignored-inclusive JF935128 search returned zero lines across the same ten roots, with no additional matches in SOURCE.json metadata or history filenames. The inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories likewise have no exact target entries. These findings are limited to the searched inputs and query forms, not a global absence of biological evidence or deposits.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current record assertions. Identity, ordered lineage, grounding, attestation, count semantics, and seed-event provenance agree with the inspected sources. Source-specific differences among excluded candidates do not create conflicts for this taxon.

## Recommended Edits

None required.

For future authorized enrichment, retain the exact accession/isolate connection and keep biological claims at their supported scope. A new source representation must enter through maintained inputs and any necessary tested change to `src/taxonmech/seed.py`. Do not hand-edit this YAML, invent a culture deposit, turn a sequence into an assembly, or promote `SEEDED` based on this read-only report.

## Follow-up Checks

Following any authorized upstream change, run documented extraction/seeding and `just verify-corpus`, then schema and target strict validation. Read the emitted strict TSV and inspect the changed inventory rows and regenerated fields.

Require an authority-backed exact-identity bridge for any future genome/deposit link, and direct experimental evidence for any proposed causal mechanism. Do not import the excluded BioSample, run, or genome-length matches. Corpus-wide reproduction and QC remain unrun.

## Additional Notes

The record-review skill, curator ownership rules, field checklist, and repository/schema/history guidance were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The public primary PDF downloaded during this continuation was reused without alteration; source rendering used scratch space only.

The record was byte-compared with its initial full read and is unchanged. This new report is the only repository artifact for this target; no YAML, source inventories, generated outputs, history entries, prior reports, or Git/GitHub objects were changed. Eukaryota was not reopened.
