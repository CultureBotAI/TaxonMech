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

The downstream encoder/PaCMAP runtime and published view are separate work;
this exporter alone does not resolve the missing-map issue.


## Validated site publication

`conf/text_map.yaml` explicitly starts with `enabled: false`; no common map or
navigation link is claimed ready yet. After generating and reviewing the full
input-bound bundle under `data/text_map/`, set `enabled: true` and run `just render`.
The shared CLAW runtime must first be installed at `scripts/embedding_pipeline.py`.

When enabled, rendering exports fresh **full-corpus** JSONL and validates the
current pointer, artifact checksums, input coverage and pinned common BGE profile.
The runtime atomically stages the current bundle's `index.html`, `points.json`
and `manifest.json` at `pages/text-map/`. Only successful staging enables the
navigation link. Missing runtime/current pointer, stale inputs or invalid
checksums fail the build; they never silently hide an enabled map. The existing
published pages are retained if this preflight fails.

`just render --check` uses the same validation and staging inside its temporary
site. Ordinary checks do not download weights, encode text or fit PaCMAP.
The initial disabled setting is temporary rollout state, not a resolution of
the missing-map issue. Canaries must not be enabled as full-corpus publication.

Site staging binds the exact immutable bundle approved during preflight. If the
current pointer changes before staging, rendering fails instead of publishing a
different generation under the earlier encoder-policy approval (CLAW #429).
