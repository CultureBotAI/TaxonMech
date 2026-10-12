# YAML Record Review: Aliarcobacter cryaerophilus D2610

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aliarcobacter_cryaerophilus_d2610.yaml`
- Started UTC: 2026-10-03T10:17:58Z
- Finished UTC: 2026-10-03T10:20:46Z
- Verdict: needs curation

## Target

The entire generated TaxonRecord was read. `NCBITaxon:1032071` denotes
D2610, stored as STRAIN below species 28198 in BACTERIA. It contains
ten ancestors, code 11, EXACT grounding, SEEDED mapping status, two
NCBI synonyms, one GTDB mapping/synonym/xref, zero attached strains,
four source attestations and a seed event. Its index entry is
`data/taxa/PATHS.tsv:13156`.

## Validation

- `just validate data/taxa/bacteria/aliarcobacter_cryaerophilus_d2610.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/aliarcobacter_cryaerophilus_d2610.yaml`:
  passed, one file and zero errors.
- Structured comparisons matched ID, label, stored rank, parent, code,
  all ten ancestor IDs/labels/ranks/parent links and both NCBI synonyms.
  Complete corresponding inventory scans found no child taxa or BacDive
  classifications, consistent with the zero strain count.
- `just straininfo-query --strain SI-ID976 --evidence --limit 10`:
  passed, zero matched deposits. Source/configuration/hash checks use
  `reproduce=False`, not full source replay. The complete native
  StrainInfo record and explicit exclusion were separately inspected.
- `git diff --exit-code -- data/taxa/bacteria/aliarcobacter_cryaerophilus_d2610.yaml`:
  passed. No taxon or maintained input changed.
- `just verify-corpus` was skipped because it is full-corpus-only.
  Full source reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped after an ignored-inclusive target
  ID/name/slug search found no separate history artifact. The embedded
  event was read and included in strict validation.

## Identity and Grounding

The inspected [NCBI record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032071)
supports the target identifier, label, ancestry and code but reports
no rank, not STRAIN. It labels Arcobacter cryaerophilus D2610 a
homotypic synonym and Aliiarcobacter cryaerophilus D2610 a heterotypic
synonym. The YAML presents both as exact, losing that source distinction.
This is not evidence that two biologically different D2610 cultures have
been demonstrated; it is an unresolved synonym-scope conflict.

The inspected [ATCC 49615 page](https://www.atcc.org/products/49615)
identifies the non-type culture as CDC D2610. The authors' inspected
[USDA publication abstract](https://www.ars.usda.gov/research/publications/publication/?seqNo115=358876)
for DOI 10.1128/MRA.01463-18 explicitly links ATCC 49615, CDC D2610
and LMG 10829. This is a direct culture-identity bridge, not a name-only
inference. It also distinguishes that culture from type strain ATCC
43158. The full paper was unavailable; no uninspected methods or
sequence table was used as evidence.

The LPSN species context inspected in this review sequence prefers
[Arcobacter cryaerophilus](https://lpsn.dsmz.de/species/arcobacter-cryaerophilus)
over its validly published Aliarcobacter homotypic synonym. NCBI's
lineage must remain source-specific rather than silently reconciled.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220794`, native names at
  `data/catalog/ncbi_names-0005.jsonl.gz:30008` through 30010 and
  `curation/seed_scope.tsv:26077` support the pinned baseline and seed
  rationale. Both alternate names have native class `synonym`;
  `src/taxonmech/ncbi_taxdump.py:95` unconditionally promotes that
  class, as well as equivalent names, to EXACT_SYNONYM. The live
  homotypic/heterotypic distinction is not retained by that projection.
- `data/raw/gtdb_mappings.tsv:1336` supplies closeMatch and count 147.
  A complete native GTDB shard selection reproduced 147 members at
  ten NCBI taxon IDs: 28198 (114), 2933791 (23), 1977087 (3), and
  one each at 2026809, 1852839, 3429684, 165434, 1032071, 2808971
  and 3429683. The target RS_GCF_003660085.1 at
  `data/catalog/gtdb_genomes-0007.jsonl.gz:39309` is not the
  representative; RS_GCF_014352935.1 / 16CS1292-4 at
  `data/catalog/gtdb_genomes-0013.jsonl.gz:48349` is. The count is
  cluster membership, not 147 D2610 genomes. Native cryaerophilus_A
  is distinct from the unsuffixed GTDB species.
