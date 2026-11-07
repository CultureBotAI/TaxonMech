# Typed native strain links

This advances [#226](https://github.com/CultureBotAI/TaxonMech/issues/226)
through three separate native surfaces: strain-to-NCBI assembly,
strain-to-genome-record and strain-to-related-record. The initial GTDB mapping
export and its existing receipts remain unchanged. Every added link is
**unassessed** because the native inventories do not contain exact
assertion-level review proofs.

The source pin is `ab35a0d0a0a2b47d250145db0c15b414fccbfdb8`. Shared native
contracts come from `1b5391d083ba85ac94e5279c3cba25ac4fde243c`, the immutable
contract prerequisite in CLAW PR #962. No native schema, generated taxon
record, source inventory or primary biological assertion was changed.

At this code freeze the three native canaries have passed, while complete
exports are still finishing. The source-row counts below describe the verified
input inventories, not a claim that every full output is already published.
Final full-output hashes and downstream census results will be retained in
EdgeMech validation records and linked in this PR after publication checks.
Adapter source SHA-256 is
`c422f95a82d2c39b0935fdb35d216f45a88093909174e599fbadcb5d9932aa2d`.

## Scope and evidence

| Surface | Native class / predicate | Source rows | Missing matched-owner rows |
| --- | --- | ---: | ---: |
| `assemblies` | `GenomeAssemblyLink` / `taxonmech:genome_assemblies` | 159,283 | 147 |
| `genomes` | `GenomeRecordLink` / `taxonmech:genome_records` | 126,576 | 74 |
| `related` | `GenomeRelatedRecordLink` / `taxonmech:related_records` | 455,720 | 445 |

Each row retains every original source column, including accession versions,
native database/type, source field, matched strain, verbatim strain identifiers,
source reference and GOLD organism/project/analysis chain. Taxon metadata
does not override strain classification. Plasmid or draft scope does not imply
a complete cellular genome. An unversioned NCBI accession remains unversioned.

Both owner inventories are verified against the native manifest:
101,417 BacDive strain rows and 154,969 culture-collection rows. Exact lexical
owner matches include the full selected row, source position and file/payload
hashes. Owner membership is provenance, not a new collection-identity check.
No alias rewriting, case folding, suffix normalization or species/name join is
performed. There are no missing subject owners; the 147/74/445 missing matched
owner references remain explicit in assertions and manifest counters.

Source, owner, manifest, schema, curation guidance and native genome-source
code are hash-bound. The whole source and owner inventories are checked for
byte hashes, sizes, row counts and flat native identifier/type constraints
before selecting a canary. External primary-source files named in the native
manifest have not been fetched or reverified.

Nested AllTheBacteria and StrainInfo overlays require their own evidence
adapters and are excluded from these flat source profiles. Nomenclature,
strain/deposit equivalence, exact native reviews and reviewed KG predicate
projections also remain outside this expansion. Thus #226 stays open for the
remaining evidence and scientific admission work. A native link is never
treated as taxonomic or genome identity equivalence.

## Verification

Independent read-only review found no blocking issue. The focused native
contract suite passed **35 tests**, covering typed namespace constraints,
unversioned and dotted identifiers, GOLD chains, owner-review isolation,
unavailable lexical owners, serial/spawn byte identity, worker failure,
complete input preflight and persisted valid-row reorder/duplication rejection.
Ruff passed. The previously reviewed publication helper is unchanged.

The same four-worker spawn path validates every generated envelope, retaining
source order with at most 256 submitted rows. Only the selected row's owners
are passed to workers. Persisted bytes and ordered identity/source-position
membership must match the validated stream before publication. Payload and
directory entries are flushed, and the manifest appears last in an exclusively
created destination. No output is overwritten.

Each surface used one real end-to-end canary after free full-input preflight.
The actual nonlogin Bash launcher used this worktree's `src` and the detached
`culturebotai-claw-edgemech-contract-1b5391d/src` on `PYTHONPATH`, with the
adjacent `culturebotai-claw-edgemech-20261107/.venv/bin/python`. No provider or
credentials are required. The module is the retained reproducible launcher.

```bash
python -m taxonmech.edge_links --root . \
  --source-commit ab35a0d0a0a2b47d250145db0c15b414fccbfdb8 \
  --surface assemblies --workers 4 --positions 1 \
  --output build/edge-curation-20261107/links-v1/assemblies-canary
```

Use each surface (`assemblies`, `genomes`, `related`) with `--all --plan` for
free preflight, then `--positions 1` to a fresh canary destination. Inspect the
persisted artifact before using `--all` without `--plan` for a fresh full
destination. The recorded paths already exist; repeats need new versioned
paths. Transport, persistence and typed source scope are verified; biological
approval and KG occurrence compatibility are not supplied by these checks.

## Canary receipts

All paths are under `build/edge-curation-20261107/links-v1/`. Each canary has
one unassessed row and reports zero independent reviews and zero KG approvals.

| Directory | JSONL bytes | Manifest SHA-256 |
| --- | ---: | --- |
| `assemblies-canary` | 6,696 | `b669e8cce1708487a05c3a40092a6b1df7652fa2fd4523ea78ba73c1cbf90503` |
| `genomes-canary` | 7,191 | `f859f3500ca5631a98f0548dc94899c9bd41551e55deef847e8a446065c09356` |
| `related-canary` | 6,900 | `3cb531b5a45a10f66c6b6dd68fa38e26981faba6a4fa605c26b49b391fd0938d` |

| Directory | Assertions SHA-256 |
| --- | --- |
| `assemblies-canary` | `bf3a0b99157c440d88c0707f48c2dcd83a1646b9bb408b52e7cd3c1b5c828b33` |
| `genomes-canary` | `a60f7de9c9d4302b449f3c19718a48a61ff0966acafcbb817d19d8c71948a6fd` |
| `related-canary` | `4da258c749f2a0e0e49b7835ae7b071ccfa3a26e86efea06e02ffdbaa2b760d6` |
