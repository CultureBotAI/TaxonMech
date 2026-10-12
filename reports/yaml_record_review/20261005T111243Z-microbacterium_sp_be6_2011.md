# YAML Record Review: Microbacterium sp. bE6(2011)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_be6_2011.yaml`
- Started UTC: 2026-10-05T11:09:23Z
- Finished UTC: 2026-10-05T11:12:43Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for
`NCBITaxon:1034493`, Microbacterium sp. bE6(2011). Its rank is
`SPECIES`, domain `BACTERIA`, grounding `EXACT`, and mapping
status `SEEDED`. The record contains ten root-first lineage entries,
genetic code 11, zero BacDive strains, one NCBITAXON name attestation,
and one inline seed event. The inventories and
`curation/seed_scope.tsv` are its maintained inputs.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microbacterium_sp_be6_2011.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microbacterium_sp_be6_2011.yaml --out /private/tmp/mbe6-strict-20261005.tsv`: exit 0; one file scanned, zero error rows.
- Parsed comparisons checked the complete backbone row, every ancestor,
  children, seven complete taxon-linked inventories, unique PATHS/scope
  rows, all attestations, and the inline event text. Represented fields
  agreed with the source rows.
- Complete type-material, merged-ID, and dropped inventories had no exact
  target rows.
- Ignored-inclusive filename and content searches of `history/` for
  the ID, label, and stem found no external target history artifact.
  There was no target external history file to validate; the existing
  inline event was checked.
- `just validate-products`: not applicable; no causal graph or
  curator-added graph grounding is present.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`,
  full-corpus history validation, and generated-site drift checks.
  The focused inventory comparison is not a corpus-reproduction gate.
  `--max-diffs` limits diagnostics, not the scope of reproduction.
- No literature citation is asserted by the YAML. Source identifiers and
  lineage terms were checked directly at NCBI.

## Identity and Grounding

Live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034493)
EFetch confirms the exact name, species rank, bacterial placement,
genetic code 11, direct parent `NCBITaxon:2609290` (unclassified
Microbacterium), and ancestor labels/ranks. No alternate names were
returned. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034493)
confirms the complete ancestor ID chain, including the root omitted
from EFetch's LineageEx. These agree with all ten YAML lineage entries.

The pinned source row `data/raw/ncbitaxon_taxa.tsv:221602` agrees
with the record and its 2026-09-13 snapshot attestation.
`data/taxa/PATHS.tsv:14068` contains its unique slug;
`curation/seed_scope.tsv:321913` contains the matching NCBI-only
scope decision. Species rank makes this provisional isolate taxon
eligible, without implying formal nomenclatural standing.

## Evidence

- The full scientific-name object at
  `data/catalog/ncbi_names-0005.jsonl.gz:30990` explicitly connects
  the exact label to `NCBITaxon:1034493`. The single NCBITAXON
  `NAME` attestation has the correct identifier, label, count, unit,
  and snapshot date.
- Exact NCBI searches for `txid1034493[Organism:noexp]` returned
  zero Assembly entries and one Nuccore entry, UID `333981173`.
  The Assembly response included missing-phrase/no-items diagnostics.
  This is bounded query evidence, not proof of universal genome absence.
- Complete [GenBank JF772479.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF772479.1)
  describes a 1,484-base partial 16S rRNA gene sequence, strain
  `bE6`, isolation source bulk soil, and `taxon:1034493`.
  Huang's direct submission is dated 1 April 2011. The associated
  weathering-study reference is unpublished. These data support marker
  identity and the source qualifier, not a genome, culture deposit,
  measured weathering phenotype, or isolation locality. The submitter's
  institutional address does not supply the sampling location.
- The inline seed event, dated `2026-09-13T17:54:04Z`, correctly
  records the NCBI-only scope and `SEEDED_FROM_SOURCES` action.
  It makes no human-review claim.

## Completeness

The complete taxon-linked inventories for BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin, and BactoTraits have no target rows. The backbone
has no target synonyms or children. Optional nomenclature, mapping,
strain, literature, and mechanism fields are appropriately unpopulated
on the evidence checked. `strain_count: 0` measures BacDive inventory
entries, not whether an isolate called bE6 exists.

