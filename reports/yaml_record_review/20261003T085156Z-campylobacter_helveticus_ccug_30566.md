# YAML Record Review: Campylobacter helveticus CCUG 30566

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_helveticus_ccug_30566.yaml`
- Started UTC: 2026-10-03T08:48:53Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:51:56Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1031739` denotes
Campylobacter helveticus CCUG 30566 beneath species `NCBITaxon:28898`.
The record declares `STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED`
mapping status. It has ten ancestors, two NCBI exact synonyms, code 11,
one BacDive strain with one culture identifier, eight related-record
assertions, four source attestations and one seed event. No GTDB mapping,
nomenclature block, genome assembly, genome record or causal graph is present.
The index entry is `data/taxa/PATHS.tsv:13129`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_helveticus_ccug_30566.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_helveticus_ccug_30566.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV comparison confirmed identity, stored rank, parent,
  code and all ten ancestor IDs, labels, ranks and parent links. A complete
  taxonomy-inventory scan found zero direct children.
- All eight related-record dictionaries matched their maintained inventory
  rows exactly after structured parsing of the nested StrainInfo JSON.
  They represent five distinct related IDs, not eight distinct resources.
- The pinned CAFI CCUG entry accepts the entire accession 30566. The local
  `normalize_culture_identifier` and `culture_curie_key` functions both
  returned `CCUG-30566` for the respective source and target identifiers.
