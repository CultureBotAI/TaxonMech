# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

## Repository purpose

TaxonMech is a LinkML knowledge base of microbial taxa and strains, seeded
from kg-microbe's transforms of NCBI Taxonomy, GTDB, LPSN, BacDive, MediaDive,
GOLD, Madin et al. and BactoTraits, supplemented by primary genome metadata,
GOLD's public workbook, AllTheBacteria metadata and StrainInfo deposit evidence. One generated YAML
record lives under
`data/taxa/<domain>/<slug>.yaml` for each taxon in scope. The committed
inventories in `data/raw/`, `data/atb/` and `data/straininfo/` and the scope in `curation/seed_scope.tsv` are the
reproducible inputs.

**A primary use case is strain identifier to genome identifier relationships.**
Prioritize NCBI GenBank/RefSeq assemblies and include all available genome
identifier systems when source evidence links them to BacDive and
culture-collection strain identifiers. Keep NCBI links in `genome_assemblies`
and typed GTDB, BV-BRC / PATRIC, IMG and AllTheBacteria links in
`genome_records`, including multiple links per strain. Keep sample, project and GOLD organism references
separate from genome identifiers and genome counts.

GOLD genome links must follow primary organism, sequencing-project and
analysis-project identifiers. Preserve that chain and the culture-deposit
match; analyses that refer to conflicting or unknown organisms do not supply
strain-genome links. GOLD's `Go`, `Gp` and `Ga` IDs are related records,
not genome identifiers.

AllTheBacteria uses local snapshot identifiers `atb.assembly:202505.SAM…`.
Join its whole sample accession to existing BIOSAMPLE evidence, preserving
that evidence in `atb_evidence.sample_links`. Genome crosslinks additionally
require the same explicit source chain; do not take a Cartesian product of
all genomes and samples attached to a strain. Shared BioSample does not mean
same assembly or sequence. Retain source filters, run IDs, SeqKit sums and
provided download URLs; SeqKit sum is not MD5 and AWS URLs are mutable.
The full catalog retains all statuses, but strain/genome links require an
available FASTA without NO_RUNS, RUN_REMOVED, RMMS, META_FAIL or RUN_CHANGE.
Non-HQ assemblies and available FASTAs lacking an ENA analysis remain eligible.
Render the ATB browser from committed `data/atb/` inventories, not the full
ignored SQLite catalog. Upstream metadata retain CC-BY-4.0 attribution.
See [docs/ALLTHEBACTERIA.md](docs/ALLTHEBACTERIA.md).

StrainInfo is a separate source overlay in `data/straininfo/`. SI-ID is a
source strain record, SI-DP a deposit, and the DOI a version of the strain
record. Match only the record's own eligible deposit through the pinned CAFI
authority and full accession template. Every sequence must explicitly name
that same SI-DP; source grouping, names and BacDive cross-references cannot
transfer links. Preserve unversioned NCBI accessions without appending `.1`.
Keep strain/deposit IDs and gene, rRNA operon and patent accessions in typed
`related_records`, outside genome counts. The browser/query labels other
resources as existing TaxonMech strain associations, preserving their source
evidence without attributing them to StrainInfo. Read [docs/STRAININFO.md](docs/STRAININFO.md).

Keep strain identity, taxon classification and genome-record identity distinct;
shared taxonomy, a matching strain name or co-occurrence on a BacDive record
does not establish genome equivalence. Preserve source provenance, supplied
accession versions and each database's identifier syntax. For GTDB metadata,
match whole culture-deposit tokens from `ncbi_strain_identifiers` to existing
deposit IDs only when their authority is in the pinned CAFI collection
registry and the complete accession matches that authority's
`regex_id.full` template. Prefix recognition alone is insufficient. Existing
`culture_collection_ids` can contain bare aliases and do not establish a
valid collection accession by themselves. Preserve the matched ID,
verbatim source identifiers and source field. Normalize only recognized
authority-prefix case and its initial separator; preserve suffix case,
punctuation and leading zeros. Do not rewrite collection aliases to another
prefix or join unknown authorities, unsupported accession formats, species,
taxa, bare strain names or substrings. Retain excluded source values without
using them as genome-join keys. See
[docs/STRAIN_GENOMES.md](docs/STRAIN_GENOMES.md).

Read these before changing domain behavior:

- [README.md](README.md) — public model and generated current statistics.
- [docs/HARMONIZATION.md](docs/HARMONIZATION.md) — identity, mapping and seeding design.
- [docs/CURATION.md](docs/CURATION.md) — what a record is and the evidence rules.
- [docs/SCHEMA.md](docs/SCHEMA.md) — field guide.
- [.claude/skills/curate-yaml-record/SKILL.md](.claude/skills/curate-yaml-record/SKILL.md)
  — audit one taxon record; generated YAML remains read-only.
- [.claude/skills/review-open-issues/SKILL.md](.claude/skills/review-open-issues/SKILL.md)
  — read-only, evidence-backed sweep of the open issue queue.

