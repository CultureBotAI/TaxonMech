# YAML Record Review: Rhodococcus sp. SR2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_sp_sr2.yaml`
- Started UTC: 2026-10-03T17:11:39Z
- Finished UTC: 2026-10-03T17:12:43Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303838`.
It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:192944`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
There are ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event. No synonyms, nomenclature, mappings,
equivalence xrefs, strain/genome links, experiments or causal graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rhodococcus_sp_sr2.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rhodococcus_sp_sr2.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field scans found no membership in the seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only, without an invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308171` supplies the exact label, species
rank, parent, code, empty synonym fields and 2026-09-13 snapshot.
The full native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30722` agrees. Every ancestor
matches the pinned backbone, including Bacillati, Actinomycetota,
Actinomycetes, Mycobacteriales, Nocardiaceae and Rhodococcus.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303838&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 192944,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303838)
confirms rank and all ten ancestor IDs including root. Exact grounding
is supported.

Retain the full NCBI parent label, including its high-G+C qualifier,
and its `NO_RANK`; this is carried taxonomy text, not a new experimental
phenotype assertion. The isolate-like SR2 label does not justify
changing the record's species rank or inferring a named species.

## Evidence

The NCBITAXON / NCBITaxon:1303838 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not biological
strains or genomes. The YAML asserts no DOI, PMID, assembly identifier
or experimental quotation.

`data/taxa/PATHS.tsv:106276` pins the slug.
`curation/seed_scope.tsv:393118` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains accurate;
this review neither claims nor grants human approval.

## Completeness

Complete ignored-inclusive whole-token searches by ID, label, slug
and SR2 covered raw inventories, curation and history. Complete
exact-field scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin or BactoTraits membership. No descendants can contribute
BacDive strains, supporting the zero count.

Ignored-inclusive compressed JSONL searches covered `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. Target ID, full label and slug returned only the
full scientific-name object above. The complete SR2 token scan
returned 112 lines. Identity fields were inspected for every match
without truncation; Rhodococcus and StrainInfo objects were emitted
in full. The two BacDive hits were read in full separately. Only the
target NCBI name identified Rhodococcus.

Important exclusions:

| Source evidence | Different identity or unsupported association |
| --- | --- |
| Full BacDive object `data/bacdive/records.jsonl.gz:84914` | BacDive 162679, Flavisolibacter swuensis taxon 1492899, JCM 19974 / KEMB 9004-156. Its KJ461520 marker description names SR2-4-2, not Rhodococcus SR2. |
| Full BacDive object at line 89583; raw strain row 89584 | BacDive 167351, Streptomyces xylanilyticus taxon 1807871, SR2-123, TISTR 2493 / KCTC 39909, marker LC128341. |
| Full StrainInfo object `data/straininfo/records.jsonl.gz:2460` | SI-ID 2460, Pectobacterium atrosepticum taxon 29471, Graham SR2/3/2 / Dye ED2, own LMG 2383, ICMP 1607, NCPPB 435 and PDDCC 1607 deposits. |
| Full StrainInfo object at line 11897 | SI-ID 11897, Acinetobacter taxon 469, Saito SR2 / Mergaert ST9, own LMG 18348 / SI-DP 45374. |
| Full StrainInfo object at line 34334 | SI-ID 46346, Pectobacterium carotovorum subsp. carotovorum taxon 555, alias SR2, own ATCC 49076 / SI-DP 125782. |
| Full StrainInfo object at line 237383 | SI-ID 308131, Nannochloris taxon 3187, SR2 / MBIC 10596, own NBRC 102832 / SI-DP 716981. This source hit is not a Rhodococcus deposit; no Eukaryota YAML was re-reviewed. |
| NCBI/GTDB/BV-BRC genome identity fields | Pectobacterium versatile SR2, taxon 2488639, GCA/GCF_020295645.1; NCBI objects occur at `data/catalog/ncbi_genbank-0018.jsonl.gz:33812` and `ncbi_refseq-0003.jsonl.gz:42970`. |
| Other native genome identity fields | Enterobacter hormaechei NR3055-SR2 (158836), Enterococcus faecium (1352), E. avium (33945), Photobacterium leiognathi subsp. mandapamensis (48408), Lacticaseibacillus rhamnosus (47715) and Salmonella Rubislaw (598) have distinct identities. |

The remaining NCBI name objects identify SR2 or longer designations in
other genera, or unresolved bacterial entities with different IDs.
Neither a shared short label nor a general unresolved bacterial name
establishes a target association. Native projections were used only
to inspect unrelated source identities, not to audit their biological
claims or substitute for the full target YAML.

GOLD organism fields identify Pectobacterium carotovorum SR2,
Go0199942, taxon 554, and P. atrosepticum Graham SR2/3/2,
Go0252819, taxon 29471. Three environmental projects were read in full
at `data/gold/projects.jsonl.gz:40778`, line 472116 and line 505415:
Gp0061085, Gp0631372 and Gp0674086. They describe macroalgal-surface,
forest-soil and sediment communities, with no organism GOLD IDs.
The latter two name PRJEB21441 / SAMEA104136230 and PRJNA671745 /
SAMN17154525 respectively. Full analysis objects at
`data/gold/analyses.jsonl.gz:5745` and line 364026, Ga0011235 and
Ga0555896, explicitly describe metagenome analyses. Their SR2 labels
do not identify a Rhodococcus culture or establish a genome link.

Complete ignored-inclusive ID/label/slug/SR2 searches additionally
covered `data/atb/`, the full `data/catalog/allthebacteria.tsv.xz`,
and StrainInfo link, assembly, exclusion and compressed related-record
tables. No match occurred in that boundary. No eligible target
deposit/BioSample chain was established.

Empty optional fields are justified within the checked source boundary,
not proof that no isolates or sequences exist elsewhere. No gene,
regulator, pathway, trait or transcriptomic assertion is present;
iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported backbone and `SEEDED` status.
Future enrichment belongs in maintained extraction inputs or
`src/taxonmech/extract.py`, with seeding changes in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML, shorten the carried parent label or join bare SR2 aliases across
distinct taxa and community samples.

## Follow-up Checks

No finding-specific check remains. New links require exact target
identity and explicit primary deposit/sample provenance, followed by
authorized dry-run/canary steps and both focused validators after
regeneration. Corpus-wide claims additionally require
`just verify-corpus` and full QC, not run in this focused review.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All source searches and
validators completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota coverage was left untouched.
