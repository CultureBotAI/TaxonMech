# YAML Record Review: Polaribacter sp. UI13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/polaribacter_sp_ui13.yaml`
- Started UTC: 2026-10-03T19:10:02Z
- Finished UTC: 2026-10-03T19:11:16Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303897`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196858`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
Twelve lineage entries, one NCBI NAME attestation, zero strains and
one embedded seed event are present. No synonyms, nomenclature,
taxonomy mappings, xrefs, strain/genome links, experiments or graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/polaribacter_sp_ui13.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/polaribacter_sp_ui13.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank,
  parent, code, empty synonym fields and all twelve lineage objects.
  No children occur. Complete exact-field scans found no membership
  in seven other source inventories. PATHS and scope each have one row;
  the attestation and embedded reason match their source inputs.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308215` supports the label, species rank,
parent, code, empty synonym fields and 2026-09-13 snapshot. The complete
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30768` agrees. The carried
chain is root, cellular organisms, Bacteria, Pseudomonadati, FCB group,
Bacteroidota/Chlorobiota group, Bacteroidota, Flavobacteriia,
Flavobacteriales, Flavobacteriaceae, Polaribacter and unclassified
Polaribacter. Both group entries have `CLADE` rank; the parent has
`NO_RANK`. All identifiers, labels and ranks match the pinned backbone.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303897&retmode=xml)
confirms identity, species rank, parent 196858, code 11 and every
non-root ancestor. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303897)
confirms label, rank and all twelve ancestor identifiers, including root.
Exact grounding and bacterial domain are supported. UI13 is an
isolate-like part of the source species label, not proof of a registered
culture deposit or a reason to change rank.

## Evidence

The single NCBITAXON / NCBITaxon:1303897 / 1 NAME attestation
matches the pinned row and snapshot. NAME is a source-coverage unit,
not a biological strain, genome or phenotype count. No literature
identifier, assembly accession or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106320` pins this slug.
`curation/seed_scope.tsv:393161` admits the species on 2026-09-13
with the exact one-source reason carried in the seed event. The
2026-09-13T17:54:04Z timestamp, seed_from_sources curator,
SEEDED_FROM_SOURCES action and NCBITAXON source list are consistent.
The event describes seeding, not human review; retain `SEEDED`.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and UI13
searches covered raw inventories, curation and history, returning only
the backbone and scope rows. Complete structured exact-field scans
found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or
BactoTraits membership. No descendants in the inspected backbone can
contribute BacDive strains, supporting the zero count in these inputs.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. Only the scientific-name
object matched; it was read in full. No eligible culture-deposit or
explicit strain-genome chain was established.

Additional complete ignored-inclusive searches covered `data/atb/`,
the full `data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV
and compressed TSV link, assembly, exclusion and related-record tables,
without a match. Empty optional fields are justified at this source
boundary, not proof that cultures or sequences cannot exist elsewhere.
Original primary archives were not independently reproduced.

No gene, regulator, pathway, trait or transcriptomic claim is present;
iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Retain the supported identity, verbatim lineage and zero strain
count. Do not infer a culture deposit from UI13 or use shared taxonomy
to join genomes. Future evidence belongs in maintained source pipelines
and inventories, followed by authorized seeding, not manual YAML edits.

## Follow-up Checks

No corrective check is required. After an authorized source refresh,
compare exact source rows and any explicit deposit/genome evidence,
then rerun both focused validators. Corpus-wide claims additionally
require `just verify-corpus` and full QC; neither was run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All searches and
validators completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
