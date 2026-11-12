# Native EdgeMech assertion adapter

The package module `taxonmech.edge_curation` exports immutable Git-committed
`data/raw/gtdb_mappings.tsv` rows as canonical native assertions. It preserves complete
selected rows, file hashes, source positions, source commit and native scope.
No generated records are edited and no independent scientific review or KG
occurrence approval is created.

The complete extracted GTDB-to-NCBI mapping inventory has no exact assertion-level native approval proof in this surface. All exported rows remain unassessed. Strain/deposit identity, genome assembly links and nomenclature need distinct native adapters and evidence, rather than inheritance from a generated record status.

The optional shared contract source is pinned at CLAW commit
`6141da81dc521d776e1ebcff1c4e63824313a9a1`. Use an explicit checkout of that
revision on PYTHONPATH alongside this repository's src directory, and run
`scripts/adhoc/check_edge_contract_pin_20261107.py --claw-root PATH`.
The dedicated CI integration tier makes a missing shared dependency an error
with `REQUIRE_EDGE_CONTRACT=1`; ordinary native tests may skip this optional
integration when CLAW is absent.

Run one real unit first through the same module, shell and environment:

```bash
python -m taxonmech.edge_curation --root . --source-commit FULL_NATIVE_COMMIT --workers 4 --positions 1 --output build/edge-curation/canary
```

Verify the persisted assertions.jsonl and manifest.json, counts and hashes.
Then replace `--positions 1` with `--all` and select a new output directory for
the complete declared native surface. Output streams into a staging directory;
the destination is reserved exclusively and the manifest is published last
after the payload is complete. Files and directories are synced; consumers
ignore incomplete destinations without a manifest.
Four spawn-safe workers validate generated assertions in bounded windows of
at most 256 rows, retaining source order. Persisted exact byte and ordered
identity/position digests must reconcile with the generated validated stream
before publication; identical persisted bytes do not undergo a duplicate
full JSON Schema pass. Use the same worker count for canary and full export.
Existing destinations are never overwritten. Keep analytical outputs in
ignored build/; there is no per-row GitHub record or Pages publication.
