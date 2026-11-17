# YAML Record Review: Pseudoalteromonas sp. C15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_c15.yaml`
- Started UTC: 2026-10-07T05:31:59Z
- Finished UTC: 2026-10-07T05:35:06Z
- Verdict: pass

## Target

Complete generated `TaxonRecord` for `NCBITaxon:1035588`,
Pseudoalteromonas sp. C15. The record has rank `SPECIES`, domain
`BACTERIA`, parent `NCBITaxon:194690`, genetic code 11, ten root-first
ancestors, `grounding_status: EXACT`, `mapping_status: SEEDED`, and
`strain_count: 0`. One NCBITAXON name attestation and one seeding event
are present. Optional synonyms, nomenclature, mappings, strains,
record-level evidence, datasets, discussions, and causal graphs are absent.

The full YAML was read and rechecked unchanged. This review writes only
this new report, not generated data or lifecycle/history changes.

## Validation

Completed using `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`
and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/pseudoalteromonas_sp_c15.yaml`:
  exit 0, no issues.
- `just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_c15.yaml --out /private/tmp/pc-strict.tsv`:
  exit 0, one file scanned, zero errors. The actual TSV was inspected and
  contains only its header.
- Read-only structured comparison of the complete backbone row, all
  ancestors, index/scope entries, attestation, and seed-event wording:
  pass. This diagnostic is not corpus reproduction.
- Exact target scans of `data/raw/ncbi_type_material.tsv`,
  `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv`:
  no matching rows.

Not run: `just verify-corpus`, `just qc`, full-corpus tests,
`just validate-all`, provenance/rendered-site gates, and corpus-wide
history/product validation. No focused substitute is claimed. No
curator-added graph nodes or target-specific append-only history files
were found in the checks below.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:222116` row agrees with
the identifier, label, rank, parent, genetic code, and empty synonym fields.
The full parent chain agrees with the YAML through Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Alteromonadales,
Pseudoalteromonadaceae, Pseudoalteromonas, and unclassified
Pseudoalteromonas. The native scientific-name row at
`data/catalog/ncbi_names-0005.jsonl.gz:31595` agrees and has no
additional unique-name value.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035588&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035588)
confirm the exact designation, species rank, parent 194690, bacterial domain,
code 11, and lineage. Datasets additionally supplies root 1, which the
XML ancestor list omits. No alternate name was returned. The browser
endpoint failed, but these complete primary responses were inspected.

The species-ranked isolate concept is eligible under the local scope rule.
Neither its short designation nor a genus-level relationship establishes
equivalence to another C15 isolate or a formally named Pseudoalteromonas
species.

## Evidence

The NCBITAXON attestation correctly counts one `NAME`, uses the exact
source identifier and label, and records snapshot 2026-09-13.
`data/taxa/PATHS.tsv:14618` and `curation/seed_scope.tsv:322386`
uniquely support the slug and scope reason. The embedded
2026-09-13T17:54:04Z event matches the seed inputs. It remains a seeding
event, not human review.

Exact-taxonomy nucleotide search returned one record,
[FR870269.1](https://www.ncbi.nlm.nih.gov/nuccore/FR870269.1).
Complete GenBank metadata, excluding sequence bases, describe an 860-nt
partial 16S rRNA gene, strain C15, taxon 1035588, submitted on 20 May 2011
and created/updated on 24 May 2011. The source feature does not supply
a culture-collection accession, isolation locality, BioSample, BioProject,
or genome assembly. A UK submitting institution is not an isolation site.
The sequence is a marker, not a genome.

The source includes an unpublished reference titled
Classification and identification of Pseudoalteromonas by mass spectrometry
and computational analysis, attributed to Davies, Zhang, Emami, and Burgess.
Its annotation does not establish a published article or a biological result.
A related [2016 MALDI-TOF study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4751257/)
was inspected as a candidate, including its environmental-isolate table.
Neither C15 nor FR870269 appeared in that table or the searchable
PMC/publisher article text. No exact alias or citation link was established,
so its strain-specific results and culture identifiers are not transferred.
Supplementary images were not independently inspected for this negative
text/table observation.

## Completeness

The target has no children in the complete pinned backbone. No exact-taxonomy
rows were found in the seven primary inventories for BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, and BactoTraits. Zero counted strains therefore agrees
with classified BacDive inputs; it is not evidence that C15 is uncultivable
or that no culture exists anywhere.

Ignored-independent local source searches found no applicable exact-target
culture/deposit, genome, nomenclature, or taxonomy-mapping assertion.
The sole non-backbone candidate was ATB
`data/catalog/allthebacteria.tsv.xz:66233`, read in full:
SAMEA1035588 is a Staphylococcus aureus sample, run ERR083758,
analysis ERZ3070756, with `META_FAIL`. Its accession suffix is a
namespace collision, not taxon 1035588.

Exact Assembly search `txid1035588[Organism:noexp]` returned zero,
with an explicit phrase-not-found warning. This bounded query and the
local catalog checks do not prove global absence of assemblies or deposits.
No required representation was established as missing. Optional literature
evidence and causal graphs need not be invented for a source-seeded identity
record, and a marker accession must remain outside genome counts.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The retained identity, lineage, grounding, source count,
strain count, and seeded history are supported within the completed checks.

## Recommended Edits

None required. Preserve the generated YAML and seeded lifecycle.

A later authorized curation task could investigate the unpublished reference
or an explicit culture-deposit link. Any durable addition must enter through
a maintained source input and the extraction/seeding implementation,
including `src/taxonmech/seed.py` where applicable, with tests.
Do not hand-edit the record, infer species identity from the short name, or
create genome links from 16S evidence.

## Follow-up Checks

For a future input refresh, resolve complete source identifiers and rerun
the documented extraction/seeding dry runs. Use
`just seed-canary NCBITaxon:1035588`, inspect the emitted canary, repeat
the two record validators, then run `just verify-corpus`, provenance,
tests, history checks, and `just qc`. No regeneration was performed here.

To establish a literature alias, require an explicit accession or documented
strain cross-reference rather than matching authors, genus, institution,
method, or a short designation.

## Additional Notes

All local absence findings include ignored, hidden, and compressed source
content. Searches used `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`.

The identifier/full-label/slug and label-separator search returned four
lines: backbone, scope, scientific name, and the unrelated ATB sample.
A broader genus/C15 co-occurrence search returned only the same three
identity/scope lines. A separate FR870269 accession/version search returned
zero matches. Every candidate native row was fully read. All five
source-component `SOURCE.json` files were parsed completely and history
filenames traversed independently for each search stage, with no target
metadata/history matches. These are bounded source searches, not an
exhaustive claim about the internet or arbitrary files elsewhere on disk.

The fresh structured `kg-microbe-sources imodulondb datasets` listing
returned 28 datasets, none matching the target organism. iModulonDB was
not applicable; this is not negative phenotype evidence.

No sequence alignment, assembly reconstruction, mass-spectrum reanalysis,
paid research, source contact, GitHub mutation, lifecycle promotion, or
append-only history creation was performed.

