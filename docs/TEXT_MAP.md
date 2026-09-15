# Semantic text map inputs

`just text-map-inputs` validates a preview of the **complete current corpus**.
It emits a summary; it does not run a model, generate coordinates or publish a map.
`just text-map-inputs --output build/text-map/inputs.jsonl` atomically exports
versioned semantic inputs for the shared fleet embedding pipeline.

For a canary, add `--limit 32` or repeat `--record data/taxa/<category>/<record>.yaml`.
The receipt explicitly says `subset`. A canary cannot stand in for full map
coverage. Taxon file paths are selected before YAML is parsed; a temporary
SQLite index keeps the file/identifier bookkeeping bounded in memory.

Each JSONL row has `identifier`, `label`, `category`, `page`, `source_path`,
`text`, `text_sha256` and `adapter_version`. The selected semantic fields
exclude citations, curation history, data-source counts and assembly/accession
identifiers. The source YAML is never edited. Duplicate identifiers and
symlink/outside-corpus paths are refused before output is published.

The taxon adapter includes name, optional definition, rank/domain, NCBI
lineage labels and source-qualified synonyms. Broad/close taxonomy mappings
are not synonyms; neither linked genomes nor text geometry establishes genome
or phylogenetic similarity. Links use the existing taxon viewer route.

The installed CLAW runtime is `scripts/embedding_pipeline.py`; its separate
locked environment and exact build commands are in the [maintained runtime guide](../conf/embedding-runtime/README.md).
Normal rendering and verification do not install that model environment or run
inference. When record membership or selected semantic fields change, export
fresh full inputs, reuse the existing profile-bound vector cache to encode only
new or changed text, regenerate PaCMAP, and validate the complete bundle before
rendering. A stale bundle must be refreshed before publishing curated changes.

## Validated site publication

`conf/text_map.yaml` enables the shared semantic text map. The verified
2026-09-15 build covers all 625,960 input records, with 50,000 displayed and
575,960 omitted from the bounded view. Every input has a validated vector;
omission affects display only. The complete site was rendered and checked
against those inputs, including all displayed taxon routes and retained content.
The current map manifest records the exact input, model and projection identity.
After refreshing a bundle, run `just render` on the complete source corpus.

The default PaCMAP display limit is 50,000 deterministically selected records.
Every input record must have a verified vector-cache entry, and the published
manifest reports the displayed and omitted counts. This does not turn a canary
into a complete-corpus build.

Rendering exports fresh **full-corpus** JSONL and validates the current pointer,
artifact checksums, complete input identity and pinned common BGE profile. The
runtime stages the selected `index.html`, `points.json` and `manifest.json` at
`pages/text-map/`; the site links to that view after successful staging. Missing
runtime or current pointer, stale inputs and invalid checksums fail an enabled
build. A failed preflight preserves the existing published pages.

`just render-check` uses the same validation and staging inside a temporary site.
These checks do not download weights, encode text or fit PaCMAP. A canary cannot
satisfy the full-corpus publication check.

Staging binds the exact immutable generation approved during preflight. A changed
current pointer or substituted generation fails validation before publication
(CLAW #429).
