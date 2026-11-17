# YAML Record Review: marine sediment bacterium BB0608_2216_4.1_6S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_4_1_6s0.yaml`
- Started UTC: 2026-10-04T07:50:13Z
- Finished UTC: 2026-10-04T07:53:07Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033379`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_2216_4.1_6S0 distinguishes this target from other BB0608 strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_4_1_6s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_4_1_6s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans found
  no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221013 and scientific-name row 30321 in
`data/catalog/ncbi_names-0005.jsonl.gz` match the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033379&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033379)
confirm ID, label, species rank and parent 49928; EFetch also confirms
code 11. All four ancestors agree: root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928). No finer taxonomic placement or
formal nomenclatural publication was inferred from the species rank.

## Evidence

Exact Nuccore search returned one entry, [JF750242.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750242.1),
UID 333384589, a 510-base partial 16S rRNA gene. Source qualifiers identify
strain BB0608_2216_4.1_6S0, taxon 1033379, coastal marine sediment,
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
All six matched lines were inspected: target scope, backbone, scientific
name, two Iodobacter source objects and one ATB Staphylococcus aureus sample.
Recursive structured SOURCE.json searches returned no matches. These
bounded local-source results are not universal absence claims.

The two full native Iodobacter objects were read at
`data/catalog/ncbi_genbank-0031.jsonl.gz:8173` and
`data/bvbrc/bvbrc-0018.jsonl.gz:45487`. Their numeric match is BioProject
PRJNA1033379, not the target taxonomy ID. Both describe Iodobacter sp. CM08,
taxon 3085902, strain CM08, BioSample SAMN38031727 and assembly
GCA_033446605.1. GenBank supplies paired GCF_033446605.1 and WGS master
JAWQUO000000000.1; BV-BRC supplies genome 3085902.3 and unversioned
JAWQUO000000000. Preserve those supplied versions separately. Neither object
establishes target strain identity.

The ATB match is sample SAMEA1033379, run ERR084582 and ENA analysis
ERZ3068713, source scientific name Staphylococcus aureus. Its available
FASTA and passing source filters do not overcome the unrelated identity.
No target strain/BioSample/assembly chain was established by these matches.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve exact strain identity and unclassified lineage. Future
evidence-backed fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:321365`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact strain/deposit identity
and inventory deltas, run `just seed-canary NCBITaxon:1033379 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13462`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets succeeded.
iModulonDB was not applicable to this taxonomy-only record. Only this report
and the documented validation TSV were written for this target; YAML,
maintained inputs, scope, history, status and GitHub remain unchanged.
