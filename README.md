# TaxonMech

Knowledge base of **microbial taxa and the strains behind them** — one record
per taxon, identified by NCBI Taxonomy and harmonized with GTDB, LPSN, BacDive
and other sources through complete primary catalogs and the
[kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe) transforms.
The [source coverage guide](docs/SOURCE_COVERAGE.md) and
[source manifest](data/catalog/MANIFEST.json) distinguish complete snapshots,
crosslinks and external resources, including strain records without an NCBI mapping.

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

**Every source is read on the taxon record, not on a page of its own.** The
site publishes no per-source browser: a strain row carries its NCBI, GTDB,
BV-BRC/PATRIC, IMG and AllTheBacteria genome records and its StrainInfo
strain and deposit records inline, each with the evidence that produced it.
Open the taxon that classifies the strain.

AllTheBacteria assembly IDs are snapshot-scoped and join through existing
BioSample evidence; a shared sample does not establish genome equivalence.
StrainInfo adds explicit deposit-to-NCBI assertions and typed strain, deposit
and nucleotide references; a sequence must name the matched source deposit,
and sharing a StrainInfo group does not transfer genome links.

Strains beyond a record's listing are not lost: the uncapped
[ATB inventories](data/atb) and [StrainInfo component](data/straininfo) hold
every imported link, and the [full catalog and query guide](docs/ALLTHEBACTERIA.md)
and [StrainInfo query guide](docs/STRAININFO.md) cover broader snapshot
searches. Source licences and citations are published on the
[source catalogue](https://culturebotai.github.io/TaxonMech/pages/sources.html).

## Current corpus

<!-- BEGIN GENERATED CORPUS STATS -->
<!-- Generated by scripts/check_docs.py; do not edit this block by hand. -->
**625,960 taxon records** are currently committed.

| Domain | Records | | Rank | Records | | Attested by | Records |
|---|---:|---|---|---:|---|---|---:|
| BACTERIA | 605695 | | SPECIES | 572305 | | NCBITAXON | 625960 |
| ARCHAEA | 14013 | | STRAIN | 46325 | | GTDB | 117809 |
| EUKARYOTA | 6243 | | NO_RANK | 4925 | | GOLD | 43822 |
| OTHER | 9 | | SUBSPECIES | 866 | | MADIN | 34148 |
|  |  | | FORMA_SPECIALIS | 667 | | BACDIVE | 27640 |
|  |  | | ISOLATE | 534 | | LPSN | 22469 |
|  |  | | SEROGROUP | 163 | | MEDIADIVE | 14154 |
|  |  | | SEROTYPE | 91 | | BACTOTRAITS | 9626 |
|  |  | | VARIETAS | 58 | |  |  |
|  |  | | FORMA | 11 | |  |  |
|  |  | | BIOTYPE | 8 | |  |  |
|  |  | | PATHOGROUP | 6 | |  |  |
|  |  | | CLADE | 1 | |  |  |

These records contain 106,294 BacDive strain classifications and 106,294 listed strain occurrences, representing 100,745 distinct listed strains. Species and descendant records can list the same strain; 0 records cap their listing. 20648 records list a type strain, 21254 carry an LPSN correct name, 117809 map to GTDB (324,404,579 genomes summed across record attestations, not deduplicated), and 0 carry causal graphs (0 evidence-backed edges).

**21,071 listed strains have genome identifier links.** Coverage below is deduplicated across records, with NCBI assemblies first:

| Database | Strain–identifier pairs | Distinct identifiers | Distinct strains |
|---|---:|---:|---:|
| NCBI | 68,752 | 68,001 | 20,884 |
| GTDB | 16,350 | 16,302 | 11,888 |
| PATRIC | 30,192 | 30,048 | 19,700 |
| IMG | 23,508 | 23,421 | 18,341 |
| AllTheBacteria | 5,334 | 5,306 | 4,727 |

These are database identifier counts, not unique biological genomes across databases. Unlisted strains remain in the complete inventories: `data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv`, plus `data/atb/strain_links.tsv` for AllTheBacteria assemblies linked through BioSample evidence, and `data/straininfo/assemblies.tsv` for StrainInfo's explicit deposit-to-NCBI assertions.

Related records are counted separately from genomes:

| Record type | Strain–record pairs | Distinct identifiers | Distinct strains |
|---|---:|---:|---:|
| BIOSAMPLE | 25,519 | 24,741 | 15,786 |
| BIOPROJECT | 38,388 | 16,998 | 15,888 |
| GOLD_ORGANISM | 76,038 | 75,623 | 35,463 |
| GOLD_PROJECT | 21,174 | 20,981 | 14,038 |
| GOLD_ANALYSIS | 18,894 | 18,845 | 13,843 |
| STRAININFO_STRAIN | 54,312 | 53,745 | 53,890 |
| STRAININFO_DEPOSIT | 107,277 | 106,843 | 53,890 |
| NUCLEOTIDE_SEQUENCE | 51,594 | 51,301 | 9,984 |

The complete related-record inventories are `data/raw/strain_related_records.tsv` and `data/straininfo/related_records.tsv.gz`. StrainInfo strain/deposit IDs, record-version DOIs and nucleotide sequence references are not counted as genomes.

**0 records are `REVIEWED`;** 14 retained records are `DEPRECATED`. Other records are `SEEDED` or `PROPOSED`.
<!-- END GENERATED CORPUS STATS -->

Run `just report` for the live report. Records are generated from the
inventories and remain unreviewed; retained retired taxa are `DEPRECATED`.

## Quick start

Development uses Python 3.13 via `.python-version`; CI selects the same minor
explicitly and runs the full quality gate once. The package compatibility
floor remains declared in `pyproject.toml`.

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
just extract-inventory              # refresh data/raw/ from the pinned primary sources
just atb-fetch                     # fetch pinned ATB metadata if not cached
just atb-index --apply             # refresh ATB crosslinks against current inventories
just straininfo-index --apply      # rebuild crosslinks from the complete strain census
just source-catalog                # refresh the full source manifest
just seed                           # dry-run: scope report, no writes
just seed-canary NCBITaxon:562      # write ONE record and check it, first
just seed-apply --force             # rewrite the scoped corpus
just seed-apply --force --prune     # ...and clean up files that left the scope
```

Extraction and primary GTDB catalog projection need a local
[kg-microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe) checkout; point
`KG_MICROBE_ROOT` or `conf/sources.yaml` at it. Extraction reads the pinned
NCBI taxonomy and assembly snapshots, complete BacDive and BV-BRC projections, and
[GOLD's public workbook](https://gold.jgi.doe.gov/download?mode=site_excel) at
`data/source_snapshots/goldData.xlsx`. Use `GOLD_WORKBOOK` or
`just extract-inventory --gold-workbook /path/to/goldData.xlsx` to select
another copy. The derived inventories in
`data/raw/`, `data/atb/`, `data/straininfo/` and the native source catalogs are committed,
so seeding, validation and tests
run without upstream downloads or the full ATB SQLite catalog.
`data/raw/MANIFEST.yaml` records the kg-microbe commit and the byte hash of
every input and output. See [the complete refresh procedure](docs/SOURCE_COVERAGE.md#reproduction-and-refresh).

## Scope: which taxa are records

The inventories cover **the complete primary NCBI bacterial and archaeal
backbone**, additional source-attested taxa and their ancestors. GTDB-only
candidates are included, and native source catalogs retain unmapped entries. The committed corpus is
the explicit subset listed in [`curation/seed_scope.tsv`](curation/seed_scope.tsv),
one identifier per line with the date and reason it was added. That file is
the reviewable answer to "which taxa are records", and `just verify-corpus`
proves the corpus is exactly what the inventories plus that scope produce.

```bash
just propose-scope --rule attested --rank '' --all --append > /tmp/taxonmech-scope-additions.tsv
# Review the proposed additions, then append them to curation/seed_scope.tsv.
just seed
just seed-canary NCBITaxon:562 --force
# Inspect the canary before the bulk write.
just seed-apply
just render
just docs-stats
```

The `core` rule selects species with a BacDive strain, an LPSN correct name
that names a type strain, and a GTDB identity mapping (LPSN-linked or 1:1) —
the best-corroborated taxa — ranked by how many sources attest them. The current
scope includes **every attested species-or-below taxon in the committed inventory**,
using `--rule attested --rank '' --all`. The original starter entries retain their
dates and reasons. Future inventory refreshes require explicit scope additions.
The seeder's `--all` switch bypasses the scope for exploration; production expansion
updates the scope first so `just verify-corpus` continues to reproduce every record.

The site provides search across all records and static browse pages of 200 records.
Large strain tables and StrainInfo detail batches use lossless gzip compression;
the original source assertions remain in the YAML and inventories. GitHub Actions
publishes only `pages/` and the root redirect after main passes QC, retaining existing
`/pages/` URLs. `scripts/build_pages_artifact.py` enforces a 950 MB publication budget.

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
  `related_records`. Records retain every classified strain, with type strains
  first. The site displays the full listing in pages of 200.
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
- **Coverage is bounded by the committed inventories.** Every eligible attested
  taxon is included, but this is not all of NCBI Taxonomy or every genome database.
  Ancestors above species remain lineage entries. A source-attested taxon can
  have no BacDive strain, and records with several sources are not automatically reviewed.
- **Strain-level data** (phenotypes, media,
  isolation sources) is deliberately left to TraitMech, CultureMech and
  HabitatMech; a strain entry here holds identifiers, deposits and genome links.
- **Genome coverage depends on source assertions and explicit identifiers.**
  BacDive links, NCBI/BV-BRC/GTDB culture-deposit matches, GOLD project chains and ATB
  sample associations preserve source evidence; a link does not imply a complete
  genome or confirm its current status. Unversioned NCBI accessions remain
  unversioned.
  RefSeq pairing and cross-database equivalence require explicit metadata;
  species-level GTDB mappings do not supply it. ATB IDs are local to their
  metadata snapshot, and shared samples do not equate assemblies.
- **Cross-source deposit matching requires a registered authority and valid accession format.**
  BacDive's deposit field also contains bare strain aliases. Aliases and
  formats unsupported by the pinned registry remain in source records but
  cannot establish cross-source genome joins;
  see [the authority boundary](docs/STRAIN_GENOMES.md#culture-collection-authorities).
- **Secondary MicrobeDecoder associations need independent evidence.** Its
  GOLD/NCBI columns contain verified organism mismatches, tracked in
  [issue #25](https://github.com/CultureBotAI/TaxonMech/issues/25). The genome
  import uses primary GTDB and GOLD records for those relationships.
- **NCBI ranks and lineage follow the pinned primary taxonomy snapshot.**
  Its complete bacterial and archaeal backbone includes environmental and
  uncultured taxa. Source disagreements remain visible rather than reconciled.

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

## Merge queue

See [the native merge-queue guide](docs/MERGE_QUEUE.md) for the reviewed merge workflow
when queue enforcement is enabled on `main`.

## License

CC0-1.0 for everything this project authored. Upstream resources keep their
own terms; the inventories in `data/raw/` are derived counts and identifiers,
not redistributed source records. GOLD metadata remain subject to
[GOLD's usage policy](https://gold.jgi.doe.gov/usagepolicy). The packaged CAFI
register retains CC-BY-4.0 licensing and its
[source attribution](src/taxonmech/data/cafi_acronyms.metadata.json).
See [LICENSE](LICENSE).
