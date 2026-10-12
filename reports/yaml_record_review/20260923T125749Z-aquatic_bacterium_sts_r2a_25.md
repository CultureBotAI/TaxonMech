# YAML Record Review: aquatic bacterium STS_R2A_25

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/aquatic_bacterium_sts_r2a_25.yaml
- Started UTC: 2026-09-23T12:56:18Z
- Finished UTC: 2026-09-23T12:57:49Z
- Verdict: pass

## Target

`data/taxa/bacteria/aquatic_bacterium_sts_r2a_25.yaml` is the generated `TaxonRecord` for `NCBITaxon:100876`, label `aquatic bacterium STS_R2A_25`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:57609` `unclassified Lysobacteraceae`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*aquatic_bacterium_sts_r2a_25.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/aquatic_bacterium_sts_r2a_43.yaml data/taxa/bacteria/aquatic_bacterium_sts_r2a_25.yaml data/taxa/bacteria/aquatic_bacterium_sts_r2a_01.yaml data/taxa/bacteria/aquatic_bacterium_sts_r2a_20.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/aquatic_bacterium_sts_r2a_25.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:17335` supports the identifier, label, species rank, parent, genetic code `11`, the NCBI-only source flag, and the `2026-09-13` snapshot note. The generated lineage terminates at the same `NCBITaxon:57609` parent and includes the `NCBITaxon:2` Bacteria domain ancestor.

## Evidence

The only `source_attestations` entry is a one-count `NCBITAXON` `NAME` assertion, matching the pinned NCBI row and the `curation/seed_scope.tsv:143116` inclusion row.

## Completeness

Exact gitignore-independent searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon rows for `NCBITaxon:100876`, the full label, or the slug. The absence of synonyms, LPSN nomenclature, GTDB mappings, BacDive strains, ATB or StrainInfo genome links, evidence, definitions, discussions, and causal graphs is expected for this NCBI-only seeded record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:100876`, rerun `just seed-canary NCBITaxon:100876`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
