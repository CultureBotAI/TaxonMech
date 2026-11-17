# YAML Record Review: marine sediment bacterium BB0608_2216_4.2_1S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_4_2_1s0.yaml`
- Started UTC: 2026-10-04T07:58:39Z
- Finished UTC: 2026-10-04T07:59:29Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033382`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_2216_4.2_1S0 distinguishes this record from neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_4_2_1s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_4_2_1s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans returned no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Focused comparisons are not substitutes for those gates.

## Identity and Grounding

Backbone row 221016 and scientific-name row 30324 in
`data/catalog/ncbi_names-0005.jsonl.gz` match the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033382&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033382)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first chain matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not imply valid
nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750245.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750245.1),
UID 333384592, a 499-base partial 16S rRNA gene. Its source explicitly names
strain BB0608_2216_4.2_1S0 and taxon 1033382, coastal marine sediment,
Australia: Gulf of Carpentaria, and June 2008 collection. It supplies a
strain qualifier, not a clone or environmental-sample qualifier. This locus
is not a genome, collection deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither includes a DOI or
PMID. Full manuscript text was not obtained; no phenotype was inferred from
the title. Exact Assembly search returned zero with a phrase-not-found and
no-items warning. The single NAME attestation and 2026-09-13 snapshot agree
with the pinned inventory; counts do not denote independent studies.

## Completeness

Complete exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
BactoTraits inventories returned no rows. Empty optional slots reflect
checked source coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All four matches were inspected: target backbone, scope and scientific name,
and unrelated ATB sample SAMEA1033382. Recursive structured SOURCE.json
searches found no matches. These are bounded local searches, not universal
absence claims.

ATB sample SAMEA1033382, run ERR084498 and ENA analysis ERZ3068719 is
Staphylococcus aureus. Its available FASTA and passing filters do not
establish target identity. No target strain/deposit/genome chain was found
in that unrelated hit.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future source-backed corrections belong in maintained inventory inputs
and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained
at `curation/seed_scope.tsv:321368`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, verify exact strain/deposit identity,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033382 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run for this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13465`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
