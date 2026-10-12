# YAML Record Review: Arthrobacter sp. SR6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_sr6.yaml`
- Started UTC: 2026-10-03T17:07:18Z
- Finished UTC: 2026-10-03T17:08:23Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303836`.
It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`,
code 11, grounding `EXACT` and mapping status `SEEDED`. There are
ten lineage entries, one NCBI NAME attestation, zero strains and one
embedded seed event. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/arthrobacter_sp_sr6.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/arthrobacter_sp_sr6.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  genetic code and all ten lineage objects. No target children occur.
  Complete exact-field source scans found no membership in the seven
  other inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308169` supplies the exact label, rank,
parent, code, empty synonym fields and 2026-09-13 snapshot. The complete
scientific-name object at `data/catalog/ncbi_names-0007.jsonl.gz:30720`
agrees. All ten ancestors match the pinned backbone, including
Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae
and Arthrobacter.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303836&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 235627,
code 11 and all non-root ancestors, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303836)
confirms rank and all ten ancestor IDs including root. Exact grounding
to this entity is supported. Preserve NCBI's species rank and the
unclassified parent's `NO_RANK`; the SR6 label does not justify
reclassifying the record as a strain or assigning a named species.

## Evidence

The NCBITAXON / NCBITaxon:1303836 / 1 NAME attestation agrees with
the backbone and snapshot. NAME is a source-coverage count, not a
biological strain or genome count. No DOI, PMID, assembly identifier
or experimental quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106274` pins the slug.
`curation/seed_scope.tsv:393116` admits the taxon on 2026-09-13 with
the exact one-source reason in the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains accurate;
this report neither claims nor grants human-review status.

## Completeness

Complete ignored-inclusive whole-token searches by ID, label, slug and
SR6 covered raw inventories, curation and history. Complete exact-field
scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or
BactoTraits membership. There are no descendants to contribute BacDive
strains, supporting the zero count.

Ignored-inclusive native searches covered all compressed JSONL under
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. Full ID, label and slug searches
returned the target NCBI name and two unrelated numeric matches, all
read as full objects:

- `data/catalog/ncbi_genbank-0066.jsonl.gz:46560`, GCA_983105545.1,
  Thermodesulfobacteriota bacterium taxon 2202153: 1303836 is genome
  size, not a taxon reference.
- `data/catalog/ncbi_genbank-0038.jsonl.gz:13097`, GCA_041814925.1,
  Glaesserella sp. taxon 2094731: 1303836 is genome size and ungapped
  size, not the target ID.

The complete SR6 token search returned 33 lines. Native identity fields
were inspected for every match without truncation; Arthrobacter and
StrainInfo matches were emitted in full. Only the target NCBI name
identified Arthrobacter. Important excluded identities were:

| Source evidence | Reason not to transfer to this target |
| --- | --- |
| BacDive 169696, raw line 91929; full native object `data/bacdive/records.jsonl.gz:91928` | Adlercreutzia agrestimuris, taxon 2941324, aliases CLA-SR-6 / SR6, own type deposit DSM 109821. Its unversioned GCA_943193125, BV-BRC 2941324.3 and IMG 8045735997 are not Arthrobacter links. |
| Full StrainInfo object `data/straininfo/records.jsonl.gz:299320` | SI-ID 401431, SI-DP 908367 / DSM 109821, the same Adlercreutzia taxon. OM658561 and unversioned GCA_943193125 explicitly name that deposit. |
| Frondihabitans native identities, including `data/catalog/ncbi_refseq-0001.jsonl.gz:1123`, `gtdb_genomes-0011.jsonl.gz:22987`, BV-BRC 0006 lines 35964-35966 | Frondihabitans sp. PAMC 28766 / older SR6 name, taxon 1795630, GCA/GCF_001577365.1. |
| `data/catalog/ncbi_genbank-0018.jsonl.gz:33861`, `ncbi_refseq-0003.jsonl.gz:43008`, GTDB and BV-BRC identity fields | Pectobacterium brasiliense SR6, taxon 180957, GCA/GCF_020296625.1. |
| `data/catalog/ncbi_genbank-0053.jsonl.gz:1888` and `ncbi_refseq-0008.jsonl.gz:40782` | Aliivibrio friggae SR6, taxon 3707497, GCA/GCF_057368525.1. |
| `data/catalog/ncbi_genbank-0020.jsonl.gz:25247` | Klebsiella pneumoniae isolate SR6, taxon 573, GCA_022184205.1. |
| Other native identity fields | Salmonella Newport FL_UFL-SR6, Lacticaseibacillus rhamnosus SR6-prefixed isolates, beta proteobacterium SR6, Micromonospora, Sphingomonas, Microcoleus and Pseudomonas all carry distinct identities. |

GOLD identities at `data/gold/organisms.jsonl.gz:270011`,
`projects.jsonl.gz:133459` and `analyses.jsonl.gz:113888` identify
Frondihabitans SR6, Go0364649 / Gp0203767 / Ga0175816, not Arthrobacter.
The native projections were used only to identify unrelated source
hits, not to audit those other records' biological assertions.

Complete ignored-inclusive ID/label/slug/SR6 searches additionally
covered `data/atb/`, the full `data/catalog/allthebacteria.tsv.xz`,
and StrainInfo link, assembly, exclusion and compressed related-record
tables. No match occurred in that boundary. No eligible target
deposit/BioSample chain was established.

Empty optional fields are justified at the inspected source boundary,
not proof that no isolates or sequences exist elsewhere. No functional
gene, regulator, pathway, trait or transcriptomic assertion is present;
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
YAML, transfer a bare SR6 alias or treat a genome length as a taxon ID.

## Follow-up Checks

No finding-specific check remains. New links require exact target
identity and explicit primary deposit/sample provenance, followed by
authorized dry-run/canary steps and both focused validators after
regeneration. Full `just verify-corpus` and QC remain necessary for
future corpus-wide claims; neither is claimed by this focused review.

## Additional Notes

Absence checks included ignored files via complete structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All source and validator
processes completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No prior report, record, source, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
