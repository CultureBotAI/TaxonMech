# YAML Record Review: Campylobacter sputorum subsp. sputorum bv. RM3237

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_sputorum_subsp_sputorum_bv_rm3237.yaml`
- Started UTC: 2026-10-03T09:10:20Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:11:50Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031754` denotes
Campylobacter sputorum subsp. sputorum bv. RM3237 under subspecies 32024
and species 206. It declares `NO_RANK`, `BACTERIA`, `EXACT` grounding and
`SEEDED` mapping status, eleven ancestors and genetic code 11. It has an
11-genome GTDB species mapping, one NCBI equivalent name, a GTDB exact
synonym/xref, zero attached strains, four source attestations and one seed
event. The index entry is `data/taxa/PATHS.tsv:13135`. It has no
nomenclature block, attached genome assertions or causal graph.

## Validation

- `just validate data/taxa/bacteria/campylobacter_sputorum_subsp_sputorum_bv_rm3237.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_sputorum_subsp_sputorum_bv_rm3237.yaml`:
  passed, one file and zero errors.
- Structured YAML/TSV checks passed for ID, label, stored rank, parent,
  genetic code and all eleven ancestor IDs, labels, ranks and parent links.
  The complete taxonomy inventory has zero direct children of this target.
- A full native GTDB-shard parse confirmed the 11-member cluster and the
  target's membership; this is a scoped census, not a full provenance replay.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_sputorum_subsp_sputorum_bv_rm3237.yaml`
  passed. No target or maintained input was edited.
- `just verify-corpus` was not rerun because it is full-corpus-only.
  Full catalog hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: ignored-file-inclusive searches
  found no separate target history artifact. The embedded event was
  inspected and covered by strict validation.

## Identity and Grounding

The inspected [NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031754)
agrees on ID, label, equivalent name, unranked status, code and lineage.
Unlike neighboring reviewed strain records, this target has no observed
rank discrepancy. An unranked descendant of a species is within scope.
The awkward `subsp. sputorum bv. RM3237` wording is the retained NCBI name,
not justification for rewriting the generated label or inferring rank.

Native sources associate the RM3237 genome with the GTDB species
`s__Campylobacter_F sputorum`. Membership does not establish that this
single infraspecific node is identical to that species cluster.

## Evidence

| Claim group | Inspected source and conclusion |
| --- | --- |
| Taxonomy and synonym | `data/raw/ncbitaxon_taxa.tsv:220787` supplies identity, code, rank, parent and exact synonym. `data/catalog/ncbi_names-0005.jsonl.gz:29984` records the equivalent name and the following row records the scientific name. Every ancestor was checked separately. |
| GTDB mapping/count | `data/raw/gtdb_mappings.tsv:1321` and `gtdb_species.tsv:40561` supply the closeMatch and count 11. The same cluster maps to five other NCBI taxa, not just this target. |
| Native cluster census | Eleven members have NCBI taxids 206 (four), 32024 (three), and 1031754, 1031920, 1032066 and 32023 (one each). Representative RS_GCF_008245005.1, LMG 7795, is at `data/catalog/gtdb_genomes-0000.jsonl.gz:38840`, not the RM3237 genome. |
| Other attestations | `data/raw/gold_organisms.tsv:412` supplies one ORGANISM; `madin_taxa.tsv:592` supplies four TRAIT_ASSERTION rows; NCBI supplies one NAME. These are distinct source counts, not confirmed phenotypes or genome totals. |
| Scope/history | `curation/seed_scope.tsv:26075` supplies the four-source rationale reproduced in the seed event. SEEDED is not human review. |

The following native records establish that RM3237 is sequenced, but they
do not establish a registered culture deposit for this record:

- `data/catalog/ncbi_genbank-0001.jsonl.gz:38547` and
  `ncbi_refseq-0001.jsonl.gz:22395` supply paired GCA_002220795.1 and
  GCF_002220795.1, target taxid 1031754, species taxid 206, whole strain
  name RM3237, sample SAMN03737991, and projects PRJNA66801/PRJNA224116.
- `data/catalog/gtdb_genomes-0001.jsonl.gz:8217` supplies
  RS_GCF_002220795.1, its GenBank accession, sample/project and the bare
  strain name RM3237, with nonrepresentative status.
- `data/bvbrc/bvbrc-0000.jsonl.gz:3101` supplies genome 1031754.3,
  GCA_002220795.1, CP019682, RM3237, SAMN03737991 and PRJNA66801.
