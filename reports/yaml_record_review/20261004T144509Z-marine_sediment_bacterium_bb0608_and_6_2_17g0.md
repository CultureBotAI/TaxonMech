# YAML Record Review: marine sediment bacterium BB0608_AND_6.2_17G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_17g0.yaml`
- Started UTC: 2026-10-04T14:43:58Z
- Finished UTC: 2026-10-04T14:45:09Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033586`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.2_17G0 distinguishes neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_17g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_17g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221220 and scientific-name row 30528 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033586&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033586)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750132.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750132.1),
UID 333384479, one 327-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.2_17G0, taxon 1033586, genomic DNA,
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
All eight matches were inspected: target scope/backbone/scientific name,
one ATB row and four native JSON objects, each read in full. Recursive
structured SOURCE.json scans found zero matches. These bounded searches
do not establish universal absence.

- `data/catalog/allthebacteria.tsv.xz:64942`: SAMEA1033586, ERR068299 and ERR086008, ERZ3068988; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the BioSample suffix and its AWS URL match.
- `data/bvbrc/bvbrc-0002.jsonl.gz:14877`: genome 1313.8699, Streptococcus pneumoniae C14971, taxon 1313, explicit GCF_900050955.1, SAMEA1033586, PRJEB2656 and unversioned FIWJ00000000.
- GenBank `data/catalog/ncbi_genbank-0056.jsonl.gz:35007` and RefSeq `data/catalog/ncbi_refseq-0009.jsonl.gz:23082`: GCA_900050955.1 and GCF_900050955.1, explicitly reciprocal identical pairs, same strain C14971, taxon/species 1313, BioSample SAMEA1033586 and versioned WGS FIWJ00000000.1. GenBank project PRJEB2656 and RefSeq project PRJNA224116 remain distinct. Both are Contig assemblies with 54 contigs and total/ungapped length 2044271.
- `data/catalog/gtdb_genomes-0008.jsonl.gz:26700`: RS_GCF_900050955.1 explicitly links GCA_900050955.1 and carries the same strain, taxon, sample, versioned WGS and PRJNA224116. GTDB and carried NCBI classifications both name Streptococcus pneumoniae.

Exclusions are identity-based, not quality-based. Shared BioSample does
not establish ATB/NCBI assembly equivalence. Explicit source crosslinks and
accession versions are preserved, but none supplies a target
strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321572`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033586 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13669`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
