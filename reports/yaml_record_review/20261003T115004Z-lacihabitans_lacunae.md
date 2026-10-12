# YAML Record Review: Lacihabitans lacunae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lacihabitans_lacunae.yaml`
- Started UTC: 2026-10-03T11:45:49Z
- Finished UTC: 2026-10-03T11:50:04Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028214`, Lacihabitans lacunae,
rank SPECIES, domain BACTERIA, parent `NCBITaxon:1649462`. The entire
456-line YAML was read. It has EXACT grounding, SEEDED mapping status,
one LPSN name, one GTDB mapping, six synonyms, two xrefs, one BacDive
strain, five source attestations and one embedded seed event. Its eight
assembly, four genome-record and eighteen related-record assertions are
source-specific evidence rows, not counts of distinct genomes.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/lacihabitans_lacunae.yaml` | PASS; no issues, exit 0. |
| `just validate-strict data/taxa/bacteria/lacihabitans_lacunae.yaml` | PASS; one file, zero errors, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive target searches found no separate history entry; strict validation covered the embedded event. |

Structured comparison matched all eleven lineage entries to the pinned
taxonomy inventory. Complete subtree traversal found only this taxon;
the full BacDive inventory contained exactly strain 140675 classified
here. Structured comparisons proved exact reproduction of all eight
assembly, four genome-record and eighteen related-record rows from the
raw inventories. These checks do not substitute for full-corpus validation.

## Identity and Grounding

Raw taxonomy row 219027 and the inspected
[NCBI taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028214)
agree on species identity, rank, genetic code 11 and the NCBI lineage
through Leadbetterellaceae and Lacihabitans. Native NCBI names preserve
the generic synonym Lacihabitans jumunjinensis, its separately related
authority string, the includes-name Leadbetterella sp. HME7103 and the
equivalent name s__Leadbetterella lacunae. The YAML follows these source
categories. The NCBI page's distinction between an effectively published
earlier name and a validly published name is not erased by treating the
generic name as a taxonomic synonym.

