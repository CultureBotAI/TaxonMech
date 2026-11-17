# YAML Record Review: marine sediment bacterium BB0608_2216_1.1_2G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_2g0.yaml`
- Started UTC: 2026-10-04T06:13:09Z
- Finished UTC: 2026-10-04T06:13:59Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033325`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The exact designation is
BB0608_2216_1.1_2G0, distinct from 1G0 and 2S0.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_2g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_2g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete identity, lineage, synonym, attestation, scope and seed-event
  comparisons passed. No direct children or exact type-material, merged-ID
  or dropped rows were found in the corresponding source scans.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source checks do not substitute for these gates.

## Identity and Grounding

Backbone row 220959 and scientific-name row 30267 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
EFetch and Datasets confirm [taxon 1033325](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033325),
exact label, species rank, code 11 and parent 49928. All four ancestors and
ranks match: root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928). No genus, phylum or nomenclatural validity was inferred.

## Evidence

Exact Nuccore search returned one entry, [JF750188.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750188.1),
UID 333384535, a 482-base partial 16S rRNA gene. Inspected source qualifiers
give strain BB0608_2216_1.1_2G0, taxon 1033325, coastal marine sediment,
Australia's Gulf of Carpentaria and collection in June 2008. The source
uses a strain qualifier, not a clone or environmental-sample qualifier.
This does not create a registered culture-deposit identifier or genome.

Both sequence references were inspected: Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb's marine-sediment cryopreservation study, marked
unpublished, and Cornall's 2011-04-01 direct submission. Neither supplies
a DOI or PMID. Exact-title/author searches for that same study during this
turn identified no exact publication to inspect; no DOI was guessed. Full
manuscript text was not obtained, and no cryopreservation phenotype was
assigned to this isolate from the reference title.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single NAME attestation and 2026-09-13 snapshot agree with the inventory,
not a count of biological strains or independent experiments.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits row. Zero inventoried strains
does not assert that this named isolate was never cultured. Empty optional
slots reproduce the maintained source coverage.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and the exact label/stem designation, preserving the
dot/underscore distinction, across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. All four matching lines were inspected: the target
scope, backbone, scientific name and unrelated ATB sample SAMEA1033325.
That sample is classified as Staphylococcus aureus and provides no strain
or BioSample evidence chain to this sediment isolate. Separate recursive
structured SOURCE.json searches returned no matches. No assembly equivalence
or neighboring-isolate evidence was inferred. These bounded searches do not
prove universal absence of additional biological information.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and the documented checks.

## Recommended Edits

None. Preserve the exact isolate designation and unclassified NCBI lineage.
Future supported corrections belong in maintained inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321311`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact isolate/deposit evidence
and inventory deltas, run `just seed-canary NCBITaxon:1033325 --force`, both
focused validators, `just verify-corpus` and the remaining QC gates. No
canary or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13406`. The seed event remains
2026-09-13T17:54:04Z. The Taxonomy Browser request failed; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub are unchanged.
