# YAML Record Review: Caryophanon sp. ChST3.6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/caryophanon_sp_chst3_6.yaml`
- Started UTC: 2026-10-06T21:07:05Z
- Finished UTC: 2026-10-06T21:09:37Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035300` is Caryophanon sp. ChST3.6, `SPECIES` in `BACTERIA`, parent `NCBITaxon:2626429`. The record carries ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event.

There are no synonym, nomenclature, taxonomy-mapping, strain-listing, genome, phenotype, citation, or causal-graph assertions. Generated fields remain read-only. Future corrections belong in maintained source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not in this YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/caryophanon_sp_chst3_6.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/caryophanon_sp_chst3_6.yaml --out /private/tmp/c36-strict.tsv`: exit 0, one file scanned, zero errors. The actual output TSV was read and is header-only.
- Structured comparisons inspected the full backbone row, each ancestor in order, direct children, seven non-NCBI inventories, PATHS, seed scope, attestation, and seed-event text. All compared fields agree.
- Exact checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target entries.
- Ignored-inclusive searches, full native candidate inspection, complete SOURCE.json parsing, and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` ran with network access and exited 0. All 28 rows were inspected before external follow-ups. No Caryophanon organism/dataset matches; iModulonDB is not applicable. This absence is not negative biological evidence.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query succeeded.
- The exact-isolate Table II row and adjacent family-placement text in the primary paper were visually checked on printed page 886 using the existing PDFKit rendering. This is a bounded source-page inspection, not a full-paper review.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, and source-file hashes. Manual comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222001`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31477`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035300&retmode=xml) agree on taxon ID, exact label, species rank, parent, bacterial placement, and genetic code. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035300) confirms the full ancestor-ID chain.

Every ID, label, and normalized rank matches in the root-first lineage: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Caryophanaceae; Caryophanon; unclassified Caryophanon. Family 186818, genus 33976, and parent 2626429 agree. EFetch omits root from its displayed chain; Datasets includes ID 1.

Pinned synonyms and live alternate-name content are empty; there are no direct children in the pinned backbone. Authority-assigned species rank does not establish a formal binomial or a type strain. ChST3.6 and CtST3.6 are distinct isolate codes, not spelling variants.

## Evidence

- The NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14492` maps this identifier to its stem; `curation/seed_scope.tsv:322275` supplies the exact reason embedded in the seed event.
- Raw, ATB, and StrainInfo extraction timestamps were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum agrees with the seed-event timestamp and inspected seeder rule. This is source-seeding provenance, not human sign-off.
- Exact nuccore searching returned one record, UID 334899385, [JF935100.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935100.1). Complete metadata excluding nucleotide bases describes an 883 bp partial 16S rRNA sequence, strain ChST3.6, taxon 1035300, female shoulders, host Sturnira lilium, Venezuela, and collection date 16-Feb-2010 as supplied by GenBank. The direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. This marker is not an assembly or a culture-deposit accession.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on page 886, associates JF935100 with ChST3.6, Caryophanon sp., female S. lilium, and shoulders. Those fields agree with GenBank; the inspected table does not supply an isolate-specific collection date. No DOI or PMID occurs in the inspected sequence reference metadata.
- The same paper page places Caryophanon in Planococcaceae, while pinned and live NCBI use Caryophanaceae. The historical source difference is retained, not reconciled away. TaxonMech carries NCBI lineage rather than substituting the paper's hierarchy; this does not invalidate the exact-isolate accession association.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035300/dataset_report) returned an empty object. These bounded results do not prove global genome absence.

## Completeness

The seeded identity is complete enough. Optional sequence, host, or culture context is not a missing required representation. `strain_count: 0` counts inventoried BacDive-backed entries; it does not deny the cultured biological isolate. A GenBank strain qualifier cannot supply a culture-collection accession.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035300|ChST[-_ ]?3[._ -]?6\b|caryophanon_sp_chst3_6` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed data were included. All five source-native SOURCE.json files were parsed in full; history filenames were searched independently.

All seven candidate lines were inspected completely: four native JSON objects and three TSV rows, using lossless structured displays that asserted reconstruction. Three are target backbone, scientific-name, and scope records; four are unrelated:

| Candidates | Why excluded |
| --- | --- |
| Two M. tuberculosis records | BV-BRC 1773.18318, taxon 1773, strain ERR1035300; corresponding ATB run ERR1035300, SAMEA3558833, ERZ9334441. Run digits do not denote this Caryophanon. |
| Two C. jejuni assembly versions | Historical GCA_010353005.1 and current GCA_010353005.2, taxon 197, CFSAN096341, SAMN13656974, PRJNA258022. The current assembly name is ASM1035300v2. Accession/name digits are not a taxon identifier. |

A separate ignored-inclusive `JF935100` search returned zero lines across the same ten roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target entries were found in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These local negatives are bounded to the inspected snapshots and roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, NCBI lineage, grounding, count, attestation, and seed event are supported. The historical paper family placement was preserved as context rather than substituted into this NCBI-grounded record.

## Recommended Edits

None required.

Separately authorized enrichment should preserve exact accession identity and source scope in maintained source inputs or a deliberately designed representation. Necessary seeder changes belong in `src/taxonmech/seed.py` with focused tests. Do not hand-edit this generated YAML, infer deposits, count the marker as a genome, or promote `SEEDED` based on this report.

## Follow-up Checks

After an authorized upstream change, use the documented extraction/seeding workflow and `just verify-corpus`, then schema and single-target strict validation. Inspect the actual emitted TSV, changed source rows, and regenerated values.

Require explicit authority-backed identity bridges for new genome/deposit links. Functional or causal claims need directly relevant evidence; isolation context alone does not establish an effect. Any collection-date enrichment should preserve the exact accession's qualifier until independently reconciled, not borrow another isolate's date. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, and history documentation were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The source PDF/rendering remained in scratch space; no other isolate's verdict was reused.

The target was byte-compared against its initial full read and remains unchanged. This new report is the sole repository artifact of this target review. No YAML, inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
