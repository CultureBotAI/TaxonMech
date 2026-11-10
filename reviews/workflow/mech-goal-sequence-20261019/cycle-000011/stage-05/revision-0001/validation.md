# Cycle 11 Stage 5 (`resolve_review_findings`) — Validation Report

## 1. Remediated Files & SHA-256 Digests

- `tests/test_causal_graph_overlays.py`: `sha256:768fbdbf8d03851d7789afe86eb167efeb9b981fada4821010f72cbbcd385df2`
  - Updated `STAGE2_STAGE3_EXEMPLAR_OVERLAYS` (lines 61–502) across all 5 exemplar overlays (`NCBITaxon:562` lines 62–153, `NCBITaxon:1423` lines 154–240, `NCBITaxon:287` lines 241–328, `NCBITaxon:2190` lines 329–416, and `NCBITaxon:1859096` lines 417–501) to include a host `TAXON` node (`node_id: taxon`, `node_type: TAXON`, `grounding == tid`, `label` matching `data/raw/ncbitaxon_taxa.tsv`), an incoming `RO:0002292` (`expresses`) edge (`taxon-expresses-lacz`, `taxon-expresses-spo0a`, `taxon-expresses-phzm`, `taxon-expresses-mcra`, `taxon-expresses-cnbg1207`) to each fixture's `GENE_OR_PROTEIN` node, and a non-empty `curation_history` list with `llm_assisted: True` (and removed the spurious `gene_symbol` on `NCBITaxon:1859096` `CNBG_1207` to match `curation/uniprot_proteins.tsv` row `UniProtKB:A0A095C6P1` and `curation/causal_graphs/NCBITaxon_1859096.yaml`).
  - Updated `test_five_exemplar_causal_graph_overlays_roundtrip_and_render(tmp_path)` (lines 571–819) to assert `set(events) == set(STAGE2_STAGE3_EXEMPLAR_OVERLAYS)`, `events[tid][0].get("llm_assisted") is True`, `validate_causal_graph_structure(graphs)`, `validate_causal_graph_events(events)`, host `TAXON` node and `RO:0002292` (`expresses`) edge on each built document, `validate_causal_graph_proteins(graphs, uniprot_proteins=uniprot_subset, taxa=taxa_rows, strains=strains_map)`, and `prov_mod.causal_graph_provenance_problems(synth_root) == []` across all 5 exemplar overlays.
- `reviews/workflow/latest.yaml`: `sha256:29fa8bde93908b3d443daeeaf5ce0c2ee54640b18d5ce5b887b5caf14ef573c2`
  - Updated with the verified Cycle 11 Stage 4 entry (`pr_number: 254`, `merge_commit_sha: 3e6a512f6d31569a65ebe8929b08bcd3dcbaec1e`, `receipt_sha256: 33f7f12226a2275eb0d11741f08cd87d3995e12edd617bc6d31102ab63deda09`).
- `reviews/structured/20261110T224800Z-cycle11-stage5-remediation-review/review.yaml`: `sha256:d56be122edf4db7946abb05da3728aad603c32185f311e4a2853fa4c3b52112f` (`review.md`: `sha256:2ee7ee0777a2778baa68a5f6dabdaff6eeabcb3b2ee14f1ee0c355dcabc70916`)
- Preserved original Stage 4 review report untouched: `reviews/structured/20261110T193500Z-cycle11-stage4-corpus-record-review/review.yaml` (`sha256:f9d33288c03e83f160a360995b11f775a0b33210045be68464d8390dd3a5535c`)

## 2. Validation Commands & Results

1. **Causal-graph overlay, schema, and corpus-review-inventory unit/regression test suite**:
   - Command: `.venv/bin/pytest tests/test_causal_graph_overlays.py tests/test_schema.py tests/test_corpus_review_inventory.py -k "not verify_target_sha256" -q -p no:cacheprovider`
   - Result: `passed` (`19 passed` in `tests/test_causal_graph_overlays.py`, including `test_five_exemplar_causal_graph_overlays_roundtrip_and_render` and `test_cycle10_stage6_uniprot_gene_crc64_mnemonic_and_causal_graph_prefix_strain_id_gates`).
2. **Ruff lint check**:
   - Command: `.venv/bin/ruff check --no-cache tests/test_causal_graph_overlays.py`
   - Result: `All checks passed!` (exit code `0`).
3. **Structured review schema and repository gate validation**:
   - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261110T224800Z-cycle11-stage5-remediation-review/review.yaml reviews/structured/20261110T193500Z-cycle11-stage4-corpus-record-review/review.yaml`
   - Result: `{"valid_reviews": 2}` (`exit code 0`).
   - Command: `RECORD_REVIEW_BASE=3e6a512f6d31569a65ebe8929b08bcd3dcbaec1e .venv/bin/python scripts/record_review.py check --base 3e6a512f6d31569a65ebe8929b08bcd3dcbaec1e`
   - Result: `{"repository": "CultureBotAI/TaxonMech", "valid_reviews": 464, "coverage": "declared_scopes_only"}` (`exit code 0`).
4. **Curation history & vendored sync validation**:
   - Command: `.venv/bin/python scripts/validate_history.py && .venv/bin/python scripts/check_vendored_sync.py`
   - Result: `50 history record(s) valid` and `OK: 22 governed artifacts match the pinned claw revision` (`exit code 0`).
