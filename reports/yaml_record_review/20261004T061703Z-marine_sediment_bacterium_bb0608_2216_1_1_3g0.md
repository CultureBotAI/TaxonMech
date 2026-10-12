# YAML Record Review: marine sediment bacterium BB0608_2216_1.1_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_3g0.yaml`
- Started UTC: 2026-10-04T06:16:16Z
- Finished UTC: 2026-10-04T06:17:03Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033327`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The exact isolate designation
is BB0608_2216_1.1_3G0; nearby BB0608 names are not interchangeable.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_3g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. No direct children or exact type-material, merged-ID
  or dropped rows were found in the corresponding scans.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not replace those gates.

## Identity and Grounding

Backbone row 220961 and scientific-name row 30269 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
EFetch and Datasets confirm [taxon 1033327](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033327),
exact label, species rank, code 11 and parent 49928. All four ancestors and
ranks match: root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928). No phylum, genus or valid-publication status was inferred.

## Evidence

Exact Nuccore search returned one entry, [JF750190.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750190.1),
UID 333384537, a 379-base partial 16S rRNA gene. Inspected source qualifiers
explicitly identify strain BB0608_2216_1.1_3G0, taxon 1033327, coastal marine
sediment, Australia's Gulf of Carpentaria and collection in June 2008.
It uses a strain qualifier, not clone or environmental-sample qualifiers.
That alone does not establish a culture-collection deposit or genome.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study, marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Exact-title/author searches for this same study during the current
turn did not identify an exact publication to inspect. Full manuscript text
was not obtained, and no DOI or preservation phenotype was guessed.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single NAME attestation and 2026-09-13 snapshot match the pinned
inventory, not a biological strain census or independent-experiment count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits row. Zero linked inventory
strains does not imply that the named isolate was never cultured. The
unpopulated optional slots match the maintained source coverage.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and the exact label/stem designation, preserving the
dot/underscore distinction, throughout `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`. All four matching lines were inspected:
target scope, backbone, scientific name and unrelated ATB sample SAMEA1033327.
The latter is classified as Staphylococcus aureus and supplies no exact
isolate/BioSample identity chain. Recursive structured SOURCE.json scans
returned no matches. No neighboring-isolate evidence or assembly equivalence
was inferred. These are bounded local-source findings, not universal absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and the documented checks.

## Recommended Edits

None. Preserve the exact isolate designation and carried unclassified lineage.
Future evidence-backed corrections belong in maintained inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321313`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact isolate/deposit evidence
and inventory deltas, run `just seed-canary NCBITaxon:1033327 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13408`. The seed event remains
2026-09-13T17:54:04Z. The Taxonomy Browser request failed; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub remain unchanged.
