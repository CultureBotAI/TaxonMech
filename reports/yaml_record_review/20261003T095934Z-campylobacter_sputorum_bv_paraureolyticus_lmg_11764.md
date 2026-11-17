# YAML Record Review: Campylobacter sputorum bv. paraureolyticus LMG 11764

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_sputorum_bv_paraureolyticus_lmg_11764.yaml`
- Started UTC: 2026-10-03T09:56:40Z
- Finished UTC: 2026-10-03T09:59:34Z
- Verdict: needs curation

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1032066` denotes
LMG 11764, stored as `STRAIN` under biovar 593874 in `BACTERIA`.
It has eleven ancestors, code 11, `EXACT` grounding, `SEEDED` mapping
status, two NCBI synonyms, one GTDB mapping/synonym/xref, zero attached
strains, four source attestations and a seed event. The index entry is
`data/taxa/PATHS.tsv:13152`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_sputorum_bv_paraureolyticus_lmg_11764.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_sputorum_bv_paraureolyticus_lmg_11764.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code, all
  eleven ancestor IDs/labels/ranks/parent links and both NCBI synonyms.
  There are no children or BacDive classifications at the target in the
  complete corresponding inventories; the zero strain count agrees.
- `just straininfo-query --strain SI-ID264336 --evidence --limit 10`:
  passed, three matched deposits. Its source/configuration/hash validation
  uses `reproduce=False`, not full source replay. Native records were also
  inspected; none of the three deposits supplies a StrainInfo assembly.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_sputorum_bv_paraureolyticus_lmg_11764.yaml`:
  passed. No taxon or maintained input changed.
- `just verify-corpus` was skipped because it is full-corpus-only.
  Full source reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped after an ignored-inclusive target
  search found no separate history artifact. The embedded event was read
  and included in strict validation.

## Identity and Grounding

The inspected [NCBI page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032066)
supports the identifier, label, two equivalent names, code and ancestry,
but currently reports no rank instead of the pinned STRAIN. This does
not by itself prove an importer bug or wrong taxon identity.

The inspected [CCUG 30522 page](https://www.ccug.se/strain?id=30522)
confirms LMG 11764, CIP 105555 and LCDC 12978 as collection references
and explains its former biovar-paraureolyticus designation. Native and
inspected [BacDive 136424](https://bacdive.dsmz.de/strain/136424) classify
the culture at species 206, not at the target strain node. Genomic
source fields disagree over LMG 11764 versus LMG 17589; shared taxonomy
or an assembly description containing both names does not resolve that.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220790`, native name rows
  `data/catalog/ncbi_names-0005.jsonl.gz:29993` through 29995, and
  `curation/seed_scope.tsv:26076` support the pinned identity, two
  equivalent-name synonyms, one NAME attestation and seed rationale.
- `data/raw/gtdb_mappings.tsv:1332` supplies the closeMatch and count 11.
  A fresh complete native cluster selection found eleven genomes at six
  NCBI IDs: 206 (four), 32024 (three), and one each at 1032066, 1031920,
  1031754 and 32023. The target's RS_GCF_002220755.1 is not the cluster
  representative. Species membership is not strain identity, and the
  native Campylobacter_F suffix must not become Campylobacter F.
- `data/raw/gold_organisms.tsv:413` supports the stored count two;
  `data/raw/madin_taxa.tsv:594` supports four TRAIT_ASSERTION rows.
  These are source-record counts, not two proven cultures or four
  independently validated phenotypes. The individual transformed GOLD
  and Madin edges were not replayed. `src/taxonmech/extract.py:676`
  counts transformed GOLD subclass edges, a different input surface
  from the native GOLD workbook projection.
- Native GOLD has three organism rows carrying taxon 1032066:
  Go0009295 names LMG 11764; Go0622807 names DSM 5363; Go0622808 names
  ATCC 33562. Their locations are `data/gold/organisms.jsonl.gz:8286`,
  453426 and 453427. The latter two match a different local culture,
  BacDive 2125. Do not infer that their source taxon ID makes them LMG
  11764 aliases. Go0283415 instead names LMG 17589 at species 206.
- Full native BacDive `data/bacdive/records.jsonl.gz:58728` names four
  culture identifiers and supplies unversioned GCA_002220755 and BV-BRC
  1032066.3 in genome fields. Its type flag is no. The live page retains
  the dual-name genome description, rather than resolving the conflict.
- Native GenBank `ncbi_genbank-0001.jsonl.gz:38545`, RefSeq
  `ncbi_refseq-0001.jsonl.gz:22393`, GTDB
  `gtdb_genomes-0010.jsonl.gz:40273` and BV-BRC
  `data/bvbrc/bvbrc-0000.jsonl.gz:3135` all carry taxon 1032066 and
  an LMG 11764 organism label but LMG 17589 in the strain field.
  They agree on the versioned assembly pair and SAMN03737990. Preserve
  GenBank/BV-BRC PRJNA66807 separately from RefSeq PRJNA224116.