- `data/raw/gold_organisms.tsv:415` supports one transformed ORGANISM
  assertion and `data/raw/madin_taxa.tsv:598` supports three
  TRAIT_ASSERTION rows. Their underlying transformed edges were not
  replayed, and trait counts are not validated phenotype claims.
- Native GenBank `data/catalog/ncbi_genbank-0002.jsonl.gz:44460`
  and RefSeq `data/catalog/ncbi_refseq-0002.jsonl.gz:4586` identify
  latest complete GCA_003660085.1 / GCF_003660085.1, D2610,
  taxon 1032071 and SAMN03737949. Preserve GenBank PRJNA66819
  separately from RefSeq PRJNA224116. The native GTDB target row
  carries the same strain, sample and paired GenBank accession.
- Native BV-BRC at `data/bvbrc/bvbrc-0000.jsonl.gz:3140` supports
  1032071.3, GCA_003660085.1, CP032825, SAMN03737949 and
  PRJNA66819. The bare strain value D2610 is not itself a registered
  collection accession under the current matching contract.
- Native GOLD `data/gold/organisms.jsonl.gz:9919` supplies Go0011293,
  taxon 1032071, culture ATCC 49615 and strain CDC D2610. Row
  346096 supplies Go0496673, also taxon 1032071, with D2610 but an
  empty collection field. Row 180579 supplies Go0242474 / LMG 10829
  at parent species 28198. Thus the transformed count one is not a
  complete count of native rows carrying this target taxon.
