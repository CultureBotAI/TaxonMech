# YAML Record Review: Acinetobacter sp. CtST9.3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_ctst9_3.yaml`
- Started UTC: 2026-10-06T20:40:50Z
- Finished UTC: 2026-10-06T20:43:07Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. It identifies `NCBITaxon:1035294`, Acinetobacter sp. CtST9.3, at `SPECIES` rank in `BACTERIA`. The parent is `NCBITaxon:196816`; ten root-first ancestors and genetic code 11 are represented. It has `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event.

No synonyms, nomenclature, taxonomy mappings, strain listings, genome entries, phenotypes, citations, or causal graph are asserted. Seeded fields are generated and read-only. Future corrections belong in maintained upstream source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not in the YAML or generated pages.

## Validation

The project environment used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/acinetobacter_sp_ctst9_3.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/acinetobacter_sp_ctst9_3.yaml --out /private/tmp/a93-strict.tsv`: exit 0; one file scanned, zero errors. The actual TSV was read and is header-only.
- Structured, read-only comparisons checked the full backbone row, every ancestor in order, direct children, seven non-NCBI inventories, PATHS, seed scope, source attestation, and complete seed-event text. All compared values agree.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` returned no target entries.
- Ignored-inclusive searches and full native candidate inspection completed as described below.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 rows inspected. Acinetobacter baumannii is not this placeholder taxon. No matching organism/dataset covers CtST9.3, so iModulonDB is not applicable.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, full sequence metadata, and an independent Datasets genome query completed successfully.
- The primary paper's exact-isolate table was inspected on printed page 886, including visual reinspection of the PDFKit rendering. Its methods on page 884 had already been read and visually checked in this continuation. The downloaded primary PDF was reused, not another record's verdict.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance checks, full tests, taxon-page rendering, original-taxdump regeneration, and source-file hash verification. The manual source comparisons do not replace a corpus-only gate.

## Identity and Grounding

The pinned backbone `data/raw/ncbitaxon_taxa.tsv:221995`, native scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31471`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035294&retmode=xml) agree on exact identifier, scientific label, species rank, parent, bacterial placement, and genetic code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035294) confirms its label, rank, and full ancestor-ID chain.

The root-first lineage is root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; unclassified Acinetobacter. Every ID, label, and normalized rank matches the inspected pinned and live lineage. Root is omitted from EFetch's displayed chain but present as ID 1 in Datasets.

Pinned synonym fields and live alternate-name content are empty, and the pinned backbone has no direct children of this target. The authority's species rank does not establish a formal binomial or type-strain designation. CtST9.3 must remain distinct from ChST9.3 and other similarly coded isolates.

## Evidence

- The one NCBITAXON attestation correctly represents one NAME assertion at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14486` maps the exact identifier to the target stem; `curation/seed_scope.tsv:322269` supplies the precise reason embedded in the seed event.
- The raw, ATB, and StrainInfo extraction timestamps were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum matches the event timestamp and inspected seeder rule. The event is a source-seeding event, not human-review evidence.
- Exact-organism nuccore searching returned one record, UID 334899372, [JF935087.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935087.1). Complete metadata, excluding nucleotide bases, describes a 584 bp partial 16S rRNA sequence, strain CtST9.3, and taxon cross-reference 1035294. Source qualifiers specify a female's back, host Sturnira lilium, Venezuela, and collection date 16-Feb-2010. Direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. The short marker sequence is not a genome or evidence for a species-level identity beyond its recorded assignment.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on page 886, pairs JF935087 with CtST9.3, Acinetobacter sp., female S. lilium, and back. This agrees with GenBank. No DOI or PMID is supplied in the sequence's reference metadata.
- Exact-organism Assembly searching returned count 0 with a no-items warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035294/dataset_report) returned an empty object. These bounded results do not establish global genome absence.

## Completeness

The supported seeded identity is complete enough. Optional host, culture, or sequence information is not a required missing field. `strain_count: 0` is the count of inventoried BacDive-backed entries, not a declaration that the organism was never cultured. A GenBank strain qualifier does not automatically create a culture-collection accession.

The ignored-inclusive local search used `rg --no-ignore --hidden -n -z -i` with `1035294|CtST[-_ ]?9[._ -]?3\b|acinetobacter_sp_ctst9_3` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Compressed data was included. All five source-native SOURCE.json files were separately parsed completely, and history filenames were searched independently.

All 35 candidate lines were inspected in full native form: 24 JSON objects and 11 TSV rows. Structured shared-field/value-column displays retained every JSON value and asserted reconstruction; TSV values were parsed without dropping nested objects. Three are the exact backbone, scientific-name, and scope records. Thirty-two are unrelated:

| Candidates | Why excluded |
| --- | --- |
| 26 E. coli records | Six BV-BRC, one GOLD project, six current GenBank, seven historical GenBank, and six ATB rows match BioSamples SAMN10352940, SAMN10352941, SAMN10352942, SAMN10352943, SAMN10352944, or SAMN10352945. GOLD Gp0386950/Go0502673 concerns PNUSAE019542. Taxonomy-bearing records use taxon 562. |
| Two Shigella flexneri records | GenBank GCA_013937225.1, strain PNUSAE019629, and the corresponding ATB row match BioSample SAMN10352946, not the target taxon. The GenBank taxon is 623; ATB's current computational label is unknown and its older label is E. coli. |
| Two M. tuberculosis records | BV-BRC 1773.18302 and an ATB row match strain/run ERR1035294. The ATB row links SAMEA3558827 and ERZ9334435. Run digits do not define taxon identity. |
| One C. jejuni record | GCA_010352945.1, strain PNUSAC014881, BioSample SAMN13763571, and taxon 197 match digits within an assembly accession. |
| One K. pneumoniae ATB row | SAMEA111266590, ERR12107434, and ERZ26310468 match digits within the assembly checksum. Its computational species is unknown, not evidence for this Acinetobacter. |

A separate ignored-inclusive JF935087 search returned zero lines across the same ten roots, with no additional matches in parsed SOURCE.json metadata or history filenames. No exact target entries were found in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These are bounded local findings, not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's current assertions. The identity, lineage, grounding, source count, attestation unit, and seed event are supported. No broad study-level biological interpretation was promoted into a target-specific claim.

## Recommended Edits

None required.

For any separately authorized enrichment, preserve the accession's exact identity and scope in maintained source inputs or a deliberately designed evidence representation. A necessary seeder change belongs in `src/taxonmech/seed.py` with a focused test. Do not hand-edit this YAML, infer culture deposits, count a sequence as an assembly, or promote `SEEDED` from this report.

## Follow-up Checks

After an authorized upstream change, run the documented extraction/seeding workflow and `just verify-corpus`, followed by schema and single-target strict validation. Inspect the actual emitted TSV, changed source rows, and regenerated fields.

Require an exact, authority-backed identity bridge for new genome or deposit links. Proposed functional or causal claims require their own directly relevant evidence. Do not transfer any of the excluded BioSample, run, assembly, or checksum matches. Corpus-wide reproduction and QC remain unrun.

## Additional Notes

The record-review skill, curator ownership rules, field checklist, and repository/schema/history guidance were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The primary PDF and rendered source pages stayed in scratch space outside the repository.

The target was byte-compared with its initial complete read and is unchanged. This new report is the sole repository artifact of this target review. No YAML, source inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