- `data/gold/organisms.jsonl.gz:8287` supplies Go0009296, target taxid and
  bare strain RM3237, with blank collection identifier.
  `projects.jsonl.gz:8152` links Gp0009296 to that organism and PRJNA66801;
  its BioSample field is blank. The exact organism/project-ID search did
  not find an analysis row in the inspected compressed GOLD surfaces.

The assembly metadata cite [PMID 28633450](https://pubmed.ncbi.nlm.nih.gov/28633450/),
which resolves to the 2017 comparative genomics study, DOI
10.1093/gbe/evx112. Its inspected abstract describes four completed genomes.
The full text could not be inspected through either PMC or the publisher,
so it supplies no additional target-deposit or phenotype assertion here.
The YAML itself cites no paper, gene, regulator or transcriptomic claim;
iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/name/slug searches covered reports, history,
curation, raw, ATB and StrainInfo uncompressed inventories. They found
the source and legacy-path rows, not a prior target review or separate
history artifact. A standalone RM3237 spelling search of the uncompressed
inventories found the taxonomy row, not a BacDive/culture deposit.
Decompressed JSONL.GZ/TSV.GZ searches included ignored files under
catalog, BacDive, BV-BRC, GOLD and StrainInfo and returned the native
taxonomy/genome/GOLD evidence above, not a BacDive or StrainInfo deposit.
The ATB full TSV.XZ was not scanned. These are bounded local findings.

The pinned CAFI-based `normalize_culture_identifier("RM3237")` returns an
empty key. Existing rules do not join genomes to BacDive deposits using
bare strain names or taxon co-occurrence. Zero attached strains is therefore
consistent with the model and available deposit evidence, not proof that
the taxon is unsequenced and not a reason to fabricate a deposit entry.
Any future taxon-level genome representation needs a separately authorized
model design; it should not bypass culture-deposit evidence rules.

A search-returned type-strain link-out is not a target match. Its BacDive
2130 is inventoried as S-17 at `data/raw/bacdive_strains.tsv:2108`, classified
under species 206/subspecies 32024, with deposits including LMG 7795 and
NCTC 11528. Neither the generic type-strain link nor membership in the same
GTDB cluster establishes S-17/LMG 7795 as RM3237.

## Findings

- **Blocker:** None found in primary identity or structure.
- **Major (1): GTDB species membership becomes an exact infraspecific
  identity claim.** The exact synonym `Campylobacter F sputorum` and xref
  arise from a closeMatch to an 11-genome cluster covering six NCBI nodes.
  One matching genome supports membership, not equivalence. The synonym
  also flattens GTDB's `_F` genus suffix when replacing every underscore
  with a space. The maintained owner is the identity/synonym block in
  `src/taxonmech/seed.py:451`, with tests in `tests/test_seed.py`, plus
  upstream kg-microbe mapping semantics consumed by `src/taxonmech/extract.py`.
- **Minor (1): Live GTDB/assembly verification is incomplete.** The GTDB
  page and NCBI assembly page failed retrieval. Native catalogs explicitly
  establish the scoped evidence above, but current remote cluster state
  and assembly-page contents were not independently verified. This does
  not establish a broken identifier or require removing source evidence.

## Recommended Edits

1. Add an infraspecific identity guard in `src/taxonmech/seed.py` so GTDB
   species membership does not automatically generate exact synonyms and
   identity xrefs on strain or unranked descendants. Preserve native GTDB
   suffix spelling in any retained display name. Review upstream mapping
   semantics instead of mechanically reversing a SKOS predicate or
   replacing the 11-genome cluster count with one.
2. Retain the NCBI label, unranked status and parent chain. Do not create a
   BacDive strain or culture accession for RM3237 from bare-name evidence.
3. Retry the unavailable live pages before claiming a current independent
   source verification. No immediate generated-record edit is authorized.

## Follow-up Checks

- Add regression coverage for an unranked below-species target, a GTDB
  suffixed genus and a cluster spanning multiple NCBI nodes.
- After a separately authorized upstream/seeder fix, run the normal seed
  dry run, `just seed-canary NCBITaxon:1031754`, both target validators
  and full `just verify-corpus`.
- Retain native GCA/GCF pairing evidence and source-specific sample/project
  fields without equating the entire GTDB cluster or nearby type strain to
  this target. Require an explicit whole deposit identifier before any
  future strain-genome join.

## Additional Notes

The inspected PubMed abstract is only bounded context, not a source for
new phenotype fields. Other search-returned experiments and gene catalogs
were not used as target assertions. No paid research, outbound messages,
GitHub mutation, history addition or review-status promotion occurred.
