# YAML Record Review: Arthrobacter sp. KMSZP6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_kmszp6.yaml`
- Started UTC: 2026-10-04T20:01:38Z
- Finished UTC: 2026-10-04T20:02:55Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord` for `NCBITaxon:1033891`,
Arthrobacter sp. KMSZP6: SPECIES, BACTERIA, parent `NCBITaxon:235627`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It contains ten root-first ancestors, zero inventoried BacDive strains,
one NCBITAXON name attestation and one seed event. No deposit, genome,
external name equivalence or mechanism is asserted.

The target is KMSZP6, not another KMSZP isolate or its closest literature
match. No generated record, inventory, code or curation-history entry
was changed during this read-only review.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_kmszp6.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_kmszp6.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`; its standard diagnostic
  is `reports/instance_validation_failures.tsv`.
- Passed bounded source comparisons of identity, every ancestor label
  and rank, direct inventories, filename lock, scope and seed wording.
  A complete backbone scan found no child taxa.
- Not run: `just verify-corpus`. Its inspected implementation is a
  full-corpus byte-comparison gate; `--max-diffs` limits diagnostics, not
  the records inspected. Bounded checks here are not a substitute.
- Not applicable: `just validate-products`, because there are no
  curator-added graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline seed event was checked.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221325`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30665` and live
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033891&retmode=xml)
agree on the identifier, scientific name, species rank, unclassified
Arthrobacter parent, bacterial domain and code 11. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033891)
confirms all ten lineage IDs, including root 1. The expanded live
lineage labels and ranks agree with the pinned backbone where supplied.

The carried hierarchy places the taxon under Arthrobacter,
Micrococcaceae, Micrococcales, Actinomycetes, Actinomycetota and Bacillati.
SPECIES is NCBI's operational rank for this placeholder concept, not
a claim that the laboratory designation is a validly published name.
The native name object contains only the scientific name, and all
backbone synonym fields are empty.

Complete exact-ID scans of type-material, merged-ID and dropped-taxon
tables returned no matching rows. The live response gives no successor
or synonym. The literature match below does not supersede these NCBI
identity assertions under the repository's carried-lineage policy.

## Evidence

The sole source attestation reproduces the exact NCBI identifier and
label, one NAME assertion and snapshot `2026-09-13`. Complete directly
mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventory scans found no target rows. With no children, the zero BacDive
strain count is also the complete descendant-inclusive count.

The exact-taxonomy nuccore query returned one entry, whose metadata,
references and feature qualifiers were inspected in the
[NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768707.1&rettype=gb&retmode=xml).
`JF768707.1` is a 1,435-base partial 16S rRNA sequence explicitly
assigned to taxon 1033891 and strain KMSZP6. Its source describes a
uranium-rich site at Domiasiat, India, and provides no registered
culture deposit or genome accession.

The entry links [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, whose metadata and article body were
inspected earlier in this same review session. A fresh
[Europe PMC XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
verified Table 2's exact KMSZP6/JF768707 row, headers, footnotes and
preceding merged cells. Those cells assign Arthrobacter nicotinovorans
as the closest 16S match, with similarity greater than 99.20%.
This is not a culture-deposit identity or an NCBI reclassification.
Supplementary PDF content was not inspected.

The record makes no phenotype or gene claim, so literature findings
are not imported into new mechanism fields or transferred between
isolates. Optional record-level literature evidence is not required for
this source-attested seeded taxon.

The exact-taxonomy Assembly query returned zero entries and a
`phrasesnotfound` warning for `txid1033891[Organism:noexp]`. It does
not prove global genome absence under all classifications. The
Taxonomy Browser HTML was inaccessible to the web tool; public NCBI
APIs successfully supplied the primary identity and sequence evidence.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The taxon, name, slug and
KMSZP6 spelling variants returned six matching lines, all inspected.
The complete native NCBI name object was then read.

The relevant matches were the backbone, scope and scientific name.
Two Staphylococcus aureus GTDB records share the numeric value 1,033,891
as a contig N50; AllTheBacteria sample `SAMEA1033891` is Streptococcus
pneumoniae. These numeric collisions do not establish KMSZP6 identity.
A separate ignored-inclusive search for `JF768707` across the same
roots completed with zero matches.

No eligible native deposit or strain-genome assertion for KMSZP6 was
found within that searched scope. Zero inventoried BacDive strains
does not mean there is no biological isolate. A marker sequence and a
closest-match literature identification do not supply a missing genome
assembly or deposit-backed association. Omitted optional nomenclature,
mappings, definitions, evidence and mechanism sections are appropriate.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
source attestation, strain count, lifecycle status and inline provenance
agree with the available source assertions. The reported literature
identification remains distinct from NCBI taxonomy.

## Recommended Edits

None. Preserve the generated YAML. Future evidence-backed source or
identity corrections belong in the maintained inventory pipeline and,
as needed, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`.
Scope changes belong in `curation/seed_scope.tsv`. Do not substitute
a literature closest-match species for the current taxon identifier.

## Follow-up Checks

On future source refreshes, recheck the exact taxon and KMSZP6/JF768707
pair for explicit deposit or genome evidence. Preserve marker and
assembly distinctions, and keep individual study isolates separate.
Rerun focused validators after an authorized change and the full
`just verify-corpus` gate after regeneration. No unresolved blocker
prevents the present verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13781` locks the current slug.
`curation/seed_scope.tsv:321655` records the September 13, 2026 addition
and one-source reason. The event at `2026-09-13T17:54:04Z` exactly
reproduces the NCBITAXON source list and scope reason. This review does
not promote SEEDED to REVIEWED or append an event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to this taxonomic
record; no gene or expression-module claim was added from the paper.
No paid research, outside contact, GitHub mutation or generator run
occurred.
