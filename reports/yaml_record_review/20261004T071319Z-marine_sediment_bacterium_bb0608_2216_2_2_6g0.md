# YAML Record Review: marine sediment bacterium BB0608_2216_2.2_6G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_2_2_6g0.yaml`
- Started UTC: 2026-10-04T07:12:32Z
- Finished UTC: 2026-10-04T07:13:19Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033357`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. BB0608_2216_2.2_6G0 is distinct
from the neighboring 2.2_4G0 and similarly named 2.1_6G0 strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_2_2_6g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_2_2_6g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans found
  no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not replace these gates.

## Identity and Grounding

Backbone row 220991 and scientific-name row 30299 in
`data/catalog/ncbi_names-0005.jsonl.gz` match the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033357&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033357)
confirm ID, label, species rank, code 11 and parent 49928. The root-first
chain matches: root (1), cellular organisms (131567), Bacteria (2),
unclassified Bacteria (49928). No finer taxonomic placement or formal
nomenclatural publication was inferred from the species rank.

## Evidence

Exact Nuccore search returned one entry, [JF750220.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750220.1),
UID 333384567, a 369-base partial 16S rRNA gene. Source qualifiers identify
strain BB0608_2216_2.2_6G0, taxon 1033357, coastal marine sediment,
Australia's Gulf of Carpentaria and June 2008 collection. The strain
qualifier is not a clone or environmental-sample qualifier. This locus
does not establish a registered deposit, genome or independent classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study, marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI or
PMID. Full manuscript text was not obtained; no isolate cryopreservation
phenotype or publication identifier was inferred from the title.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME assertion and 2026-09-13 taxonomy snapshot reproduce the pinned
source; assertion count is not a biological-strain or independent-study count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero inventoried strains
does not imply the named strain was never cultured. Empty optional fields
reflect the maintained source coverage checked.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and exact label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All four matched lines were inspected: target scope, backbone, scientific
name and ATB Staphylococcus aureus sample SAMEA1033357. Recursive structured
SOURCE.json searches returned no matches. The unrelated sample establishes
no target strain/BioSample/assembly identity chain. These bounded local-source
results are not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve exact strain identity and unclassified lineage. Future
evidence-backed fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321343`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact strain/deposit identity
and inventory deltas, run `just seed-canary NCBITaxon:1033357 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13440`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets succeeded.
iModulonDB was not applicable to this taxonomy-only record. Only this report
and the documented validation TSV were written for this target; YAML,
maintained inputs, scope, history, status and GitHub remain unchanged.
