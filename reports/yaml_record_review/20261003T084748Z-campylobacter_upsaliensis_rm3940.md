# YAML Record Review: Campylobacter upsaliensis RM3940

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_upsaliensis_rm3940.yaml`
- Started UTC: 2026-10-03T08:46:42Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:47:48Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031733` denotes
Campylobacter upsaliensis RM3940 beneath species `NCBITaxon:28080`. It has
`STRAIN` rank, `BACTERIA` domain, `EXACT` grounding and `SEEDED` mapping
status. The record contains ten ancestors, one GTDB mapping, three exact
synonyms, a GTDB xref, code 11, zero attached strains, three attestations
and one seed event. Its index entry is `data/taxa/PATHS.tsv:13128`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_upsaliensis_rm3940.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_upsaliensis_rm3940.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV checks confirmed identity, stored rank, parent, code
  and all ten ancestor IDs, labels, ranks and parent links. The full taxonomy
  inventory contains zero direct children of this target.
- A structured native GTDB scan counted 168 members of the exact species
  cluster across seven NCBI taxa. Only one member has taxon 1031733. The
  mapping inventory has seven targets for the cluster: five closeMatch and
  two broadMatch rows.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_upsaliensis_rm3940.yaml`
  passed. No source or generated record was edited.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full source
  hashes/censuses and rendered pages were not checked. Focused checks are
  not evidence of a fresh reproduction pass.
- `just validate-products` is not applicable without causal-graph nodes.
  `just validate-history` was not run: an ignored-file-inclusive target search
  found no separate history artifact. The embedded event was inspected and
  covered by strict validation.

## Identity and Grounding

The inspected [NCBI RM3940 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1031733&mode=Info)
supports the identifier, label, two strain-name equivalents, code 11 and
lineage. It reports `no rank`, unlike the pinned inventory's `STRAIN`.
Identity, parentage and species-and-below eligibility are supported; the
source-version rank discrepancy remains unresolved.

The GTDB species concept `s__Campylobacter_D upsaliensis` is not identical
to the single strain-level taxon RM3940. Its promoted exact synonym,
`Campylobacter D upsaliensis`, and equivalence-style xref overstate the
source evidence. GTDB's class/genus labels remain source classification,
not permission to replace the carried NCBI lineage.

## Evidence

| Claim group | Inspected evidence and interpretation |
| --- | --- |
| NCBI identity and synonyms | `data/raw/ncbitaxon_taxa.tsv:220782` supports the stored target fields. `data/catalog/ncbi_names-0005.jsonl.gz:29968` and the following two rows support the scientific name and the `strain RM3940`/`str. RM3940` equivalents. All ten ancestor rows were compared separately. |
| GTDB mapping and total | `data/raw/gtdb_mappings.tsv:1317` supplies closeMatch and 168; `data/raw/gtdb_species.tsv:40551` supplies the same species-cluster total. Native metadata contain 157 genomes at species taxon 28080, six at taxon 2974565 and one each at five other taxa, including RM3940. |
| Target member | `data/catalog/gtdb_genomes-0002.jsonl.gz:37042` identifies RS_GCF_013372245.1 with taxon 1031733, bare strain RM3940, GenBank GCA_013372245.1, BioSample SAMN03737994 and RefSeq project PRJNA224116. It is not the GTDB representative. |
| Representative | RS_GCF_900637395.1 is the GTDB representative, with taxon 28080 and designation NCTC11541, not RM3940. The species cluster includes distinct strain identities. |
| Native assembly catalogs | `data/catalog/ncbi_genbank-0012.jsonl.gz:2024` and `data/catalog/ncbi_refseq-0003.jsonl.gz:498` identify latest paired assemblies GCA_013372245.1/GCF_013372245.1, taxon 1031733, species 28080, strain RM3940 and sample SAMN03737994. Projects are PRJNA66789 and PRJNA224116 respectively. |
| Native BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:3096` supplies genome 1031733.3, the same GenBank assembly/sample, PRJNA66789 and nucleotide accession CP053849. Its source-specific representative label is not the GTDB representative flag. |
| Native GOLD | `data/gold/organisms.jsonl.gz:10417` identifies Go0011840, taxon 1031733 and bare strain RM3940 with an empty collection field. `data/gold/projects.jsonl.gz:10275` links Gp0011840 to that organism and PRJNA66789, with an empty sample field. No analysis-project row was found by exact Go/Gp search in the decompressed GOLD catalog. Do not invent an IMG link. |
| Attestations and event | `data/raw/madin_taxa.tsv:587` supports four trait-assertion rows, not four independently checked phenotypes. The NCBI count is one name assertion. `curation/seed_scope.tsv:36137` supports the 2026-09-12 three-source rationale retained by the seed event. The GTDB count is a cluster total requiring explicit scope. |

