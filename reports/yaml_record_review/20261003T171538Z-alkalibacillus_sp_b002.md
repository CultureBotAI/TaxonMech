# YAML Record Review: Alkalibacillus sp. B002

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alkalibacillus_sp_b002.yaml`
- Started UTC: 2026-10-03T17:14:31Z
- Finished UTC: 2026-10-03T17:15:38Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303839`.
It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2626834`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded seed
event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experimental assertions or graph
are claimed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/alkalibacillus_sp_b002.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/alkalibacillus_sp_b002.yaml`:
  PASS; one file, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field scans found no membership in the seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308172` supplies the exact label, species
rank, parent, code, empty synonym fields and 2026-09-13 snapshot.
The full native name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30723` agrees. All ten ancestors
match the pinned backbone, including Bacillati, Bacillota, Bacilli,
Caryophanales, Bacillaceae and Alkalibacillus.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303839&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2626834,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303839)
confirms rank and all ten ancestor IDs including root. Exact grounding
is supported. Retain the source rank and unclassified parent's
`NO_RANK`; the isolate-like designation does not justify a rank change.

B002 is a bare designation reused in other genera, not a unique deposit
accession or a basis for assigning type status or a named species.

## Evidence

The NCBITAXON / NCBITaxon:1303839 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not biological
strains or genomes. No DOI, PMID, assembly identifier or experimental
quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106277` pins the slug.
`curation/seed_scope.tsv:393119` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains accurate;
this review neither claims nor grants human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/B002 searches
covered raw inventories, curation and history. Complete exact-field
scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or
BactoTraits membership. No descendants can contribute BacDive strains,
supporting the zero count.

Ignored-inclusive compressed JSONL searches covered `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. Target ID, full label and slug returned only the
full scientific-name object above. The complete B002 token scan
returned 35 lines. Identity fields were inspected for every match
without truncation; Alkalibacillus and StrainInfo objects were emitted
in full. The BacDive hit was also read in full separately. Only the
target NCBI name identified Alkalibacillus.

Important exclusions:

| Source evidence | Different identity and reason not to join |
| --- | --- |
| BacDive 175489, `data/raw/bacdive_strains.tsv:97720`; full native object `data/bacdive/records.jsonl.gz:97719` | Limosilactobacillus galli taxon 2991834, B002 / BC6G17, type deposits DSM 113833 and LMG 32623. Its type flag does not concern Alkalibacillus. |
| Full StrainInfo object `data/straininfo/records.jsonl.gz:225054` | SI-ID 283110, the same Limosilactobacillus taxon, own DSM 113833 / SI-DP 55349 and aliases B002, BC6G17 and LMG 32623. |
| NCBI/GTDB/BV-BRC identity fields for GCA/GCF_947381495.1 | Limosilactobacillus galli / older Limosilactobacillus sp. BC6G17 name, taxon 2991834, including `data/catalog/ncbi_genbank-0059.jsonl.gz:35495` and `ncbi_refseq-0010.jsonl.gz:6327`. |
| GCA_001331415.1 and historical GCF_001331415.1 identity fields | Bordetella pertussis B002 / BP2, taxon 520, including `data/catalog/ncbi_genbank-0001.jsonl.gz:156` and `ncbi_refseq_historical-0000.jsonl.gz:10604`. |
| Other genome identity fields | Bacillus mycoides B002-3, taxon 1405 (GCA/GCF_024498055.1); Micromonospora SYSU B002, taxon 47850 (GCA/GCF_056150505.1); Pseudomonas B002-5F, taxon 3458702 (GCA/GCF_056171715.1); Staphylococcus aureus isolate B002, taxon 1280 (GCA_027896495.1). |
| Other NCBI name fields | Sphingomonas sp. LDB-B002, taxon 1199437, and Halomonas sp. B002, taxon 1857621, are distinct entities. |

GOLD organism/project/analysis identities identify Bordetella pertussis
B002 (Go0356300 / Gp0190567 / Ga0160975), Limosilactobacillus galli
B002 (Go0680379 / Gp0782398 / Ga0633289) or Eutypa lata B002
(Go0680647 / Gp0782669 / Ga0663259), not Alkalibacillus. The fungal
source hit was excluded by identity, not re-reviewed as a Eukaryota
YAML. Native projections were used only to inspect unrelated source
identities, not to audit their other biological assertions.

Complete ignored-inclusive ID/label/slug/B002 searches additionally
covered `data/atb/`, the full `data/catalog/allthebacteria.tsv.xz`,
and StrainInfo link, assembly, exclusion and compressed related-record
tables. No match occurred in that boundary. No eligible target
deposit/BioSample chain was established.

Empty optional fields are justified within the inspected source boundary,
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
YAML or transfer B002 aliases, type status or genome links across taxa.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact target
identity and explicit primary deposit/sample provenance, followed by
authorized dry-run/canary steps and both focused validators after
regeneration. Corpus-wide claims additionally require
`just verify-corpus` and full QC, not run in this focused review.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All search and validator
processes completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota coverage was left untouched.
