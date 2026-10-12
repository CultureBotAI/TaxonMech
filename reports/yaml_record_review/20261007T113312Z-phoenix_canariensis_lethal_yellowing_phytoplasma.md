# YAML Record Review: 'Phoenix canariensis' lethal yellowing phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/phoenix_canariensis_lethal_yellowing_phytoplasma.yaml`
- Started UTC: 2026-10-07T11:29:56Z
- Finished UTC: 2026-10-07T11:33:12Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. It represents
`NCBITaxon:1035884`, 'Phoenix canariensis' lethal yellowing
phytoplasma, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:3048141`. It carries ten root-first ancestors, genetic
code 11, one related synonym, `EXACT` grounding, `SEEDED`
status, zero BacDive strains, one NCBI name attestation, and one
source-seeding event.

The record is the phytoplasma taxon, not its eukaryotic palm host.
No phenotype, genome, culture deposit, nomenclature entry, taxonomy
mapping, literature citation, or causal graph is asserted.
Maintained owners of future changes are `src/taxonmech/ncbi_taxdump.py`,
`src/taxonmech/extract.py`, `src/taxonmech/seed.py`, and
`curation/seed_scope.tsv`; generated YAML is not a hand-edit target.

## Validation

- `just validate data/taxa/bacteria/phoenix_canariensis_lethal_yellowing_phytoplasma.yaml`:
  passed, exit 0, no issues.
- `just validate-strict data/taxa/bacteria/phoenix_canariensis_lethal_yellowing_phytoplasma.yaml --out /private/tmp/phoenixLy-strict.tsv`:
  passed, one file, zero errors. The TSV was read and contains only
  its header. Validators used offline uv resolution and a temporary cache.
- Structured comparisons passed for the complete backbone row,
  ten-entry lineage, synonym scope, PATHS row, scope reason,
  NCBI attestation, and inline history wording.
- Live NCBI EFetch and Datasets corroborated the current identity
  and lineage and separately resolved the historical merged ID.
- OAK graph-term validation: not applicable; no curator graph.
  NCBI identifiers were checked at their authority.
- External-history validation: not applicable after the bounded
  ignored-inclusive content and filename searches found no target
  artifact. The inline seed event was checked against source manifests.
- Not checked: full-corpus reproduction, QC, tests, provenance,
  generated pages, docs, and vendored-sync gates. Focused checks do
  not prove those repository-wide gates.
- The target remained byte-identical to its initial read before
  writing this report.

## Identity and Grounding

The pinned backbone `data/raw/ncbitaxon_taxa.tsv:222184`,
native name rows `data/catalog/ncbi_names-0005.jsonl.gz:31673`
and 31674, and
[live NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035884)
agree on this species-ranked bacterial concept under
16SrIV (Coconut lethal yellows group), NCBITaxon:3048141.

The alternate name 'Phoenix canariensis' phytoplasma is an NCBI
`includes` name, not an exact synonym. The parser maps that name
class to `RELATED_SYNONYM`; the backbone and seeder preserve that
scope correctly. The quotes around the host name are part of the
source label and are correctly escaped in YAML.

`data/raw/ncbi_merged_ids.tsv:35104` maps old
`NCBITaxon:2021201` to the target. Live EFetch returns 1035884 and
lists 2021201 in `AkaTaxIds`; Datasets also resolves the old query
to 1035884. The old ID has no PATHS entry. The current record is not
itself retired; an upstream historical redirect is not a reason to
mark this record deprecated or invent a superseded TaxonMech record.

A distinct near-name concept, 'Phoenix canariensis' yellowing
phytoplasma, is NCBITaxon:1853302, with parent NCBITaxon:3098986 in
the pinned backbone. Its rows at backbone 483955, scope 541593,
and native names shard 0011 line 22375 were read and excluded.
A shared host name does not make these taxon concepts equivalent.

## Evidence

### Existing assertions

- The complete backbone row supplies identifier, label, rank, parent,
  code 11, related synonym, and the 2026-09-13 snapshot.
  All ten lineage entries match the pinned ancestor chain.
- `data/taxa/PATHS.tsv:14683` pins the correct identifier and stem.
- `curation/seed_scope.tsv:322445` supplies the inclusion date
  and one-source NCBI scope reason.
- The sole attestation correctly counts one `NAME`, not one
  strain, genome, host, or disease observation.
- The seed event at 2026-09-13T17:54:04Z matches the latest source
  manifest timestamp: raw 17:50:44, ATB 17:54:04, and StrainInfo
  17:29:00 UTC that day. This agrees with `_seed_timestamp`
  in `src/taxonmech/seed.py`.

### Primary sequence context

The exact-taxid Nuccore search returned seven items. Their full
source features and reference metadata were read, excluding the
nucleotide payload. Every item carries taxon:1035884; all are
partial ribosomal markers, not genome assemblies.

| Accession | Length | Explicit source context |
|---|---:|---|
| [MW850419.1](https://www.ncbi.nlm.nih.gov/nuccore/MW850419.1) | 806 nt | 16S; isolate FITPc21; sawdust; host Phoenix canariensis |
| [MN607700.1](https://www.ncbi.nlm.nih.gov/nuccore/MN607700.1) | 1,745 nt | 16S and spacer; Coahuila_Pca5; Phoenix canariensis; Torreon, Coahuila, Mexico |
| [MN389510.1](https://www.ncbi.nlm.nih.gov/nuccore/MN389510.1) | 1,745 nt | 16S and spacer; Coahuila_Pca11; same explicit host and locality |
| [MF491872.1](https://www.ncbi.nlm.nih.gov/nuccore/MF491872.1) | 1,534 nt | 16S and spacer; clone PD348; Phoenix canariensis; Saint Bernard Parish, Louisiana; 5 May 2016 |
| [MF491869.1](https://www.ncbi.nlm.nih.gov/nuccore/MF491869.1) | 1,535 nt | 16S and spacer; clone PD045; same host; Jefferson Parish, Louisiana; 1 October 2015 |
| [MF491868.1](https://www.ncbi.nlm.nih.gov/nuccore/MF491868.1) | 1,536 nt | 16S and spacer; clone PD014; same host; Orleans Parish, Louisiana; 16 September 2015 |
| [HQ613894.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ613894.1) | 1,560 nt | 23S; isolate SA1; no explicit host or locality qualifier |

None of these seven metadata records supplies an assembly, BioSample,
BioProject, or registered culture-deposit identifier. Source references
are marked unpublished and direct submission. The Mexico City wording
in FITPc21's unpublished title is not a geographic qualifier; the
Brazilian submitting address is not an isolation locality. SA1's Florida
submitting address is likewise not a specimen-locality assertion.

### Inspected literature

The primary publisher's
[2020 Coahuila paper](https://academicjournals.org/journal/AJB/article-full-text/54451C065653),
DOI 10.5897/AJB2020.17185, was inspected through its public HTML main
text. The results explicitly identify MN389510 and MN607700 as the
two 1,745-base products and classify the studied phytoplasmas as
16SrIV-D. This supports accession-specific context even though the
GenBank study reference is still marked unpublished.

The paper distinguishes the studied Texas Phoenix palm decline
association from subgroup 16SrIV-A lethal yellowing. That does not
authorize rewriting NCBI's current scientific-name field or assigning
a phenotype to every sequence under the node. No experimental figure,
sequence alignment, or phylogeny was independently reanalyzed.

iModulonDB is not applicable: the record has no gene, regulator,
mechanism, expression, or phenotype assertion. Ribosomal marker
metadata is not transcriptomic-module evidence.

## Completeness

No consequential required field was found missing. Optional
literature, phenotype, and genome fields need not be populated.

Exact-taxid scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and
BactoTraits raw inventories found no target rows. The backbone has no
direct children, so the zero BacDive subtree count is supported.
No exact type-material or dropped-record row was found. The historical
merged-ID row is retained separately as described above.

Ignored-independent searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`, including compressed files.
Patterns covered the bounded taxid, host-name/label variants, stem,
historical taxid 2021201, and all seven sequence accessions.
All ten initial and all seventeen expanded matching rows were
read in full through structured TSV/JSONL parsing.

