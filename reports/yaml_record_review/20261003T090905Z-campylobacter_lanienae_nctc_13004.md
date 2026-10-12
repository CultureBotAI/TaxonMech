# YAML Record Review: Campylobacter lanienae NCTC 13004

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_lanienae_nctc_13004.yaml`
- Started UTC: 2026-10-03T09:06:45Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:09:05Z
- Verdict: needs curation

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1031753` denotes
Campylobacter lanienae NCTC 13004 beneath species 75658. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding, `SEEDED` mapping status, ten
ancestors and genetic code 11. It carries one GTDB mapping with 42 genomes,
three NCBI synonyms, a GTDB species exact synonym/xref, one BacDive strain
with four culture deposits, six attestations and a seed event. Its strain
has eight assembly assertions, four typed genome assertions and 33 related
assertions. The index is `data/taxa/PATHS.tsv:13134`. There is no causal
graph or strain-level nomenclature block.

## Validation

- `just validate data/taxa/bacteria/campylobacter_lanienae_nctc_13004.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_lanienae_nctc_13004.yaml`:
  passed, one file and zero errors.
- Structured checks matched identity, stored rank, parent, code and every
  ancestor ID, label, rank and parent link against the taxonomy inventory.
  A complete inventory scan found zero direct children.
- All eight assembly, four typed genome and 33 related-record assertions
  exactly matched the raw/StrainInfo inventories as multisets, including
  decoded nested evidence.
- `just straininfo-query --strain SI-ID26326 --limit 5` passed. Its five
  paths comprise the four target deposits and a distinct local BacDive
  strain for CIP 106585. Only the NCTC path supplies a StrainInfo assembly;
  the unrelated CIP path has no assemblies or existing genome associations.
  Startup checks StrainInfo and ATB provenance with `reproduce=False`, not
  a fresh full-source reproduction.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_lanienae_nctc_13004.yaml`
  passed. No generated record or maintained input was edited.
- `just verify-corpus` was not rerun because it is full-corpus-only.
  Generated pages and full catalog reproduction were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: ignored-file-inclusive target
  searches found no separate history artifact. Strict validation covers
  the embedded seed event.

## Identity and Grounding

The inspected [NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031753)
supports the identifier, label, code, species parent and lineage. It reports
`no rank` rather than the inventory's `STRAIN`. It lists the two str./strain
forms as equivalent and CCUG 44467 under a heterotypic-synonym heading;
the pinned native name catalog records the latter as class `synonym`.

Independent culture authorities support the exact deposit relationship:
[CCUG 44467](https://www.ccug.se/strain?id=44467) lists CIP 106785 and NCTC
13004, [NCTC 13004](https://www.culturecollections.org.uk/nop/product/campylobacter-lanienae-2)
lists those deposits and type status, and
[DSM 101946](https://www.dsmz.de/collection/catalogue/details/culture/DSM-101946)
traces to NCTC 13004. All four whole identifiers pass the repository's
pinned CAFI-based normalizer, including the BV-BRC spelling `NCTC:13004`.
This is deposit evidence, not merely a shared taxon name.

The target genome is the GTDB cluster representative. Representative
status still does not make a single strain identical to the whole species;
the broader exact synonym is unsupported.

## Evidence

| Claim group | Inspected evidence and conclusion |
| --- | --- |
| Taxonomy, names and scope | `data/raw/ncbitaxon_taxa.tsv:220786` supplies stored taxonomy and three synonyms. Native names begin at `data/catalog/ncbi_names-0005.jsonl.gz:29980`. `curation/seed_scope.tsv:10790` supports the six-source seed rationale. |
| Counts | `data/raw/gtdb_mappings.tsv:1320` and `gtdb_species.tsv:40567` supply 42; BacDive row 53447 supplies one strain; MediaDive row 93 supplies one medium (693); Madin row 591 supplies one trait assertion; BactoTraits row 68 supplies five trait assertions; NCBI supplies one NAME. These counts retain separate units and do not prove a set of measured phenotypes. |
| GTDB census | Parsing every native GTDB shard found 42 members: 41 with NCBI species taxid 75658 and one with target 1031753. Target `RS_GCF_002139935.1` is representative at `data/catalog/gtdb_genomes-0009.jsonl.gz:19204`. The mapping inventory also maps the species cluster broadly to parent 75658. |
| BacDive | `data/bacdive/records.jsonl.gz:53446` supplies BacDive 131136, four deposits, strain taxid 1031753, species taxid 75658 and explicit type status. Genome reference 66792 supplies unversioned GCA_002139935 and BV-BRC 1031753.3. |
| NCBI assemblies | `data/catalog/ncbi_genbank-0001.jsonl.gz:34929` and `ncbi_refseq-0001.jsonl.gz:19423` supply GCA_002139935.1/GCF_002139935.1, explicit paired links, target taxid, whole strain identifier NCTC 13004, sample SAMN03737977 and projects PRJNA66799/PRJNA224116. Both describe assembly from type material. |
| GTDB genome links | The native representative row explicitly supplies NCTC 13004, both versioned NCBI accessions, sample SAMN03737977 and project PRJNA224116. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:3100` supplies genome 1031753.3, GCA_002139935.1, chromosome CP015578, NCTC 13004/NCTC:13004, sample SAMN03737977 and project PRJNA66799. |
| GOLD related records | `data/gold/organisms.jsonl.gz:9252` supplies Go0010518 with both NCTC fields and taxid 1031753. `projects.jsonl.gz:9117` links Gp0010518 to that organism and PRJNA66799, with blank BioSample. `organisms.jsonl.gz:450602` supplies DSM-associated Go0619954 at species taxid 75658. The YAML correctly preserves related records without inventing a GOLD assembly or sample link. |
| StrainInfo | `data/straininfo/records.jsonl.gz:23080` supplies SI-ID26326 and version DOI 10.60712/SI-ID26326.3. Target deposit links are at `strain_links.tsv:11071` and the following three rows. `assemblies.tsv:1820` preserves the unversioned accession and exact NCTC deposit evidence. |