Sibling repositories use the same conventions: TraitMech, HabitatMech,
CultureMech, MediaIngredientMech, CommunityMech, CellStructureMech,
ProteinTraitsMech, AntibioticMech. The upstream pattern is
monarch-initiative/dismech.

## Authoritative commands

```bash
just qc                # every local and CI quality gate
just report            # current corpus statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just verify-corpus     # prove data/taxa reproduces from data/raw + the scope
just render            # regenerate the committed site under pages/
just docs-stats        # refresh the generated README statistics block
just propose-scope ... # rank candidate taxa for curation/seed_scope.tsv (prints; never writes)
just new-history ...   # scaffold an append-only curation-history record
just validate-history  # validate history/ against the vendored schema
just vendored-check    # claw-governed files match canon at scripts/.vendored_canon_ref
just validate-products # id<->label gate via OAK, for curator-added graph nodes
```

`just qc` is authoritative: lint, README statistics, raw-data provenance,
tests, history records, closed-schema validation, corpus reproduction,
generated-site drift, publication size budget, corpus report. CI runs the same script.

For an upstream refresh:

```bash
just extract-inventory-dry
just extract-inventory
just atb-fetch         # fetch pinned metadata if not already cached
just atb-index --apply # rebuild ATB evidence against the refreshed inventories
just straininfo-index --apply # requires a source snapshot pinned to current deposits
just seed
just seed-canary NCBITaxon:562
just seed-apply --force
just seed-apply --force --prune  # only when files that left the scope should be removed
```

Extraction requires the configured kg-microbe checkout and GOLD's public
workbook at `data/source_snapshots/goldData.xlsx`, or a `GOLD_WORKBOOK` /
`--gold-workbook` override. The workbook is an external source snapshot;
committed inventories suffice for seeding and QC. See
[docs/STRAIN_GENOMES.md](docs/STRAIN_GENOMES.md) for source provenance.

## Scope rule: species and strains only

**TaxonMech records are species-level and below** — species, subspecies,
strains and other infraspecific taxa, and unranked NCBI taxa that sit under a
species. Genera, families and every higher rank are **never records**; they
appear only as `lineage` entries. The seeder refuses a higher taxon in the
scope, `just propose-scope` never proposes one, and a corpus test enforces it.

**Lineage is carried, not curated.** A record's `lineage` is NCBI Taxonomy's
parent chain, verbatim. TaxonMech does not reconcile NCBI with GTDB or LPSN
hierarchies, does not resolve disagreements between them, and never infers a
placement. GTDB classification and LPSN nomenclature appear as
`taxonomy_mappings` and `nomenclature` on the record they concern. GTDB genome
links on strains do not change that classification. Work that needs a
reconciled or inferred taxonomy belongs upstream (kg-microbe, NCBI, GTDB,
LPSN), not here.

## Fact-based answers only

Verify counts, statuses and identifiers with a live command (`just report`,
`grep`, `Read`) before stating them. Do not quote numbers from prose.

## Generated-file boundaries

**Never hand-edit a taxon record.** `data/taxa/` is generated from the
committed inventories plus the scope. Put harmonization changes in the
extractor or seeder and scope changes in `curation/seed_scope.tsv`.
`just verify-corpus` rejects drift.

**Never write a record except through `write_validated_taxon`.** It performs
closed-schema validation before writing. Every mutation must also append a
`CurationEvent` with `taxonmech.curate.curation_event.record_curation_event`.

**Re-emitting an unchanged record must be byte-identical.** Preserve the YAML
emission contract enforced by `tests/test_write_validated.py`.

**Edit site templates, not `pages/`.** Change `src/taxonmech/templates/`, run
`just render`, and commit the regenerated pages. `pages/` is published and
checked byte-for-byte.

**Do not edit any claw-governed vendored file here** —
`src/taxonmech/schema/mech_shared.yaml`, `src/taxonmech/schema/history.yaml`,
`scripts/check_vendored_sync.{py,sh}`, `scripts/validate_id_label_correspondence.py`,
`scripts/chem_formula.py`, `scripts/deep_research_contract.py`,
`prompts/backlog-loop-goal.md` and the five vendored `tests/test_*` contract
files. They are vendored byte-identically from culturebotai-claw at the commit
pinned in `scripts/.vendored_canon_ref`. Fix upstream in claw, then re-sync
and bump the pin.

## Safe corpus workflow

**Canary before a bulk write.** Run `just seed`, then `just seed-canary
<IDENTIFIER>`. Inspect the written file, not only the exit code, before a full
`seed-apply`.

**Never rename a record file directly.** Change the identifier-to-slug entry in
`data/taxa/PATHS.tsv` and re-seed.

**Never guess a CURIE.** Every identifier in a record came from an inventory;
a curator-added grounding must resolve at its authority.

**An LLM-drafted change is `PROPOSED`, never `REVIEWED`.** Promotion is a
human decision.

## Git workflow

Branch before the first edit. Open a PR for every change, including docs-only
changes. Review the diff as a separate adversarial pass and file findings as
issues. Do not merge without explicit approval. Delete branches after merge.
