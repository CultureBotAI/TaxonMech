# YAML Record Review: Alcaligenes sp. SR1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alcaligenes_sp_sr1.yaml`
- Started UTC: 2026-10-03T17:04:42Z
- Finished UTC: 2026-10-03T17:06:20Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`. It denotes `NCBITaxon:1303835`,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:259357`, code 11,
grounding `EXACT` and mapping status `SEEDED`. Ten lineage entries,
one NCBI NAME attestation, zero strains and one embedded seed event
are present. No synonyms, nomenclature, mappings, equivalence xrefs,
strain/genome links, experimental assertions or graph are claimed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/alcaligenes_sp_sr1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/alcaligenes_sp_sr1.yaml`:
  PASS; one file, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- A full structured backbone comparison reproduced identity, rank, parent,
  genetic code and every lineage object. No children occur. Complete
  exact-field scans found no target membership in the seven other source
  inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, rendered products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308168` supplies the exact label, species
rank, unclassified-Alcaligenes parent, code 11, empty synonym fields
and 2026-09-13 snapshot. The full native name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30719` agrees. All ten ancestors
match the pinned backbone, including Betaproteobacteria,
Burkholderiales, Alcaligenaceae and Alcaligenes.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303835&retmode=xml)
confirms ID, label, rank, Bacteria division, parent 259357, code 11
and the complete non-root lineage, with no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303835)
confirms species rank and all ten ancestor IDs including root.
Exact NCBI grounding is supported. Keep the source species rank and
the direct parent's `NO_RANK`; an isolate-like label does not change rank.

SR1 is not a unique collection accession. It is also used by unrelated
strains and in the name of a candidate bacterial division. None of
those uses establishes a named species or type status for this target.

## Evidence

The NCBITAXON / NCBITaxon:1303835 / 1 NAME attestation agrees with
the backbone and its snapshot. NAME counts source coverage, not
biological strains or genomes. No DOI, PMID, assembly or experimental
quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106273` gives the target slug.
`curation/seed_scope.tsv:393115` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. The event's
2026-09-13T17:54:04Z timestamp, seed_from_sources curator,
SEEDED_FROM_SOURCES action and NCBITAXON source agree with seeding.
`SEEDED` is retained; this review neither claims nor grants human approval.

## Completeness

Complete ignored-inclusive whole-token searches by ID, label, slug and
SR1 covered raw inventories, curation and history. Complete exact-field
scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or
BactoTraits membership. No children can contribute BacDive strains,
supporting the zero count.

Ignored-inclusive searches of compressed JSONL under `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/` found only the NCBI name for the full target ID,
label or slug. A broader SR1 search returned 290 lines. Its first
display was truncated, so it was not treated as a complete inspection.
A corrective complete scan grouped the explicit name/taxon identity
fields of all 285 catalog, BV-BRC, GOLD and SeqCode matches into
212 unrelated identity groups plus the full target name object.
All grouped output was inspected without truncation. The remaining
one BacDive and four StrainInfo objects were read in full separately.
Grouping was used only to exclude unrelated source identities, not to
review their biological claims or replace the full target YAML.

Important exclusions:

| Inspected evidence | Reason not to join to Alcaligenes |
| --- | --- |
| BacDive 6371, raw line 6254; full native object `data/bacdive/records.jsonl.gz:6253` | Sporobacterium olearium, species taxon 100133 and strain taxon 1123283, type deposit DSM 12504; its AF116854 marker is not target evidence. |
| Full StrainInfo object `data/straininfo/records.jsonl.gz:37168` | SI-ID 49307, SI-DP 163226 / DSM 12504, Sporobacterium olearium taxon 100133; AF116854 explicitly belongs to that deposit. |
| Full StrainInfo object at line 11904 | SI-ID 11904, Acidovorax taxon 12916, Saito SR1 / Mergaert ST26, own deposit LMG 18347 / SI-DP 45398. |
| Full StrainInfo object at line 22982 | SI-ID 24127, Serratia, aliases Alaoui Sr1 / CCMM/FM/Sr1. Its own deposits LMG 21088 and CCMM B34 have differing Serratia classifications, neither Alcaligenes. |
| Full StrainInfo object at line 30506 | SI-ID 42279, Pectobacterium carotovorum subsp. carotovorum taxon 555, SR1, ATCC 49075 / SI-DP 113706. |
| Native NCBI, GTDB and BV-BRC identity fields | Streptococcus sp. SR1 taxon 1161416, Shewanella sp. SR1 taxon 2855505, Piscirickettsia salmonis taxon 1238 and Pectobacterium versatile taxon 2488639 are distinct genome identities. |
| Other complete grouped identity fields | Candidate-division SR1 taxa, Methylobacterium SR1.6/6 and SR1.6/4, Ruminococcus SR1/5, Candidatus Nitrososphaera evergladensis SR1, Enterococcus, Photobacterium, Lacticaseibacillus, Bacillus and other explicitly different taxa provide no target association. |

GOLD's environmental matches were also read in full:
`data/gold/projects.jsonl.gz:40777` is Gp0061084, a macroalgal-surface
project; line 472115 is Gp0631371, a forest-soil community project,
PRJEB21441 / SAMEA104136229; line 505414 is Gp0674085, a sediment
community project, PRJNA671745 / SAMN17154524. All lack organism GOLD
IDs. The associated Ga0016719 and Ga0555747 objects at
`data/gold/analyses.jsonl.gz:10228` and line 363877 explicitly describe
metagenome analyses, with no organism ID. These SR1-labelled projects
are not identified Alcaligenes cultures. Other GOLD identities name
different taxa. A fungal source hit was excluded by identity, not
re-reviewed as a Eukaryota YAML record.

Complete ignored-inclusive searches additionally covered `data/atb/`,
the full `data/catalog/allthebacteria.tsv.xz`, and StrainInfo link,
assembly, exclusion and compressed related-record tables. Three ATB
rows matched SR1: catalog line 21856, SAMD00253636, candidate division
SR1 bacterium; line 1020560, SAMN02344623, Streptococcus sp. SR1 /
Streptococcus halitosis; line 1253977, SAMN06718548, Flavobacterium
sp. SR1. Full rows were read. None establishes an Alcaligenes deposit
or BioSample chain; no other match occurred within that boundary.

Empty optional fields are justified within the inspected source boundary,
not proof that isolates or sequences do not exist elsewhere. There are
no functional gene, regulator, pathway, trait or transcriptomic claims;
iModulonDB is not applicable. An identity-only record does not require
an invented causal graph.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve NCBI lineage, zero classified strains and
`SEEDED` status. Future enrichment belongs in maintained extraction
inputs or `src/taxonmech/extract.py`, with seeding changes in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML or join bare SR1 aliases across these different identities.

## Follow-up Checks

No finding-specific check remains. New links require exact target
identity and explicit primary deposit/sample provenance. An authorized
future change should use the documented dry-run/canary workflow and
both focused validators after regeneration, followed by full
`just verify-corpus` and QC for corpus-wide claims.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. The corrective grouped
scan and separate full-object reads resolved the initial output
truncation. All processes completed. Public NCBI metadata reads used
network escalation after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No prior report, YAML, source, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota coverage was left untouched.