- Native project `data/gold/projects.jsonl.gz:9781` connects Gp0011293
  to Go0011293 and PRJNA66819, with no BioSample. Row 268316
  connects Gp0380737 to the different organism Go0496673,
  SAMN03737949 and PRJNA66819. Analysis
  `data/gold/analyses.jsonl.gz:209214` follows Gp0380737 to Ga0349355,
  GCA_003660085.1 and IMG 2843852374. Do not substitute Go0011293
  into this analysis chain merely because it has the desired deposit.
  The inspected [JGI portal](https://genome.jgi.doe.gov/portal/IMG_2843852374/IMG_2843852374.info.html)
  independently labels IMG 2843852374 as D2610 with taxon 1032071.
  Go/Gp/Ga, BioSample and BioProject remain separate entity types.
- Full native StrainInfo `data/straininfo/records.jsonl.gz:976`
  identifies version `10.60712/SI-ID976.2` with two available,
  non-erroneous own deposits: LMG 10829 / SI-DP3948 and ATCC 49615 /
  SI-DP3949. CDC D2610 is a designation. The record supplies LPSN
  773367 but no explicit BacDive ID or NCBI taxon ID. Both deposits
  are non-type. Native evidence exists despite zero overlap matches.

StrainInfo sequence ownership is narrow: FN257290 belongs to LMG 10829;
DQ059481, AB081300, U25805 and AB104483 belong to ATCC 49615.
There is no genome sequence in this SI-ID version. AB081300 has source
type `gene` but a 23S-rRNA description; preserve those original fields
instead of inferring protein coding or a genome. The ATCC page separately
links U25805 as a 16S reference. No function or phenotype was inferred
from any sequence title, and the native nucleotide records are not
evidence that StrainInfo asserts the complete assembly.

## Completeness

Ignored-inclusive ID/name/slug and exact culture-accession searches covered
reports, history, curation, raw, ATB and StrainInfo inventories.
Decompressed native catalog, BacDive, BV-BRC, GOLD and StrainInfo
JSONL.GZ searches were also completed. The full native BacDive projection
has no match for CDC D2610, ATCC 49615 or LMG 10829 in the checked
spellings. The raw BacDive inventory likewise has no corresponding
deposit or target classification. No prior report or separate history
artifact was found.

`data/straininfo/exclusions.tsv:260718` explicitly records
`no_eligible_own_deposit_match` for SI-ID976. Exact identifier searches
of committed links, including StrainInfo TSV.GZ, found no accepted
sequence/deposit join. Longer SI-ID numeric-prefix hits were excluded;
they are unrelated records. This is a BacDive identity-coverage boundary,
not evidence that the culture is absent from StrainInfo or lacks genomes.

No committed ATB row/link for SAMN03737949 was found in the searched
TSV/YAML/JSON surfaces. The full ATB TSV.XZ was not inspected, so
global ATB absence is not established. No culture or genome was added
through shared species identity, the bare designation or an unrelated
type-strain record.

GTDB and live StrainInfo pages were unavailable. PubMed/PMC returned
browser challenges and the journal page failed; the inspected author
institution's abstract supplies only the identity/publication evidence
stated above. Native catalogs support auxiliary accessions, but every
remote accession and DOI was not independently revalidated. Optional
nomenclature, graph and type-strain fields are not required here.
iModulonDB is not applicable to the target's taxon/count assertions;
incidental native sequence titles were not used for expression claims.

## Findings

- **Blocker:** None found; the target taxon and culture bridge are supported.
- **Major (1): A GTDB species is promoted to exact strain identity.**
  The 147-member cluster becomes an EXACT_SYNONYM and identity-style
  xref on D2610, and its `_A` suffix is flattened. Owners:
  `src/taxonmech/seed.py:451`, its synonym emission,
  `tests/test_seed.py` and upstream kg-microbe GTDB mapping semantics
  consumed by `src/taxonmech/extract.py`. Preserve count 147 and
  membership, not an invented count one or automatically reversed SKOS.
- **Major (2): A source synonym qualifier is lost.** Aliiarcobacter
  cryaerophilus D2610 is stored as exact although the inspected NCBI
  page explicitly labels it heterotypic. Arcobacter D2610 is separately
  labeled homotypic. The unconditional plain-synonym promotion cannot
  preserve that distinction. Owners: `src/taxonmech/ncbi_taxdump.py:95`,
  `tests/test_ncbi_taxdump.py` and the upstream NCBI evidence surface.
  Verify the pinned versus current qualifiers; do not assert that the
  spelling variant proves a different biological culture or demote all
  homotypic synonyms indiscriminately.
- **Minor (1): Rank-source discrepancy.** Current NCBI reports no rank;
  the pinned inventory reports STRAIN. Owners: `conf/ncbi_taxdump.yaml`
  and `src/taxonmech/ncbi_taxdump.py` after native-node inspection.
- **Minor (2): Supported culture/genome context is not exposed.**
  The record has zero strains despite primary culture evidence,
  retained StrainInfo deposits and a complete native assembly/genome
  chain. Existing BacDive/deposit requirements explain this and should
  not be bypassed. Owners: evidence-backed culture inventory design,
  `src/taxonmech/bacdive_v2.py`, seeder/templates and harmonization
  guidance for any separately authorized source-qualified context.
- **Minor (3): GOLD count scope is opaque.** The one transformed
  organism assertion differs from two native target-taxoned organisms,
  with a third deposit-related organism at parent species 28198.
  These are different source surfaces, not proof of an arithmetic error.
  Owners: upstream GOLD transform, `src/taxonmech/extract.py:676`,
  `conf/sources.yaml` and source-coverage documentation. Reconcile the
  exact transformed membership before proposing a replacement count.

## Recommended Edits

Do not edit generated YAML. Correct rank/scope-independent GTDB identity
promotion and suffix handling, and preserve or explicitly flag NCBI
synonym qualifier conflicts. Investigate the pinned rank separately.

Use primary deposit evidence to improve maintained identity coverage or
design an explicitly source-qualified context surface. Do not invent a
BacDive identifier, transfer SI-ID976 nucleotides between deposits, claim
that StrainInfo asserts the complete assembly, or bridge the two GOLD
organism IDs through their shared BioProject. Retain the full native
evidence while clarifying transformed counts.

## Follow-up Checks

- Inspect the native node and name classes in the archive pinned by
  `conf/ncbi_taxdump.yaml`. An ignored-inclusive checkout filename
  search did not locate that archive or nodes.dmp; no absence outside
  the checkout is claimed.
- Reconcile the source synonym qualifier and exact GOLD transformed
  membership. Any new deposit representation must preserve own-deposit
  sequence ownership and the distinct organism/project analysis chain.
- After separately authorized fixes, run focused seeder, NCBI-taxdump
  and source-link tests, normal input refresh,
  `just seed-canary NCBITaxon:1032071`, both target validators and
  full `just verify-corpus`. Verify rendering for presentation changes.

## Additional Notes

No curation status, history, source inventory or taxon YAML changed.
No paid research, outbound messages or GitHub mutation occurred.
Eukaryota was not reviewed. Source counts remain in their own units.
ATCC's Belgium location and native GTDB's USA metadata were not
reconciled or imported; neither changes the supported culture bridge.
