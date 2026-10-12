# YAML Record Review: marine sediment bacterium BB0608_AND_7.1_8G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_8g0.yaml`
- Started UTC: 2026-10-04T15:21:10Z
- Finished UTC: 2026-10-04T15:22:06Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033602, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_7.1_8G0 distinguishes this record from neighboring strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_8g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_8g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221236 and scientific-name row 30544 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033602&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033602)
confirm name and rank; EFetch confirms parent 49928 and code 11. Root-first
lineage is root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928), with matching ranks. Species rank alone does not establish
valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750147.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750147.1),
UID 333384494, one 590-base partial 16S rRNA sequence. Inspected qualifiers
identify strain BB0608_AND_7.1_8G0, taxon 1033602, genomic DNA, coastal
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
`history`. All seven matches were inspected: target scope/backbone/name,
one ATB row and three native JSON objects, each read in full. Structured
recursive SOURCE.json scans found zero matches. Absence is bounded to
these local searches and exact public queries.

- `data/catalog/allthebacteria.tsv.xz:64958`: SAMEA1033602, ERR064608 and ERR085867, ERZ3069017; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ PASS, prior-HQ T. Only the sample suffix and AWS URL match.
- `data/bvbrc/bvbrc-0002.jsonl.gz:14841`: genome 1313.8663, Streptococcus pneumoniae strain D55377, taxon 1313, explicit GCF_900050145.1 link, SAMEA1033602, PRJEB2656 and unversioned FIYI00000000. Only the sample suffix matches.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:34927` and `data/catalog/ncbi_refseq_historical-0001.jsonl.gz:48289`: GCA_900050145.1 and GCF_900050145.1, explicitly reciprocal identical pairs, same organism/strain/taxon/sample, FIYI00000000.1; GenBank project PRJEB2656 and RefSeq PRJNA224116. Scaffold assembly, 586 contigs and 169 scaffolds, total length 2591966 and ungapped length 2551018. GenBank is marked latest; the historical RefSeq entry is suppressed with not-live date 2023-08-22. Both carry an annotation-completeness exclusion reason. Separate annotations and their counts are not equated by sequence pairing. Only the BioSample suffix matches the target's numeric taxon ID.

Exclusions are identity-based, not quality-based. The historical RefSeq
status is preserved rather than presented as current. Shared BioSample
does not prove ATB/NCBI assembly equivalence. Explicit links and supplied
versions are retained without transferring these unrelated genome records
to the target; no target strain/deposit/genome chain was found.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321588`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:1033602 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13686`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.
