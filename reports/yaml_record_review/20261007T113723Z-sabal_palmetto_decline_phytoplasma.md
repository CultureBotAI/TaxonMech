# YAML Record Review: 'Sabal palmetto' decline phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sabal_palmetto_decline_phytoplasma.yaml`
- Started UTC: 2026-10-07T11:34:22Z
- Finished UTC: 2026-10-07T11:37:23Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. It represents
`NCBITaxon:1035885`, 'Sabal palmetto' decline phytoplasma,
rank `SPECIES`, domain `BACTERIA`, direct parent
`NCBITaxon:3048141`. It has ten root-first ancestors, genetic
code 11, `EXACT` grounding, `SEEDED` status, zero BacDive
strains, one NCBI name attestation, and one seed event.

No synonym, nomenclature, taxonomy mapping, strain list, genome link,
phenotype, literature citation, or causal graph is asserted.
This is the bacterial taxon, not the eukaryotic palm host.
Maintained change ownership is in `src/taxonmech/ncbi_taxdump.py`,
`src/taxonmech/extract.py`, `src/taxonmech/seed.py`, and
`curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `just validate data/taxa/bacteria/sabal_palmetto_decline_phytoplasma.yaml`:
  passed, exit 0, no issues.
- `just validate-strict data/taxa/bacteria/sabal_palmetto_decline_phytoplasma.yaml --out /private/tmp/sabalDecline-strict.tsv`:
  passed, one file, zero errors. The TSV was read and contains only
  its header. Validators used offline uv resolution and a temporary cache.
- Structured comparisons passed for the full backbone row, all ten
  lineage entries, empty synonym fields, PATHS row, scope reason,
  source attestation, and inline history wording.
- Live NCBI EFetch and Datasets agree with the identity and lineage.
- OAK graph-term validation: not applicable because the record has
  no curator graph. NCBI identifiers were verified directly.
- External-history validation: not applicable after bounded
  ignored-inclusive content and filename searches found no target
  artifact. The inline seed timestamp was checked against manifests.
- Not checked: full-corpus reproduction, QC, tests, provenance,
  generated pages, docs, and vendored-sync gates. Focused checks
  do not replace those repository-wide gates.
- The YAML was byte-identical to its initial read before this report.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:222185`,
native scientific name at
`data/catalog/ncbi_names-0005.jsonl.gz:31675`, and
[live NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1035885)
agree. The parent is the species group 16SrIV (Coconut lethal
yellows group), not an asserted species synonym or a strain deposit.

Both the pinned source and live response have no alternate name for
this exact node. The source's host-based label and NCBI species rank
are preserved; the record does not claim a formally published
species name or that all similarly labelled palm phytoplasmas are
one biological isolate.

Ignored-inclusive name searches found five other NCBI concepts
whose complete backbone, scope, and native-name rows were read:

| NCBI ID | Distinct source name |
|---|---|
| 1004767 | 'Sabal palmetto' lethal yellowing phytoplasma |
| 1035886 | 'Sabal palmetto' wilt phytoplasma; includes PD179 |
| 1035887 | 'Sabal palmetto' lethal decline phytoplasma |
| 2051676 | 'Sabal palmetto' phytoplasma |
| 2461345 | 'Sabal palmetto' phytoplasma Sab4 |

The first has pinned parent NCBITaxon:3098986; the other four share
3048141 with this record. None is thereby a synonym, descendant, or
eligible genome source for this exact taxon. In particular, adding
the word lethal to the present name would select another current
NCBI node, not merely improve its wording.

## Evidence

### Existing assertions

- Backbone row 222185 supplies the exact ID, label, species rank,
  parent, code 11, empty synonyms, and 2026-09-13 snapshot.
  Its ancestor chain exactly reproduces all ten lineage entries.
- `data/taxa/PATHS.tsv:14684` pins the identifier and stem.
- `curation/seed_scope.tsv:322446` supplies the 2026-09-13
  inclusion and one-source NCBI reason.
- The attestation correctly counts one `NAME`; it does not count
  biological isolates, genomes, hosts, or disease observations.
- The event timestamp 2026-09-13T17:54:04Z matches the newest
  manifest timestamp: raw 17:50:44, ATB 17:54:04, StrainInfo
  17:29:00 UTC on that date. The inspected `_seed_timestamp`
  implementation selects that maximum.

### Primary sequence context

The exact-taxid Nuccore search returned three records. Their full
source features and references were inspected, excluding sequence
payloads and protein translations. All carry taxon:1035885 and
isolate Sabal1:

| Accession | Scope |
|---|---|
| [HQ613895.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ613895.1) | 5,033 nt complete ribosomal operon region, including 16S, 23S, 5S, spacers, tRNA-Ile and tRNA-Val |
| [HQ613897.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ613897.1) | 604 nt partial hflB2 CDS on the complement strand; protein AEG64725.1 |
| [HQ613899.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ613899.1) | 1,294 nt partial hflB1 CDS; protein AEG64727.1 |

