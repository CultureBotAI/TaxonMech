# YAML Record Review

- Target: `data/taxa/eukaryota/morchella_snyderi.yaml`
- Taxon: `NCBITaxon:1174678` (`Morchella snyderi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1174678`, label `Morchella snyderi`.
- It is grounded exactly under `NCBITaxon:1051054` (`Morchella sect. Distantes`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Morchella sect. Distantes`.

## Validation

- `just validate data/taxa/eukaryota/morchella_snyderi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/morchella_septentrionalis.yaml ... morchella_sp.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58197` contains the seeded identifier with reason `attested rule: Morchella snyderi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:260864` matches the YAML parent and rank, has no exact synonyms, and carries 42 related synonyms: 40 `Morchella cf. elata` strain-style names, `Morchella snyderi M. Kuo & Methven, 2012`, and `Morchella sp. Mel-12`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:260864` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3866`, where `NCBITaxon:1174678` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0401823` / `Morchella snyderi CBS 144464`, linked to projects `Gp0272393` and `Gp0304612`.
- Native analysis `Morchella snyderi CBS 144464 Standard Draft` links through `AP PROJECT GOLD IDS` `Gp0272393`.
- `data/raw/ncbi_type_material.tsv:11430-11431` has two holotype aliases, `OSC 139277` and `OSC:139277`.

## Completeness

- BacDive exact rows, generated strain rows, exact StrainInfo direct/deposit rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1174678`.
- A complete ignored-file-inclusive scan of `data/raw/ncbi_merged_ids.tsv` found 42 retired IDs mapping into this target: contiguous `NCBITaxon:1051010` through `NCBITaxon:1051049`, plus `NCBITaxon:746134` and `NCBITaxon:746154`.
- A complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` rows for those retired IDs, so they are side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation adds strain data or retained retired-ID provenance to this record.

## Additional Notes

- The large synonym list and large merge list are both generated side effects of the collapsed `Morchella cf. elata` strain-style historical identifiers.
