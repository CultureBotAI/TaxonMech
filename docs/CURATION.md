# Curation rules

What is and is not a TaxonMech record, how it is identified, and what evidence
each part must carry. The schema and tests enforce the checkable parts; this
text explains the judgements.

## What is a record

A record is **one species-level or lower taxon in NCBI Taxonomy** that at
least one strain-bearing source attests: a species, a subspecies, a
strain-level or other infraspecific taxon, or an unranked taxon under a
species. **This is a repository rule.** Genera, families and every higher
rank are never records; they appear only as `lineage` entries. The seeder
refuses a higher taxon in the scope and `tests/test_corpus_integrity.py`
enforces it on the corpus.

Ancestry determines eligibility only for `NO_RANK` (including an empty
inventory rank) and `CLADE` entries. An explicitly higher rank remains out
of scope even if its inventory parent chain contains a species.

**Lineage is carried, not curated.** `lineage` is NCBI Taxonomy's parent
chain, verbatim. TaxonMech does not reconcile the NCBI, GTDB and LPSN
hierarchies, does not resolve disagreements between them, and never infers a
placement. A curator who finds NCBI's placement wrong reports it upstream; a
curator who wants GTDB's placement finds it in `taxonomy_mappings`.

| Thing | Record? |
|---|---|
| A species, subspecies, strain-level or unranked-under-species NCBI taxon | **Yes**, when in scope |
| A genus, family or any higher taxon | **No** — a `lineage` entry, never a record |
| A BacDive strain | **No** — a `strains` entry on its taxon's record, identified by its kg-microbe strain id and deposits |
| A GTDB species with no NCBI counterpart | **Not yet** — see the identity discussion in [HARMONIZATION.md](HARMONIZATION.md) |
| A trait, habitat, medium or phenotype of the taxon | **No** — TraitMech, HabitatMech and CultureMech own those; a TaxonMech record carries only the attestation count |

## Identifiers

1. **The NCBITaxon CURIE is the identity.** `NCBITaxon:562`, never the LPSN
   or GTDB id, which are `xrefs` and `taxonomy_mappings`.
2. **Never reuse an identifier.** A superseded record stays in place with
   `mapping_status: DEPRECATED`; the successor names it in `replaces`.
3. **Never guess a CURIE.** Every identifier in a seeded record came from an
   inventory. A curator adding a grounding to a causal-graph node must have
   resolved it at its authority; `just validate-products` checks the label.

## Files

`data/taxa/<domain>/<slug>.yaml`, where `<domain>` is the lower-cased
`taxon_domain` and `<slug>` is pinned in `data/taxa/PATHS.tsv`. A test checks
both. Rename by editing the lockfile and re-seeding, never by moving the file.

## Seeded fields are read-only

Everything the seeder writes — identity, lineage, synonyms, nomenclature,
mappings, strains, attestations, the seed event — is regenerated on every
`seed-apply`, and `just verify-corpus` fails on any difference. A hand edit to
a seeded field is therefore not curation; it is drift that the next re-seed
reverts. Curation goes in:

- **the scope** (`curation/seed_scope.tsv`) — which taxa are records;
- **the seeder** — when a harmonization rule is wrong for a class of records;
- **kg-microbe** — when a mapping is wrong upstream (an LPSN name mapped to
  the wrong NCBI taxon, a GTDB predicate that should be `closeMatch`). Fix it
  there, re-extract, re-seed; this repository does not carry mapping
  overrides yet.

Curator-owned overlays for `causal_graphs`, `definition`, `evidence` and
`mapping_status: REVIEWED` — merged by the seeder so they survive a re-seed,
as HabitatMech does under `curation/causal_graphs/` — are the next step and
are tracked in the issues. Until they exist, a curated change is a seeder
change with a test.

## Evidence

- **Record-level `evidence` is optional** for seeded records: their provenance
  is `source_attestations`, each of which names its source identifier.
- **Every causal-graph edge requires evidence.** The schema enforces it. A
  mechanism claim is curator-asserted and nothing upstream backs it.
- `snippet` is for **verbatim** quotes only. When you have not seen the
  source text, use `notes` to paraphrase what the source establishes.
- Prefer DOIs; PMIDs are fine. A reference the curator has not opened is not
  evidence.

## Nomenclature

LPSN is the authority on prokaryotic names. A record keeps every LPSN name
that maps to its NCBI taxon, with LPSN's own status line verbatim and three
booleans parsed from it. The `is_correct_name` flag is LPSN's, not ours; if
NCBI and LPSN disagree about which name is current, the record shows both and
a curator's job is to say so in a discussion, not to pick one silently.

## Strains

A strain entry is an identity — the BacDive id, the designation, the
culture-collection deposits, and `classified_as` when BacDive files it under
a descendant taxon — with explicit `genome_assemblies` and `genome_records`
and one derived flag, `is_type_strain`. Strain-to-genome relationships are a
primary curation priority. Prioritize NCBI assemblies and include typed
BV-BRC / PATRIC and IMG genome records with their source evidence. Retain
multiple links, source-supplied accession versions and descriptions such as
`plasmid` or `wgs`; an imported link need not represent a complete assembly.

A shared species name or taxon ID does not establish a strain-to-genome link.
Co-occurrence on one BacDive record does not establish that two database
identifiers denote the same genome. Assemblies, genome records, BioSamples,
marker-gene sequences and culture deposits denote different things; see
[STRAIN_GENOMES.md](STRAIN_GENOMES.md). Strain phenotypes, media and isolation
sources belong to the sibling repositories that model them. `medium_count`
is kept because it says how well characterised the strain is, which is what
a reader choosing a strain wants to know.

## Discussions

A discussion is provenance, not a task description. It records a question that
was raised, who raised it, and why it matters. `prompt` may be narrowed as
parts are answered; `rationale` is appended to, never replaced; `posed_date`
never moves. Issue links belong in `evidence`.

## Status

| `mapping_status` | Meaning |
|---|---|
| `SEEDED` | Generated from the inventories; unread. |
| `PROPOSED` | A curator (or an LLM) has changed something; unread by a second curator. |
| `REVIEWED` | A human curator has checked identity, nomenclature and mappings. Requires a `curation_history`. |
| `DEPRECATED` | Superseded; see `replaces` on the successor. |

An LLM-drafted change is `PROPOSED`, never `REVIEWED`. Every mutation appends
a `CurationEvent` through `taxonmech.curate.curation_event.record_curation_event`;
set `llm_assisted: true` when a model produced the change.
