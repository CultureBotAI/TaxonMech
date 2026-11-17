# YAML Record Review: Ascoidea tarda (nom. inval.)

## Target

- File: `data/taxa/eukaryota/ascoidea_tarda_nom_inval.yaml`
- Identifier: `NCBITaxon:1301102`
- Label: `Ascoidea tarda (nom. inval.)`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2917583` / `unclassified Ascoidea (in: budding yeasts & allies)`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Saccharomycetes` -> `Ascoideales` -> `Ascoideaceae` -> `Ascoidea` -> `unclassified Ascoidea (in: budding yeasts & allies)`
- Existing review report: none found for `*ascoidea_tarda_nom_inval.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascoidea_tarda_nom_inval.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascoidea_tarda_nom_inval.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1301102`, labelled `Ascoidea tarda (nom. inval.)` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1301102` is a `SPECIES` child of `NCBITaxon:2917583` / `unclassified Ascoidea (in: budding yeasts & allies)`.
- The generated `genetic_code: 12` matches the raw NCBI genetic-code column for this yeast species.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Ascoidea tarda` plus related synonyms `Ascoidea sp. CJR-2013` and `Ascoidea tarda Kurtzman & Robnett, 2013`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascoidea tarda (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1301102`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1301102`, the exact `Ascoidea tarda` label stem, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1301102`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1301102` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0705381`, `Ascoidea tarda NRRL Y-2393`, with strain and culture collection ID `NRRL Y-2393`.
- GOLD organism `Go0705381` has one project, `Gp0831422`, with BioProject `PRJNA736342` and BioSample `SAMN20341658`.
- No native GOLD genome analysis rows were linked to `Go0705381` or to its project.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `1301102`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1301102`.
- Exact `NRRL Y-2393`, `NRRL:Y-2393`, and `NRRL:Y:2393` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1301102`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, yeast mitochondrial genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD `NRRL Y-2393` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascoidea_tarda_nom_inval.yaml`; it is generated and validates strictly.
- Preserve the invalid-name label, no-rank unclassified `Ascoidea` parent, yeast mitochondrial genetic code, NCBI synonym split, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascoidea_tarda_nom_inval.yaml` and `just validate-strict data/taxa/eukaryota/ascoidea_tarda_nom_inval.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has no genome-analysis row for `Ascoidea tarda NRRL Y-2393`; the generated record only attests the same aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
