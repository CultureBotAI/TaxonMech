# YAML Record Review: Campylobacter hyointestinalis subsp. lawsonii CCUG 27631

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_hyointestinalis_subsp_lawsonii_ccug_27631.yaml`
- Started UTC: 2026-10-03T09:02:34Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:05:33Z
- Verdict: needs curation

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1031752` denotes
Campylobacter hyointestinalis subsp. lawsonii CCUG 27631, a bacterial strain
beneath subspecies 91353 and species 198. It declares `STRAIN`, `EXACT`
grounding, `SEEDED` mapping status, eleven ancestors and genetic code 11.
It has a 13-genome GTDB species mapping, two NCBI equivalent-name synonyms,
one GTDB exact synonym/xref, one BacDive strain, five source attestations
and one seed event. Its strain carries nine assembly assertions, seven
typed genome assertions and 28 related-record assertions. The index entry
is `data/taxa/PATHS.tsv:13133`. There is no causal graph or nomenclature block.

## Validation

- `just validate data/taxa/bacteria/campylobacter_hyointestinalis_subsp_lawsonii_ccug_27631.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_hyointestinalis_subsp_lawsonii_ccug_27631.yaml`:
  passed, one file and zero errors.
- Structured YAML/TSV checks passed for identity, stored rank, parent, code
  and all eleven ancestor IDs, labels, ranks and parent links. The complete
  taxonomy inventory has zero direct children of this target.
- All nine assembly, seven typed genome and 28 related-record assertions
  exactly matched the raw/StrainInfo inventories as multisets, including
  parsed nested evidence. The first comparison script needed its own
  `_evidence_json` column-to-object conversion corrected; the corrected
  comparison passed without changing repository data.