An ID/label/stem/whole-token bE6 search used
`rg --no-ignore --hidden -n -z -i` across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation`,
and `history`, excluding `SOURCE.json` bookkeeping. It included
ignored/hidden files and gzip catalogs, completed with 24 matching
lines, and was followed by full native-object reads:

- Rahnella sp. BE6 is `NCBITaxon:1001623`; Enterobacter sp. BE6
  is `NCBITaxon:1194410`. Their separate backbone, scope, and
  native-name records provide no identity bridge to Microbacterium.
- Neobacillus niacini BE6 is taxon 86668, with paired
  `GCA_048572935.1` / `GCF_048572935.1`, BV-BRC
  `86668.40`, and GTDB `RS_GCF_048572935.1`.
  The native objects identify BioSample `SAMN46817547` and a
  different bacterial lineage.
- GOLD organism `Go0716478`, project `Gp0879812`, and analysis
  `Ga0688546` describe that Neobacillus candidate; the analysis
  names IMG identifier `8140404427` and the same GenBank assembly.
  Those organism/project/analysis IDs are not genome identifiers and
  do not connect the target to the candidate's assembly.
- Ruegeria sp. BE6 is `NCBITaxon:3437581`, with paired
  `GCA_056538845.1` / `GCF_056538845.1` and BioSample
  `SAMN48980607`. A matching short alias does not override its
  separate source identity.
- The punctuation-boundary match Be6.6H belongs to Tomato twisted
  leaf virus, taxon 2571287, in GOLD `Go0585855`,
  `Gp0592187`, and `Ga0504160`. It is not this bacterial isolate.

A second ignored-inclusive, gzip-aware search for JF772479 and the
exact target label/stem found only the target scope, backbone, and
native-name rows. No accession hit was found in those searched
inventories.

PubMed searches for `JF772479[All Fields]`,
`"BE6"[All Fields] AND Microbacterium[All Fields]`, and the exact
unpublished reference title each returned zero records. BE6 remained
literal in the query translation; the accession/title queries reported
missing phrases. An exact-accession web search also returned no
results. These are bounded search results, not universal absence of
literature.

Two apparent literature candidates were resolved independently:

- [Tangapo et al. (2018)](https://li01.tci-thaijo.org/index.php/anres/article/view/231890),
  DOI 10.1016/j.anres.2018.10.003: the journal PDF's methods
  and Table 2 were inspected, with printed page 313 rendered and
  visually checked. BE6 is an endophytic sweet-potato isolate
  with a reported 94% closest match to Pantoea sequence NR 111998.
  Microbacterium laevaniformans is listed for BR9 and BE9, not BE6.
  These source assignments do not identify the reviewed bE6 taxon.
- [Omomowo and Babalola (2023)](https://www.researchgate.net/publication/369001753_Bioassessment_of_Phylogenetic_Relatedness_and_Plant_Growth_Enhancement_of_Endophytic_Bacterial_Isolates_from_Cowpea_Vigna_unguiculata_Plant_Tissues),
  DOI 10.3390/horticulturae9030332: inspected methods and Table 2
  identify cowpea isolate Be6 as Micrococcus luteus NwuBe06.
  Complete [GenBank OK050083.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/OK050083.1)
  confirms a different 566-base partial 16S marker, strain
  `NWUBe06`, taxon 1270, submitted in September 2021.
  Plant-associated traits from that isolate cannot be transferred
  to Microbacterium bE6.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted identity, lineage, counts, status, or provenance.
The checked evidence establishes no consequential missing strain-genome
association and does not justify importing same-alias records.

## Recommended Edits

None required. Do not hand-edit generated YAML or promote its review status.
Do not count the partial marker as a genome or join BE6 aliases without
an explicit source chain.

A future demonstrated source-processing defect belongs in
`scripts/extract_source_inventory.py` / `src/taxonmech/extract.py`,
or `scripts/seed_from_sources.py` and its maintained modules.
Scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

For any future supported culture or genome association, verify the
exact taxon and culture-deposit chain, add an owner-level regression
test, run the focused validators, then full `just verify-corpus`
and `just qc` for the authorized curation change. No regeneration
or source mutation was performed during this review.

## Additional Notes

The branch is `codex/record-review-extensimonas-20261003`, HEAD
`b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The previously read
review/curation guidance and target had no HEAD diff. Tracked and
staged diffs were empty before writing this report.

The [journal PDF](https://li01.tci-thaijo.org/index.php/anres/article/download/231890/158211)
has eight pages. PDFKit extracted pages 1, 2, and 5 and rendered
page 5; despite a CoreGraphics warning, the inspected image was legible.
Its front matter says available online 18 October 2018, whereas the
journal landing page displays 30 August 2018; the year is sufficient
for the identity comparison. A separate CA-BE6 Centella-paper lead
returned a PMC browser challenge and was not used as evidence.

iModulonDB was not applicable: the target asserts no gene, regulator,
protein, trait, or transcriptomic dataset. This single-record review
created only this new report. It did not edit YAML, inventories, code,
pages, prior reports, history, or lifecycle status, and did not reopen
Eukaryota, spend provider credits, contact anyone, commit, or mutate
GitHub.

