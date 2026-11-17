# YAML Record Review: marine sediment bacterium BB0608_2216_1.1_2S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_2s0.yaml`
- Started UTC: 2026-10-04T06:14:43Z
- Finished UTC: 2026-10-04T06:15:30Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033326`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The exact isolate designation
is BB0608_2216_1.1_2S0, not neighboring 2G0.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_2s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_2s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full identity, lineage, synonym, attestation, scope and seed-event
  comparisons passed. No direct children or exact type-material, merged-ID
  or dropped rows were found in their corresponding source scans.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused comparisons do not replace those gates.

## Identity and Grounding

Backbone row 220960 and scientific-name row 30268 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
EFetch and Datasets confirm [taxon 1033326](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033326),
exact label, rank, code 11 and parent 49928. The complete root-first chain
and ranks match: root (1), cellular organisms (131567), Bacteria (2),
unclassified Bacteria (49928). No more specific classification or valid
publication status was inferred.

## Evidence

Exact Nuccore search returned one entry, [JF750189.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750189.1),
UID 333384536, a 497-base partial 16S rRNA gene. Its inspected qualifiers
name strain BB0608_2216_1.1_2S0, taxon 1033326, coastal marine sediment,
Australia's Gulf of Carpentaria and collection in June 2008. The source
uses a strain qualifier, not a clone or environmental-sample qualifier;
no registered deposit or assembly identity follows from that alone.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study, marked unpublished,
and Cornall's direct submission dated 2011-04-01. No DOI or PMID is supplied.
Exact-title/author searches for the same study during this turn did not
identify an exact publication to inspect. Full manuscript text was not
obtained, and no identifier or cryopreservation phenotype was guessed.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single NAME attestation and 2026-09-13 snapshot reproduce the inventory,
not a count of biological strains or independent studies.

## Completeness

Complete exact-ID scans returned no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero linked inventory
strains does not mean that the named isolate was never cultured. Empty
optional slots match the maintained inputs.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and the exact label/stem designation, including its
dot/underscore punctuation, across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. All four matching lines were inspected: target
scope, backbone, scientific name and unrelated ATB sample SAMEA1033326.
That sample is classified as Staphylococcus aureus; its numeric accession
is not this taxon and supplies no strain/sample identity chain. Recursive
structured SOURCE.json searches returned no matches. No assembly equivalence
or neighboring-isolate evidence was inferred. These are bounded local-source
results, not a universal absence claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and stated checks.

## Recommended Edits

None. Preserve the exact isolate designation and carried unclassified lineage.
Future supported corrections belong in maintained inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321312`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact isolate/deposit evidence
and inventory deltas, run `just seed-canary NCBITaxon:1033326 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13407`. The seed event remains
2026-09-13T17:54:04Z. The Taxonomy Browser request failed; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub remain unchanged.