The StrainInfo sequence-to-deposit boundary is supported explicitly:

- SI-DP83909, NCTC 13004: unversioned GCA_002139935 plus nucleotide
  AB542727, AF043425, DQ174181, DQ174238 and KF855289.
- SI-DP329620, CCUG 44467: nucleotide AY628402 and JX912520 only.
- SI-DP329621, CIP 106785, and SI-DP905945, DSM 101946: no explicit
  StrainInfo sequence assertion in this native record.

Gene and rRNA references remain outside genome counts. The inspected
[LPSN species page](https://lpsn.dsmz.de/species/campylobacter-lanienae) and
Table 1 of the inspected
[primary 16S study](https://journals.asm.org/doi/10.1128/jcm.41.6.2537-2546.2003)
associate the type strain with AF043425. The
[MediaDive 693 target view](https://mediadive.dsmz.de/medium/693?bacdive=131136)
explicitly names DSM 101946, corroborating the one-medium attestation;
the review does not expand that count into an inferred phenotype.

## Completeness

Ignored-file-inclusive ID/name/slug searches covered reports, history,
curation, raw, ATB and StrainInfo uncompressed inventories. They found
source rows and the legacy page path, but no prior target review or separate
history artifact. Deposit/sample searches of ATB TSVs and StrainInfo
exclusions found no target match. Decompressed native searches included
ignored files under catalog, BacDive, BV-BRC, GOLD and StrainInfo. An exact
GOLD organism/project-ID search found the three cited native rows, not an
analysis chain for this target. The full ATB TSV.XZ was not scanned.
These are bounded local findings, not a claim about every remote resource.

The single listed strain is uncapped. Eight assembly assertions retain
three distinct accession strings; four typed genome assertions retain two
identifiers. Repetition records distinct source support, not extra genomes.

The apparent type-flag omission is consistent with the current schema,
not a finding. `is_type_strain` is defined in
`src/taxonmech/schema/taxonmech.yaml:477` relative to an LPSN name of the
record's taxon. The strain node has no such species-name mapping. The
parent `data/taxa/bacteria/campylobacter_lanienae.yaml` already carries
LPSN 783595 and this same BacDive strain with `is_type_strain: true` and
`classified_as: NCBITaxon:1031753`. Its type evidence is not lost from
the corpus. The seeder's taxon-local designation lookup explains the
difference; no broad nomenclature block should be copied onto this strain.

The native SI-ID group also includes CIP 106585, SI-DP155648, classified
as Streptococcus pneumoniae (1313), unlike CIP 106785. The query keeps that
path on local BacDive 139375 with no transferred target sequences. It is
not an additional deposit of the target record. Preserve this source-group
conflict rather than inferring biological equivalence from group membership.

The iModulonDB runner was unavailable on PATH and the ignored-inclusive
sibling Mechs manifest search found no claw project during this review
session. Its fallback homepage supplied no inspectable dataset content.
No dataset match or expression-module evidence was established. The YAML's
gene descriptions are sequence metadata, not functional assertions.

## Findings

- **Blocker:** None found in primary identity, structure or deposit joins.
- **Major (1): Species membership is promoted to strain identity.** The
  exact synonym `Campylobacter lanienae` and identity xref derive from a
  closeMatch to a 42-genome species cluster. Being the type strain and
  cluster representative does not make the strain equivalent to the species.
  `src/taxonmech/seed.py:451` and the subsequent synonym/xref block lack
  an infraspecific identity guard. The maintained owners are
  `build_document`, `tests/test_seed.py`, and the upstream kg-microbe GTDB
  mapping transform consumed by `src/taxonmech/extract.py`.
- **Minor (1): NCBI rank discrepancy.** The browser says `no rank` while
  the inventory/YAML say `STRAIN`. `src/taxonmech/ncbi_taxdump.py` directly
  normalizes source rank. The pinned archive was not found by an
  ignored-inclusive checkout filename search in this session; original
  snapshot rank versus import error remains unresolved.
- **Minor (2): Independent live accession verification is incomplete.**
  GTDB, GOLD, BV-BRC, the NCBI assembly and all seven nucleotide requests
  failed. StrainInfo returned a JavaScript shell and the DOI request failed;
  PubMed returned browser-check pages. Explicit native evidence and the
  passing local query support retained links, but do not establish current
  remote status. Retrieval failures are not proof of broken identifiers.

## Recommended Edits

1. Add rank-aware GTDB identity handling in `src/taxonmech/seed.py`, with
   strain/type-strain regression coverage in `tests/test_seed.py`. Keep
   membership, cluster count and explicit genome links; do not derive
   species-level exact synonyms for infraspecific records. Review the
   upstream mapping semantics without mechanically reversing predicates.
2. Recover the hash-verified taxonomy pin before changing rank inputs or
   importer behavior. Keep the NCBI parent chain and scope intact.
3. Retry the unavailable accession authorities. Preserve StrainInfo's
   deposit-specific sequence evidence and its explicit versioned DOI;
   do not import CIP 106585 into this strain or expand its sequence links.

## Follow-up Checks

- Run focused seeder regression tests, the normal dry run, separately
  authorized `just seed-canary NCBITaxon:1031753`, both target validators
  and full `just verify-corpus` after any future fix.
- Inspect taxon 1031753 in the archive pinned by `conf/ncbi_taxdump.yaml`,
  SHA256 `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- Keep the parent's type flag and target classification unchanged while
  testing the GTDB identity correction.
- Recheck the exact StrainInfo paths. Only NCTC receives its source
  assembly; CCUG receives only its two source nucleotide references;
  source-group co-membership must never transfer either set.

## Additional Notes

The initial NCBI request failed; its BacDive link then resolved. The native
StrainInfo NCTC deposit has `typeStrain: false`, contrary to the inspected
NCTC/LPSN evidence, while the other three target deposits have true flags.
This source discrepancy does not override TaxonMech's LPSN-based contract.
DSMZ and the native BacDive record also mention AF043424 for UB 994, whereas
LPSN and the inspected paper associate NCTC 13004 with AF043425. The YAML
does not transfer AF043424 from that co-occurrence; no such addition is
recommended. No paid research, GitHub mutation, history entry or status
promotion occurred.
