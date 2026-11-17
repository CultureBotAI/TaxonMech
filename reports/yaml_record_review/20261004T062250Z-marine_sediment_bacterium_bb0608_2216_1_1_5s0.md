# YAML Record Review: marine sediment bacterium BB0608_2216_1.1_5S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_5s0.yaml`
- Started UTC: 2026-10-04T06:20:14Z
- Finished UTC: 2026-10-04T06:22:50Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033329`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The exact strain designation
is BB0608_2216_1.1_5S0; neighboring BB0608 records are distinct.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_5s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_5s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonyms, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans
  found no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not replace these gates.

## Identity and Grounding

Backbone row 220963 and scientific-name row 30271 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033329&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033329)
confirm the exact ID, label, species rank, code 11 and parent 49928.
The complete ancestor chain agrees: root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928). No finer placement or formal
nomenclatural status was inferred from the species rank.

## Evidence

Exact Nuccore search returned one entry, [JF750192.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750192.1),
UID 333384539, a 411-base partial 16S rRNA gene. Inspected source qualifiers
give strain BB0608_2216_1.1_5S0, taxon 1033329, coastal marine sediment,
Australia's Gulf of Carpentaria and collection in June 2008. This uses a
strain qualifier, not a clone or environmental-sample qualifier. It does
not establish a registered culture deposit or genome; the partial locus
was not used to independently reassess taxonomy.

Both sequence references were inspected: Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb's marine-sediment cryopreservation study, marked
unpublished, and Cornall's direct submission dated 2011-04-01. Neither
provides a DOI or PMID. Full manuscript text was not obtained; no isolate
cryopreservation phenotype or publication identifier was inferred.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single NAME attestation and 2026-09-13 taxonomy snapshot agree with the
pinned source. One assertion is not a strain census or independent-study count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero linked inventory
strains does not mean the named strain was never cultured. Empty optional
fields accurately reflect the maintained inventories checked.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the numeric ID
with digit boundaries and exact label/stem designation, allowing its
dot/underscore representation, across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`. All three matching lines were inspected:
target scope, backbone and scientific name. Recursive structured
SOURCE.json searches returned no matches. No related isolate or numeric
coincidence was substituted for this target; these bounded local-source
results are not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve the exact strain identity and unclassified lineage.
Future evidence-backed corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321315`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact strain/deposit evidence
and inventory deltas, run `just seed-canary NCBITaxon:1033329 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13410`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets
succeeded. iModulonDB was not applicable to this taxonomy-only record.
Only this report and the documented validation TSV were written for this
target; YAML, maintained inputs, scope, history, status and GitHub remain
unchanged.