- `just straininfo-query --deposit SI-DP130066 --evidence --limit 2` passed
  and returned exactly one path, SI-ID52284 -> SI-DP130066 -> CCUG 30566 ->
  BacDive 146194. Assemblies and existing genome associations were empty.
  The command executes StrainInfo and ATB provenance gates with
  `reproduce=False`; this is not a full corpus reproduction run.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_helveticus_ccug_30566.yaml`
  passed. No source or generated record was edited.
- `just verify-corpus` was not rerun: it is full-corpus-only. Catalog-wide
  hashes outside the query's component checks and rendered pages were not
  revalidated. `just validate-products` is not applicable without graph nodes.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation.

## Identity and Grounding

The pinned taxonomy and native NCBI name rows agree on CCUG 30566 and taxon
1031739. The inspected [BacDive record](https://bacdive.dsmz.de/strain/146194)
connects that deposit to the same strain-level taxon and parent species.
The [collection's own CCUG 30566 page](https://www.ccug.se/strain?id=30566)
independently supports the culture identifier and C. helveticus assignment.

StrainInfo carries species taxon 28898 while BacDive carries strain taxon
1031739. The match is supported by the exact deposit identifier, not by
equating those taxon IDs. The source-specific classification is correctly
preserved. Similarly, SI-ID, SI-DP, DOI, GOLD organism/project and BioProject
IDs retain distinct roles and do not inflate genome counts.

Live NCBI taxonomy requests by ID, Info mode and name were unavailable, as
were the BioProject, GOLD, StrainInfo and DOI endpoints attempted below.
No current external rank discrepancy is asserted. Pinned source support and
successful local component checks are distinguished from live resolution.

## Evidence

| Claim group | Inspected evidence and interpretation |
| --- | --- |
| NCBI identity, lineage and synonyms | `data/raw/ncbitaxon_taxa.tsv:220783` supplies the stored label/rank/parent/code. `data/catalog/ncbi_names-0005.jsonl.gz:29971` and the next two rows support the scientific name and `strain CCUG 30566`/`str. CCUG 30566` equivalents. All ancestors were checked independently. |
| BacDive strain and deposit | `data/raw/bacdive_strains.tsv:68470` supplies BacDive 146194, taxon 1031739, CCUG-30566 and zero medium rows. `data/raw/culture_collection_strains.tsv:21045` supplies the same culture/taxon association. `data/bacdive/records.jsonl.gz:68469` explicitly links the deposit and both strain/species taxon IDs, with type-strain value no and empty sequence information. |
| GOLD organism | `data/gold/organisms.jsonl.gz:9942` identifies Go0011318 and taxon 1031739. Both the culture-collection field and the strain field contain the complete CCUG 30566 token. The latter also carries Burnens E2289-9. |
| GOLD project | `data/gold/projects.jsonl.gz:9803` connects Gp0011318 to Go0011318 and PRJNA66791, with an empty BioSample field. The six corresponding rows in `data/raw/strain_related_records.tsv:161606` and the next five rows preserve the two distinct source-field paths for each of three related IDs. They are not accidental duplicate genome assertions. |
| StrainInfo source | `data/straininfo/records.jsonl.gz:40040` supplies SI-ID52284, DOI 10.60712/SI-ID52284.2 and its archive entry, published-online status, BacDive 146194 and the sole own deposit SI-DP130066. That deposit is CCUG 30566, available, non-erroneous, in a non-deprecated CCUG collection, and has typeStrain false. No sequence array is present. |
| StrainInfo projection | `data/straininfo/strain_links.tsv:36467` and the two rows beginning at `data/straininfo/related_records.tsv.gz:86559` reproduce the matched deposit, source fields, statuses, versioned DOI and species taxon. The documented query confirmed the same evidence path and no assembly association. |
| Attestations and event | `data/raw/gold_organisms.tsv:409` supports one ORGANISM assertion; `data/raw/madin_taxa.tsv:588` supports one TRAIT_ASSERTION, not an independently checked phenotype. The taxonomy and BacDive inventories support one NAME and one STRAIN respectively. `curation/seed_scope.tsv:22136` supplies the 2026-09-12 four-source rationale retained by the seed event. |

The source DOI is a versioned strain-record identifier, not a paper citation
or genome identifier. Its spelling and version are supported by the native
StrainInfo archive, although the [DOI resolver](https://doi.org/10.60712/SI-ID52284.2)
and [live strain page](https://straininfo.dsmz.de/strain/52284) were unavailable.

The [LPSN species page](https://lpsn.dsmz.de/species/campylobacter-helveticus)
identifies the type deposit as CCUG 30682, alongside other collection numbers,
not CCUG 30566. The target correctly does not acquire species nomenclature
or a type-strain flag merely from its parent-species association.

## Completeness

Ignored-file-inclusive searches covered the exact identifier, name and slug
in review reports, history, curation, raw, ATB and StrainInfo uncompressed
inventories. No prior target report or separate history artifact was found
in those surfaces before this report. Exact BacDive/culture/SI IDs were
searched separately to avoid misleading numeric-substring hits. No assembly
or genome inventory row matched the target strain/culture keys; the validated
StrainInfo query independently returned no existing genome association.

Decompressed JSONL.GZ/TSV.GZ searches covered `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/` and `data/straininfo/` for exact taxon fields,
CCUG 30566 including separator variants, the source Burnens aliases, Go/Gp
IDs and the search-discovered RM4087 lead. No eligible assembly, BV-BRC or
GTDB genome row was found for the target in those surfaces. A loose alias
search hit E. coli strain PNUSAE228991, GCA_059603105.1; its unrelated taxon
and substring-only resemblance were rejected, not used as a join.

GOLD Go0299332 carries the bare Burnens E2289-91 alias and species taxon
28898, but no culture-collection value. It is not an additional eligible
CCUG deposit path under the documented whole-identifier rule. The GOLD
organism/project searches found no analysis linked to Go0011318/Gp0011318;
there is no supported IMG or assembly claim to manufacture. Empty sample
and sequence fields likewise provide no ATB sample join. The compressed ATB
full TSV.XZ was not scanned independently.

These are bounded source findings, not a claim that the strain has never
been sequenced. A literature search found an RM4087/CCUG 30566 lead; the
attempted primary full-text page returned a browser challenge, so snippets
were not used to establish a new synonym, phenotype or genome accession.

## Findings

- **Blocker:** None found in identity or file structure.
- **Major:** None found in the represented links or their source scope.
- **Minor (1): Inconsistent auxiliary Burnens designation.** The joined GOLD
  organism/project calls the strain Burnens E2289-9, whereas the collection's
  own page and native StrainInfo relation use Burnens E2289-91. The explicit
  CCUG 30566 deposit agrees, so this does not invalidate the existing join.
  The YAML accurately preserves GOLD's wording; the discrepancy belongs to
  the GOLD source, followed by a reviewed refresh through
  `src/taxonmech/gold_genomes.py` and the extraction workflow, not silent
  rewriting of verbatim provenance in generated YAML.
- **Minor (1): Incomplete live authority resolution.** Current NCBI rank,
  live BioProject/GOLD records and the versioned StrainInfo DOI could not be
  fetched. Their identifiers and chains are supported by pinned sources,
  and StrainInfo/ATB provenance checks passed, but those facts do not prove
  current remote availability. Retry before treating live correspondence
  as verified; no unsupported data correction follows from network failure.

## Recommended Edits

1. No generated-record edit is justified now. Preserve all eight evidence
   paths, the exact CCUG deposit match, source-specific taxon IDs and distinct
   related-record types.
2. Reconcile the Burnens spelling with GOLD in a separately authorized
   source-maintenance task. Preserve current source text until a supported
   upstream correction or explicit provenance-aware overlay exists; do not
   merge the two GOLD organism records on alias resemblance alone.
3. Retry live NCBI, GOLD, BioProject and StrainInfo resolution. A verified
   taxonomy-source change belongs to `conf/ncbi_taxdump.yaml` and
   `src/taxonmech/ncbi_taxdump.py`; a StrainInfo change belongs to its pinned
   snapshot and `src/taxonmech/straininfo.py`/`straininfo_links.py` workflow.

## Follow-up Checks

- Re-run `just straininfo-query --deposit SI-DP130066 --evidence --limit 2`
  after any source refresh. Require the same own-deposit path, not merely
  shared SI-ID membership or a BacDive cross-reference.
- Resolve taxon 1031739, PRJNA66791, Go0011318, Gp0011318 and DOI
  10.60712/SI-ID52284.2 at their authorities. Compare source versions before
  changing a stored field. The pinned NCBI archive remains the reference
  for any rank-import audit.
- For a supported future genome addition, require an explicit assembly or
  sequence path through the matched deposit; do not turn a project, alias,
  DOI, source type label or species association into a genome link.
- After an authorized source change, rebuild the relevant component, run
  `just seed-canary NCBITaxon:1031739`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

The BacDive text extraction included an unqualified Type strain heading,
while its retained native record says no, StrainInfo says false, and LPSN's
type list names a different CCUG deposit. The extracted heading was not used
to override these explicit source assertions or to diagnose a TaxonMech
type-flag defect; its display context was not independently inspected.

iModulonDB is not applicable: aggregate source counts and deposit identity
do not assert a specific gene, regulator or expression module. No paid
research, external messages, GitHub mutation, history addition or review-status
promotion occurred. The taxdump archive was not recovered, genome sequences
were not downloaded, and this report does not imply human-reviewed status.
