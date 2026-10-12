# YAML Record Review: Caryophanon sp. CtST3.1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/caryophanon_sp_ctst3_1.yaml`
- Started UTC: 2026-10-06T21:10:40Z
- Finished UTC: 2026-10-06T21:12:55Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035301` identifies Caryophanon sp. CtST3.1, `SPECIES` in `BACTERIA`, parent `NCBITaxon:2626429`. Ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event are asserted.

No synonyms, nomenclature, taxonomy mappings, strain listings, genomes, phenotypes, citations, or causal graph are asserted. Generated fields are read-only. Future corrections belong in maintained source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not this YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/caryophanon_sp_ctst3_1.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/caryophanon_sp_ctst3_1.yaml --out /private/tmp/c31-strict.tsv`: exit 0, one file scanned, zero errors. The actual emitted TSV was read and is header-only.
- Read-only structured comparisons inspected the full backbone row, every ancestor in order, direct children, seven non-NCBI inventories, PATHS, seed scope, attestation, and seed-event text. All compared fields agree.
- Exact checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target entries.
- Ignored-inclusive searches, full native candidate inspection, complete SOURCE.json parsing, and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` ran with network access and exited 0. All 28 rows were inspected before external follow-ups. No Caryophanon organism/dataset matches; iModulonDB is not applicable. Its absence is not negative biological evidence.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query succeeded.
- The exact-isolate Table II row and adjacent family-placement text in the primary paper were visually checked on printed page 886 using the existing PDFKit rendering. This is a bounded source-page inspection, not full-paper review.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance checks, full tests, page rendering, original-taxdump regeneration, or source-file hashes. Manual source comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222002`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31478`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035301&retmode=xml) agree on ID, exact label, species rank, parent, bacterial placement, and code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035301) confirms every ancestor ID.

The root-first chain agrees in all IDs, labels, and normalized ranks: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Caryophanaceae; Caryophanon; unclassified Caryophanon. Family 186818, genus 33976, and parent 2626429 agree. EFetch omits root from its displayed chain; Datasets includes ID 1.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. NCBI's species rank does not establish a formal binomial or type strain. CtST3.1 must not be conflated with ChST3.1 or another Caryophanon isolate.

## Evidence

- The NCBITAXON attestation correctly represents one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14493` maps the identifier to the target stem; `curation/seed_scope.tsv:322276` provides the exact scope reason in the seed event.
- Raw, ATB, and StrainInfo extraction timestamps were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum equals the event timestamp under the inspected seeder rule. This is source-seeding provenance, not human sign-off.
- Exact nuccore searching returned one record, UID 334899364, [JF935079.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935079.1). Complete metadata excluding nucleotide bases describes a 702 bp partial 16S rRNA sequence, strain CtST3.1, taxon cross-reference 1035301, female back, host Sturnira lilium, Venezuela, and collection date 13-Feb-2010. Direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. This marker is not an assembly or a culture-deposit accession.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on page 886, pairs JF935079 with CtST3.1, Caryophanon sp., female S. lilium, and back, agreeing with GenBank. No DOI or PMID occurs in the inspected sequence reference metadata.
- The same paper page places Caryophanon in Planococcaceae, while pinned and live NCBI use Caryophanaceae. This historical difference is retained as source context. The repository carries NCBI lineage and does not substitute or reconcile a paper's hierarchy; the exact-isolate accession association remains supported.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035301/dataset_report) returned an empty object. These bounded results do not establish global genome absence.

## Completeness

The seeded identity is complete enough. Optional host, culture, or sequence context is not missing required content. `strain_count: 0` counts inventoried BacDive-backed entries; it does not deny the cultured biological isolate. A GenBank strain qualifier cannot establish a registered culture deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035301|CtST[-_ ]?3[._ -]?1\b|caryophanon_sp_ctst3_1` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed data were included. Five source-native SOURCE.json files were parsed completely; history filenames were searched independently.

All seven candidate lines were inspected in full native form: four JSON objects and three TSV rows. Lossless structured displays retained every value and asserted reconstruction. Three are exact backbone, scientific-name, and scope records; four are unrelated:

| Candidates | Why excluded |
| --- | --- |
| Two M. tuberculosis records | BV-BRC 1773.18317, taxon 1773, strain ERR1035301; corresponding ATB run ERR1035301, SAMEA3558834, ERZ9334456. The ATB computational species is unknown and its HQ filter records CHECKM2_MAX_CONTAM and SYLPH_RESULTS_FAIL. Regardless of quality, the run digits do not identify this Caryophanon. |
| Two Atopobiaceae genome records | GenBank GCA_002424225.1 and GTDB GB_GCA_002424225.1, taxon 1951472, isolate UBA5465, SAMN06452768, PRJNA348753. NCBI calls it Atopobiaceae bacterium UBA5465; GTDB calls it Olegusella sp002407925. The matching value is ungapped length 1035301, not a taxon identifier. |

A separate ignored-inclusive `JF935079` search found zero lines across the ten roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target rows occur in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These negatives are bounded to the inspected snapshots and roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, NCBI lineage, grounding, inventory count, attestation, and seed event agree with inspected sources. Historical taxonomy and unrelated genome classifications were retained as context rather than transferred into this record.

## Recommended Edits

None required.

Separately authorized enrichment must preserve exact accession identity and source scope in maintained inputs or a deliberately designed representation. Necessary seeder changes belong in `src/taxonmech/seed.py` with focused tests. Do not hand-edit the generated YAML, infer deposit links, count a marker as a genome, or promote `SEEDED` from this report.

## Follow-up Checks

After an authorized upstream change, run the documented extraction/seeding workflow and `just verify-corpus`, followed by schema and single-target strict validation. Inspect the actual emitted TSV, changed source rows, and regenerated fields.

Require explicit authority-backed identity bridges for new deposit/genome links and directly relevant evidence for functional or causal claims. Isolation context alone does not demonstrate a biological effect. Corpus-wide reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, and history documentation were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The primary-source PDF/rendering remained in scratch space; no other isolate's verdict was reused.

The target was byte-compared against its initial full read and remains unchanged. This new report is the sole repository artifact of this target review. No YAML, inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
