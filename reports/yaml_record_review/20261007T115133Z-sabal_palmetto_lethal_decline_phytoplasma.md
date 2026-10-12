# YAML Record Review: 'Sabal palmetto' lethal decline phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sabal_palmetto_lethal_decline_phytoplasma.yaml`
- Started UTC: 2026-10-07T11:48:43Z
- Finished UTC: 2026-10-07T11:51:33Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035887`,
`'Sabal palmetto' lethal decline phytoplasma`, rank `SPECIES`, domain
`BACTERIA`, parent `NCBITaxon:3048141`, grounding `EXACT`, mapping
status `SEEDED`. It carries ten ancestors, genetic code 11, zero source-counted
strains, one NCBI name attestation, and one seed event. No synonyms,
nomenclature, taxonomy mappings, genome links, phenotypes, literature claims,
or causal graph are asserted.

The record is generated from maintained source inventories and scope.
Future identity or extraction corrections belong upstream and in the pinned
source ingestion; emission changes belong in `src/taxonmech/seed.py`;
scope changes belong in `curation/seed_scope.tsv`. Generated YAML is not
a direct editing surface.

## Validation

- `just validate data/taxa/bacteria/sabal_palmetto_lethal_decline_phytoplasma.yaml`:
  passed with no issues.
- `just validate-strict data/taxa/bacteria/sabal_palmetto_lethal_decline_phytoplasma.yaml --out /private/tmp/sabalLethalDecline-strict.tsv`:
  passed, one file, zero errors; the TSV was read and contains only the header.
  Both commands used offline uv resolution and a temporary uv cache.
- Structured source comparisons passed for the target, every ancestor,
  empty synonym fields, genetic code, scope/index rows, NCBI attestation,
  and seed-history wording. These are bounded checks, not corpus reproduction.
- Live NCBI EFetch and Datasets returned the exact target identity and lineage.
- `just validate-products` via OAK: not applicable; no curator-added graph
  grounding is asserted.
- Separate `just validate-history`: not run for this target; ignored-inclusive
  history content and filename searches found no target artifact. The inline
  seed event was inspected against the inputs.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`,
  `just validate-all`, provenance, site drift, documentation statistics, and
  vendored-sync gates. No full-repository success is claimed.

## Identity and Grounding

Backbone row 222187 in `data/raw/ncbitaxon_taxa.tsv` agrees with the YAML.
[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035887&retmode=xml)
confirms the label, species rank, bacterial placement, parent 3048141
(16SrIV, Coconut lethal yellows group), and genetic code 11.
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035887)
confirms the species and all ten root-inclusive ancestor IDs.

The complete root-first chain agrees with the pinned backbone for IDs, labels,
and ranks: root; cellular organisms; Bacteria; Bacillati; Mycoplasmatota;
Mollicutes; Acholeplasmatales; Acholeplasmataceae; Candidatus Phytoplasma;
16SrIV group. TaxonMech carries this NCBI lineage rather than inferring a
taxonomic reconciliation from disease names.

Native name row 31678 in `data/catalog/ncbi_names-0005.jsonl.gz` is the exact
scientific name. Pinned synonym columns and live target name metadata do not
supply alternative names requiring representation.

Complete matched source rows distinguish this node from Sabal lethal yellowing
`NCBITaxon:1004767`, decline `NCBITaxon:1035885`, wilt
`NCBITaxon:1035886`, phytoplasma `NCBITaxon:2051676`, and Sab4
`NCBITaxon:2461345`. Shared host names or marker similarity do not authorize
merging those records.

## Evidence

`data/taxa/PATHS.tsv` row 14686 maps the target to the reviewed slug.
`curation/seed_scope.tsv` row 322448 supplies its dated 2026-09-13 inclusion
and one-source NCBI reason. The sole source attestation correctly records
`NCBITAXON`, the exact identifier and label, count 1, unit `NAME`, and
the 2026-09-13 snapshot. This is a source-name count, not an isolate count.

The seed event's wording matches scope and source support. Its timestamp
2026-09-13T17:54:04Z is the newest extraction time of the raw, ATB, and
StrainInfo manifests, following `_seed_timestamp`. `SEEDED` does not imply
human review, and this report does not promote the status.

Exact `txid1035887[Organism:noexp]` searches returned zero Assembly results
and ten Nuccore results. The Assembly query reports phrase-not-found; it is
not proof that no relevant assembly exists under any other representation.
All ten sequence records' complete feature/reference metadata were inspected,
excluding nucleotide sequence payloads and protein translations:

