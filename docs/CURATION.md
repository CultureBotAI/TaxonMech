# Curation rules

What is and is not a TaxonMech record, how it is identified, and what evidence
each part must carry. The schema and tests enforce the checkable parts; this
text explains the judgements.

## What is a record

A record is **one taxon in NCBI Taxonomy**, at any rank, that at least one
strain-bearing source attests. Species dominate because that is what LPSN
names, GTDB delimits and BacDive files strains under; genera and higher ranks
appear as records when a source attests them directly, and always appear as
`lineage` entries.

| Thing | Record? |
|---|---|
| A species, subspecies, genus or higher taxon with an NCBI id | **Yes**, when in scope |
| A strain | **No** — a `strains` entry on its taxon's record, identified by its kg-microbe strain id and deposits |
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
a descendant taxon — and one derived flag, `is_type_strain`. Nothing
about the strain's phenotype, medium or isolation source lives here; those
belong to the sibling repositories that model them. `medium_count` is kept
because it says how well characterised the strain is, which is what a reader
choosing a strain wants to know.

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