Raw LPSN row 31990 supplies name 795648, Kang et al. 2017, the
legitimate/valid/correct flags, citations, sequence accession and only
KCTC 23619 as a type designation. The inspected
[LPSN page](https://lpsn.dsmz.de/species/lacihabitans-lacunae) supports the
identity and correct-name status but additionally lists CECT 7956 and
HME7103. It places the genus in Spirosomataceae, whereas the pinned
NCBI tree uses Leadbetterellaceae; this is a preserved source difference,
not a reason to silently replace the NCBI lineage.

## Evidence

**GTDB species mapping.** Ignored-inclusive decompressed searches of all
native GTDB genome shards found exactly one member of
`s__Leadbetterella lacunae`: representative `RS_GCF_042649125.1`,
CECT 7956, NCBI taxid/species taxid 1028214. It supplies paired
GenBank accession `GCA_042649125.1`, sample `SAMN43282068` and RefSeq
project `PRJNA224116`. The species-scoped mapping and GENOME count of
one agree with raw GTDB row 1222 and native RS232 metadata. The different
GTDB genus, class Bacteroidia and family Spirosomataceae are not substituted
into the NCBI tree. This is not a strain record receiving a species-cluster
count. The GTDB web endpoint was inaccessible; native metadata supplied
the independent source check.

**Type strain.** Raw BacDive row 62960, the complete native identity and
sequence object, and inspected identity sections of the
[BacDive page](https://bacdive.dsmz.de/strain/140675) agree on strain
140675, target taxid, type status and KCTC 23619 / CECT 7956 / HME 7103.
The LPSN KCTC overlap supports the generated type flag. The parser accepts
CECT 7956 and KCTC 23619 as collection joins and rejects HME 7103 and
its encoded HME%207103 form as unregistered collection keys. Keeping the
source designation is not permission to promote it to a genome join.

**Assembly and sample chain.** Exact-taxid searches across native current
and historical NCBI assembly shards returned the paired
`GCA_042649125.1` / `GCF_042649125.1` Contig assembly, ASM4264912v1,
explicit strain CECT 7956, sample `SAMN43282068` and WGS
`JBHRYQ000000000.1`. Both are marked assemblies from type material.
GenBank supplies `PRJNA595761`; RefSeq supplies `PRJNA224116`.
Native BV-BRC `1028214.3` independently supplies the GenBank assembly,
sample and primary project through its explicit strain field. Its
genome-status value Complete is not an assembly-level assertion and
does not override the NCBI Contig level.

Native GOLD `Go0717148 -> Gp0880784 -> Ga0689480` connects CECT 7956,
the same sample, `PRJNA595761`, `GCA_042649125.1` and IMG `8144586957`.
The analysis has an empty organism field but an unambiguous project
chain. Separate collection-ID and strain-field evidence rows are retained
deliberately. Native BacDive reference 124043 supplies the unversioned
GenBank accession, assembly name and target taxid; its missing accession
version is not silently supplied from a different source.

**Publications and marker.** The inspected
[original publisher abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.001899)
explicitly identifies HME7103 as the type strain equivalent to KCTC 23619
and CECT 7956. Inspected
[PubMed metadata](https://pubmed.ncbi.nlm.nih.gov/28809153/) independently
connects PMID 28809153, DOI 10.1099/ijsem.0.001899 and the species paper.
LPSN supplies the notification-list citation and JF700250 marker.
Native BacDive associates JF700250 with HME7103 and also retains the
optional MT760283 marker for CECT 7956. The notification DOI publisher
page repeatedly timed out; the live JF700250 NCBI page was inaccessible.
Their raw/source associations were checked, but independent live
accession metadata and notification-DOI resolution remain unverified.

**Scope and audit.** The five NAME/GENOME/STRAIN/ORGANISM attestations
match their separate inventories; units are not summed. The scope row
14824 and legacy page row 653 identify this species. The embedded
2026-09-13 seed event accurately describes generated provenance and
does not claim human review. No causal, phenotype or expression-module
claim is introduced. iModulonDB is not applicable: the nomenclatural
16S marker is not a gene-function or transcriptomics claim.

## Completeness

One non-blocking nomenclatural provenance gap is recorded below. The
type strain and genome remain correctly identified, and optional
phenotype, graph and curator-evidence fields need not be populated.

Ignored-inclusive searches covered target identifier, label and slug in
raw inventories, `curation/` and `history/`, plus target and deposit keys
in all ATB/StrainInfo TSV overlays. No separate history entry or matching
overlay was found. A whole-file decompressed native ATB search for
`SAMN43282068` found no occurrence, so no ATB sample link is supported
by that snapshot. Native StrainInfo searches for the target, deposits,
HME designation and SI-ID26349 DOI/exact ID found no object. The BacDive
StrainInfo 26349 linkout is a lead, not proof of a local overlay omission;
its live page was inaccessible. These are bounded local-snapshot results,
not claims that records cannot exist in the live databases. Ignored files
were included in these absence checks.

## Findings

Blocker: 0. Major: 0. Minor: 1.

**Minor - CECT 7956 is absent from LPSN type-strain designations.**
The YAML nomenclature list and `data/raw/lpsn_names.tsv:31990` retain
only KCTC 23619. LPSN and the original species paper independently
identify CECT 7956 as another deposit of the same type strain. It is
already present in BacDive culture IDs and explicitly supports every
cross-source genome join, so this is a provenance/completeness gap,
not a wrong strain or missing genome.

The maintained owner is the kg-microbe LPSN source/transform feeding
`data/transformed/lpsn/edges.tsv`, consumed by
`src/taxonmech/extract.py:445`. `src/taxonmech/seed.py:405` faithfully
projects `type_strain_ids`; the omission predates YAML generation.
The upstream transformed files were unavailable at configured paths,
so source age versus transform loss cannot be distinguished here.
This review does not establish a specific parser defect.

## Recommended Edits

1. In a later curation change, refresh or repair the maintained upstream
   LPSN type-designation evidence for name 795648 so CECT 7956 is retained.
   Inspect the native payload and transformed edges before assigning the
   exact loss stage. Do not hand-edit generated YAML or raw tables.
2. Add a regression at the responsible transform/extractor layer, then
   re-extract and canary-reseed `NCBITaxon:1028214` through the documented
   commands. Preserve both registered deposits and the type flag. Do not
   make the personal HME designation a collection join without authority.

## Follow-up Checks

Compare the refreshed type-designation row against LPSN and the original
paper; verify the strain remains BacDive 140675 and the genome join stays
CECT 7956. Run both record validators, focused regression tests and then
the full-corpus reproduction check after an authorized regeneration.
Retry the notification DOI and marker authority endpoints when available;
do not interpret access failures as invalid identifiers. Recheck any new
StrainInfo or ATB object independently before adding overlay evidence.

## Additional Notes

This was a read-only review. Only this new report was written; the target
YAML, generated pages, source inventories, statuses and both history
surfaces were unchanged. No paid research, GitHub mutation, source-index
rebuild or cache regeneration was performed. A standalone `uv run`
coverage-count invocation later hit a cache permission error; the same
read-only count succeeded using the existing `.venv/bin/python`. This
does not alter the completed validator results reported above.
