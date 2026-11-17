# YAML Record Review: marine sediment bacterium BB0608_AND_7.1_5G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_5g0.yaml`
- Started UTC: 2026-10-04T15:19:21Z
- Finished UTC: 2026-10-04T15:20:30Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033601, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_7.1_5G0 distinguishes this record from neighboring strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_5g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_5g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221235 and scientific-name row 30543 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033601&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033601)
confirm name and rank; EFetch confirms parent 49928 and code 11. Root-first
lineage is root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928), with matching ranks. Species rank alone does not establish
valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750146.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750146.1),
UID 333384493, one 540-base partial 16S rRNA sequence. Inspected qualifiers
identify strain BB0608_AND_7.1_5G0, taxon 1033601, genomic DNA, coastal
marine sediment, Australia: Gulf of Carpentaria and June 2008. The source
uses strain, not clone or environmental sample. This locus is not a genome,
culture deposit or independent classification.

Both references were inspected: the Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb cryopreservation study is unpublished; Cornall's
direct submission is dated 2011-04-01. Neither supplies DOI/PMID. Full
manuscript text was not obtained and no phenotype was inferred from its
title. Exact Assembly search returned zero with phrase-not-found/no-items
warnings. The one NAME attestation and snapshot 2026-09-13 agree with the
inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional fields are
appropriate; zero inventoried strains does not mean never cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full designation with dot/underscore variants, including label/slug
forms, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and
`history`. All five matches were inspected: target scope/backbone/name,
one ATB row and one native assembly JSON object, read in full. Structured
recursive SOURCE.json scans found zero matches. Absence is bounded to
these local searches and exact public queries.

- `data/catalog/allthebacteria.tsv.xz:64957`: SAMEA1033601, ERR064773, ERZ3069015; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ PASS, prior-HQ T. Only the sample suffix and AWS URL match.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:49789`: GCA_964962005.1, Limnohabitans sp., taxon/species 1907725, isolate `PELAGICS-MAG-x7-bin072178-TRCHH-SM-23mar22.` including its terminal period; SAMEA117455264, PRJEB75477, CBBSOC000000000.1. This metagenome-derived Contig assembly has 239 contigs and no RefSeq pair. Only total and ungapped length 1033601 match the taxon number. The assembly name lacks the isolate field's terminal period; both source values are preserved.

Exclusions are identity-based, not quality-based. Neither numerical length
nor sample suffix establishes a target strain/deposit/genome chain. Supplied
accession versions are retained; sample and assembly identities differ.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321587`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:1033601 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13685`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.
