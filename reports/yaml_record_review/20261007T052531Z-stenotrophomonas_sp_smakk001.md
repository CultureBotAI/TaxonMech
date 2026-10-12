# YAML Record Review: Stenotrophomonas sp. SMAKK001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/stenotrophomonas_sp_smakk001.yaml`
- Started UTC: 2026-10-07T05:21:42Z
- Finished UTC: 2026-10-07T05:25:31Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1035586` was read.
It identifies Stenotrophomonas sp. SMAKK001 as `SPECIES` in `BACTERIA`,
with parent `NCBITaxon:196198`, ten root-first ancestors, genetic code 11,
`grounding_status: EXACT`, `mapping_status: SEEDED`, and
`strain_count: 0`. It contains one NCBITAXON name attestation and one
seeding event, with no optional synonyms, mappings, nomenclature, strain
listing, literature evidence, datasets, discussions, or causal graphs.

Generated YAML remains read-only. This review creates only this report.

## Validation

Completed with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`
and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/stenotrophomonas_sp_smakk001.yaml`:
  exit 0, no issues.
- `just validate-strict data/taxa/bacteria/stenotrophomonas_sp_smakk001.yaml --out /private/tmp/sm-strict.tsv`:
  exit 0, one file scanned, zero errors. The actual TSV was read and is
  header-only.
- Structured read-only comparison with the complete backbone row, every
  ancestor, scope and path-index rows, attestation, and embedded seeding
  text: pass. This diagnostic is not full corpus reproduction.
- Exact scans of `data/raw/ncbi_type_material.tsv`,
  `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv`:
  no matching target rows.

Not run: `just verify-corpus`, `just qc`, full-corpus tests,
`just validate-all`, provenance and generated-site gates, and corpus-wide
history/product validation. No narrower substitute is claimed for these
gates. No curator-added graph nodes or target-specific history files were
found within the bounds below.

## Identity and Grounding

The full `data/raw/ncbitaxon_taxa.tsv:222114` row matches the YAML label,
rank, parent, code, and empty synonym fields. All ancestor identifiers,
labels, ranks, and order agree with the pinned parent chain. The native name
at `data/catalog/ncbi_names-0005.jsonl.gz:31593` is the same scientific
name, with an empty unique-name field.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035586&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035586)
confirm taxon 1035586, the exact designation, species rank, Bacteria, code 11,
and the same lineage through Lysobacterales, Lysobacteraceae,
Stenotrophomonas, and unclassified Stenotrophomonas. Datasets supplies root 1;
the XML supplies the other ancestors. No alternate scientific name was
returned. The browser endpoint failed, but both structured primary responses
were inspected successfully.

This is a species-ranked NCBI isolate taxon, not an assertion of a formally
named species, a genus-wide phenotype, or equivalence to S. maltophilia.
The species rank makes it eligible under the repository's scope rule.

## Evidence

The one-name NCBITAXON attestation, source identifier, label, assertion count,
unit, and 2026-09-13 snapshot note match the backbone. Path index row 14616
and `curation/seed_scope.tsv:322384` uniquely resolve the slug and scope
reason. The 2026-09-13T17:54:04Z seeding event agrees with that reason.
No human sign-off is implied by this report.

Exact-taxonomy nucleotide search returned one record,
[JF895518.1](https://www.ncbi.nlm.nih.gov/nuccore/JF895518.1).
Its complete GenBank metadata, excluding sequence bases, identifies a
778-nt partial 16S rRNA sequence, strain SMAKK001, taxon 1035586, and a
Gulf of Mannar locality in India. It was submitted in April 2011 and made
public in June 2011. The metadata contain an unpublished Marine bacteria
reference and direct submission, without a culture-collection qualifier,
assembly, BioSample, or BioProject link. This is marker evidence, not a
genome or a deposited culture.

[Manikandan et al. 2014](https://scialert.net/fulltext/?doi=jm.2014.25.33)
explicitly associates isolate 3/SMAKK001 with JF895518, describes cultivation
from Gulf of Mannar sponges, and reports a Halichondria association and
antimicrobial filtrate assays. These observations concern that isolate and
experimental context. They do not establish clinical efficacy, a chemically
identified antibiotic, or resistance of the producing isolate.
The historical Xanthomonadaceae wording does not override current NCBI
lineage. The paper's GenBank deposition is a sequence submission, not a
culture-collection accession.
[Crossref metadata](https://api.crossref.org/works/10.3923/jm.2014.25.33)
confirm DOI `10.3923/jm.2014.25.33`, title, journal, volume, and pages.
The inspected publisher text, rather than search snippets or later papers,
supports this context.

## Completeness

No target rows occurred in the seven exact-taxonomy primary inventories
for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits.
The backbone has no children of this taxon. The zero strain count therefore
agrees with the available classified BacDive inventory; it does not mean
the organism was never cultured.

Ignored-independent source searches found no applicable native culture,
deposit, or genome linkage for the target. No public culture-collection
accession was established by the inspected primary evidence. Exact Assembly
search `txid1035586[Organism:noexp]` returned zero, with an explicit
phrase-not-found warning. This bounded result does not prove that no genome
or culture exists anywhere.

The native catalog's apparent GTDB hit is an unrelated Enterobacter ludwigii
record, `RS_GCF_030811815.1`: the matching number 1035586 is its contig N50,
not its taxonomy. Two ATB candidates are namespace collisions, not matches:
SAMEA1035586 is Staphylococcus aureus, while SRR1035586 belongs to a
Salmonella Senftenberg sample. Their complete native rows were read.

No required representation was established as omitted. Record-level
literature evidence is optional for seeded records. Habitat, media, and
phenotype curation belong to the sibling repositories named in
`docs/CURATION.md`; they are not missing TaxonMech identity fields.
Do not create a BacDive strain, an LPSN equivalence, a GTDB mapping, or a
genome link from a bare designation or marker accession.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The retained identity, lineage, source count, strain count,
grounding, and seeded lifecycle are supported within the completed checks.

## Recommended Edits

None required for this record. Leave generated YAML and its embedded event
unchanged; do not promote the lifecycle after an automated review.

A future authorized literature overlay could preserve the explicit
marker/publication association. It must be implemented through the
maintained seeder in `src/taxonmech/seed.py` with tests and a durable input,
not as a hand edit. Any new culture/genome assertion must first obtain the
source-specific identity evidence required by the maintained extraction
pipeline. No such change is proposed by this review.

## Follow-up Checks

For a future source refresh, recheck exact taxonomy and whole deposit/assembly
identifiers, then use the documented extraction dry run, seeding dry run,
and `just seed-canary NCBITaxon:1035586`. Inspect the emitted canary and
repeat schema/strict validation before full `just verify-corpus` and
`just qc`. No regeneration was performed here.

Any later phenotype review must preserve the producing strain, tested
organisms, filtrate context, and experimental endpoint separately. Do not
reinterpret activity against resistant organisms as resistance of SMAKK001.

## Additional Notes

The source search used `rg --no-ignore --hidden -n -z -i` over
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation`, and `history`, including ignored, hidden, and compressed
content. It searched identifier 1035586, full label, slug, and SMAKK001
separator variants. Six matching lines were fully inspected: backbone,
scope, scientific name, the unrelated GTDB N50, and two unrelated ATB rows.

A second search for JF895518 with optional version and the publication DOI
found no content matches in those roots. For both search stages, all five
source-component `SOURCE.json` files were parsed completely and history
filenames were traversed independently of ignore rules; neither supplied
a target match. These are bounded source-content findings, not a claim
about arbitrary files elsewhere on disk or the entire internet.

The local structured adapter was resolved in
`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw`.
The fresh `kg-microbe-sources imodulondb datasets` listing contained
28 datasets and no target organism. iModulonDB was not applicable, not
negative biological evidence.

The publisher's full-text narrative was inspected; image-only assay tables
and phylogenetic figures were not independently transcribed or reanalyzed.
No numerical phenotype claim was imported. No sequence reanalysis, paid
research, source contact, GitHub mutation, lifecycle change, or history
scaffolding was performed.