- `just straininfo-query --strain SI-ID8231 --limit 3` passed and returned
  exactly two deposit paths. Both have empty StrainInfo assembly lists;
  only SI-DP33731 supplies the two nucleotide accessions. The query checks
  StrainInfo and ATB provenance with `reproduce=False`; this is not a fresh
  full-source reproduction pass.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_hyointestinalis_subsp_lawsonii_ccug_27631.yaml`
  passed. The target and maintained inputs were not edited.
- `just verify-corpus` was not rerun: it is full-corpus-only. Generated
  pages and full catalog reproduction were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-file-inclusive
  search found no separate target history artifact. Strict validation
  covers the embedded seed event.

## Identity and Grounding

The inspected [NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031752)
supports the ID, name, two equivalent names, code and subspecies parentage.
It reports `no rank`, not the inventory's `STRAIN`; the pinned source rank
requires follow-up. Primary identity is not in doubt.

[BacDive 145089](https://bacdive.dsmz.de/strain/145089) links CCUG 27631 and
LMG 15993 to the target and its genome identifiers. The inspected
[CCUG deposit](https://www.ccug.se/strain?id=27631) explicitly lists LMG 15993
as another collection accession. CAFI entries 3 and 2 and the existing
`normalize_culture_identifier` function accept the complete CCUG and LMG
accessions, including source spelling `LMG:15993`; no substring join is needed.

GTDB assigns one target genome to its broader species cluster, but that
does not establish that the species name is an exact synonym of this strain.
This unsupported equivalence is the major finding, not a rejection of the
supported deposit-to-genome associations.

## Evidence

| Claim group | Inspected source and conclusion |
| --- | --- |
| Taxonomy and scope | `data/raw/ncbitaxon_taxa.tsv:220785` supports the stored taxonomy and NCBI synonyms. Native names are at `data/catalog/ncbi_names-0005.jsonl.gz:29977` and the following two rows. `curation/seed_scope.tsv:14829` supplies the five-source rationale. |
| Counts | Mapping row `data/raw/gtdb_mappings.tsv:1319` and species row `data/raw/gtdb_species.tsv:40568` carry 13. BacDive row 67370 supplies one strain; GOLD row 411 supplies one organism; Madin row 590 supplies two trait assertions. The NCBI NAME count is one. These units must not be summed or interpreted as confirmed phenotypes. |
| GTDB cluster | Parsing every native GTDB shard found 13 members: eleven with NCBI taxid 91353, one with 198 and one with target 1031752. Representative `RS_GCF_013372165.1`, strain CHY5, is at `data/catalog/gtdb_genomes-0001.jsonl.gz:10275`, not the target genome. The mapping inventory also maps the cluster to 198 and 91353. |
| BacDive strain | `data/bacdive/records.jsonl.gz:67369` explicitly supplies strain taxid 1031752, both deposits, a non-type status and reference 66792 for GCA_001643975, IMG 2687453245 and BV-BRC 1031752.3. The raw culture inventory retains both deposits under this target. |
| NCBI assemblies | `data/catalog/ncbi_genbank-0001.jsonl.gz:13759` and `ncbi_refseq-0001.jsonl.gz:3375` supply GCA_001643975.1 and GCF_001643975.1, explicit paired-assembly links, target taxid, whole strain identifier CCUG 27631, sample SAMN03737974 and projects PRJNA66797/PRJNA224116 respectively. The live GenBank assembly page title also resolves to this strain. |
| GTDB genome | `data/catalog/gtdb_genomes-0004.jsonl.gz:35990` supplies RS_GCF_001643975.1, GCA_001643975.1, the CCUG deposit, sample, project PRJNA224116 and nonrepresentative status. |
| BV-BRC genome | `data/bvbrc/bvbrc-0000.jsonl.gz:3099` explicitly links genome 1031752.3, GCF_001643975.1, CP015576, CCUG 27631, LMG:15993, sample SAMN03737974 and project PRJNA66797. |
| GOLD chain | `data/gold/organisms.jsonl.gz:9939` supplies Go0011315 and both CCUG source fields. `projects.jsonl.gz:9800` links Gp0011315 to that organism, sample and project. `analyses.jsonl.gz:75483` links Ga0129127 through Gp0011315 to GCA_001643975.1, CP015576 and IMG 2687453245. The blank direct analysis-organism field does not break this explicit project chain. |
| Other GOLD organism | `data/gold/organisms.jsonl.gz:214643` supplies Go0276607 with LMG 15993 and species taxid 198. The YAML preserves it only as an organism association, including that different source classification, not as an inferred additional genome. |
| StrainInfo | `data/straininfo/records.jsonl.gz:8231` supplies SI-ID8231, version DOI 10.60712/SI-ID8231.2, own eligible deposits SI-DP33730/33731, published/available statuses and BacDive 145089. Both sequences explicitly name SI-DP33731 only. Links are retained at `strain_links.tsv:34758` and the next row; six related assertions start at decompressed `related_records.tsv.gz:82451`. |

StrainInfo's AF097683 is a 16S reference and KF855284 an atpA gene reference,
not whole genomes. The inspected primary paper
[Species-Specific Identification of Campylobacters by Partial 16S rRNA Gene Sequencing](https://journals.asm.org/doi/10.1128/jcm.41.6.2537-2546.2003)
also associates CCUG 27631 with AF097683 in Table 1. No functional,
transcriptomic or phenotype claim was inferred from these accessions.

The inspected [LPSN subspecies page](https://lpsn.dsmz.de/subspecies/campylobacter-hyointestinalis-lawsonii)
names different type deposits, including CCUG 34538 and LMG 14432. The native
BacDive and StrainInfo records explicitly say this target is not a type
strain. Its omission of a type flag is appropriate; a broad subspecies
nomenclature block should not be copied onto the strain.

## Completeness

Ignored-file-inclusive target ID/name/slug searches covered reports,
history, curation, raw, ATB and StrainInfo uncompressed inventories. They
found the source rows and legacy page path, but no prior target report or
separate history artifact. Deposit/sample searches of ATB TSVs and
StrainInfo exclusions found no target candidate or exclusion there. Native
JSONL.GZ/TSV.GZ searches under catalog, BacDive, BV-BRC, GOLD and StrainInfo
included decompression and ignored files; the GTDB species census was
additionally parsed across every shard. The ATB full TSV.XZ was not scanned.
These findings are bounded to the inspected local surfaces.

The single listed strain is uncapped here and retains its available
multi-source associations. Nine assembly assertions are three distinct
accession strings, including the unversioned BacDive accession; seven typed
assertions are three identifiers. Repeated identifiers preserve different
source fields, not extra genomes. Gene, deposit, sample, project, GOLD and
SI-ID identifiers correctly remain outside genome counts.

The structured iModulonDB runner was not on PATH; an ignored-inclusive
manifest search beneath the sibling Mechs directory found no claw project.
The fallback iModulonDB homepage returned no inspectable dataset content.
No covered dataset was established. This limits optional transcriptomic
context, not the explicit sequence-to-deposit evidence checked here.

## Findings

- **Blocker:** None found in primary identity, structure or deposit joins.
- **Major (1): A GTDB species is promoted to strain identity.** The YAML's
  exact synonym `Campylobacter lawsonii` and identity xref follow a
  `closeMatch` to a 13-genome species spanning three NCBI nodes. Target
  membership supports association, not species/strain equivalence.
  `src/taxonmech/seed.py:451` treats every closeMatch as identity and adds
  the exact synonym/xref without an infraspecific rank guard. Future fixes
  belong in `build_document`, its tests and the upstream kg-microbe GTDB
  mapping transform consumed by `src/taxonmech/extract.py`.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the retained inventory/YAML report `STRAIN`. The importer directly
  normalizes `nodes.dmp` rank. The archive pinned by `conf/ncbi_taxdump.yaml`
  was not found in the ignored-inclusive checkout filename search, so
  source-version divergence versus import error remains unresolved.
- **Minor (2): Independent live verification remains incomplete.** GTDB,
  GOLD, BV-BRC, IMG, BioSample, BioProject, RefSeq and nucleotide requests
  failed; StrainInfo returned only a JavaScript shell and its DOI did not
  resolve through this tool. The native evidence is explicit and the local
  query passed, but these outcomes cannot establish current remote state.
  No broken identifier is inferred solely from a retrieval failure.

## Recommended Edits

1. Add a rank-aware identity guard to `src/taxonmech/seed.py` and an
   infraspecific regression case in `tests/test_seed.py`. Retain supported
   GTDB membership/count evidence and deposit-linked genomes, but do not
   derive an exact strain synonym/xref from species membership alone.
   Review the maintained upstream mapping semantics; do not mechanically
   reverse broad/narrow predicates or change the cluster count to one.
2. Recover and inspect the hash-verified pinned NCBI source before changing
   the rank inventory or importer. Keep the NCBI parent chain intact.
3. Retry unavailable authorities before promoting review status. Preserve
   exact accession versions, sequence/deposit boundaries and source taxids.

## Follow-up Checks

- Test the future identity guard against species and strain cases; rerun
  the normal input refresh, seed dry run and separately authorized
  `just seed-canary NCBITaxon:1031752`, both target validators and the full
  `just verify-corpus`.
- Inspect target 1031752 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- Retry the failed authority endpoints and exact StrainInfo DOI. Confirm
  that neither nucleotide accession moves to SI-DP33730 and that neither
  deposit acquires a StrainInfo assembly merely from existing associations.
- Preserve the distinction among paired NCBI assemblies, unversioned
  accessions, genome identifiers and sample/project/organism records.

## Additional Notes

The initial NCBI request failed, then the BacDive link resolved successfully.
The BacDive text extraction contains an unqualified type-strain heading;
it was not treated as an affirmative flag against explicit native records.
The genome-announcement DOI and PMC fallback also failed retrieval; their
search leads were not used as source text. No paid research, GitHub
mutation, history entry or review-status promotion occurred.