| Accession | Isolate | Sequence scope |
| --- | --- | --- |
| [MG993140.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993140.1) | 11SP14 | 1,533 nt partial 16S/spacer; Oct-2015 |
| [MG993141.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993141.1) | 11SP15 | 1,533 nt partial 16S/spacer; Oct-2015 |
| [MG993142.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993142.1) | 11SP22 | 1,533 nt partial 16S/spacer; Oct-2015 |
| [MG993143.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993143.1) | 11SP30 | 1,533 nt partial 16S/spacer; Oct-2015 |
| [MG993144.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993144.1) | 12SP3 | 1,533 nt partial 16S/spacer; Nov-2015 |
| [MG993145.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993145.1) | 12SP7 | 1,533 nt partial 16S/spacer; Nov-2015 |
| [MG993146.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993146.1) | 12SP13 | 1,533 nt partial 16S/spacer; Nov-2015 |
| [MG993147.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993147.1) | 12SP17 | 1,533 nt partial 16S/spacer; Nov-2015 |
| [MG993148.1](https://www.ncbi.nlm.nih.gov/nuccore/MG993148.1) | 12SP19 | 1,533 nt partial 16S/spacer; Nov-2015 |
| [HQ613889.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ613889.1) | LDT | 649 nt partial gcp CDS; protein AEH05552.1; code 11 |

All ten source features explicitly assign taxon 1035887. The nine MG accessions
supply host Sabal palmetto and trunk tissue as isolation source. HQ613889.1
has no explicit host, collection date, or locality qualifier; a submitter's
Florida address is not an isolation locality. None of the inspected metadata
supplies an assembly, BioSample, BioProject, or registered culture-deposit ID.
These are marker/gene sequences, not genomes or eligible culture accessions.

[The primary Bahder et al. paper](https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/ppa.12882),
DOI 10.1111/ppa.12882, was inspected as publisher HTML, including methods,
results, discussion, and extracted tables. Its results explicitly identify
the deposited range MG993138-MG993148 from nine Sabal and two queen palms;
the nine target-associated MG accessions fall within that range. The methods
place the study at FLREC in Davie, Florida, and support a study-scoped 16SrIV-D
association. The publication appeared in Plant Pathology 67(8), 1821-1828
(2018), although the sequence references still say unpublished. That stale
external reference does not make the current taxonomy-only YAML incorrect.
Marker identity with comparison sequences does not establish isolate or
genome equivalence. Proposed vector or reservoir routes in the discussion
remain hypotheses, not causal edges to import.

HQ613889.1 instead cites an unpublished Ntushelo genetic-characterization
submission. Its gcp annotation is not direct functional experimental evidence
and does not inherit the nine MG accessions' study context.

iModulonDB is not applicable to the current bare identity record. Optional
sequence leads do not create an asserted gene, regulator, or expression-module
claim.

## Completeness

The pinned backbone has no target children. Exact target checks in all seven
raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories
found no matching enrichment row. Zero `strain_count` therefore agrees
with source-count semantics; it does not deny the existence of field isolates.
No target type-material, merged-ID, or dropped-ID row was found.

Gitignore-independent, hidden- and compressed-inclusive searches used
`rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation`, and `history`.
Queries covered the taxon number, Sabal/phytoplasma names, exact slug, all ten
nucleotide accessions, AEH05552, all nine MG isolate labels, and bounded LDT.
All five source-level `SOURCE.json` files were parsed separately; history
filenames were also checked independently of ignore rules.

The initial search returned 19 lines, and the sequence/isolate expansion
returned 23; all matched rows were read completely through structured TSV or
native JSON parsing. Four extra rows were unrelated Corynebacterium glutamicum
catalog entries matching Ldt in a company name: GOLD Go0181180/Go0181183 and
StrainInfo SI-ID37385/SI-ID37386. Their deposits cannot be transferred to this
phytoplasma. The searched roots had no matching accession evidence requiring
sequence enrichment and no target-specific history artifact. These are
bounded snapshot findings, not universal absence claims.

Optional nomenclature, mappings, strains, genomes, traits, and causal graph
fields are correctly left unpopulated given the checked evidence and model.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current identity, lineage, source counts, attestation, or
seed-history claims. External partial sequences and the publication provide
bounded context, not a required missing genome representation.

## Recommended Edits

None required.

Preserve the exact NCBI node and source-count semantics. Do not replace its
name with the broader disease name, merge sibling taxon nodes, or add
culture/genome links through taxon ID, marker similarity, or bare isolate name.

Any future evidence-backed enrichment must be implemented through maintained
source inputs and the seeder with explicit accession ownership. Do not patch
the generated YAML or change the review status from this read-only report.

## Follow-up Checks

Before adding study phenotypes, inspect accession-level sample correspondence
and the original visual tables where symptom shading matters; this review did
not interpret table shading or validate quantitative endpoints. Retrieve
additional primary evidence before assigning isolate LDT to a study or place.

For an authorized maintained-input change, inspect the result of
`just seed-canary NCBITaxon:1035887`, rerun focused schema and strict checks,
then run `just verify-corpus` and `just qc` before publication.
Those write/generation steps were not run here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`; HEAD
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target was byte-compared
with the initial complete read before this report was added. No YAML,
source, scope, history, mapping status, generated page, existing report,
GitHub item, or worktree was changed by the review.
