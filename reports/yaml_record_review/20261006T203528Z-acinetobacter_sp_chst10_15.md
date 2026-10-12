# YAML Record Review: Acinetobacter sp. ChST10.15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_chst10_15.yaml`
- Started UTC: 2026-10-06T20:30:47Z
- Finished UTC: 2026-10-06T20:35:28Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. It identifies `NCBITaxon:1035292`, Acinetobacter sp. ChST10.15, at `SPECIES` rank in `BACTERIA`. Its parent is `NCBITaxon:196816`; there are ten root-first ancestors and genetic code 11. Grounding is `EXACT`, mapping status is `SEEDED`, and `strain_count` is zero. It contains one NCBITAXON NAME attestation and one seed event, with no synonym, nomenclature, mapping, strain-list, genome, phenotype, citation, or causal-graph claims.

Seeded values are generated and read-only. Any future correction must be made in maintained upstream source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not directly in this YAML or generated pages.

## Validation

The project commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/acinetobacter_sp_chst10_15.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/acinetobacter_sp_chst10_15.yaml --out /private/tmp/a1015-strict.tsv`: exit 0; one file, zero errors. The actual TSV was read and is header-only.
- Read-only structured comparisons checked the full backbone record, every ancestor and its rank, direct children, seven non-NCBI inventories, PATHS, seed scope, the attestation, and the complete seed-event text. All compared values agree.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` returned no target entries.
- Ignored-inclusive searches and full native candidate inspection completed as described below.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0; all 28 dataset rows inspected. The Acinetobacter baumannii dataset is not this unidentified Acinetobacter. No covered organism/dataset matches ChST10.15, so iModulonDB is not applicable.
- Live NCBI taxonomy XML and Datasets taxonomy JSON, exact-organism Assembly and nuccore searches, complete sequence metadata, and an independent Datasets genome query completed successfully.
- The cited primary paper's methods and exact-isolate table were read in author-posted text and in the downloaded PDF. Printed pages 884 and 886 were rendered with macOS PDFKit and visually inspected; Poppler and the queried Python PDF packages were unavailable in the checked command path/project environment. Redalyc failed through the web tool but the direct public PDF download succeeded.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance gates, full tests, rendered taxon pages, original-taxdump regeneration, or source-file hash verification. The manual source comparisons are not a focused replacement for any corpus-only gate.

## Identity and Grounding

The pinned backbone `data/raw/ncbitaxon_taxa.tsv:221993`, native scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31469`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035292&retmode=xml) agree on identifier, scientific label, species rank, parent, bacterial division, and code 11. The [Datasets taxonomy endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035292) confirms the label, rank, and full ancestor-ID chain including root.

The ordered lineage is root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Moraxellales; Moraxellaceae; Acinetobacter; unclassified Acinetobacter. All IDs, labels, and normalized ranks agree with the pinned lineage and live authority. EFetch's displayed lineage omits root; Datasets includes it.

The pinned synonym fields and live alternate-name content are empty. The pinned backbone has no direct children of this node. Species rank here is the authority's rank for a placeholder label, not a valid-binomial or type-strain assertion. This node must not be conflated with other Acinetobacter isolates from the same study.

## Evidence

- The sole NCBITAXON attestation correctly represents one NAME assertion at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14484` resolves the exact identifier to the target stem, and `curation/seed_scope.tsv:322267` supplies the exact inclusion reason in the seed event.
- The raw, ATB, and StrainInfo manifest extraction times were read: 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum matches the seed event and the inspected timestamp-selection logic. The event is source provenance, not a claim that a curator reviewed this record.
- Exact-organism nuccore searching returned one record, UID 334899355, [JF935070.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935070.1). Its complete metadata, excluding nucleotide bases, identifies a 1,406 bp partial 16S rRNA sequence with strain ChST10.15 and taxon cross-reference 1035292. Source qualifiers specify male epaulettes, host Sturnira bogotensis, Venezuela, and collection date 16-Feb-2010. Submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. These are accession-scoped source annotations, not genus-wide traits.
- The sequence cites Gonzalez-Quinonez, Fermin, and Munoz-Romo, Interciencia 39(12):882-889 (2014), with no DOI or PMID in the sequence metadata. The [primary paper](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on printed page 886, explicitly pairs JF935070 with ChST10.15, Acinetobacter sp., male S. bogotensis, and epaulettes. Methods on page 884 include both host species and describe LB agar isolation at 37 C aerobically, colony purification, and 16S identification. Thus the title's emphasis on S. lilium is not a host conflict. This supports the particular isolate's reported recovery, not a demonstrated odor-production mechanism, species-wide host restriction, or equivalence to adjacent A. lwoffii isolates.
- Exact-organism Assembly searching returned count 0 with a no-items warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035292/dataset_report) returned an empty object. These bounded results do not prove that no genome exists under another identifier.

