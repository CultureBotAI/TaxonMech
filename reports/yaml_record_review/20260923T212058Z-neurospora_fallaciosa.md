# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_fallaciosa.yaml`
- Taxon: `NCBITaxon:2082126` (`Neurospora fallaciosa`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2082126`, label `Neurospora fallaciosa`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_fallaciosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_fallaciosa.yaml data/taxa/eukaryota/neurospora_foveaconica.yaml data/taxa/eukaryota/neurospora_galapagosensis.yaml data/taxa/eukaryota/neurospora_hapsidophora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62285` contains the seeded identifier with reason `attested rule: Neurospora fallaciosa, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:517713` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:517713` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19930`, where `NCBITaxon:2082126` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651460` / `Neurospora fallaciosa MNHN RF-02373`, linked to two native projects and no native analyses.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:2082126` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 1 direct record and 1 exact deposit assertion, `CBS 458.67`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:2082126`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