Besides the current and near-name taxon rows, matches were unrelated
numeric collisions:

- ATB rows 795503 and 2846939 are Salmonella enterica entries whose
  SeqKit sum contains 1035884. They concern SAMEA6145406/ERZ25321595
  and SAMN40352670/ERZ26919392, not this taxon.
- BacDive 10742 and its culture row concern NCBITaxon:1210081;
  IMSNU 21201 appears as the encoded token IMSNU%2021201.
  That is not NCBITaxon:2021201.
- GCA_059890135.1 is a Salmonella entry with strain SM2021201.
- GCA_965299935.1, GCA_052788665.1, GCA_002349345.1, and the
  corresponding GTDB row for GCA_002349345.1 matched genome-length
  values 2021201, not taxon identifiers.

The five source metadata JSON files were separately parsed with the
expanded pattern; no target match was found. Ignored-inclusive history
content and filename searches found no target artifact. A separate
ignored-inclusive report filename search found no pre-existing report
for this exact stem before review.

The exact-taxid live Assembly search returned zero items with a
phrase-not-found notice. This is bounded index evidence, not proof
that no related genome exists elsewhere. No inspected source supplies
the eligible deposit-level chain needed for a strain-genome join.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The current record accurately represents the pinned NCBI
node, its source synonym scope, and its seed provenance.

## Recommended Edits

None required. Do not modify the generated YAML or its review status.

Future enrichment should retain exact accession and isolate scope,
distinguish the host from the bacterium, and keep marker sequences
outside genome counts. A source change would belong in the maintained
NCBI extraction or seeding logic and tests, followed by regeneration,
not an ad hoc label or lineage edit.

## Follow-up Checks

- Before adding any strain-genome link, verify an eligible culture
  deposit and the explicit primary genome ownership chain.
- For literature-based claims, match the exact accession and experimental
  scope rather than a shared host or disease label.
- After a separately authorized maintained-input change, rerun focused
  schema and strict validation plus applicable corpus reproduction,
  provenance, history, and publication gates.
- No unresolved blocker remains for this record's existing assertions.

## Additional Notes

This review writes one new report only. No YAML, source inventory,
history, status, generated page, worktree, or GitHub item was changed.

The Louisiana paper lead DOI 10.1094/PHP-06-20-0046-S appeared in
search output, but direct publisher and full-text requests returned
403 errors. It was not treated as independently retrieved full-text
evidence. The inspected Louisiana source qualifiers above are from
GenBank. FITPc21 and SA1 unpublished study titles were not independently
resolved to complete publications.

The Coahuila article's main text was inspected; image-only tables and
figures were not independently verified. No quantitative phenotype,
causal graph, diagnostic protocol, or transmission claim was imported.
