# YAML Record Review: marine sediment bacterium BB0608_AND_6.1_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_3g0.yaml`
- Started UTC: 2026-10-04T14:22:11Z
- Finished UTC: 2026-10-04T14:23:31Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033574`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.1_3G0 distinguishes neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_3g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221208 and scientific-name row 30516 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033574&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033574)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750119.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750119.1),
UID 333384466, one 525-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.1_3G0, taxon 1033574, genomic DNA,
coastal marine sediment, Australia: Gulf of Carpentaria and June 2008.
The qualifier is strain, not clone or environmental sample. This locus is
not a genome, deposit or independent classification.

Both sequence references were inspected: the unpublished Cornall, Beyer,
Streten-Joyce, McGuinness, Parry and Gibb cryopreservation study and
Cornall's direct submission dated 2011-04-01. Neither supplies a DOI/PMID;
full manuscript text was not obtained and no phenotype was inferred from
the title. Exact Assembly search returned zero with phrase-not-found and
no-items warnings. The NCBITAXON NAME count and 2026-09-13 snapshot match
the inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target entries in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Optional fields may remain
empty; zero inventoried strains does not establish absence of cultivation.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full label/stem designation with dot/underscore alternatives across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All six matches were inspected: target scope/backbone/scientific name,
two ATB rows and one native GenBank object, read in full. Recursive
structured SOURCE.json scans found zero matches. These bounded searches
do not establish universal absence.

- `data/catalog/allthebacteria.tsv.xz:64930`: SAMEA1033574, ERR068138, ERZ3068980; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix and its AWS URL match.
- ATB row 1021308: SAMN02345510, SRR1033574, ERZ4070406; scientific name and both Sylph fields Salmonella enterica. Only the run suffix matches.
- `data/catalog/ncbi_genbank-0058.jsonl.gz:18800`: GCA_903946975.1, uncultured Pseudomonadota bacterium, taxon/species 153809, isolate I-2_bin-061, SAMEA6946933, PRJEB38681 and CAJAXL000000000.1. This Contig assembly has 421 contigs, no RefSeq pair, and exclusions for metagenome derivation, fragmentation and undefined genus. Only total and ungapped length 1033574 match.

Both ATB rows have available FASTAs, assembly/Sylph/HQ filters PASS and
prior-HQ T. Exclusions are identity-based, not quality-based. None supplies
a target strain/deposit/genome chain. Assembly accession versions and
quality fields remain explicit.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321560`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033574 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13657`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