The two CDS annotations use translation table 11, consistent with
the taxon's code. The sequences were submitted by Ntushelo on
15 November 2010 and created on 31 May 2011. Neither a complete
operon nor a partial coding sequence is a genome assembly.

None of the three source records carries a registered culture
deposit, BioSample, BioProject, or assembly identifier. Their source
features do not give explicit host or locality qualifiers. The
taxon label, study title, and Florida submitter address must not
be substituted for specimen-level metadata. The shared Sabal1
designation supports the submitter's isolate label but does not
create a culture-deposit link to other resources.

HQ613895.1 explicitly cites Ntushelo, Harrison, and Elliott's 2012
paper, Comparison of the ribosomal RNA operon from Texas Phoenix
decline and lethal yellowing phytoplasmas, European Journal of Plant
Pathology 133(4):779-782. Publisher-deposited
[Crossref metadata](https://api.crossref.org/works/10.1007/s10658-012-0007-4)
verifies DOI 10.1007/s10658-012-0007-4, title, authors, journal,
volume, and pages. Publisher article/PDF routes were inaccessible;
no full-text molecular comparison was claimed to have been read.

The two hflB sequences retain an unpublished genetic-characterization
reference and a direct-submission reference. They provide annotated
gene identity, not direct experimental proof of a protein mechanism,
phenotype, or expression-module membership.

### Bounded literature context

The
[University of Florida project report submitted to USDA NIFA](https://training-portal.nifa.usda.gov/web/crisprojectpages/0222402-texas-phoenix-decline-a-newly-emerging-disease-threatens-sabal-palm-survival-in-florida.html)
was inspected. It lists the 2012 operon paper and related 2013
studies, and describes broader palm-disease and host-genetics work.
It is project-level context, not an exact accession-to-genome
crosswalk or permission to merge the separate NCBI taxa above.

Its citation list prints volume 33 for the 2012 paper, whereas both
GenBank and the publisher-deposited Crossref record give 133.
This external citation discrepancy is not a defect in the YAML,
which has no literature citation.

iModulonDB is not applicable to the actual record: no gene,
regulator, expression, mechanism, or phenotype claim is asserted.
Finding hflB marker annotations during optional source checks does
not warrant substituting another organism's transcriptomics data.

## Completeness

No required representation was found missing for this seeded
taxonomy-and-provenance record.

Exact-taxid scans found no target rows in the raw BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. The pinned
backbone has no direct children, so the zero BacDive subtree count
is supported. There are no exact target entries in the type-material,
merged-ID, or dropped-record inventories. These are bounded source
findings, not claims that biological isolates or publications do
not exist.

Ignored-independent searches used
`rg --no-ignore --hidden -n -z -i` over `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`, including compressed source files.
Initial patterns covered bounded taxid, label/host variants, and
stem; expansion added all three nucleotide accessions, both protein
accessions, and Sabal1 spelling variants.

Both scans returned the same nineteen rows: six backbone entries,
six scope entries, and seven native name rows. All were read fully
using structured parsing, including the distinct taxa described
above. No eligible target strain-genome evidence emerged.

All five source metadata JSON files were separately parsed with
the expanded pattern and contained no target match. History
filenames and ignored-inclusive content had no target match. The
ignored-inclusive report filename search found no existing review
for the exact stem before this review.

The live exact-taxid Assembly index returned zero items and a
phrase-not-found notice. This does not establish global absence of
a genome under other names or classifications. Optional sequence
and literature context does not require populating genome links.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current record. The source identity, lineage,
attestation, count semantics, and seed provenance are supported.

## Recommended Edits

None required. Do not change the generated YAML, infer an alias
from another Sabal-associated taxon, or promote the review status.

Future enrichment should preserve isolate/accession scope and
the distinction among marker genes, operon sequences, genome
assemblies, and culture deposits. Any separately authorized
harmonization fix belongs in maintained extraction/seeding inputs
and tests, followed by regeneration.

## Follow-up Checks

- Retrieve complete primary methods before importing a molecular,
  phenotype, or diagnostic claim from the cited studies.
- Require an eligible registered deposit and explicit source chain
  for any new strain-genome relationship.
- After a maintained-input change, run the focused schema and
  strict validators and the applicable full-corpus gates.
- No unresolved blocker remains for the record's existing assertions.

## Additional Notes

This review creates one new report only. It does not edit YAML,
inventories, history, status, generated pages, worktrees, or GitHub.

The 2012 publisher text and PDF could not be retrieved. A 2013
molecular-survey article at Academic Journals was also unavailable
through the attempted HTML/abstract/PDF routes; the direct PDF
download returned HTTP 403. Search snippets were treated as leads,
not inspected experimental evidence. No PDF content or figure is
claimed to have been reviewed.

Sequence alignment, protein function experiments, expression
analysis, and quantitative trait curation were not performed.
