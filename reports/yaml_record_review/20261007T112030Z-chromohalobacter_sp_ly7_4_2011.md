# YAML Record Review: Chromohalobacter sp. LY7-4(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chromohalobacter_sp_ly7_4_2011.yaml`
- Started UTC: 2026-10-07T11:16:48Z
- Finished UTC: 2026-10-07T11:20:30Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. It represents
`NCBITaxon:1035879`, Chromohalobacter sp. LY7-4(2011), rank
`SPECIES`, domain `BACTERIA`, with parent `NCBITaxon:2628571`
(unclassified Chromohalobacter). It contains ten root-first lineage
entries, genetic code 11, `EXACT` grounding, `SEEDED` mapping
status, zero BacDive strains, one NCBI name attestation, and one
source-seeding event.

No synonyms, nomenclature, GTDB mappings, listed strains, genome links,
phenotypes, or causal graphs are asserted. The generated YAML is read-only;
maintained owners for any future supported change are
`src/taxonmech/extract.py`, `src/taxonmech/seed.py`, and the
scope table `curation/seed_scope.tsv`.

## Validation

- `just validate data/taxa/bacteria/chromohalobacter_sp_ly7_4_2011.yaml`:
  passed, exit 0, no schema issues.
- `just validate-strict data/taxa/bacteria/chromohalobacter_sp_ly7_4_2011.yaml --out /private/tmp/chromohaloLy742011-strict.tsv`:
  passed, one file, zero errors; the TSV was read and contains only its
  header. Commands used the existing environment, offline uv resolution,
  and a temporary cache.
- Structured source comparison passed for the complete target backbone
  row, every ancestor, synonyms, attestation, PATHS entry, scope, and seed
  event wording. This is a bounded record check, not corpus reproduction.
- Live NCBI taxonomy EFetch and Datasets corroborate the identity, rank,
  domain, parent, genetic code, and complete lineage.
- OAK graph-term validation: not applicable; there are no curator-added
  graph nodes. Carried NCBI lineage was checked directly.
- External-history validation: not applicable to this target after the
  bounded ignored-inclusive history searches below. The inline seed
  event was checked against the manifests and scope.
- Not checked: full-corpus reproduction, QC, tests, provenance, pages,
  docs, and vendored-sync gates. No invented focused equivalent is claimed.
- The target was byte-for-byte unchanged immediately before this report.

## Identity and Grounding

The exact node is supported by
`data/raw/ncbitaxon_taxa.tsv:222182`,
`data/catalog/ncbi_names-0005.jsonl.gz:31671`, and the live
[NCBI taxonomy authority](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035879).
NCBI uses species rank for this isolate-style label. Retaining that rank
does not establish a formally named species. The root-first lineage
through Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Oceanospirillales, Halomonadaceae, and Chromohalobacter is carried as
NCBI classifies it.

