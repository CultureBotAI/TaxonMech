# YAML Record Review: Aliarcobacter cryaerophilus ATCC 43158

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aliarcobacter_cryaerophilus_atcc_43158.yaml`
- Started UTC: 2026-10-03T10:13:07Z
- Finished UTC: 2026-10-03T10:16:40Z
- Verdict: needs curation

## Target

The complete 1,356-line generated TaxonRecord was read, including a
separate read of the middle section truncated by the initial display.
`NCBITaxon:1032070` denotes ATCC 43158, stored as STRAIN below species
28198 in BACTERIA. It has ten ancestors, code 11, EXACT grounding,
SEEDED status, four NCBI synonyms, one GTDB mapping/synonym/xref,
one BacDive entry with ten deposit/alias identifiers, seven source
attestations and an embedded seed event. The index entry is
`data/taxa/PATHS.tsv:13155`.

## Validation

- `just validate data/taxa/bacteria/aliarcobacter_cryaerophilus_atcc_43158.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/aliarcobacter_cryaerophilus_atcc_43158.yaml`:
  passed, one file and zero errors.
- Structured comparisons matched ID, label, stored rank, parent, code,
  all ten ancestor IDs/labels/ranks/parent links and four NCBI synonyms.
  A complete inventory scan found no children and exactly one BacDive
  classification, with the same ten identifiers as the YAML.
- Exact multiset comparisons, decoding the TSV evidence JSON columns,
  matched all 20 assembly, 13 genome-record and 66 related-record
  assertions against raw plus StrainInfo inventories. The assembly
  split is 17 raw plus 3 StrainInfo; related records are 46 plus 20.
- `just straininfo-query --strain SI-ID944 --evidence --limit 10`:
  passed, eight matched deposits. Displayed output was truncated;
  the full native source and exact committed assertions were separately
  inspected. Its provenance checks use `reproduce=False`, not full
  source replay.
- A direct call to `taxonmech.atb_catalog.crosslink_exclusion_reason`
  on committed SAMN03737948 metadata returned
  `metadata_identity_flags:META_FAIL`, matching the exclusion inventory.
- `git diff --exit-code -- data/taxa/bacteria/aliarcobacter_cryaerophilus_atcc_43158.yaml`:
  passed. No taxon or maintained input changed.
- `just verify-corpus` was skipped because it is full-corpus-only.
  Full source reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped after ignored-inclusive target
  ID/name/slug searches found no separate history artifact. The embedded
  seed event was read and included in strict validation.

## Identity and Grounding

The inspected [NCBI page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032070)
supports the identifier, label, ancestry and code. It calls all four
stored NCBI synonyms homotypic, including the two LMG names; their
exact scope is supported here. It reports no rank instead of STRAIN.

The inspected [BacDive 2091](https://bacdive.dsmz.de/strain/2091) and
[CCUG 17801](https://www.ccug.se/strain?id=17801) pages support the
culture identity and A169/B / 02766 designations. The inspected LPSN
pages identify [Arcobacter cryaerophilus](https://lpsn.dsmz.de/species/arcobacter-cryaerophilus)
as the correct name and
[Aliarcobacter cryaerophilus](https://lpsn.dsmz.de/species/aliarcobacter-cryaerophilus)
as a validly published homotypic synonym. They list ATCC 43158 and
the relevant CCUG, DSM, CIP, LMG and NCTC deposits as the type culture.
This disagreement with NCBI's preferred genus must not be resolved by
silently rewriting the NCBI lineage.

The absent strain-node type flag is not a false claim of non-type status.
The seeder derives the flag from LPSN names mapped to the record's own
taxon. A focused context check of parent species 28198 found BacDive
2091 with `classified_as: NCBITaxon:1032070` and `is_type_strain: true`.
This check does not constitute a review of the full parent record.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220793`, native name rows at
  `data/catalog/ncbi_names-0005.jsonl.gz:30003` through 30007 and
  `curation/seed_scope.tsv:7206` support the pinned baseline and seed
  rationale. Native synonym classes are plain `synonym`; the inspected
  authority's homotypic display and collection evidence support their
  identity in this case.
- `data/raw/gtdb_mappings.tsv:1335` supplies closeMatch and count
  three. A complete native GTDB shard selection reproduced three
  members: RS_GCF_003660105.1 / ATCC 43158, representative, and
  RS_GCF_006165035.1 / LMG 9904 at taxon 1032070; plus
  RS_GCF_002992955.1 / LMG 24291 at species 28198. Locations are
  `data/catalog/gtdb_genomes-0015.jsonl.gz:7702`, 37808 and
  `data/catalog/gtdb_genomes-0014.jsonl.gz:46032`. A species remains
  a broader concept than its type strain, even with these related
  culture deposits.