- Full SI-ID264336 at `data/straininfo/records.jsonl.gz:206280` names
  LMG 11764 / SI-DP38722, status dead, taxon 593874; CCUG 30522 /
  SI-DP130649, available, taxon 206; and CIP 105555 / SI-DP149643,
  available, without an explicit deposit taxon. DOI
  10.60712/SI-ID264336.2 identifies the source record version.
  Historical dead-deposit identity is retained; it is not availability.
  No sequence is supplied. The query correctly labels BacDive genomes
  as existing associations, not StrainInfo-supported sequences.
- Full SI-ID10640 at native row 10640 is a separate published record
  for LMG 17589 / SI-DP41662, with aliases BU 464B and Vandamme R-121.
  It also supplies no sequence. `data/straininfo/exclusions.tsv:1543`
  records no eligible own-deposit match, and the ignored-inclusive
  BacDive inventory search found no LMG 17589 deposit. This is not a
  license to join it to LMG 11764 through the shared biovar.
- A focused context check of the BacDive 136424 entry on
  `data/taxa/bacteria/campylobacter_sputorum.yaml` found one BacDive
  assembly, one BacDive genome record and sixteen related assertions,
  including the three own StrainInfo deposit paths. Thus culture evidence
  is retained elsewhere, with its original sources. This is not a review
  verdict on the entire species record.

iModulonDB is not applicable to this taxon/count record. No functional
claim was inferred from incidental literature or genome predictions.

## Completeness

Ignored-inclusive ID/name/slug and exact LMG-accession searches covered
reports, history, curation, raw, ATB and StrainInfo inventories. No prior
target report or separate history artifact was found. Decompressed
JSONL.GZ/TSV.GZ searches included ignored files under catalog, BacDive,
BV-BRC, GOLD and StrainInfo. Zero attached strains follows the BacDive
classification/subtree contract; it is not absence of the culture.

The full ATB TSV.XZ and every live auxiliary accession/DOI were not
audited. GTDB failed, BCCM returned an empty loading page, and live
StrainInfo returned a JavaScript shell. CCUG succeeded through its
BacDive link after a direct request failed. The 2017 genome-publication
search was a lead only: PMC returned a browser challenge and its DOI
request failed, so no uninspected article claim resolves the two LMG IDs.

## Findings

- **Blocker:** None found; the target NCBI identifier resolves correctly.
- **Major (1): A GTDB species is promoted to strain identity.** The
  eleven-member species becomes an EXACT_SYNONYM and identity-style
  xref on a single strain, with the suffix also flattened. The owner is
  `src/taxonmech/seed.py:451` and its synonym emission. Review upstream
  kg-microbe GTDB mapping semantics consumed by `src/taxonmech/extract.py`
  and add rank/scope-aware coverage in `tests/test_seed.py`.
- **Minor (1): Rank-source discrepancy.** Current NCBI says no rank;
  the pinned inventory says STRAIN. Inspect the pinned source before
  deciding between refresh and importer correction. Owners:
  `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`.
- **Minor (2): Culture context and genomic identity conflict are hidden.**
  This node exposes zero strains while culture evidence is retained at
  species 206, including an unresolved LMG 11764/17589 genome mismatch.
  The target does not itself assert a particular assembly, so this is
  not a finding of a wrong attached genome here. Source-labeled context
  belongs in the seeder/templates and harmonization guidance; resolving
  conflicting source identities requires source-level evidence, not a
  new alias invented by `src/taxonmech/genome_sources.py`.
- **Minor (3): GOLD count scope is not transparent.** Two transformed
  organism assertions coexist with three native taxon-tagged organism
  rows, two naming another local culture. The count is reproduced from
  its inventory, but is not verified as a complete native census or as
  independent LMG 11764 identity evidence. Owners: the upstream GOLD
  transform, `src/taxonmech/extract.py:676`, `conf/sources.yaml` and
  source-coverage documentation. Do not replace two with three blindly.

## Recommended Edits

Do not edit generated YAML. Make GTDB identity promotion rank/scope-aware
while preserving native suffixes and the cluster count eleven. Separately
investigate the rank and transformed GOLD membership. Improve culture
navigation only with explicit provenance and an unresolved-identity
qualification. Do not merge the two LMG deposits, transfer a source
sequence between them, append `.1` to BacDive's unversioned accession,
or treat a project/organism identifier as a genome.

## Follow-up Checks

- Inspect the rank in the archive pinned by `conf/ncbi_taxdump.yaml`.
  An ignored-inclusive checkout filename search did not locate that
  archive or nodes.dmp; no absence outside this checkout is claimed.
- Obtain the primary culture and genome-deposition evidence distinguishing
  LMG 11764 and LMG 17589 before changing links. Reconcile the exact
  manifest-pinned transformed GOLD edges with the native three rows.
- After separately authorized fixes, run focused seeder/source-link tests,
  normal input refresh, `just seed-canary NCBITaxon:1032066`, both target
  validators and full `just verify-corpus`. Check pages if templates change.

## Additional Notes

The review leaves counts in their own source units. No paid research,
outbound messages, GitHub mutation, history addition or review-status
promotion occurred. Eukaryota was not reviewed.