The exact sequence
[JF796143.1](https://www.ncbi.nlm.nih.gov/nuccore/JF796143.1)
has taxon cross-reference 1035879 and strain LY7-4. The literature's
LY7-4/JF796143 pairing therefore has accession-level support. LY7-3,
which is prominent in phage publications, is not an alias established
for this target. A phage studied using a bacterial strain is also not
the bacterial organism or its genome.

## Evidence

### Pinned assertions

- Backbone row 222182 supplies the exact name, species rank, direct
  parent, code 11, empty synonym lists, and snapshot 2026-09-13.
  Every one of the ten ancestor entries matches its pinned row.
- `data/taxa/PATHS.tsv:14681` associates the target identifier with
  the exact filename stem.
- `curation/seed_scope.tsv:322443` records inclusion on 2026-09-13
  and one attesting source, NCBI.
- The NCBI attestation has matching ID and label, count 1, unit `NAME`,
  and the correct snapshot note. This is a name count, not a genome count.
- The inline seed event preserves the scope reason and source list.
  Its timestamp, `2026-09-13T17:54:04Z`, is the latest of the raw
  (17:50:44), ATB (17:54:04), and StrainInfo (17:29:00) manifest
  timestamps, consistent with `src/taxonmech/seed.py:_seed_timestamp`.

### Primary sequence and literature

Exact-taxid Nuccore search returned one item, UID `334086022`.
Full source-feature and reference metadata were inspected, excluding
sequence payload. JF796143.1 is a 1,435-base partial 16S rRNA sequence
with both ends partial, strain LY7-4, isolation source salt lake, and
country China. Li and Yu submitted it on 9 April 2011; its record
was created on 31 May 2011. The study reference remains marked
unpublished and concerns bacteria from Yuncheng Salt Lake; the other
reference is the direct submission. Neither supplies a DOI or PMID.

The full main text of the
[2018 JMT-1 study](https://new.scielo.br/j/bjm/a/mfSPbJKFD4KyBXRNkyjfd8m/?ilang=en&lang=en)
was inspected on SciELO. Its methods identify LY7-4 by JF796143.1;
results report no plaques on that strain in the tested host-range
assay, while LY7-3 was the isolation host. This supports a bounded
assay observation, not universal phage resistance. Its occasional
use of the word archaea for the test panel does not override the
accession's bacterial classification. The viral genome description
must not become a bacterial assembly link. PubMed verifies the paper's
[PMID 29699780](https://pubmed.ncbi.nlm.nih.gov/29699780/) and DOI
10.1016/j.bjm.2018.03.004.

The publisher's public main text for the
[2026 Yuncheng phage study](https://cjournal.hep.com.cn/0253-2395/CN/10.13451/j.sxu.ns.2024072)
was also inspected, including sections 1.1 and 2.1. It explicitly
pairs LY7-4 with JF796143 and lists the strain among hosts of recovered
phages. This does not conflict with the different JMT-1 assay and
does not justify a general susceptibility or resistance claim.
The study's viral measurements and host phylogeny are not imported
as a bacterial genome or a replacement NCBI lineage.

These publications provide optional accession-linked context. Their
absence from this minimal seeded record is not a missing required
representation; the record makes no phenotype assertion.

iModulonDB is not applicable: the record contains no gene, regulator,
trait, or transcriptomics claim needing an expression-module check.

## Completeness

No required field or supported mandatory genome join was found missing.

All seven raw enrichment inventories were searched by exact target
identifier: BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and
BactoTraits. No target rows were found. The pinned backbone has no
direct target children, and the type-material, merged-ID, and
dropped-record tables contain no exact target entry.
`strain_count: 0` is consequently consistent with the BacDive subtree
inventory; it does not deny the existence of the cultured strain.

Initial and expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation`,
and `history`. These searches included ignored, hidden, and
compressed sources. Patterns included the bounded taxid, LY7-4 name
variants, exact slug, JF796143, and UID 334086022.

Both searches returned the same four matching rows, all read in full:
the backbone, native NCBI name, scope, and one ATB collision.
`data/catalog/allthebacteria.tsv.xz:547120` is a Staphylococcus
aureus entry with run `ERR1035879`, sample `SAMEA3323180`,
and assembly `ERZ3253874`. Its numeric run suffix is not taxonomic
identity. Its other retained source context includes an unknown
sylph classification and non-HQ flags, but none supplies a link to
Chromohalobacter.

The five source metadata JSON files for BacDive, BV-BRC, GOLD,
SeqCode, and StrainInfo were separately parsed using the expanded
pattern without a match. Ignored-independent history filename and
content searches found no target artifact. These absence statements
apply only to the inspected local sources.

The live exact-taxid Assembly query returned zero items with a
phrase-not-found notice; this is not a global claim that no genome
exists. The sole exact-target nucleotide metadata has no assembly,
BioSample, BioProject, or culture-deposit identifier. A partial 16S
sequence and an experimental laboratory strain label do not supply
the eligible BacDive/deposit ownership chain needed for a strain
genome join. Optional links remain appropriately empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the existing taxonomy and provenance assertions.
This verdict does not certify a general phage phenotype, formal
species nomenclature, or external genome completeness.

## Recommended Edits

None required. Do not change the generated record or its seed history.

Future enrichment must preserve the LY7-4/JF796143 identity and the
distinction between host bacteria, other test strains, and phages.
A genome addition requires an explicit eligible culture-deposit and
source chain. Route separately authorized changes through maintained
source transforms and reproducible inputs, not a YAML hand edit.
Trait and interaction evidence should retain study and assay scope
in the appropriate sibling corpus rather than being inferred here.

## Follow-up Checks

- For future genome enrichment, resolve strain/deposit ownership and
  verify the source identifier and accession version before joining.
- For future phenotype curation, inspect the exact accession-linked
  experiment and conditions; do not transfer LY7-3 results or viral
  measurements to the target.
- After an authorized maintained-input change, rerun the relevant
  extraction/seeding workflow, focused schema and strict validation,
  and applicable full-corpus consistency gates.
- No blocking follow-up remains for current assertions.

## Additional Notes

This individual review created exactly one timestamped report.
No YAML, source inventory, status, history, generated page, GitHub
object, or worktree was changed.

The PMC frontend presented a browser challenge; the same 2018 primary
article was successfully read through SciELO, with its citation also
verified through NCBI. Public publisher main text was used for the 2026
article. Figures and underlying experimental data were not independently
reanalyzed; no numerical figure-derived finding is claimed.

The YAML's explicit 2026-09-13 snapshot is preserved. Live corroboration
and optional literature do not silently update its provenance.
