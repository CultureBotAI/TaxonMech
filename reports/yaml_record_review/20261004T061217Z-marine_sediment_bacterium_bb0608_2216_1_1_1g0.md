# YAML Record Review: marine sediment bacterium BB0608_2216_1.1_1G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_1g0.yaml`
- Started UTC: 2026-10-04T06:10:56Z
- Finished UTC: 2026-10-04T06:12:17Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033324`, `SPECIES`,
`BACTERIA`, `EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried
strains, one NCBITAXON NAME attestation and one seed event. The label's
punctuation and final `1G0` distinguish it from other BB0608 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_1g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_1g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonyms, attestation, scope and seed-event
  comparisons passed. No direct children or exact type-material, merged-ID
  or dropped rows were found in the corresponding source scans.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, history/provenance/product gates and rendering.
  Focused source comparisons are not substitutes for those gates.

## Identity and Grounding

Backbone row 220958 and scientific-name row 30266 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the record. Live NCBI
EFetch and Datasets confirm [taxon 1033324](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033324),
the exact label, species rank, genetic code 11 and parent 49928. The full
root-first chain and ranks match: root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928). This is not the environmental
samples parent 48479 carried by the nearby TIHP records. No phylum, genus
or species-name publication status was inferred.

## Evidence

Exact Nuccore search returned one entry, [JF750187.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750187.1),
UID 333384534, a 412-base partial 16S rRNA gene. The source explicitly names
strain `BB0608_2216_1.1_1G0`, taxon 1033324, coastal marine sediment,
Australia's Gulf of Carpentaria and collection in June 2008. It uses a
strain qualifier, not a clone qualifier or environmental-sample flag.
Those distinctions were preserved; this review does not call the isolate
uncultured or equate its strain name with a registered culture deposit.

The inspected sequence references are the Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb study titled "A simple method for cryopreservation
of eukaryotic and prokaryotic micro-organisms in bulk marine sediment",
marked unpublished, and Cornall's direct submission of 2011-04-01. Neither
supplies a DOI or PMID. Exact-title and author/title web searches did not
identify an exact publication to inspect. No DOI was guessed or preservation
phenotype assigned to this isolate. Full manuscript text was not obtained.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The 16S accession is a locus, not an assembly. The single NAME attestation
and 2026-09-13 taxonomy snapshot match the pinned inventory.

## Completeness

Complete exact-ID scans returned no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits inventory entry. Consequently
`strain_count: 0` means zero linked inventory strains, not that the named
isolate was never cultured. Empty optional slots are supported within these
maintained inputs; a source strain qualifier alone cannot fabricate a
BacDive or culture-collection record.

An initial broad BB0608 family search returned 952 lines and exceeded the
display limit; it was not used to claim exact completeness. A completed
target-specific `rg --no-ignore --hidden -n -z` search covered numeric ID
with digit boundaries and the exact label/stem designation, including its
dot/underscore punctuation, across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. All four results were inspected: target scope,
backbone, scientific name and unrelated ATB sample SAMEA1033324. The latter
is a Staphylococcus aureus assembly row, not a taxonomy identifier or a
source-supported strain/sample link to BB0608_2216_1.1_1G0. Separate recursive
structured SOURCE.json scans returned no target matches. These searches
include ignored data but do not establish universal absence of evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and the stated checks.

## Recommended Edits

None. Preserve the exact isolate designation, unclassified placement and
source-count semantics. Future evidence-backed corrections belong in
maintained source inputs and `src/taxonmech/extract.py` /
`src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321310`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, verify the exact isolate/deposit
identity chain, inspect inventory deltas, run
`just seed-canary NCBITaxon:1033324 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration was
performed during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13405`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable: this YAML has no gene,
regulator or expression-module claim. Only this report and the documented
strict-validation TSV were written; YAML, inputs, scope, history, status and
GitHub state are unchanged.
