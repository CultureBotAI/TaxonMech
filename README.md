# TaxonMech

Knowledge base of **microbial taxa and the strains behind them** — one record
per taxon, identified by NCBI Taxonomy and harmonized with GTDB, LPSN, BacDive
and the other taxon-bearing sources that
[kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe) transforms.

A primary focus is **linking strain identifiers to genome identifiers**,
prioritizing NCBI GenBank/RefSeq assemblies while including GTDB, BV-BRC /
PATRIC, IMG and AllTheBacteria genome records. Coverage expands to available
identifier systems when their strain links have source evidence. The links preserve
source records, culture-deposit matches and supplied accession versions. A
strain can have multiple links; sharing a species does not establish a
strain-to-genome link.

TaxonMech is the taxonomic counterpart of
[TraitMech](https://github.com/CultureBotAI/TraitMech) (traits),
[HabitatMech](https://github.com/CultureBotAI/HabitatMech) (habitats),
[CultureMech](https://github.com/CultureBotAI/CultureMech) (growth media),
[MediaIngredientMech](https://github.com/CultureBotAI/MediaIngredientMech)
(ingredients), [CommunityMech](https://github.com/CultureBotAI/CommunityMech)
(communities), [CellStructureMech](https://github.com/CultureBotAI/CellStructureMech)
(cell structures), [ProteinTraitsMech](https://github.com/CultureBotAI/proteintraitsmech)
(proteins) and [AntibioticMech](https://github.com/CultureBotAI/AntibioticMech)
(antimicrobials), and follows the curation pattern established by
[dismech](https://github.com/monarch-initiative/dismech): one YAML per entity,
ontology-grounded, evidence-backed, closed-schema validated, curated
incrementally with an append-only audit trail.

**[Browse the corpus online →](https://culturebotai.github.io/TaxonMech/)**

## Scope: species and strains, lineage as given

TaxonMech records are **species-level and below** — species, subspecies,
strains and other infraspecific taxa, and unranked NCBI taxa under a species.
Higher taxa are never records; they appear only in a record's `lineage`,
which is NCBI Taxonomy's parent chain carried verbatim. TaxonMech does not
reconcile NCBI, GTDB and LPSN hierarchies, resolve conflicts between them, or
infer placements: GTDB and LPSN are recorded as mappings and nomenclature on
the taxon they concern. The seeder refuses higher taxa and a test enforces
the rule.

## The problem it solves

The same organism is a different thing in each resource that describes it:

| Source | What it holds for *Escherichia coli* |
|---|---|
| NCBI Taxonomy | `NCBITaxon:562`, rank species, the lineage, synonyms |
| GTDB | `GTDB:s__Escherichia_coli` and the assemblies under it, mapped to `NCBITaxon:562` as a *broader* match because GTDB splits the species |
| LPSN | `lpsn:776057`, authority "(Migula 1895) Castellani and Chalmers 1919", correct name, type strain ATCC 11775 = DSM 30083 = … |
| BacDive | thousands of strain records, each with its culture-collection deposits |
| MediaDive, GOLD, Madin, BactoTraits | media, organisms and trait assertions attached to the same taxon |

Every one of those is a *source concept*. A `TaxonRecord` resolves them onto
one NCBI-grounded identity and keeps each source's own identifier, mapping
predicate and assertion count, so a reader can tell what each resource says
and how much data sits behind it. `data/taxa/bacteria/escherichia_coli.yaml`
is one record that carries the lineage, the LPSN nomenclature with type strain
designations, the GTDB species mapping with its genome count, and the strains
with their deposits — type strains first.

## Strain identifiers to genome identifiers

Each `strains[].genome_assemblies[]` entry carries a GenBank (`GCA_`) or
RefSeq (`GCF_`) assembly identifier, the source record asserting the link,
and the source's reference number, description, assembly level and taxon
when supplied. Additional `strains[].genome_records[]` entries carry typed
GTDB (`gtdb.genome:`), BV-BRC / PATRIC (`patric:`), IMG (`img.taxon:`)
and AllTheBacteria (`atb.assembly:`) identifiers. BacDive supplies direct strain
assertions; GTDB metadata adds links through whole culture-deposit identifiers whose authority and accession
format match the pinned collection registry, with the matched ID and
verbatim source field retained. GOLD's primary workbook adds NCBI and IMG
links through explicit organism, sequencing-project and analysis-project
relationships. Species membership and strain-name matching never supply
these links.

The primary [NCBI assembly inventory](data/raw/strain_assemblies.tsv) and
additional [genome-record inventory](data/raw/strain_genome_records.tsv) are
uncapped and join to [strain identifiers and deposits](data/raw/bacdive_strains.tsv)
on `strain_id`. Species records and pages show links for their listed strains.
Related BioSample, BioProject and GOLD organism/project references have their
own `related_records` field and [inventory](data/raw/strain_related_records.tsv);
they are excluded from genome counts.
Identifiers from different databases remain separate assertions, even when
BacDive lists them together. An absent entry means no link of that kind was
imported for that strain; it does not mean the strain has never been
sequenced. See [the relationship model and evidence rules](docs/STRAIN_GENOMES.md).

[Browse AllTheBacteria assemblies](https://culturebotai.github.io/TaxonMech/atb.html)
by sample, ENA analysis, strain, deposit or genome ID. Its snapshot-scoped
assembly IDs join through existing BioSample evidence; a shared sample does
not establish genome equivalence. The browser includes eligible assemblies
for unlisted strains and exposes FASTA/archive links, source flags and the
original evidence. The [ATB inventories](data/atb) are uncapped; the
[full catalog and query guide](docs/ALLTHEBACTERIA.md) explains broader
snapshot searches and source attribution.

## Current corpus

<!-- BEGIN GENERATED CORPUS STATS -->
<!-- Generated by scripts/check_docs.py; do not edit this block by hand. -->
**100 taxon records** are currently committed.

| Domain | Records | | Rank | Records | | Attested by | Records |
|---|---:|---|---|---:|---|---|---:|
| BACTERIA | 100 | | SPECIES | 100 | | NCBITAXON | 100 |
|  |  | |  |  | | LPSN | 100 |
|  |  | |  |  | | GTDB | 100 |
|  |  | |  |  | | BACDIVE | 100 |
|  |  | |  |  | | MEDIADIVE | 100 |
|  |  | |  |  | | GOLD | 100 |
|  |  | |  |  | | MADIN | 100 |
|  |  | |  |  | | BACTOTRAITS | 100 |

15,096 BacDive strains are classified under these taxa (9,602 listed in records; 17 records cap their listing). 100 records list a type strain, 100 carry an LPSN correct name, 100 map to GTDB (186,716 genomes), and 0 carry causal graphs (0 evidence-backed edges).

**765 listed strains have genome identifier links.** Coverage below is deduplicated across records, with NCBI assemblies first:

| Database | Strain–identifier pairs | Distinct identifiers | Distinct strains |
|---|---:|---:|---:|
| NCBI | 3,119 | 3,112 | 753 |
| GTDB | 769 | 769 | 427 |
| PATRIC | 1,242 | 1,242 | 623 |
| IMG | 728 | 724 | 413 |
| AllTheBacteria | 233 | 233 | 191 |

These are database identifier counts, not unique biological genomes across databases. Unlisted strains remain in the complete inventories: `data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv`, plus `data/atb/strain_links.tsv` for AllTheBacteria assemblies linked through BioSample evidence.

Related records are counted separately from genomes:

| Record type | Strain–record pairs | Distinct identifiers | Distinct strains |
|---|---:|---:|---:|
| BIOSAMPLE | 1,199 | 1,180 | 598 |
| BIOPROJECT | 1,414 | 655 | 601 |
| GOLD_ORGANISM | 9,135 | 9,117 | 5,321 |
| GOLD_PROJECT | 1,045 | 1,015 | 500 |
| GOLD_ANALYSIS | 880 | 876 | 491 |

The complete related-record inventory is `data/raw/strain_related_records.tsv`.

**0 records are `REVIEWED`;** the remaining 100 are `SEEDED` or `PROPOSED`.
<!-- END GENERATED CORPUS STATS -->

Run `just report` for the live report. Every current record is `SEEDED`:
generated from the inventories, not yet read by a curator.

## Quick start

```bash
just install                        # uv sync --extra dev
just report                         # corpus stats: domains, ranks, sources, strains
just validate-all                   # closed-mode schema validation of every record
just verify-corpus                  # check data/taxa/ is what data/raw/ + the scope produce
just test                           # unit + corpus-integrity tests
just render                         # regenerate the site under pages/
just qc                             # everything CI runs
```

Re-seeding is only needed when the upstream data or the scope changes:

```bash
just extract-inventory-dry          # what extraction would produce (no writes)
just extract-inventory              # refresh data/raw/ from a kg-microbe checkout
just atb-fetch                     # fetch pinned ATB metadata if not cached
just atb-index --apply             # refresh ATB crosslinks against current inventories
just seed                           # dry-run: scope report, no writes
just seed-canary NCBITaxon:562      # write ONE record and check it, first
just seed-apply --force             # rewrite the scoped corpus
just seed-apply --force --prune     # ...and clean up files that left the scope
```

`just extract-inventory` is the only step that needs a local
[kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe) checkout; point
`KG_MICROBE_ROOT` or `conf/sources.yaml` at it. Extraction also reads
[GOLD's public workbook](https://gold.jgi.doe.gov/download?mode=site_excel) at
`data/source_snapshots/goldData.xlsx`. Use `GOLD_WORKBOOK` or
`just extract-inventory --gold-workbook /path/to/goldData.xlsx` to select
another copy. The derived inventories in
`data/raw/` and `data/atb/` are committed, so seeding, validation and tests
run without upstream downloads or the full ATB SQLite catalog.
`data/raw/MANIFEST.yaml` records the kg-microbe commit and the byte hash of
every input and output.

## Scope: which taxa are records

The inventories cover **every taxon at least one strain-bearing source
attests** — tens of thousands — plus their ancestors. The committed corpus is
the explicit subset listed in [`curation/seed_scope.tsv`](curation/seed_scope.tsv),
one identifier per line with the date and reason it was added. That file is
the reviewable answer to "which taxa are records", and `just verify-corpus`
proves the corpus is exactly what the inventories plus that scope produce.

```bash
just propose-scope --rule core --top 100        # rank candidates; never writes the file
just propose-scope --rule core --top 100 --append >> curation/seed_scope.tsv
```

The `core` rule selects species with a BacDive strain, an LPSN correct name
that names a type strain, and a GTDB identity mapping (LPSN-linked or 1:1) —
the best-corroborated taxa — ranked by how many sources attest them. `just seed-apply --all` seeds the
whole attested universe instead, for when the corpus is ready to grow past the
scope file.

Filenames are pinned by `data/taxa/PATHS.tsv` (identifier → slug), so a
re-seed never renames an existing record just because the corpus grew around
it. **To rename a record, edit its slug there and re-seed** — never rename the
file directly.

## Schema

`src/taxonmech/schema/taxonmech.yaml` defines **TaxonRecord**, one per YAML
file; [docs/SCHEMA.md](docs/SCHEMA.md) walks through it.

- **Identity** — `identifier` (the NCBITaxon CURIE), `label`, `rank`,
  `taxon_domain`, `parent_taxon`, `lineage`, `synonyms`, `xrefs`,
  `genetic_code`.
- **`nomenclature`** — what LPSN says about each name: authority,
  validly-published / legitimate / correct-name status, type strain
  designations, cited publications, 16S accessions.
- **`taxonomy_mappings`** — GTDB species mapped onto this taxon, with the
  predicate kg-microbe assigned and the assemblies behind each. The species
  LPSN links to the name comes first; `skos:broadMatch` entries are pooled
  species that share NCBI-labelled genomes with this taxon, flagged as such.
- **`strains`** and **`strain_count`** — BacDive strains classified under
  the taxon or, for species, its NCBI subtree (`classified_as` says where),
  with culture-collection deposits and `is_type_strain` derived from LPSN's
  designations, plus explicit NCBI `genome_assemblies` and additional
  `genome_records` links, with sample, project and organism references in
  `related_records`. The listing is capped at 200 per record, type strains
  first; the count is always the full number.
- **`source_attestations`** — the harmonization layer: one entry per upstream
  resource with `source_id`, `mapping_predicate`, `assertion_count` and
  `assertion_unit` (BacDive counts strains, GTDB genomes, GOLD organisms,
  MediaDive media — the numbers are **not summable across sources**).
- **`causal_graphs`** — the "Mech" half: evidence-backed mechanism graphs
  linking a taxon to its traits, habitats and metabolism. Unlike the seeded
  descriptive fields, **every causal edge must carry a citation**.
- **`grounding_status`** and **`mapping_status`**, kept deliberately separate.
- **`discussions`** / **`datasets`** from the shared `mech_shared` module,
  vendored byte-identical across the Mech repos.

## Curation

Records are generated, and `just verify-corpus` gates that they reproduce
exactly from `data/raw/` and the scope — so **curation is never a hand-edit to
a seeded field**, which the next re-seed would silently revert. Today the
seeder owns every field; the design for curator-owned overlays (causal graphs,
reviewed status, definitions) follows HabitatMech's `curation/` pattern and is
tracked in the issues. See [docs/CURATION.md](docs/CURATION.md) and
[docs/HARMONIZATION.md](docs/HARMONIZATION.md).

## Known limitations

- **Every record is unreviewed.** `SEEDED` means the seeder's harmonization
  is plausible, not verified. LPSN and GTDB mappings are kg-microbe's; this
  repository has not yet checked any of them by hand.
- **The scope is a starter set.** The inventories describe far more taxa than
  the corpus; growing the scope is a curation decision, not a technical one.
- **Strain listings are capped**, and strain-level data (phenotypes, media,
  isolation sources) is deliberately left to TraitMech, CultureMech and
  HabitatMech; a strain entry here holds identifiers, deposits and genome links.
- **Genome coverage depends on source assertions and explicit identifiers.**
  BacDive links, GTDB culture-deposit matches, GOLD project chains and ATB
  sample associations preserve source evidence; a link does not imply a complete
  genome or confirm its current status. Unversioned NCBI accessions remain
  unversioned.
  RefSeq pairing and cross-database equivalence require explicit metadata;
  species-level GTDB mappings do not supply it. ATB IDs are local to their
  metadata snapshot, and shared samples do not equate assemblies.
- **Cross-source deposit matching requires a registered authority and valid accession format.**
  BacDive's deposit field also contains bare strain aliases. Aliases and
  formats unsupported by the pinned registry remain in source records but
  cannot establish GTDB or GOLD genome joins;
  see [the authority boundary](docs/STRAIN_GENOMES.md#culture-collection-authorities).
- **Secondary MicrobeDecoder associations need independent evidence.** Its
  GOLD/NCBI columns contain verified organism mismatches, tracked in
  [issue #25](https://github.com/CultureBotAI/TaxonMech/issues/25). The genome
  import uses primary GTDB and GOLD records for those relationships.
- **NCBI rank comes from kg-microbe's raw semantic-sql build**, not from the
  KGX transform, which drops it. The extractor records that input in the
  manifest like any other.

## Layout

```
TaxonMech/
├── conf/sources.yaml                     # where kg-microbe lives; source provenance
├── conf/allthebacteria.yaml              # pinned ATB snapshot and local cache paths
├── conf/id_label_targets.yaml            # id<->label gate targets (vendored gate)
├── curation/seed_scope.tsv               # which taxa are records, and why
├── data/
│   ├── raw/                              # inventories + MANIFEST.yaml provenance
│   ├── atb/                              # ATB metadata overlap, crosslinks and provenance
│   └── taxa/
│       ├── PATHS.tsv                     # identifier -> slug, pins filenames
│       └── <domain>/<slug>.yaml          # generated TaxonRecords
├── history/                              # append-only curation-session records
├── src/taxonmech/
│   ├── extract.py                        # inventory extraction library + CLI
│   ├── seed.py                           # harmonization library + CLI
│   ├── report.py                         # corpus reporting
│   ├── schema/taxonmech.yaml             # LinkML schema
│   ├── schema/mech_shared.yaml           # vendored from claw (Discussions, Datasets)
│   ├── schema/history.yaml               # vendored from claw (history records)
│   ├── validation/write_validated.py     # write-time closed-schema gate
│   ├── curate/curation_event.py          # append-only audit trail helper
│   └── templates/                        # site templates
├── scripts/                              # CLIs, QC gate, renderer, vendored claw files
├── pages/                                # generated site (committed)
├── docs/                                 # CURATION.md, SCHEMA.md, HARMONIZATION.md
├── .claude/skills/                       # agent workflows
└── tests/
```

## Sources

- **NCBI Taxonomy** — [ncbi.nlm.nih.gov/taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy)
- **AllTheBacteria** — [assembly metadata](https://allthebacteria.org/docs/metadata_sqlite/),
  [snapshot source](https://osf.io/4kjh7/), CC-BY-4.0; cite
  [AllTheBacteria](https://doi.org/10.1101/2024.03.08.584059).
- **GTDB** — [Genome Taxonomy Database](https://gtdb.ecogenomic.org/)
- **LPSN** — [List of Prokaryotic names with Standing in Nomenclature](https://lpsn.dsmz.de/)
- **BacDive** — [DSMZ BacDive](https://bacdive.dsmz.de/)
- **MediaDive** — [DSMZ MediaDive](https://mediadive.dsmz.de/)
- **GOLD** — [JGI Genomes OnLine Database](https://gold.jgi.doe.gov/), including
  its primary public workbook; [GOLD v.10 citation](https://doi.org/10.1093/nar/gkae1000)
- **Madin et al.** — [prokaryotic phenotypic trait compilation](https://doi.org/10.1038/s41597-020-0497-4)
- **BactoTraits** — [functional trait database](https://doi.org/10.1016/j.ecolind.2021.108047)
- **CAFI** — [DSMZ collection-acronym registry](https://github.com/LeibnizDSMZ/cafi),
  the pinned authority and accession-template list used for cross-source
  culture-deposit matching
- [kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe) supplies the
  harmonized KGX inputs, BacDive and GTDB snapshots, and GTDB→NCBI and
  LPSN→NCBI mappings. The GOLD workbook is downloaded from its authority.

## License

CC0-1.0 for everything this project authored. Upstream resources keep their
own terms; the inventories in `data/raw/` are derived counts and identifiers,
not redistributed source records. GOLD metadata remain subject to
[GOLD's usage policy](https://gold.jgi.doe.gov/usagepolicy). The packaged CAFI
register retains CC-BY-4.0 licensing and its
[source attribution](src/taxonmech/data/cafi_acronyms.metadata.json).
See [LICENSE](LICENSE).
