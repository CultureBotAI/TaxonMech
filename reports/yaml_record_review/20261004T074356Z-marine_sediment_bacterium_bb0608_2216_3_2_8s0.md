# YAML Record Review: marine sediment bacterium BB0608_2216_3.2_8S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_3_2_8s0.yaml`
- Started UTC: 2026-10-04T07:43:03Z
- Finished UTC: 2026-10-04T07:43:56Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033375`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. BB0608_2216_3.2_8S0 is distinct
from the adjacent 3.2_8G0 record and other BB0608 strain designations.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_3_2_8s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_3_2_8s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans found
  no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221009 and scientific-name row 30317 in
`data/catalog/ncbi_names-0005.jsonl.gz` match the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033375&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033375)
confirm ID, label, species rank, code 11 and parent 49928. All four ancestors
agree: root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928). No finer placement or formal nomenclatural publication
was inferred from the species rank.

## Evidence

Exact Nuccore search returned one entry, [JF750238.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750238.1),
UID 333384585, a 570-base partial 16S rRNA gene. Source qualifiers identify
strain BB0608_2216_3.2_8S0, taxon 1033375, coastal marine sediment,
Australia's Gulf of Carpentaria and June 2008 collection. A strain qualifier
is present, not a clone or environmental-sample qualifier. This partial locus
does not establish a registered deposit, genome or independent classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study, marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI or
PMID. Full manuscript text was not obtained; no isolate cryopreservation
phenotype or publication identifier was inferred from the title.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME assertion and 2026-09-13 taxonomy snapshot reproduce the pinned
source; assertion count is not an independent-study or biological-strain count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero inventoried strains
does not imply the named strain was never cultured. Empty optional fields
reflect the maintained source coverage checked.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and exact label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All nine matched lines were inspected: three target rows and six source rows
matching BioSample SAMEA1033375. Recursive structured SOURCE.json searches
returned no matches. These bounded local checks are not universal absence claims.

Complete source objects were read at `data/bvbrc/bvbrc-0000.jsonl.gz:47437`,
`data/gold/projects.jsonl.gz:77926`,
`data/catalog/ncbi_refseq-0000.jsonl.gz:29185`,
`data/catalog/ncbi_genbank-0000.jsonl.gz:33730` and
`data/catalog/gtdb_genomes-0000.jsonl.gz:18948`. They identify Staphylococcus
aureus BSAR58, taxon 1280, BV-BRC 1280.3383 and source-paired assemblies
GCA_000982735.1/GCF_000982735.1. GOLD project Gp0129885 points to organism
Go0121989; these are related source records, not genome identifiers.
BV-BRC/GenBank/GOLD carry PRJEB2655, while RefSeq/GTDB carry PRJNA224116.
BV-BRC supplies unversioned CHEJ00000000; assembly catalogs supply
CHEJ00000000.1. These source differences were retained, not normalized away.

The sixth source row is ATB's Staphylococcus aureus sample SAMEA1033375.
No inspected source connects that BioSample to the marine-sediment target.
Shared BioSample alone also does not establish ATB/NCBI assembly equivalence.
None of these source associations was transferred into the target record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve exact strain identity and unclassified lineage. Future
evidence-backed fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321361`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact strain/deposit identity
and inventory deltas, run `just seed-canary NCBITaxon:1033375 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13458`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets succeeded.
iModulonDB was not applicable to this taxonomy-only record. Only this report
and the documented validation TSV were written for this target; YAML,
maintained inputs, scope, history, status and GitHub remain unchanged.
