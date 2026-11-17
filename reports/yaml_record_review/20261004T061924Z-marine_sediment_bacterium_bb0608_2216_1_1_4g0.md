# YAML Record Review: marine sediment bacterium BB0608_2216_1.1_4G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_4g0.yaml`
- Started UTC: 2026-10-04T06:18:32Z
- Finished UTC: 2026-10-04T06:19:24Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033328`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The exact isolate designation
is BB0608_2216_1.1_4G0; neighboring BB0608 identifiers are not synonyms.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_4g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_1_1_4g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans
  found no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not replace these gates.

## Identity and Grounding

Backbone row 220962 and scientific-name row 30270 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
EFetch and Datasets confirm [taxon 1033328](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033328),
the exact label, species rank, code 11 and parent 49928. All ancestors and
ranks match: root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928). No more specific placement or valid publication was inferred.

## Evidence

Exact Nuccore search returned one entry, [JF750191.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750191.1),
UID 333384538, a 286-base partial 16S rRNA gene. Inspected source qualifiers
give strain BB0608_2216_1.1_4G0, taxon 1033328, coastal marine sediment,
Australia's Gulf of Carpentaria and collection in June 2008. It uses a
strain qualifier, not a clone or environmental-sample qualifier. This does
not establish a registered culture deposit or a genome, and the short locus
was not used to independently reassess taxonomy.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study, marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither provides a DOI or
PMID. Full manuscript text was not obtained, and no identifier or isolate
cryopreservation phenotype was guessed from the reference title.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single NAME attestation and 2026-09-13 taxonomy snapshot match the pinned
inventory; their count is not a strain census or independent-study count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero linked inventory
strains does not mean the named isolate was never cultured. Empty optional
fields reproduce the maintained source coverage.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and the exact label/stem designation, allowing its
dot/underscore representation, across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`. All six matching lines were inspected:
target scope, backbone, scientific name, two unrelated genome-size matches
and ATB sample SAMEA1033328. The size matches belong to an uncultured archaeon
MarMAG_087850 (GCA_977537655.1) and an Actinomycetes bacterium
Loc090116-7m_bin-0881 (GCA_903951505.1); the ATB sample is Staphylococcus
aureus. None establishes the exact isolate/BioSample identity chain.
Recursive structured SOURCE.json searches returned no matches. No source
grouping or numeric coincidence was treated as assembly equivalence. These
are bounded local-source results, not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve the exact isolate identity and carried unclassified lineage.
Future evidence-backed corrections belong in maintained inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321314`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact isolate/deposit evidence
and inventory deltas, run `just seed-canary NCBITaxon:1033328 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13409`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets
succeeded. iModulonDB was not applicable to this taxonomy-only record.
Only this report and the documented validation TSV were written; YAML,
maintained inputs, scope, history, status and GitHub remain unchanged.