- `data/raw/bacdive_strains.tsv:2086` reproduces the designation,
  ten culture values and strain classification. Full native BacDive
  `data/bacdive/records.jsonl.gz:2085` has strain taxon 1032070 and
  species taxon 28198, DOI `10.13145/bacdive2091.20260601.11`, and
  type flag yes. Its explicit genome fields supply both unversioned
  assemblies, both BV-BRC IDs and both IMG IDs with reference 66792.
- Native GenBank `data/catalog/ncbi_genbank-0002.jsonl.gz:44461`
  and `data/catalog/ncbi_genbank-0005.jsonl.gz:6890` support latest
  GCA_003660105.1 / ATCC 43158 / SAMN03737948 / PRJNA66817 and
  GCA_006165035.1 / LMG 9904 / SAMN04027997 / PRJNA294647.
  RefSeq `data/catalog/ncbi_refseq-0002.jsonl.gz:4587` and 22614
  supply the paired GCF accessions, both under PRJNA224116. Preserve
  Complete Genome versus Chromosome and all source-supplied versions.
- Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3138` and 3139
  support 1032070.4 and 1032070.5 with the corresponding assemblies,
  samples and projects. The first matches both strain ATCC 43158 and
  culture_collection ATCC:43158. The second matches strain LMG 9904;
  its separate LMG 9904T value is not silently normalized into that
  deposit. Multiple source-field assertions are intentional provenance.
- Native GOLD organism `data/gold/organisms.jsonl.gz:9920` supplies
  Go0011294 with ATCC 43158 in both culture and strain fields.
  Projects at `data/gold/projects.jsonl.gz:268315` and 488230 connect
  Gp0380736 and Gp0653637 to this organism and the respective two
  sample/project pairs. Analyses at `data/gold/analyses.jsonl.gz:209684`
  and 367816 connect Ga0349825 to IMG 2847260338 / GCA_003660105.1
  and Ga0561560 to IMG 8002856167 / GCA_006165035.1. Their empty
  organism fields are supported through explicit project-to-organism
  chains, not guessed name joins.
- Six GOLD organism IDs are retained as culture-matched related records.
  In addition to Go0011294, native row 267656 supplies Go0358483 /
  LMG 9904 at taxon 1032070; rows 454237, 454239, 454240 and 454241
  supply Go0623624 / NCTC 11885, Go0623626 / LMG 7536, Go0623627 /
  DSM 7289 and Go0623628 / CCUG 17801 at species 28198. None is
  promoted to a genome identifier.
- Taxon counts reproduce `data/raw/gold_organisms.tsv:414` (one),
  `data/raw/mediadive_taxa.tsv:95` (one, medium 693),
  `data/raw/madin_taxa.tsv:597` (three) and
  `data/raw/bactotraits_taxa.tsv:69` (four). The inspected
  [MediaDive page](https://mediadive.dsmz.de/medium/693?bacdive=2091)
  explicitly associates medium 693 with DSM 7289. The BacDive raw
  strain's medium_count is zero, explaining its omission on the strain
  entry; taxon and strain transformed MediaDive edges are separately
  counted by `extract_mediadive`. The underlying transformed edges were
  not replayed, so do not equate a missing strain count with no known
  medium or treat trait counts as independently verified phenotypes.

Full native StrainInfo at `data/straininfo/records.jsonl.gz:944`
identifies `10.60712/SI-ID944.2`, BacDive 2091 and twelve own deposits.
Eight overlap the current BacDive inventory. The source supplies LPSN
773367 but no explicit NCBI taxon for these deposits; the YAML correctly
does not fabricate a StrainInfo taxon ID. Sequence ownership is retained:

| Own deposit | Retained source sequences |
| --- | --- |
| ATCC 43158 / SI-DP112227, available | GCA_003660105, GCA_006165035 and AB104482. |
| LMG 9904 / SI-DP3871, available | GCA_006165035, EU669899 and GU291960. |
| LMG 7536 / SI-DP3873, dead | X80383 only; historical identity, not availability. |
| CCUG 17801 / SI-DP3872; NCTC 11885 / SI-DP3874; DSM 7289 / SI-DP128222; CIP 104014 / SI-DP148606; CCM 3933 / SI-DP217399 | Deposit and strain-record references only. |

GCA_006165035 explicitly names both SI-DP3871 and SI-DP112227, so
its two assertions are supported rather than a group-based transfer.
Three gene accessions and one 23S accession remain NUCLEOTIDE_SEQUENCE
related records outside genome counts. No BacDive-reference conflict
flag is needed for these matching sources.

The other four own deposits are JCM 5361, CNCTC 7379, LMG 24291 and
CECT 8222. Only LMG 24291 / SI-DP834468 supplies additional sequences:
FN257285, MG195893 and GCA_002992955. They are not transferred to
ATCC 43158 through SI-ID grouping, shared taxonomy or BacDive's 16S
context. An ignored-inclusive search found none of these four deposits
in the BacDive inventory or committed StrainInfo strain links. That
bounded source limitation is not a failed own-deposit sequence join.

## Completeness

Ignored-inclusive target ID/name/slug searches covered reports, history,
curation and committed raw/ATB/StrainInfo inventories; compressed native
catalogs, BacDive, BV-BRC, GOLD and StrainInfo were also searched.
No prior target report or separate history artifact was found.

The absence of an ATB genome link is supported, not missing evidence.
`data/atb/assemblies.tsv:3779` retains SAMN03737948 with available
FASTA, ERZ4158321, source runs and SeqKit sum, but META_FAIL warnings.
`data/atb/exclusions.tsv:2066` records the matching exclusion reason.
Neither availability nor a valid ENA identifier overrides the identity
warning. Searches found no committed ATB rows for SAMN04027997 or
SAMN07515811. The full ATB TSV.XZ was not inspected; no global source
absence is claimed.

LPSN inventory rows `data/raw/lpsn_names.tsv:1136` and 15388 retain
Aliarcobacter and Arcobacter names and the type deposits. Only the former
maps to species 28198; neither maps directly to this strain node.
Consequently no local nomenclature block or type flag is generated.
The parent record retains the synonym status and type role. A missing
optional graph is not a defect.

Live GTDB and four nucleotide-accession pages were unavailable; the
genome announcement link also failed, so it was not used as evidence.
StrainInfo returned a JavaScript shell. Native records support the
accession/DOI-version checks, but every remote accession and DOI was
not independently revalidated.

The iModulonDB runner was not on PATH; ignored-inclusive sibling
pyproject searches found comments referencing claw, not an available
claw project in that bounded scope. The iModulonDB page had no readable
content. No dataset was verified, and no functional or transcriptomic
claim was inferred from sequence titles.

## Findings

- **Blocker:** None found; culture and NCBI target identity are supported.
- **Major (1): A GTDB species becomes an exact synonym of its strain.**
  Count three is reproducible, but species identity is not strain
  identity, including for a representative/type strain. Owners:
  `src/taxonmech/seed.py:451`, `tests/test_seed.py` and upstream
  kg-microbe GTDB semantics consumed by `src/taxonmech/extract.py`.
  Preserve the cluster count and membership while correcting automatic
  exact-synonym/xref promotion; do not force count one.
- **Minor (1): Rank-source discrepancy.** Current NCBI says no rank;
  the pinned inventory says STRAIN. Owners: `conf/ncbi_taxdump.yaml`
  and `src/taxonmech/ncbi_taxdump.py` after native-node inspection.
- **Minor (2): Source nomenclature context is hard to see at the strain.**
  NCBI retains Aliarcobacter while LPSN prefers Arcobacter; type-role
  context exists on the parent rather than here. This is a visibility
  limitation, not a wrong culture identity or justification for changing
  lineage. Owners: `src/taxonmech/seed.py`, templates and harmonization
  guidance; any future context must name the parent taxon and source.
- **Minor (3): GOLD count scope is not transparent.** One transformed
  organism attestation coexists with two native organism rows explicitly
  carrying taxon 1032070, both already retained as related records.
  The count matches its inventory but is not a complete native census.
  Owners: upstream GOLD transform, `src/taxonmech/extract.py:676`,
  `conf/sources.yaml` and source-coverage documentation. Do not replace
  one with two without reconciling the manifest-pinned transformed edges.

## Recommended Edits

Do not edit generated YAML. Make GTDB identity promotion rank/scope-aware,
investigate the native rank, and expose source-qualified species-name/type
context without changing NCBI ancestry. Clarify the GOLD attestation's
transformed-edge scope. Preserve the complete assembly/source assertions,
unversioned accessions, own-deposit StrainInfo joins and ATB exclusion.
Additional deposit coverage belongs in evidence-backed identity inputs,
not a relaxation of sequence ownership or automatic alias equivalence.

## Follow-up Checks

- Inspect the pinned NCBI node; the ignored-inclusive checkout filename
  search did not locate the archive or nodes.dmp. No absence outside the
  checkout is claimed.
- Reconcile the transformed GOLD membership and separate taxon/strain
  MediaDive edges with their native evidence before altering counts.
- After separately authorized changes, run focused seeder/source-link
  tests, normal input refresh, `just seed-canary NCBITaxon:1032070`,
  both target validators and full `just verify-corpus`. Recheck all
  three StrainInfo assembly assertions, deposit-specific nucleotides,
  dead-deposit status and the META_FAIL exclusion. Check pages if
  source-context presentation changes.

## Additional Notes

No curation status, history, source inventory or taxon YAML changed.
No paid research, outbound messages or GitHub mutation occurred.
Eukaryota was not reviewed. Source counts remain in their own units;
20 assembly assertions do not mean 20 distinct biological genomes.
