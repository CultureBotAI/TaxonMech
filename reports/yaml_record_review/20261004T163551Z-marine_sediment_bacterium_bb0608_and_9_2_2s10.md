# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_2S10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_2s10.yaml`
- Started UTC: 2026-10-04T16:34:46Z
- Finished UTC: 2026-10-04T16:35:51Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033633, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_9.2_2S10 distinguishes this record from neighboring strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_2s10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_2s10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221267 and scientific-name row 30575 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033633&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033633)
confirm name and rank; EFetch confirms parent 49928 and code 11. Root-first
lineage is root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928), with matching ranks. Species rank alone does not establish
valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750186.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750186.1),
UID 333384533, one 535-base partial 16S rRNA sequence. Inspected qualifiers
identify strain BB0608_AND_9.2_2S10, taxon 1033633, genomic DNA, coastal
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
`history`. All eight matches were inspected: target scope/backbone/name,
one ATB row, one BV-BRC object, two assembly objects and one GTDB object.
The four native genome objects were also read in full. Structured recursive
SOURCE.json scans found zero matches. Absence is bounded to these local
searches and exact public queries.

`data/catalog/allthebacteria.tsv.xz:64989` concerns SAMEA1033633,
ERR068295 and ERR086004, and ERZ3069054. Scientific name and both Sylph
species fields are Streptococcus pneumoniae; FASTA is available,
assembly/Sylph/HQ filters PASS and prior-HQ T. Only the sample suffix
and AWS URL match the target's numeric identifier. There is no target
strain/deposit/genome chain. The shared BioSample with the unrelated
NCBI assemblies below does not establish that the ATB assembly is the
same assembly or sequence. Exclusion from target evidence is based on
identity, not quality. SeqKit signatures are not MD5 values and AWS
URLs are mutable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321619`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:1033633 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

`data/bvbrc/bvbrc-0002.jsonl.gz:14897` identifies BV-BRC 1313.8719,
Streptococcus pneumoniae C12797a, taxon 1313. Unlike a sample-only
association, this object explicitly supplies GCF_900051325.1,
SAMEA1033633/PRJEB2656 and unversioned FIUV00000000, with WGS status.

`data/catalog/ncbi_genbank-0056.jsonl.gz:35044` and
`data/catalog/ncbi_refseq-0009.jsonl.gz:23119` identify
GCA_900051325.1 and GCF_900051325.1 with reciprocal identical pairing.
Both are latest scaffold-level assemblies for C12797a, taxon 1313,
SAMEA1033633, WGS FIUV00000000.1, 48 contigs and 47 scaffolds,
total length 2080702 and ungapped length 2080691. GenBank project is
PRJEB2656; RefSeq project is PRJNA224116. Neither supplies a PMID.

`data/catalog/gtdb_genomes-0007.jsonl.gz:576` identifies
RS_GCF_900051325.1 and explicitly supplies GCA_900051325.1,
SAMEA1033633, PRJNA224116, FIUV00000000.1 and strain C12797a.
GTDB and NCBI taxonomy agree on Streptococcus pneumoniae. Its
Malawi/CSF metadata concern that strain, not the target. Explicit
accession/pairing fields support the BV-BRC/NCBI/GTDB relationships;
numeric BioSample coincidence does not connect any of them to
BB0608_AND_9.2_2S10. Unversioned and .1 accessions are preserved.

Unique PATHS entry: `data/taxa/PATHS.tsv:13720`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.