The inspected [NCBI BioProject PRJNA66789 page](https://www.ncbi.nlm.nih.gov/bioproject/66789)
independently connects RM3940 and taxon 1031733 to GCA_013372245.1 and
SAMN03737994, and links GOLD Gp0011840. It supports the taxon-to-genome
association, not a culture-deposit join. The target cites no paper or LPSN
name; search-discovered studies were not used to introduce extra claims.

## Completeness

Identifier, exact name and slug were searched with
`rg --no-ignore --hidden` across reports, history, curation, raw, ATB and
StrainInfo uncompressed inventories. Before this report, matches were the
taxonomy, GTDB mapping, Madin, scope and legacy-page rows; no prior review
or separate history artifact was found in those surfaces. A decompressed
ignored-file-inclusive search of JSONL.GZ/TSV.GZ under `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/` and `data/straininfo/` checked
exact numeric taxonomy fields, current/name variants, slug and standalone
RM3940. The nine native matches are described above; none was a target
BacDive or StrainInfo record.

A separate exact-taxid/standalone-RM3940 search in the BacDive and
culture-collection inventories returned no candidates. These findings are
bounded to the searched sources, including ignored files, not worldwide
absence claims. The compressed ATB full TSV.XZ was not searched.

The [BacDive 2126 type-strain page](https://bacdive.dsmz.de/strain/2126)
identifies C231, including deposits DSM 5365, ATCC 43954 and NCTC 11541,
with taxon IDs 1121269 and 28080. It is not evidence of an RM3940 deposit.
Likewise, the LPSN inventory entry `lpsn:774391` at
`data/raw/lpsn_names.tsv:16020` concerns parent species 28080. Do not transfer
its type designations or nomenclature onto RM3940.

Zero attached strains is consistent with the current supported-BacDive/
registered-deposit boundary. Bare RM3940 cannot establish a collection join,
and native genome existence does not change that rule. A future direct
taxon-to-genome representation is separate from the erroneous synonym.
GOLD attestation omission reflects the maintained KGX inventory, not absence
from the native workbook. Empty phenotype and causal-graph slots should not
be filled from unreviewed species-level material.

## Findings

- **Blocker:** None found in primary identity or file structure.
- **Major (1): Species-cluster association promoted to strain equivalence.**
  The imported GTDB closeMatch is treated as identity by
  `src/taxonmech/seed.py:451`; lines 467-469 add an exact synonym and xref.
  The resulting species-only synonym is unsupported for RM3940, because the
  cluster contains 167 other genome rows and six other NCBI taxon IDs.
  Owners are the upstream kg-microbe GTDB predicate rule, consumed through
  `src/taxonmech/extract.py:extract_gtdb`, and the local promotion logic in
  `src/taxonmech/seed.py:build_document`. The count 168 remains the supported
  cluster total and is not itself proof of strain identity.
- **Minor (1): Unresolved rank discrepancy.** The inspected NCBI browser
  reports `no rank`, while the pinned inventory says `STRAIN`.
  `src/taxonmech/ncbi_taxdump.py` normalizes the supplied rank; no inference
  from the strain name occurs there. The source archive pinned in
  `conf/ncbi_taxdump.yaml` is unavailable in this checkout, leaving
  source-version divergence versus import error unresolved.

## Recommended Edits

1. In a separately authorized correction, prevent the seeder from promoting
   species-cluster membership to exact identity for an infraspecific taxon
   merely because its imported mapping is closeMatch. Preserve both supported
   NCBI synonyms and the original GTDB source identifier/classification.
2. Review the owning upstream mapping rule and re-extract as needed. Resolve
   scope and direction from evidence; do not mechanically flip the predicate
   or change the species total from 168 to one.
3. Add a `tests/test_seed.py` regression for this strain-level mapping and
   retain supported species-level behavior. Keep genome, sample, project and
   culture-deposit identities distinct; do not attach C231's deposits.
4. Inspect the pinned NCBI rank before correcting input/importer behavior.
   Do not hand-edit the generated YAML or reconcile its lineage to GTDB.

## Follow-up Checks

- Run focused and existing seeder tests; confirm ID 1031733, parent 28080
  and its two NCBI synonyms remain without species-wide exact equivalence.
- Recheck the native GTDB total 168, seven taxon IDs and single RM3940
  member. Preserve the evidence chain for GCA/GCF_013372245.1 and SAMN03737994.
- Recover the original archive pinned in `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`,
  and inspect the exact 1031733 `nodes.dmp` row.
- After an authorized source/seeder correction, run the normal refresh,
  `just seed-canary NCBITaxon:1031733`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

Initial NCBI requests failed, but the Info page was retrieved and inspected
on retry. The live GTDB tree remained unavailable; pinned RS232 metadata
support the mapping finding. The ignored-file-inclusive repository taxdump
filename search in this session found no archive or `nodes.dmp`; copies
outside this checkout were not assessed. Full source hashes, external
sequence payloads and rendered pages were not revalidated.

iModulonDB is not applicable to aggregate trait counts without specific gene,
regulator or expression-module claims. No paid research, outbound messages,
GitHub mutation, history addition or review-status promotion occurred.
