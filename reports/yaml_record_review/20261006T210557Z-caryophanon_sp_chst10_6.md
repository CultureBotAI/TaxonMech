# YAML Record Review: Caryophanon sp. ChST10.6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/caryophanon_sp_chst10_6.yaml`
- Started UTC: 2026-10-06T21:03:28Z
- Finished UTC: 2026-10-06T21:05:57Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035299` denotes Caryophanon sp. ChST10.6, `SPECIES` in `BACTERIA`, parent `NCBITaxon:2626429`. Ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event are asserted.

No synonyms, nomenclature, taxonomy mappings, strain listings, genomes, phenotypes, citations, or causal graph are asserted. Generated fields remain read-only. Future corrections belong in maintained source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not this YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/caryophanon_sp_chst10_6.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/caryophanon_sp_chst10_6.yaml --out /private/tmp/c106-strict.tsv`: exit 0, one file scanned, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons read the full backbone row, each ancestor, direct children, seven non-NCBI inventories, PATHS, scope, attestation, and seed-event text. All compared fields agree.
- Exact checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target entries.
- Ignored-inclusive searches, full native candidate inspection, complete SOURCE.json parsing, and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` ran with network access and exited 0. All 28 rows were inspected before external follow-ups. No Caryophanon organism/dataset matches; iModulonDB is not applicable, not negative biological evidence.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query succeeded.
- The exact-isolate row and adjacent family-placement text in the primary paper were visually inspected on printed page 886 using the existing PDFKit rendering. This is a bounded source-page check, not a claim of full-paper review.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, or source-file hashes. The manual comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222000`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31476`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035299&retmode=xml) agree on ID, exact label, species rank, parent, bacterial placement, and code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035299) confirms the full ancestor-ID chain.

Every ID, label, and normalized rank agrees in the root-first lineage: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Caryophanaceae; Caryophanon; unclassified Caryophanon. The terminal lineage identifiers are family 186818, genus 33976, and parent 2626429. EFetch omits root from its displayed chain; Datasets includes ID 1.

Pinned synonyms and live alternate-name content are empty; the pinned backbone has no direct children. NCBI's species rank does not establish a formal binomial or type strain. ChST10.6 must remain distinct from CtST10.6 and the other Caryophanon isolates in the study.

## Evidence

- The NCBITAXON attestation correctly counts one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14491` maps the identifier to the target stem. `curation/seed_scope.tsv:322274` supplies the precise reason carried in the seed event.
- Raw, ATB, and StrainInfo extraction timestamps were checked as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum matches the event timestamp and inspected `_seed_timestamp()` implementation. This is source-seeding provenance, not human-review evidence.
- Exact nuccore searching returned one record, UID 334899349, [JF935064.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935064.1). Complete metadata excluding nucleotide bases describes a 1429 bp partial 16S rRNA sequence, strain ChST10.6, taxon cross-reference 1035299, male epaulettes, host Sturnira bogotensis, Venezuela, and collection date 16-Feb-2010. Direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. This marker is not an assembly, deposit accession, or independent species-level resolution.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on page 886, pairs JF935064 with ChST10.6, Caryophanon sp., male S. bogotensis, and epaulettes, agreeing with GenBank. No DOI or PMID occurs in the sequence's inspected reference metadata.
- The same paper page places Caryophanon in Planococcaceae, whereas the pinned and live NCBI lineage uses Caryophanaceae. This historical source difference is retained here. The repository requires carrying the NCBI lineage, not replacing it with a paper's hierarchy; the difference does not invalidate the exact-isolate accession association.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035299/dataset_report) returned an empty object. These bounded results do not establish universal genome absence.

## Completeness

The supported seeded identity is complete enough. Optional host, sequence, or culture details are not missing required fields. Zero inventoried BacDive-backed strains does not mean no biological isolate exists. A GenBank strain qualifier cannot supply a registered culture-collection deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035299|ChST[-_ ]?10[._ -]?6\b|caryophanon_sp_chst10_6` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed data were included. All five source-native SOURCE.json files were parsed completely; history filenames were searched independently.

All nine candidate lines were inspected in full native form: five JSON objects and four TSV rows. Lossless structured displays retained every value and asserted reconstruction. Three are exact backbone, scientific-name, and scope records; six are unrelated:

| Candidates | Why excluded |
| --- | --- |
| Two M. tuberculosis records | BV-BRC 1773.18321, taxon 1773, strain ERR1035299; corresponding ATB run ERR1035299, SAMEA3558832, ERZ9334447. Run digits do not identify this Caryophanon. |
| Two L. monocytogenes records | GCA_004764455.1, taxon 1639, OH-18-22731, SAMN10352998, PRJNA338675; ATB ERZ9092833/SRR8139286 has the same BioSample. ATB's computational species is Listeria monocytogenes_B. BioSample digits are the match. |
| Two metagenomic genome records | GenBank GCA_964415435.1 and GTDB GB_GCA_964415435.1, taxon 86473, SAMEA117297859, PRJEB82487, isolate SRP329715_co1_181. NCBI calls it uncultured Gammaproteobacteria bacterium; GTDB places CAYPZT01 sp964415435 in Patescibacteriota. Their classifications differ, but neither is this target. The matching number is ungapped length 1035299. |

A separate ignored-inclusive `JF935064` search found zero lines across the ten roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target rows occur in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These negatives are bounded to the inspected sources and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's current assertions. Identity, NCBI lineage, grounding, inventory count, attestation, and seed event agree with inspected sources. The historical paper classification and unrelated genome-classification differences were not silently substituted for the target's NCBI lineage.

## Recommended Edits

None required.

Any separately authorized enrichment must preserve exact accession identity and claim scope in maintained source inputs or a deliberately designed representation. Seeder changes belong in `src/taxonmech/seed.py` with focused tests. Do not hand-edit the YAML, infer deposits, count a marker as an assembly, or promote `SEEDED` from this report.

## Follow-up Checks

After an authorized upstream change, use the documented extraction/seeding workflow and `just verify-corpus`, then schema and single-target strict validation. Inspect the emitted TSV, source rows, and regenerated fields.

Require explicit authority-backed identity bridges for deposit/genome links and directly relevant evidence for functional or causal claims. Isolation from epaulettes does not alone establish odor production or any other causal effect. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, and history documentation were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Source PDF/renderings were reused in scratch space; another isolate's verdict was not reused.

The target was byte-compared against its initial full read and remains unchanged. This new report is the sole repository artifact of the target review. No YAML, source inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
