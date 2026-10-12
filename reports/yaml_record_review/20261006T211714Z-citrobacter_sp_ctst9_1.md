# YAML Record Review: Citrobacter sp. CtST9.1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/citrobacter_sp_ctst9_1.yaml`
- Started UTC: 2026-10-06T21:15:00Z
- Finished UTC: 2026-10-06T21:17:14Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035302` is Citrobacter sp. CtST9.1, `SPECIES` in `BACTERIA`, parent `NCBITaxon:2644389`. Ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event are asserted.

No synonyms, nomenclature, taxonomy mappings, strain listings, genomes, phenotypes, citations, or causal graph are asserted. Generated fields remain read-only. Future corrections belong in maintained source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not this YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/citrobacter_sp_ctst9_1.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/citrobacter_sp_ctst9_1.yaml --out /private/tmp/ci91-strict.tsv`: exit 0, one file scanned, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons inspected the complete backbone row, each ancestor in order, direct children, seven non-NCBI inventories, PATHS, seed scope, attestation, and seed-event text. All compared fields agree.
- Exact checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target entries.
- Ignored-inclusive searches, full native candidate inspection, complete SOURCE.json parsing, and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` ran with network access and exited 0. All 28 rows were inspected before external follow-ups. No Citrobacter organism/dataset matches; iModulonDB is not applicable, not negative biological evidence.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query succeeded.
- The exact-isolate Table II row in the primary paper was visually checked on printed page 886 using the existing PDFKit rendering. This is a bounded table inspection, not a claim of full-paper review.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, or source-file hashes. Manual comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222003`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31479`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035302&retmode=xml) agree on ID, exact label, species rank, parent, bacterial placement, and code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035302) confirms every ancestor ID.

All IDs, labels, and normalized ranks agree in the root-first lineage: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Citrobacter; unclassified Citrobacter. Family 543, genus 544, and parent 2644389 agree. EFetch omits root from its displayed chain; Datasets includes ID 1.

Pinned synonyms and live alternate-name content are empty; the pinned backbone has no direct children. NCBI's species rank does not establish a formal binomial or type strain. CtST9.1 remains distinct from ChST9.1 and other Citrobacter isolates in the study.

## Evidence

- The NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14494` maps the identifier to this stem. `curation/seed_scope.tsv:322277` supplies the exact scope reason reproduced in the seed event.
- Raw, ATB, and StrainInfo extraction timestamps were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum equals the seed-event timestamp under the inspected `_seed_timestamp()` implementation. This is source-seeding provenance, not human sign-off.
- Exact nuccore searching returned one record, UID 334899370, [JF935085.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935085.1). Complete metadata excluding nucleotide bases describes an 812 bp partial 16S rRNA sequence, strain CtST9.1, taxon cross-reference 1035302, female back, host Sturnira lilium, Venezuela, and collection date 13-Feb-2010 as supplied by GenBank. Direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. The marker is not an assembly or a culture-deposit accession.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on page 886, associates JF935085 with CtST9.1, Citrobacter sp., female S. lilium, and back. Those fields agree with GenBank; the inspected table does not supply an isolate-specific collection date. No DOI or PMID occurs in the inspected sequence reference metadata.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035302/dataset_report) returned an empty object. These bounded results do not prove global genome absence.

## Completeness

The seeded identity is complete enough. Optional host, sequence, or culture context is not missing required content. `strain_count: 0` counts inventoried BacDive-backed entries and does not deny the cultured biological isolate. A GenBank strain qualifier cannot establish a registered culture deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035302|CtST[-_ ]?9[._ -]?1\b|citrobacter_sp_ctst9_1` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed data were included. Five source-native SOURCE.json files were parsed completely; history filenames were searched independently.

All eight candidate lines were inspected in full native form: five JSON objects and three TSV rows. Lossless structured displays retained every value and asserted reconstruction. Three are exact backbone, scientific-name, and scope records; five are unrelated:

| Candidates | Why excluded |
| --- | --- |
| Two M. tuberculosis records | BV-BRC 1773.18323, taxon 1773, strain ERR1035302; corresponding ATB run ERR1035302, SAMEA3558835, ERZ9334444. Run digits do not identify this Citrobacter. |
| Two C. jejuni assembly versions | Historical GCA_010353025.1 and current GCA_010353025.2, taxon 197, CFSAN096337, SAMN13656961, PRJNA258022. The current assembly name is ASM1035302v2. Assembly/name digits are not the target taxon ID. |
| One Patescibacteria genome | GCA_060828225.1, taxon 2052139, isolate gs.3185, SAMN61839569, PRJNA1497497. Its total and ungapped sequence lengths are 1035302. |

A separate ignored-inclusive `JF935085` search found zero lines across the ten roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target entries occur in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These negatives are bounded to the inspected snapshots and roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, NCBI lineage, grounding, inventory count, attestation, and seed event agree with inspected sources. No marker sequence or unrelated numeric match was promoted into a target genome link.

## Recommended Edits

None required.

Separately authorized enrichment must preserve exact accession identity and source scope in maintained inputs or a deliberately designed representation. Necessary seeder changes belong in `src/taxonmech/seed.py` with focused tests. Do not hand-edit this YAML, infer deposits, count a marker as a genome, or promote `SEEDED` from this report.

## Follow-up Checks

After an authorized upstream change, use the documented extraction/seeding workflow and `just verify-corpus`, followed by schema and single-target strict validation. Inspect the actual TSV, changed source rows, and regenerated values.

Require explicit authority-backed identity bridges for new genome/deposit links and directly relevant evidence for functional or causal claims. Isolation context alone does not establish a biological effect. Any collection-date enrichment should preserve the exact accession's qualifier rather than borrow a neighboring isolate's metadata. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, and history documentation were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The source PDF/rendering remained in scratch space; no other isolate's verdict was reused.

The target was byte-compared with its initial full read and remains unchanged. This new report is the sole repository artifact of the target review. No YAML, source inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