## Completeness

The current seeded identity is supported. Optional biological enrichment is not required for this record to pass. In particular, `strain_count: 0` means zero inventoried BacDive-backed entries, not that cultivation has never occurred. Neither the GenBank strain qualifier nor the paper's isolated colony automatically creates a BacDive entry or culture-collection deposit.

The local search used `rg --no-ignore --hidden -n -z -i` with `1035292|ChST[-_ ]?10[._ -]?15\b|acinetobacter_sp_chst10_15` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content was included. All five source-native SOURCE.json files were separately parsed in full, and history filenames were searched independently.

All 14 candidate lines were read in full native form: nine JSON objects and five TSV rows. Structured shared-field/value-column output preserved every JSON field and checked reconstruction; TSV objects were parsed without dropping nested values. Three are the exact backbone, scientific-name, and scope records. Eleven are unrelated:

| Candidates | Reason for exclusion |
| --- | --- |
| Eight E. coli records | Two BV-BRC, two current GenBank, two historical GenBank, and two ATB entries match BioSamples SAMN10352924 or SAMN10352928. They concern PNUSAE018789/PNUSAE018788, GCA_003769205.1/.2 and GCA_003770505.1/.2, taxon 562 where supplied, not taxon 1035292. |
| Two M. tuberculosis records | BV-BRC 1773.18308 and an ATB entry match strain/run ERR1035292. The latter links SAMEA3558825 and ERZ9334428. A run's digits are not an NCBI taxon identity. |
| One C. jejuni record | GenBank GCA_010352925.1, strain 266728, BioSample SAMN13268924, and taxon 197 match only digits within the assembly accession. |

A second ignored-inclusive search for JF935070 returned zero lines across the same ten roots, with no matches in separately parsed SOURCE.json metadata or history filenames. No exact target entries were found in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These are bounded local findings, not claims that other databases or the literature contain no evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's assertions. The live identity, pinned lineage, attestation, count semantics, and seed history are consistent. The accession's host agrees with the exact-isolate table; broad study context was not substituted for strain evidence. Optional host/culture information remains separate from required seeded fields.

## Recommended Edits

None required.

If biological enrichment is separately authorized, retain the accession and isolate-specific source scope in a maintained source transform or explicitly designed evidence representation. Any necessary seeder change belongs in `src/taxonmech/seed.py` with a focused test. Do not hand-edit this YAML, invent a deposit accession, increment a BacDive count from a paper, promote `SEEDED`, or add a causal edge from a suggested ecological role.

## Follow-up Checks

After a future authorized upstream change, run the documented extraction/seeding workflow and `just verify-corpus`, followed by schema and single-target strict validation. Inspect the actual strict TSV and regenerated source-linked fields.

Any proposed phenotype or mechanism needs directly relevant experimental evidence beyond the checked isolation and sequence assignment. Before cross-linking a genome or deposit, establish a stable exact-identity bridge rather than using the excluded numeric matches. Corpus-wide reproduction and QC remain unrun.

## Additional Notes

Repository guidance, schema, history rules, curator ownership instructions, and checklist were previously inspected at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the record-review skill was reread for this continuation.

The target was byte-compared to its initial read and is unchanged. This new report is the only repository artifact of this target review; scratch PDF/render files are outside the repository. No source data, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
